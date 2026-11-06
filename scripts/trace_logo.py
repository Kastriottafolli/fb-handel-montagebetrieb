"""Trace the alpha silhouette for a code-native draw-on animation.
The original PNG is retained unchanged and is used as the finished logo.
Regeneration requires Pillow; the website itself has no new dependencies.
"""
from pathlib import Path
from PIL import Image
import math
ROOT=Path(__file__).resolve().parent.parent
image=Image.open(ROOT/'assets/img/2bfensterwerk-logo-ug-transparent.png')
alpha=image.getchannel('A').point(lambda a:255 if a>=128 else 0)
w,h=alpha.size
pixels=alpha.tobytes()
bounds=alpha.getbbox()
edges={}
def edge(a,b):edges.setdefault(a,[]).append(b)
for y in range(h):
 for x in range(w):
  if not pixels[y*w+x]:continue
  if y==0 or not pixels[(y-1)*w+x]:edge((x,y),(x+1,y))
  if x==w-1 or not pixels[y*w+x+1]:edge((x+1,y),(x+1,y+1))
  if y==h-1 or not pixels[(y+1)*w+x]:edge((x+1,y+1),(x,y+1))
  if x==0 or not pixels[y*w+x-1]:edge((x,y+1),(x,y))
def simplify(points,tolerance=1.15):
 if len(points)<3:return points
 ax,ay=points[0];bx,by=points[-1];dx=bx-ax;dy=by-ay;length=math.hypot(dx,dy)
 distances=[abs(dx*(ay-y)-(ax-x)*dy)/length if length else math.hypot(x-ax,y-ay) for x,y in points]
 index=max(range(len(points)),key=lambda i:distances[i])
 if distances[index]>tolerance:return simplify(points[:index+1],tolerance)[:-1]+simplify(points[index:],tolerance)
 return [points[0],points[-1]]
contours=[]
while edges:
 start=next(iter(edges));current=start;points=[start]
 while True:
  following=edges[current].pop()
  if not edges[current]:del edges[current]
  points.append(following);current=following
  if current==start:break
 area=abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(points,points[1:])))/2
 if area<40:continue
 points=simplify(points)
 xs=[p[0] for p in points];ys=[p[1] for p in points]
 left,right,top,bottom=min(xs),max(xs),min(ys),max(ys)
 if bottom<715:
  phase=0 if left<600 else .18 if left<930 else .36
 else:phase=.72 if top<820 else .95
 gold=(left>930 and top<715) or top>820
 d='M'+' '.join(f'{x},{y}' for x,y in points)+'Z'
 contours.append((phase,left,f'<path d="{d}" pathLength="1000" style="--line-delay:{phase}s" stroke="url(#__LOGO_ID__-{"gold" if gold else "silver"})"/>'))
contours.sort(key=lambda c:(c[0],c[1]))
x0,y0,x1,y1=bounds;padding=12
view=f'{x0-padding} {y0-padding} {x1-x0+padding*2} {y1-y0+padding*2}'
svg=f'''<svg class="logo-motion" data-logo-motion data-logo-state="ready" viewBox="{view}" role="img" aria-label="2B Fensterwerk UG" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="__LOGO_ID__-silver" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f7f6f6"/><stop offset=".45" stop-color="#bebebd"/><stop offset=".7" stop-color="#f7f6f6"/><stop offset="1" stop-color="#999899"/></linearGradient><linearGradient id="__LOGO_ID__-gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fdd782"/><stop offset=".55" stop-color="#ce9544"/><stop offset="1" stop-color="#a66e29"/></linearGradient></defs>
<image class="logo-finish" href="assets/img/2bfensterwerk-logo-ug-transparent.png" x="0" y="0" width="{w}" height="{h}"/>
<g class="logo-trace" fill="none" stroke-width="8" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true">{''.join(c[2] for c in contours)}</g>
</svg>'''
(ROOT/'scripts/sections/logo-motion.svg').write_text(svg)
print(f'{len(contours)} Konturen erzeugt; Ansicht {view}. Original-PNG bleibt unverändert.')
