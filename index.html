<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Protocol Flow</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
:root{box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);
--bg:#fafaf9;--surface:#fff;--ink:#18181b;--ink2:#71717a;--line:#e7e5e4;--soft:#f4f4f2;--dns:#7c3aed;--tcp:#d97706;--app:#2563eb}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0c0c0e;--surface:#151518;--ink:#f4f4f5;--ink2:#8b8b95;--line:#26262b;--soft:#1b1b1f;--dns:#a78bfa;--tcp:#fbbf24;--app:#60a5fa}}
:root[data-theme="dark"]{--bg:#0c0c0e;--surface:#151518;--ink:#f4f4f5;--ink2:#8b8b95;--line:#26262b;--soft:#1b1b1f;--dns:#a78bfa;--tcp:#fbbf24;--app:#60a5fa}
*{box-sizing:border-box}
html,body{margin:0}
body{background:var(--bg);color:var(--ink);font:400 15px/1.5 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.page{max-width:1000px;margin:0 auto;padding:2.25rem 1.5rem 9rem}
.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:3rem}
.mark{font-weight:600;letter-spacing:-.01em;display:flex;align-items:center;gap:.6rem}
.mark i{width:10px;height:10px;border-radius:50%;background:var(--ink);box-shadow:14px 0 0 -3px var(--ink2),28px 0 0 -4px var(--line);margin-right:1.6rem}
.mode{font-size:.72rem;color:var(--ink2);display:flex;align-items:center;gap:.4rem}.mode:empty{display:none}.mode::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--ink2)}.mode.live::before{background:#16a34a}
.ghost{background:none;border:1px solid var(--line);color:var(--ink2);width:34px;height:34px;border-radius:50%;cursor:pointer;font-size:.9rem}
.ghost:hover{color:var(--ink);border-color:var(--ink2)}
h1{font-size:clamp(1.8rem,4vw,2.5rem);font-weight:600;letter-spacing:-.03em;line-height:1.15;margin:0 0 .6rem}
.lead{color:var(--ink2);margin:0 0 2.25rem;max-width:34rem}
.tabs{display:flex;gap:1.5rem;border-bottom:1px solid var(--line);margin-bottom:1.25rem}
.tab{background:none;border:0;padding:.6rem 0;font:inherit;font-weight:500;color:var(--ink2);cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-1px}
.tab.on{color:var(--ink);border-color:var(--ink)}
.form{display:none;gap:.75rem;align-items:flex-end;flex-wrap:wrap}.form.on{display:flex}
.fld{display:flex;flex-direction:column;gap:.3rem;flex:1;min-width:160px}
.fld label{font-size:.72rem;color:var(--ink2);font-weight:500}
input,select{font:inherit;font-size:.9rem;color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:.62rem .8rem;outline:none;width:100%}
input:focus,select:focus{border-color:var(--ink2)}
.run{font:inherit;font-weight:500;font-size:.9rem;background:var(--ink);color:var(--bg);border:0;border-radius:10px;padding:.66rem 1.4rem;cursor:pointer}
.run:hover{opacity:.88}
.phases{display:grid;grid-template-columns:repeat(3,1fr);gap:.5rem;margin:2.5rem 0 1.25rem}
.ph{font-size:.72rem;font-weight:500;color:var(--ink2)}
.ph::before{content:"";display:block;height:2px;background:var(--line);border-radius:2px;margin-bottom:.45rem;transition:background .3s}
.ph.done::before{background:var(--c)}.ph.act::before{background:var(--c);height:3px}.ph.act{color:var(--ink)}
.diagram{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:0 0 .5rem}
.heads{display:grid;grid-template-columns:repeat(3,1fr);text-align:center;padding:1.1rem 0;border-bottom:1px solid var(--line);position:sticky;top:env(safe-area-inset-top,0px);background:var(--surface);border-radius:16px 16px 0 0;z-index:2}
.heads div{font-size:.8rem;font-weight:600}.heads small{display:block;color:var(--ink2);font-weight:400;font-size:.7rem}
.rows{position:relative;min-height:220px}
.ll{position:absolute;top:0;bottom:0;width:1px;background:repeating-linear-gradient(var(--line) 0 4px,transparent 4px 8px)}
.empty{position:absolute;inset:0;display:grid;place-items:center;color:var(--ink2);font-size:.85rem}
.row{position:relative;height:66px;cursor:pointer;border-radius:8px;margin:0 .5rem;--c:var(--app)}
.row:hover,.row.sel{background:var(--soft)}
.lbl{position:absolute;top:11px;transform:translateX(-50%);white-space:nowrap;font-size:.74rem;display:flex;gap:.45rem;align-items:center;animation:fade .4s .25s both}
.lbl i{font-style:normal;font-family:'JetBrains Mono',monospace;color:var(--ink2);font-size:.68rem}
.lbl b{color:var(--c);font-weight:600}
.lbl span{color:var(--ink2);font-family:'JetBrains Mono',monospace;font-size:.7rem}
.arrow{position:absolute;top:42px;height:1.5px;background:var(--c);animation:r .5s cubic-bezier(.3,.7,.2,1) both}
.arrow.l{animation-name:lf}
.arrow::before{content:"";position:absolute;top:-3px;width:7px;height:7px;border-radius:50%;background:var(--c)}
.arrow.r::before{left:-3px}.arrow.l::before{right:-3px}
.arrow::after{content:"";position:absolute;top:-3.5px;width:8px;height:8px;border-top:1.5px solid var(--c);border-right:1.5px solid var(--c)}
.arrow.r::after{right:0;transform:rotate(45deg)}.arrow.l::after{left:0;transform:rotate(-135deg)}
.static .arrow,.static .lbl{animation:none}
@keyframes r{from{clip-path:inset(-9px 100% -9px 0)}to{clip-path:inset(-9px 0 -9px 0)}}
@keyframes lf{from{clip-path:inset(-9px 0 -9px 100%)}to{clip-path:inset(-9px 0 -9px 0)}}
@keyframes fade{from{opacity:0}}
.detail{margin-top:1.25rem;border:1px solid var(--line);border-radius:14px;padding:1.1rem 1.25rem;background:var(--surface);display:none}
.detail h3{margin:0 0 .6rem;font-size:.8rem;font-weight:500;color:var(--ink2);display:flex;gap:.6rem;align-items:center;flex-wrap:wrap}
.tag{font-size:.66rem;font-weight:600;padding:2px 8px;border-radius:99px;color:var(--c);background:color-mix(in srgb,var(--c) 12%,transparent)}
pre{margin:0;white-space:pre-wrap;word-break:break-word;font:400 .82rem/1.65 'JetBrains Mono',monospace}
.dock{position:fixed;left:50%;bottom:calc(1.25rem + env(safe-area-inset-bottom,0px));transform:translateX(-50%);display:none;align-items:center;gap:.4rem;background:var(--surface);border:1px solid var(--line);border-radius:99px;padding:.4rem .5rem .4rem .6rem;box-shadow:0 12px 32px -12px rgba(0,0,0,.25);width:min(560px,calc(100% - 2rem));z-index:5}
.ib{width:34px;height:34px;flex:none;border-radius:50%;border:0;background:none;color:var(--ink);cursor:pointer;display:grid;place-items:center}
.ib:hover:not(:disabled){background:var(--soft)}.ib:disabled{opacity:.3;cursor:default}
.ib.main{background:var(--ink);color:var(--bg)}.ib.main:hover:not(:disabled){background:var(--ink);opacity:.88}
.ib svg{width:15px;height:15px;fill:currentColor}
input[type=range]{padding:0;border:0;background:none;accent-color:var(--ink);height:20px;flex:1;min-width:0}
.cnt{font:500 .72rem 'JetBrains Mono',monospace;color:var(--ink2);padding:0 .6rem 0 .3rem;white-space:nowrap}
@media(max-width:640px){.page{padding:1.5rem 1rem 9rem}.lbl span{display:none}.top{margin-bottom:2rem}}
</style>
</head>
<body>
<div class="page">
 <div class="top"><div class="mark"><i></i>Protocol Flow</div><div style="display:flex;gap:.7rem;align-items:center"><span class="mode" id="mode"></span><button class="ghost" onclick="theme()" title="Toggle theme">◐</button></div></div>
 <h1>See how a request<br>travels the network.</h1>
 <p class="lead">Pick an activity, run it, and follow each packet between client, DNS and server as a sequence.</p>

 <div class="tabs">
  <button class="tab on" data-t="browse" onclick="sw('browse')">Web browsing</button>
  <button class="tab" data-t="mail" onclick="sw('mail')">Email</button>
  <button class="tab" data-t="stream" onclick="sw('stream')">Streaming</button>
 </div>
 <div class="form on" id="f-browse"><div class="fld"><label>URL</label><input id="url" value="http://www.youtube.com"></div><button class="run" onclick="go('browse')">Run</button></div>
 <div class="form" id="f-mail">
  <div class="fld"><label>To</label><input id="to" value="instructor@university.edu"></div>
  <div class="fld"><label>Subject</label><input id="subj" value="Protocol Assignment"></div>
  <div class="fld"><label>Message</label><input id="body" value="Please find my submission attached."></div>
  <button class="run" onclick="go('mail')">Run</button></div>
 <div class="form" id="f-stream"><div class="fld"><label>Resolution</label><select id="q"><option value="1080p">1080p</option><option value="720p">720p</option></select></div><button class="run" onclick="go('stream')">Run</button></div>

 <div class="phases">
  <div class="ph" style="--c:var(--dns)">1 · Name lookup</div>
  <div class="ph" style="--c:var(--tcp)">2 · Connection</div>
  <div class="ph" style="--c:var(--app)">3 · Application data</div>
 </div>

 <div class="diagram">
  <div class="heads"><div>Client<small>your device</small></div><div>DNS server<small>resolver</small></div><div id="h3">Remote server<small>remote host</small></div></div>
  <div class="rows" id="rows">
   <div class="ll" style="left:16.667%"></div><div class="ll" style="left:50%"></div><div class="ll" style="left:83.333%"></div>
   <div class="empty" id="empty">Press Run to trace the exchange</div>
  </div>
 </div>
 <div class="detail" id="detail"></div>
</div>

<div class="dock" id="dock">
 <button class="ib" id="bk" onclick="back()" title="Previous"><svg viewBox="0 0 16 16"><path d="M3 2h2v12H3zM14 2v12L6 8z"/></svg></button>
 <button class="ib main" id="pp" onclick="pp()" title="Play / pause"></button>
 <button class="ib" id="fw" onclick="fwd()" title="Next"><svg viewBox="0 0 16 16"><path d="M11 2h2v12h-2zM2 2l8 6-8 6z"/></svg></button>
 <input type="range" id="sc" min="0" max="0" value="0" oninput="scrub(+this.value)">
 <span class="cnt" id="cnt">0/0</span>
 <button class="ib" onclick="go(cur)" title="Replay"><svg viewBox="0 0 16 16"><path d="M8 2a6 6 0 1 0 6 6h-2a4 4 0 1 1-1.2-2.8L9 7h5V2l-1.8 1.8A6 6 0 0 0 8 2z"/></svg></button>
</div>

<script>
const $=id=>document.getElementById(id);
const PLAY='<svg viewBox="0 0 16 16"><path d="M4 2l10 6-10 6z"/></svg>',PAUSE='<svg viewBox="0 0 16 16"><path d="M3 2h4v12H3zM9 2h4v12H9z"/></svg>';
const lane=n=>n==='CLIENT'?16.667:n==='DNS SERVER'?50:83.333;
const cap=n=>n.charAt(0)+n.slice(1).toLowerCase();
function theme(){const r=document.documentElement;const dark=r.dataset.theme==='dark'||(!r.dataset.theme&&matchMedia('(prefers-color-scheme: dark)').matches);r.dataset.theme=dark?'light':'dark'}

// backend contract: POST /api/{browse|mail|stream} -> {sequence:[{type,sender,receiver,protocol,msg}]}
const payload=t=>t==='browse'?{url:$('url').value}:t==='mail'?{to_email:$('to').value,subject:$('subj').value,body:$('body').value}:{quality:$('q').value};
const norm=x=>({type:x.type,from:x.sender,to:x.receiver,proto:String(x.protocol).toUpperCase(),msg:x.msg});
// offline fallback: mirrors main.py so the page still demos without the server
function mock(t,d){
 const K='CLIENT',N='DNS SERVER',o=(s,r,p,m)=>({type:'out',sender:s,receiver:r,protocol:p,msg:m}),i=(s,r,p,m)=>({type:'in',sender:s,receiver:r,protocol:p,msg:m});
 const tcp=(v,a,b)=>[o(K,v,'TCP',a),i(v,K,'TCP',b),o(K,v,'TCP','ACK Segment (Ack=1) - Connection Established')];
 if(t==='browse'){let u=d.url.trim();if(!/^https?:\/\//.test(u))u='http://'+u;let p;try{p=new URL(u)}catch(e){p=new URL('http://example.com')}
  const h=p.host,path=(p.pathname||'/')+p.search,W='WEB SERVER';
  return[o(K,N,'DNS','Query A Record: '+h),i(N,K,'DNS','Response: 192.0.2.1 (Resolved via socket)'),...tcp(W,'SYN Segment [Port 80/443] (Seq=0, Win=64240)','SYN-ACK Segment (Seq=0, Ack=1, Win=29200)'),
  o(K,W,'HTTP','GET '+path+' HTTP/1.1\nHost: '+h+'\nAccept: text/html'),i(W,K,'HTTP','HTTP/1.1 200 OK\nContent-Type: text/html\n\n[HTML Document Payload]')]}
 if(t==='mail'){const dom=d.to_email.split('@')[1]||'local.edu',M='SMTP SERVER';
  return[o(K,N,'DNS','Query MX Record: '+dom),i(N,K,'DNS','Response: mail.'+dom),...tcp(M,'SYN Segment [Port 25/587] (Seq=0)','SYN-ACK Segment (Seq=0, Ack=1)'),
  o(K,M,'SMTP','EHLO client.local'),i(M,K,'SMTP','250-mail.'+dom+' Hello\n250-8BITMIME\n250 OK'),o(K,M,'SMTP','MAIL FROM: <student@university.edu>'),i(M,K,'SMTP','250 2.1.0 OK'),
  o(K,M,'SMTP','RCPT TO: <'+d.to_email+'>'),i(M,K,'SMTP','250 2.1.5 OK'),o(K,M,'SMTP','DATA'),i(M,K,'SMTP','354 End data with <CR><LF>.<CR><LF>'),
  o(K,M,'SMTP','Subject: '+d.subject+'\n\n'+d.body+'\n.'),i(M,K,'SMTP','250 2.0.0 Ok: queued as 7F3B1C'),o(K,M,'SMTP','QUIT'),i(M,K,'SMTP','221 2.0.0 Bye')]}
 const c='cdn.stream.com',V='VIDEO SERVER',g=n=>[o(K,V,'HTTP','GET /segments/'+d.quality+'/seg_00'+n+'.ts HTTP/1.1\nHost: '+c),i(V,K,'HTTP','HTTP/1.1 200 OK\nContent-Type: video/mp2t\n\n[Binary Video Segment '+n+']')];
 return[o(K,N,'DNS','Query A Record: '+c),i(N,K,'DNS','Response: 198.51.100.14'),...tcp(V,'SYN Segment [Port 443] (Seq=0)','SYN-ACK Segment (Seq=0, Ack=1)'),
  o(K,V,'HTTP','GET /master_manifest.m3u8 HTTP/1.1\nHost: '+c),i(V,K,'HTTP','HTTP/1.1 200 OK\nContent-Type: application/vnd.apple.mpegurl\n\n[Manifest Data]'),...g(1),...g(2)]}

// player
let seq=[],idx=0,sel=-1,timer=null,playing=false,cur='browse';
const phase=p=>p==='DNS'?0:p==='TCP'?1:2, pcol=p=>['--dns','--tcp','--app'][phase(p)];
function sw(t){cur=t;document.querySelectorAll('.form').forEach(e=>e.classList.toggle('on',e.id==='f-'+t));document.querySelectorAll('.tab').forEach(e=>e.classList.toggle('on',e.dataset.t===t))}
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function rowEl(s,i,anim){
 const a=lane(s.from),b=lane(s.to),right=b>a,el=document.createElement('div');
 el.className='row'+(anim?'':' static');el.dataset.i=i;el.style.setProperty('--c','var('+pcol(s.proto)+')');
 let sum=s.msg.split('\n')[0];if(sum.length>30)sum=sum.slice(0,29)+'…';
 el.innerHTML='<div class="arrow '+(right?'r':'l')+'" style="left:'+Math.min(a,b)+'%;width:'+Math.abs(b-a)+'%"></div><div class="lbl" style="left:'+(a+b)/2+'%"><i>'+String(i+1).padStart(2,'0')+'</i><b>'+s.proto+'</b><span>'+esc(sum)+'</span></div>';
 el.onclick=()=>select(i);return el}
function select(i){sel=i;document.querySelectorAll('.row').forEach(r=>r.classList.toggle('sel',+r.dataset.i===i));
 const d=$('detail');if(i<0||!seq[i]){d.style.display='none';return}
 const s=seq[i];d.style.display='block';d.style.setProperty('--c','var('+pcol(s.proto)+')');
 d.innerHTML='<h3><span>Step '+(i+1)+'</span><span class="tag">'+s.proto+'</span><span>'+cap(s.from)+' → '+cap(s.to)+'</span><span>'+(s.type==='in'?'inbound':'outbound')+'</span></h3><pre>'+esc(s.msg)+'</pre>'}
function ui(){
 const ap=idx?phase(seq[idx-1].proto):-1;
 document.querySelectorAll('.ph').forEach((e,k)=>{e.classList.toggle('done',k<ap);e.classList.toggle('act',k===ap)});
 $('cnt').textContent=idx+'/'+seq.length;$('sc').max=seq.length;$('sc').value=idx;
 $('pp').innerHTML=playing?PAUSE:PLAY;$('bk').disabled=idx<=0;$('fw').disabled=idx>=seq.length;
 $('dock').style.display=seq.length?'flex':'none'}
function add(anim){const el=rowEl(seq[idx],idx,anim);$('rows').appendChild(el);idx++;select(idx-1);if(anim)el.scrollIntoView({block:'center',behavior:'smooth'})}
function clearRows(){document.querySelectorAll('.row').forEach(r=>r.remove());idx=0;sel=-1}
async function go(t){clearTimeout(timer);cur=t;playing=false;let data,live=true;
 try{const r=await fetch('/api/'+t,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload(t))});if(!r.ok)throw 0;data=(await r.json()).sequence}
 catch(e){live=false;data=mock(t,payload(t))}
 seq=data.map(norm);const m=$('mode');m.className='mode'+(live?' live':'');m.textContent=live?'Live backend':'Offline demo';
 const rem=(seq.find(x=>x.from!=='CLIENT'&&x.from!=='DNS SERVER')||{from:'REMOTE SERVER'}).from;$('h3').innerHTML=cap(rem)+'<small>remote host</small>';
 clearRows();$('empty').style.display='none';playing=true;ui();next()}
function next(){if(!playing)return;if(idx>=seq.length){playing=false;ui();return}add(true);ui();timer=setTimeout(next,1300)}
function pause(){playing=false;clearTimeout(timer)}
function pp(){if(playing){pause()}else{if(idx>=seq.length)return go(cur);playing=true;next()}ui()}
function fwd(){pause();if(idx<seq.length)add(true);ui()}
function scrub(n){pause();clearRows();for(let i=0;i<n;i++)add(false);if(!n)select(-1);ui()}
function back(){scrub(Math.max(0,idx-1))}
</script>
</body>
</html>
