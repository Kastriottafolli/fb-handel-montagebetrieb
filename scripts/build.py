from pathlib import Path
import shutil
root=Path(__file__).resolve().parent.parent
dist=root/'dist'
if dist.exists(): shutil.rmtree(dist)
dist.mkdir()
for f in root.glob('*.html'): shutil.copy2(f,dist/f.name)
for name in ['assets','robots.txt','sitemap.xml','site.webmanifest','.nojekyll']:
 p=root/name
 if p.is_dir(): shutil.copytree(p,dist/name)
 elif p.exists(): shutil.copy2(p,dist/name)
print('Website gebaut: dist/')
