from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

old_css = '''.hero-art{position:relative;height:400px}
.hero-art .tile{
  position:absolute;border-radius:18px;box-shadow:var(--shadow);overflow:hidden;
  background:var(--card);border:1px solid var(--line);
}
.hero-art .t1{inset:0 26% 34% 0;animation:float 9s ease-in-out infinite}
.hero-art .t2{inset:30% 0 12% 34%;animation:float 11s ease-in-out infinite reverse}
.hero-art .t3{width:132px;height:132px;left:2%;bottom:2%;animation:float 8s ease-in-out infinite .8s}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-11px)}}
.hero-art .hero-video-tile{padding:0;border:1px solid var(--line);cursor:pointer;color:inherit;background:var(--card)}
.hero-video-tile:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.hero-video-thumb{width:100%;height:100%;display:block;object-fit:cover;object-position:center;transform:scale(2.35);transition:.45s}
.hero-video-tile:hover .hero-video-thumb{transform:scale(2.42)}
.hero-video-play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:58px;height:58px;border-radius:50%;display:grid;place-items:center;padding-left:4px;background:rgba(255,255,255,.9);color:var(--accent);font-size:19px;box-shadow:0 7px 24px rgba(0,0,0,.2);transition:.2s}
.hero-video-tile:hover .hero-video-play{transform:translate(-50%,-50%) scale(1.06)}'''

new_css = '''.hero-art{position:relative;height:400px}
.hero-showcase{display:flex;align-items:center;justify-content:center}
.hero-rotator{
  position:relative;width:100%;height:100%;padding:0;border:1px solid rgba(168,111,76,.16);
  border-radius:24px;overflow:hidden;cursor:pointer;background:#221d19;color:#fff;
  box-shadow:0 24px 60px rgba(60,44,30,.18);isolation:isolate;
  transition:transform .3s ease,box-shadow .3s ease,border-color .3s ease;
}
.hero-rotator:hover{transform:translateY(-4px);box-shadow:0 30px 72px rgba(60,44,30,.24);border-color:rgba(168,111,76,.35)}
.hero-video-tile:focus-visible{outline:3px solid var(--accent);outline-offset:4px}
.hero-video-thumb{width:100%;height:100%;display:block;object-fit:cover;object-position:center;transform:scale(1.01);transition:opacity .45s ease,transform 7s ease}
.hero-rotator:hover .hero-video-thumb{transform:scale(1.045)}
.hero-rotator::after{content:'';position:absolute;inset:0;z-index:1;pointer-events:none;background:linear-gradient(to top,rgba(19,15,12,.72) 0%,rgba(19,15,12,.18) 38%,transparent 62%)}
.hero-video-play{position:absolute;left:50%;top:50%;z-index:3;transform:translate(-50%,-50%);width:66px;height:66px;border-radius:50%;display:grid;place-items:center;padding-left:4px;background:rgba(255,255,255,.94);color:var(--accent);font-size:21px;box-shadow:0 10px 30px rgba(0,0,0,.28);transition:.22s}
.hero-rotator:hover .hero-video-play{transform:translate(-50%,-50%) scale(1.08)}
.hero-video-info{position:absolute;left:22px;right:22px;bottom:18px;z-index:3;display:flex;align-items:end;justify-content:space-between;gap:18px;text-align:left}
.hero-video-copy{min-width:0}
.hero-video-kicker{display:block;font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;font-weight:700;color:rgba(255,255,255,.72);margin-bottom:3px}
.hero-video-title{display:block;font-size:16px;font-weight:700;line-height:1.35;color:#fff;text-shadow:0 1px 7px rgba(0,0,0,.28);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.hero-video-count{flex:0 0 auto;font-size:11.5px;font-weight:700;letter-spacing:.06em;color:#fff;background:rgba(20,16,13,.42);border:1px solid rgba(255,255,255,.22);padding:5px 9px;border-radius:999px;backdrop-filter:blur(8px)}
.hero-progress{position:absolute;left:0;right:0;bottom:0;height:3px;z-index:4;background:rgba(255,255,255,.16)}
.hero-progress::after{content:'';display:block;height:100%;width:0;background:rgba(255,255,255,.86);animation:heroProgress 5s linear infinite}
.hero-rotator.is-changing .hero-video-thumb{opacity:.18}
@keyframes heroProgress{from{width:0}to{width:100%}}
@media(max-width:1000px){.hero-art{height:min(54vw,430px)}}
@media(max-width:600px){.hero-art{height:58vw;min-height:250px}.hero-rotator{border-radius:18px}.hero-video-info{left:16px;right:16px;bottom:14px}.hero-video-title{font-size:14px}.hero-video-play{width:56px;height:56px;font-size:18px}}'''

if old_css not in s:
    raise SystemExit('Old hero CSS block not found')
s = s.replace(old_css, new_css, 1)

