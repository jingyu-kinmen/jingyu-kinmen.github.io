from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Clean contact settings and set LINE ID as well.
s, n = re.subn(
    r"const CONTACT\s*=\s*\{.*?\};",
    "const CONTACT = {\n  email: 'gods32166@gmail.com',\n  tel:   '0976336678',\n  line:  'gods32166'\n};",
    s, count=1, flags=re.S
)
if n != 1:
    raise SystemExit('CONTACT object cleanup failed')

# Make the existing selected-items text itself act as the cart button, instead of adding a third control.
if '#cartTxt{cursor:pointer' not in s:
    s = s.replace('/* ---------- CART DRAWER + QUICK CONTACT ---------- */',
                  '/* ---------- CART DRAWER + QUICK CONTACT ---------- */\n#cartTxt{cursor:pointer;user-select:none;font-weight:700}#cartTxt::before{content:"🛒 ";}#cartTxt:focus-visible{outline:2px solid #fff;outline-offset:4px;border-radius:6px}',1)

old_sync = """  function syncCartManageBtn(){
    if (!cartManageBtn) return;
    const n = cartTotalQty();
    cartManageBtn.innerHTML = lang==='zh' ? '🛒 購物車 '+n+' 件' : '🛒 Cart '+n;
  }"""
new_sync = """  function syncCartManageBtn(){
    const el = $('#cartTxt');
    if (!el) return;
    const n = cartTotalQty();
    el.setAttribute('aria-label', lang==='zh' ? '開啟購物車，共 '+n+' 件商品' : 'Open cart, '+n+' items');
  }"""
if old_sync in s:
    s=s.replace(old_sync,new_sync,1)

old_create = """    const cartGo = $('#cartGo');
    if (cartGo && cartGo.parentElement){
      cartManageBtn = document.createElement('button');
      cartManageBtn.id = 'cartManageBtn';
      cartManageBtn.type = 'button';
      cartManageBtn.className = 'cart-manage-btn';
      cartGo.parentElement.insertBefore(cartManageBtn, cartGo);
      cartManageBtn.addEventListener('click', openCartDrawer);
    }

    $('#cartDrawerClose').addEventListener('click', closeCartDrawer);"""
new_create = """    const cartTxt = $('#cartTxt');
    if (cartTxt){
      cartTxt.setAttribute('role','button');
      cartTxt.setAttribute('tabindex','0');
      cartTxt.addEventListener('click', openCartDrawer);
      cartTxt.addEventListener('keydown', e => { if (e.key==='Enter' || e.key===' ') { e.preventDefault(); openCartDrawer(); } });
    }

    $('#cartDrawerClose').addEventListener('click', closeCartDrawer);"""
if old_create not in s:
    raise SystemExit('Old cart button creation block not found')
s=s.replace(old_create,new_create,1)

# Gmail in the quick-contact panel opens Gmail compose directly.
s=s.replace('href="mailto:gods32166@gmail.com"><b>Gmail</b>',
            'href="https://mail.google.com/mail/?view=cm&fs=1&to=gods32166%40gmail.com" target="_blank" rel="noopener"><b>Gmail</b>',1)

# Verification
for needle in ['line:  \'gods32166\'','#cartTxt{cursor:pointer','cartTxt.addEventListener(\'click\', openCartDrawer)','gods32166%40gmail.com']:
    if needle not in s:
        raise SystemExit('Missing refinement: '+needle)

p.write_text(s,encoding='utf-8')
print('Cart trigger and contact settings refined.')
