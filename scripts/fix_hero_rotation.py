from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
old = '''  function startHeroRotation(){
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
new = '''  function startHeroRotation(){
    if (!heroRotator || heroVideoIndexes.length < 2) return;
    clearTimeout(heroTimer);
    const tick = () => {
      showHeroVideo(heroPos+1);
      heroTimer = setTimeout(tick,5000);
    };
    heroTimer = setTimeout(tick,5000);
  }
  if (heroRotator){
    /* Keep rotating even when the mouse is resting over the card. */
    startHeroRotation();
    document.addEventListener('visibilitychange',()=>{
      if (document.hidden) clearTimeout(heroTimer);
      else startHeroRotation();
    });
  }'''
if old not in s:
    raise SystemExit('Old hero rotation block not found')
s = s.replace(old,new,1)
# Make the progress bar clearly restart every slide by toggling a class on the whole rotator.
s = s.replace("      heroRotator.classList.remove('is-changing');\n    },220);", "      heroRotator.classList.remove('is-changing');\n      heroRotator.classList.remove('restart-progress');\n      void heroRotator.offsetWidth;\n      heroRotator.classList.add('restart-progress');\n    },220);", 1)
s = s.replace(".hero-progress::after{content:'';display:block;height:100%;width:0;background:rgba(255,255,255,.86);animation:heroProgress 5s linear infinite}", ".hero-progress::after{content:'';display:block;height:100%;width:0;background:rgba(255,255,255,.86);animation:heroProgress 5s linear infinite}\n.hero-rotator.restart-progress .hero-progress::after{animation:none}\n.hero-rotator.restart-progress .hero-progress::after{animation:heroProgress 5s linear infinite}", 1)
p.write_text(s,encoding='utf-8')
print('hero rotation fixed')
