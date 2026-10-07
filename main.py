import sys
import platform
from datetime import datetime, timezone, timedelta

from flask import Flask, jsonify, request

app = Flask(__name__)
WIB = timezone(timedelta(hours=7))

PAGE = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sample — catatan dari server</title>
<style>
  :root { --paper:#f4f1ea; --ink:#16140f; --mute:#6f6a5d; --rule:#16140f; --hot:#e8431c; }
  * { box-sizing:border-box; margin:0; }
  body { background:var(--paper); color:var(--ink); padding:clamp(20px,5vw,64px);
         font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace; font-size:14px; line-height:1.6; }
  .wrap { max-width:880px; margin:0 auto; }
  header { display:flex; justify-content:space-between; padding-bottom:10px;
           border-bottom:2px solid var(--rule); font-size:12px; text-transform:uppercase; letter-spacing:.08em; }
  h1 { margin:56px 0 24px; font-family:Georgia,"Times New Roman",serif; font-weight:400;
       font-size:clamp(48px,11vw,112px); line-height:.95; letter-spacing:-.03em; }
  h1 em { color:var(--hot); font-style:italic; }
  .lead { max-width:46ch; color:var(--mute); font-size:15px; }
  h2 { margin:64px 0 12px; font-size:12px; font-weight:400; text-transform:uppercase;
       letter-spacing:.08em; color:var(--mute); }
  dl { border-top:1px solid var(--rule); }
  .r { display:grid; grid-template-columns:160px 1fr; gap:16px; padding:12px 0;
       border-bottom:1px solid var(--rule); }
  dt { color:var(--mute); }
  dd { word-break:break-all; }
  a { color:var(--ink); text-decoration:underline; text-underline-offset:3px; text-decoration-thickness:1px; }
  a:hover { color:var(--hot); }
  footer { margin-top:72px; padding-top:10px; border-top:2px solid var(--rule);
           display:flex; justify-content:space-between; font-size:12px; color:var(--mute); }
  @media (max-width:520px) { .r { grid-template-columns:1fr; gap:0; } }
</style>
</head>
<body>
<div class="wrap">
  <header><span>Sample / No. 01</span><span>{{TIME}}</span></header>

  <h1>Catatan dari <em>server.</em></h1>
  <p class="lead">Halaman ini dirender oleh Flask saat kamu membukanya. Semua angka di bawah diambil langsung dari mesin yang melayani permintaanmu.</p>

  <h2>Permintaan ini</h2>
  <dl>
    <div class="r"><dt>Waktu server</dt><dd>{{TIME}}</dd></div>
    <div class="r"><dt>Metode &amp; path</dt><dd>{{METHOD}} {{PATH}}</dd></div>
    <div class="r"><dt>Browser</dt><dd>{{UA}}</dd></div>
  </dl>

  <h2>Mesin</h2>
  <dl>
    <div class="r"><dt>Python</dt><dd>{{PY}}</dd></div>
    <div class="r"><dt>Sistem</dt><dd>{{OS}}</dd></div>
    <div class="r"><dt>Endpoint</dt><dd><a href="/api/hello">/api/hello</a> — versi JSON</dd></div>
  </dl>

  <footer><span>Flask + Vercel</span><span>Muat ulang untuk waktu baru</span></footer>
</div>
</body>
</html>"""


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


@app.route("/")
def home():
    now = datetime.now(WIB).strftime("%d %b %Y, %H:%M:%S WIB")
    values = {
        "{{TIME}}": now,
        "{{METHOD}}": request.method,
        "{{PATH}}": request.path,
        "{{UA}}": request.headers.get("User-Agent", "tidak diketahui"),
        "{{PY}}": sys.version.split()[0],
        "{{OS}}": f"{platform.system()} {platform.machine()}",
    }
    html = PAGE
    for key, val in values.items():
        html = html.replace(key, esc(val))
    return html


@app.route("/api/hello")
def hello():
    return jsonify(
        message="Halo dari Flask",
        time=datetime.now(WIB).isoformat(timespec="seconds"),
        python=sys.version.split()[0],
    )
