from flask import Flask, jsonify
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

PAGE = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sample · Flask on Vercel</title>
<style>
  :root { --bg:#0b0d12; --card:rgba(255,255,255,.06); --line:rgba(255,255,255,.12);
          --text:#f2f4f8; --muted:#9aa3b2; --a:#7c5cff; --b:#22d3ee; }
  * { box-sizing:border-box; margin:0; }
  body { min-height:100vh; display:grid; place-items:center; padding:24px;
         font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
         color:var(--text); background:var(--bg); overflow:hidden; }
  .blob { position:fixed; width:420px; height:420px; border-radius:50%; filter:blur(90px);
          opacity:.45; z-index:-1; animation:float 12s ease-in-out infinite; }
  .b1 { background:var(--a); top:-120px; left:-100px; }
  .b2 { background:var(--b); bottom:-140px; right:-100px; animation-delay:-6s; }
  @keyframes float { 50% { transform:translate(40px,30px) scale(1.1); } }
  .card { width:100%; max-width:440px; padding:40px 32px; text-align:center;
          background:var(--card); border:1px solid var(--line); border-radius:24px;
          backdrop-filter:blur(18px); box-shadow:0 20px 60px rgba(0,0,0,.4); }
  .pill { display:inline-flex; align-items:center; gap:8px; padding:6px 14px;
          font-size:12px; color:var(--muted); border:1px solid var(--line); border-radius:99px; }
  .dot { width:8px; height:8px; border-radius:50%; background:#34d399;
         box-shadow:0 0 10px #34d399; }
  h1 { margin:22px 0 10px; font-size:38px; letter-spacing:-1px; line-height:1.1;
       background:linear-gradient(90deg,var(--a),var(--b)); -webkit-background-clip:text;
       background-clip:text; color:transparent; }
  p { color:var(--muted); line-height:1.6; font-size:15px; }
  .clock { margin:26px 0 6px; font-size:46px; font-weight:700; letter-spacing:2px;
           font-variant-numeric:tabular-nums; }
  .date { font-size:13px; color:var(--muted); }
  .row { display:flex; gap:10px; margin-top:28px; }
  .btn { flex:1; padding:12px; font-size:14px; font-weight:600; color:var(--text);
         text-decoration:none; border:1px solid var(--line); border-radius:12px;
         background:transparent; cursor:pointer; transition:.2s; }
  .btn:hover { transform:translateY(-2px); border-color:var(--a); }
  .btn.main { border:none; background:linear-gradient(90deg,var(--a),var(--b)); }
  #quote { margin-top:22px; min-height:22px; font-size:13px; color:var(--muted); font-style:italic; }
</style>
</head>
<body>
<div class="blob b1"></div><div class="blob b2"></div>
<main class="card">
  <span class="pill"><span class="dot"></span> Online di Vercel</span>
  <h1>Halo, Dunia.</h1>
  <p>Aplikasi Flask pertamaku. Sederhana, cepat, dan siap dikembangkan.</p>
  <div class="clock" id="clock">--:--:--</div>
  <div class="date" id="date"></div>
  <div class="row">
    <button class="btn main" onclick="newQuote()">Kutipan baru</button>
    <a class="btn" href="/api/hello">API</a>
  </div>
  <div id="quote"></div>
</main>
<script>
  const quotes = [
    "Mulai saja dulu, rapikan nanti.",
    "Kode yang jalan lebih baik daripada kode yang sempurna.",
    "Satu commit kecil tiap hari.",
    "Error adalah petunjuk, bukan musuh.",
    "Sederhana itu sulit, dan itu bagus."
  ];
  function newQuote() {
    document.getElementById("quote").textContent =
      "\\u201C" + quotes[Math.floor(Math.random() * quotes.length)] + "\\u201D";
  }
  function tick() {
    const d = new Date();
    document.getElementById("clock").textContent = d.toLocaleTimeString("id-ID", {hour12:false});
    document.getElementById("date").textContent =
      d.toLocaleDateString("id-ID", {weekday:"long", day:"numeric", month:"long", year:"numeric"});
  }
  tick(); setInterval(tick, 1000); newQuote();
</script>
</body>
</html>"""


@app.route("/")
def home():
    return PAGE


@app.route("/api/hello")
def hello():
    wib = timezone(timedelta(hours=7))
    return jsonify(
        message="Halo dari Flask!",
        status="ok",
        time=datetime.now(wib).strftime("%Y-%m-%d %H:%M:%S WIB"),
    )
