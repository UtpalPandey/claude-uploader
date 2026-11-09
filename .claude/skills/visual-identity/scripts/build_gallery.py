import json,base64,os,html,sys,collections
LIB=sys.argv[1]; S=sys.argv[2]; L=LIB+'/styles'
items=[]
for slug in sorted(os.listdir(L)):
    p=f'{L}/{slug}/style.json'
    if not os.path.exists(p): continue
    d=json.load(open(p)); img=f'{S}/frames_small/{slug}.jpg'
    if not os.path.exists(img): continue
    d['b64']=base64.b64encode(open(img,'rb').read()).decode(); items.append(d)
items.sort(key=lambda d:d.get('num','99'))
groups=collections.OrderedDict()
for d in items: groups.setdefault(d.get('category_en','Other'),[]).append(d)
def uses(u):
    try: u=eval(u) if isinstance(u,str) else u
    except Exception: u=[u]
    return ' · '.join(html.escape(x) for x in u)
nav=''.join(f'<a href="#g{i}">{html.escape(g)} <span>{len(v)}</span></a>' for i,(g,v) in enumerate(groups.items()))
secs=''
for i,(g,v) in enumerate(groups.items()):
    cards=''.join(f'''<figure class="card"><img loading="lazy" src="data:image/jpeg;base64,{d["b64"]}" alt="{html.escape(d["en"])} sample frame"><figcaption><div class="row"><span class="num">No. {html.escape(str(d.get("num","")))}</span><span class="cn">{html.escape(d.get("cn",""))}</span></div><h3>{html.escape(d["en"])}</h3><p class="film">“{html.escape(d.get("film",""))}”: {html.escape(d.get("line",""))}</p><p class="uses">{uses(d.get("uses",""))}</p></figcaption></figure>''' for d in v)
    secs+=f'<section id="g{i}"><h2>{html.escape(g)}<span>{len(v)} styles</span></h2><div class="grid">{cards}</div></section>'
page=f'''<title>Visual Identity Styles</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Instrument+Sans:wght@400;600&display=swap">
<style>
/* Layout: film-festival programme — category tabs, then a grid of frame cards */
:root{{--bg:#f6f4f0;--fg:#1d1b19;--muted:#6b645c;--card:#fffdf9;--line:#e3ddd4;--accent:#b8452c;--disp:"Fraunces",Georgia,serif;--body:"Instrument Sans",system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#141210;--fg:#efe9e1;--muted:#a39a8f;--card:#1e1b18;--line:#34302b;--accent:#e2735a;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#141210;--fg:#efe9e1;--muted:#a39a8f;--card:#1e1b18;--line:#34302b;--accent:#e2735a;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--body);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 48px}}
.wrap{{max-width:1180px;margin:0 auto}}
header h1{{font-family:var(--disp);font-size:clamp(30px,6vw,52px);line-height:1.05;margin:0 0 10px;text-wrap:balance}}
header p{{color:var(--muted);max-width:62ch;line-height:1.55;margin:0 0 6px;font-size:15px}}
nav{{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0 8px}}
nav a{{color:var(--fg);text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:6px 12px;font-size:13px}}
nav a span{{color:var(--muted)}} nav a:hover,nav a:focus-visible{{border-color:var(--accent);outline:none}}
section{{margin-top:34px}}
h2{{font-family:var(--disp);font-size:24px;display:flex;align-items:baseline;gap:10px;border-bottom:1px solid var(--line);padding-bottom:8px;margin:0 0 16px}}
h2 span{{font-family:var(--body);font-size:13px;color:var(--muted);font-weight:400}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px}}
.card{{margin:0;background:var(--card);border:1px solid var(--line);border-radius:6px;overflow:hidden;display:flex;flex-direction:column}}
.card img{{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;max-width:100%}}
figcaption{{padding:10px 12px 14px;display:flex;flex-direction:column;gap:4px;min-width:0}}
.row{{display:flex;justify-content:space-between;font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--accent)}}
.cn{{text-transform:none;letter-spacing:0;color:var(--muted)}}
h3{{font-family:var(--disp);font-size:18px;margin:2px 0 0}}
.film{{font-size:13px;line-height:1.45;margin:0;color:var(--fg)}}
.uses{{font-size:12px;color:var(--muted);margin:2px 0 0}}
</style>
<div class="wrap"><header><h1>Visual Identity Styles</h1>
<p>Every style in the Lemo-Opuscar library ({len(items)} in this copy), each shown as one frame from its demo short. Lemo-Opuscar is a free, open GitHub library of film styles that Claude makes entirely in code: no video model, every frame drawn by code. Each style comes with a written style prompt, a palette, shot directions and a demo film.</p>
<p>Look through it and note the numbers of styles you'd want on the style board for your videos.</p></header>
<nav>{nav}</nav>{secs}</div>'''
open(f'{S}/style_gallery.html','w').write(page); print(len(items), round(len(page)/1e6,2),'MB', list(groups))