old_html = '''    <div class="hero-art">
      <button class="tile t1 hero-video-tile" type="button" data-gal="0" aria-label="Play 千手觀音・金身醒覺">
        <img class="hero-video-thumb" src="https://i.ytimg.com/vi/TXJ2a91cp6A/hqdefault.jpg" alt="">
        <span class="hero-video-play" aria-hidden="true">▶</span>
      </button>
      <button class="tile t2 hero-video-tile" type="button" data-gal="6" aria-label="Play 千手觀音・金身醒覺">
        <img class="hero-video-thumb" src="https://i.ytimg.com/vi/kjy2rbjisWo/hqdefault.jpg" alt="">
        <span class="hero-video-play" aria-hidden="true">▶</span>
      </button>
      <button class="tile t3 hero-video-tile" type="button" data-gal="5" aria-label="Play 千手觀音・金身醒覺">
        <img class="hero-video-thumb" src="https://i.ytimg.com/vi/x5aTL7C3ZJM/hqdefault.jpg" alt="">
        <span class="hero-video-play" aria-hidden="true">▶</span>
      </button>
    </div>'''

new_html = '''    <div class="hero-art hero-showcase">
      <button class="hero-rotator hero-video-tile" type="button" data-gal="0" aria-label="Play 千手觀音・金身醒覺">
        <img class="hero-video-thumb" src="https://i.ytimg.com/vi/TXJ2a91cp6A/maxresdefault.jpg" alt="千手觀音・金身醒覺">
        <span class="hero-video-play" aria-hidden="true">▶</span>
        <span class="hero-video-info">
          <span class="hero-video-copy">
            <span class="hero-video-kicker"><span class="zh">精選影片</span><span class="en">Featured video</span></span>
            <span class="hero-video-title"><span class="zh">千手觀音・金身醒覺</span><span class="en">Thousand-Armed Guanyin · Awakening</span></span>
          </span>
          <span class="hero-video-count">01 / 12</span>
        </span>
        <span class="hero-progress" aria-hidden="true"></span>
      </button>
    </div>'''

if old_html not in s:
    raise SystemExit('Old hero markup not found')
s = s.replace(old_html, new_html, 1)

old_js = "  $$('.hero-video-tile').forEach(b => b.addEventListener('click', () => openLightbox(+b.dataset.gal)));"
new_js = '''  $$('.hero-video-tile').forEach(b => b.addEventListener('click', () => openLightbox(+b.dataset.gal)));

  /* ---------- ROTATING HERO VIDEO ---------- */
  const heroRotator = $('.hero-rotator');
  let heroTimer = null;
  let heroPos = 0;
  const heroVideoIndexes = GALLERY.map((g,i)=>g.kind==='video' && g.youtube ? i : -1).filter(i=>i>=0);
  function showHeroVideo(pos){
    if (!heroRotator || !heroVideoIndexes.length) return;
    heroPos = (pos + heroVideoIndexes.length) % heroVideoIndexes.length;
    const gi = heroVideoIndexes[heroPos];
    const g = GALLERY[gi];
    const img = $('.hero-video-thumb', heroRotator);
    const title = $('.hero-video-title', heroRotator);
    const count = $('.hero-video-count', heroRotator);
    heroRotator.classList.add('is-changing');
    setTimeout(()=>{
      heroRotator.dataset.gal = gi;
      heroRotator.setAttribute('aria-label','Play '+(g.title.zh || g.title.en || 'video'));
      img.src = 'https://i.ytimg.com/vi/'+g.youtube+'/maxresdefault.jpg';
      img.alt = g.title.zh || g.title.en || '';
      title.innerHTML = '<span class="zh">'+esc(g.title.zh || '')+'</span><span class="en">'+esc(g.title.en || g.title.zh || '')+'</span>';
      count.textContent = String(heroPos+1).padStart(2,'0')+' / '+String(heroVideoIndexes.length).padStart(2,'0');
      heroRotator.classList.remove('is-changing');
    },220);
  }
  function startHeroRotation(){
    if (!heroRotator || heroVideoIndexes.length < 2) return;
    clearInterval(heroTimer);
    heroTimer = setInterval(()=>showHeroVideo(heroPos+1),5000);
  }
  if (heroRotator){
    heroRotator.addEventListener('mouseenter',()=>clearInterval(heroTimer));
    heroRotator.addEventListener('mouseleave',startHeroRotation);
    heroRotator.addEventListener('focus',()=>clearInterval(heroTimer));
    heroRotator.addEventListener('blur',startHeroRotation);
    startHeroRotation();
  }'''

if old_js not in s:
    raise SystemExit('Hero click handler not found')
s = s.replace(old_js, new_js, 1)

path.write_text(s, encoding='utf-8')

check = path.read_text(encoding='utf-8')
for required in ('hero-rotator','ROTATING HERO VIDEO','heroVideoIndexes','maxresdefault.jpg','hero-video-count'):
    if required not in check:
        raise SystemExit('Missing after update: '+required)
if 'transform:scale(2.35)' in check:
    raise SystemExit('Old blurry hero scaling still present')
print('Hero showcase upgrade verified')
