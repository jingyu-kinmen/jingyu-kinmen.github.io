from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# Remove gallery entries that have no real attached media. They begin with the
# empty Inn Room Tour entry and continue to the end of GALLERY.
start = text.find("  {kind:'video', youtube:'', src:'', img:'',")
end = text.find("\n];", start)
if start < 0 or end < 0:
    raise SystemExit('gallery placeholder section not found')
text = text[:start] + text[end:]

# Remove the sample shop products that only rendered gradient placeholders.
products_start = text.find('const PRODUCTS = [')
first_real_product = text.find("  {cat:'other', img:'nobel-card.jpg'", products_start)
if products_start < 0 or first_real_product < 0:
    raise SystemExit('real product section not found')
text = text[:products_start] + 'const PRODUCTS = [\n' + text[first_real_product:]

# Remove now-empty gallery category buttons.
old = """  const galFilterDefs = [
    ['all',   {zh:'全部',en:'All'}],
    ['video', {zh:'影片',en:'Video'}],
    ['music', {zh:'音樂',en:'Music'}],
    ['photo', {zh:'攝影',en:'Photo'}]
  ];"""
new = """  const galFilterDefs = [
    ['all',   {zh:'全部',en:'All'}],
    ['video', {zh:'影片',en:'Video'}]
  ];"""
if old not in text:
    raise SystemExit('gallery filters not found')
text = text.replace(old, new, 1)

# Remove now-empty shop category buttons.
old = """  const shopFilterDefs = [
    ['all',      {zh:'全部',en:'All'}],
    ['cosmetic', {zh:'保養彩妝',en:'Skincare'}],
    ['jewelry',  {zh:'飾品',en:'Jewellery'}],
    ['other',    {zh:'其他',en:'Other'}]
  ];"""
new = """  const shopFilterDefs = [
    ['all',      {zh:'全部',en:'All'}],
    ['other',    {zh:'其他',en:'Other'}]
  ];"""
if old not in text:
    raise SystemExit('shop filters not found')
text = text.replace(old, new, 1)

text = text.replace(
    '<h2><span class="zh">保養與飾品</span><span class="en">Skincare &amp; Jewellery</span></h2>',
    '<h2><span class="zh">精選商品</span><span class="en">Selected Products</span></h2>',
    1,
)

# Verify real content remains.
for required in ('TXJ2a91cp6A', '3GBoOLpQ43s', 'nobel-card.jpg', 'ginger-poster.png', 'music-medicine-card.svg'):
    if required not in text:
        raise SystemExit('required real item missing: ' + required)

# Verify exact placeholder entries are gone without matching unrelated text elsewhere.
removed_markers = (
    "title:{zh:'客棧・房間巡禮'",
    "title:{zh:'風獅爺（Demo）'",
    "title:{zh:'夜裡的市民大道'",
    "title:{zh:'前水頭・老厝'",
    "title:{zh:'退潮'",
    "title:{zh:'信義路四段'",
    "title:{zh:'客棧的早餐桌'",
    "title:{zh:'替代役的下午'",
    "name:{zh:'保濕精華 30ml'",
    "name:{zh:'溫和潔顏慕斯'",
    "name:{zh:'修護面霜 50ml'",
    "name:{zh:'防曬乳 SPF50+'",
    "name:{zh:'925 銀細鍊項鍊'",
    "name:{zh:'珍珠耳環'",
    "name:{zh:'手工銀戒'",
    "name:{zh:'金門風獅爺明信片組'",
)
for marker in removed_markers:
    if marker in text:
        raise SystemExit('placeholder still present: ' + marker)

path.write_text(text, encoding='utf-8')
print('Placeholder cleanup verified')
