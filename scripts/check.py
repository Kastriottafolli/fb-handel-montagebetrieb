"""Check deployable HTML, local navigation, assets, metadata and brand references."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys
root=Path(__file__).resolve().parent.parent
errors=[]
class Document(HTMLParser):
 def __init__(self):
  super().__init__(); self.refs=[];self.ids=set();self.h1=0;self.title=False;self.description=False;self.lang=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang')=='de'
  if 'id' in a:
   if a['id'] in self.ids:errors.append(f'Doppel-ID: {a["id"]}')
   self.ids.add(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='title':self.title=True
  if tag=='meta' and a.get('name')=='description':self.description=bool(a.get('content'))
  if tag=='img' and 'alt' not in a:errors.append('Bild ohne Alternativtext')
  for key in ['href','src']:
   if a.get(key):self.refs.append(a[key])
  if a.get('srcset'):
   self.refs.extend(s.strip().split()[0] for s in a['srcset'].split(','))
files=list(root.glob('*.html'));docs={}
for f in files:
 d=Document();s=f.read_text();d.feed(s);docs[f.name]=d
 if d.h1!=1:errors.append(f'{f.name}: {d.h1} H1-Überschriften')
 if not all([d.title,d.description,d.lang]):errors.append(f'{f.name}: Metadaten fehlen')
 for old in ['fbmontagebetrieb@gmx.de','www.fb-handel-montagebetrieb.de','0177 000000','Faton','Au 21a','94137','Bayerbach','0177 5266889','491775266889','Fensterwerk OG','Inhaber:']:
  if old in s:errors.append(f'{f.name}: veraltete Daten {old}')
 for current in ['2B Fensterwerk UG (haftungsbeschränkt)','Lindhofstraße 14','84307 Eggenfelden','tel:+4915251511101','0152 515 11101']:
  if current not in s:errors.append(f'{f.name}: aktuelle Firmenangabe fehlt: {current}')
for file in ['kontakt.html','impressum.html','datenschutz.html','ueber-uns.html']:
 if 'Valon Bytyçi' not in (root/file).read_text():errors.append(f'{file}: Geschäftsführer fehlt')
for value in ['Amtsgericht Landshut','HRB 15577','Geschäftsführer Valon Bytyçi']:
 if value not in (root/'impressum.html').read_text():errors.append(f'Impressum: {value} fehlt')
for filename,d in docs.items():
 for ref in d.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  p=unquote(u.path);target=(root/p) if p else root/filename
  if not target.exists():errors.append(f'{filename}: Ziel fehlt: {ref}')
  if u.fragment and target.suffix=='.html' and target.name in docs and u.fragment not in docs[target.name].ids:errors.append(f'{filename}: Fragment fehlt: {ref}')
if errors:
 print('\n'.join(errors));sys.exit(1)
print(f'OK: {len(files)} Seiten, interne Links, Fragmente, Medien, H1, Metadaten und neue Kontaktdaten geprüft.')
