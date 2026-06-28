from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>THREAD — Clothing</title>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

    :root {
      --ink:     #1a1a18;
      --cream:   #f5f2ec;
      --stone:   #c8c0b4;
      --rust:    #b85c38;
      --mist:    #e8e3db;
      --display: 'Cormorant Garamond', serif;
      --body:    'DM Sans', sans-serif;
    }

    html { scroll-behavior: smooth; }

    body {
      background: var(--cream);
      color: var(--ink);
      font-family: var(--body);
      font-weight: 300;
      line-height: 1.6;
    }

    /* ── NAV ── */
    nav {
      position: fixed; top: 0; width: 100%; z-index: 100;
      display: flex; align-items: center; justify-content: space-between;
      padding: 1.4rem 3rem;
      background: rgba(245,242,236,0.92);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--mist);
    }
    .nav-logo {
      font-family: var(--display);
      font-size: 1.6rem;
      font-weight: 300;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--ink);
      text-decoration: none;
    }
    .nav-links { display: flex; gap: 2.4rem; list-style: none; }
    .nav-links a {
      text-decoration: none; color: var(--ink);
      font-size: 0.8rem; letter-spacing: 0.12em; text-transform: uppercase;
      transition: color 0.2s;
    }
    .nav-links a:hover { color: var(--rust); }

    /* ── HERO ── */
    .hero {
      min-height: 100vh;
      display: grid; grid-template-columns: 1fr 1fr;
      padding-top: 5rem;
    }
    .hero-text {
      display: flex; flex-direction: column; justify-content: center;
      padding: 4rem 4rem 4rem 3rem;
    }
    .hero-eyebrow {
      font-size: 0.72rem; letter-spacing: 0.3em; text-transform: uppercase;
      color: var(--rust); margin-bottom: 1.2rem;
    }
    .hero-headline {
      font-family: var(--display);
      font-size: clamp(3.5rem, 6vw, 6rem);
      font-weight: 300;
      line-height: 1.05;
      margin-bottom: 1.8rem;
    }
    .hero-headline em { font-style: italic; color: var(--rust); }
    .hero-sub {
      font-size: 0.95rem; color: #6b6560; max-width: 34ch;
      margin-bottom: 2.8rem; line-height: 1.8;
    }
    .btn {
      display: inline-block;
      padding: 0.85rem 2.4rem;
      border: 1px solid var(--ink);
      text-decoration: none; color: var(--ink);
      font-size: 0.78rem; letter-spacing: 0.18em; text-transform: uppercase;
      transition: background 0.25s, color 0.25s;
    }
    .btn:hover { background: var(--ink); color: var(--cream); }
    .btn-fill {
      background: var(--ink); color: var(--cream);
    }
    .btn-fill:hover { background: var(--rust); border-color: var(--rust); }

    .hero-image {
      background: var(--mist);
      position: relative; overflow: hidden;
    }
    .hero-image-inner {
      width: 100%; height: 100%;
      background: linear-gradient(135deg, #d6cfc6 0%, #c5bdb3 50%, #b8b0a6 100%);
      display: flex; align-items: center; justify-content: center;
    }
    .hero-image-placeholder {
      font-family: var(--display);
      font-size: 7rem; opacity: 0.18; user-select: none;
    }
    .hero-badge {
      position: absolute; bottom: 2rem; left: -1rem;
      background: var(--cream); padding: 1.2rem 1.6rem;
      border-left: 3px solid var(--rust);
    }
    .hero-badge strong {
      display: block; font-family: var(--display);
      font-size: 1.8rem; font-weight: 300;
    }
    .hero-badge span { font-size: 0.72rem; letter-spacing: 0.15em; text-transform: uppercase; color: #888; }

    /* ── MARQUEE ── */
    .marquee-wrap {
      overflow: hidden; background: var(--ink); padding: 0.9rem 0;
    }
    .marquee {
      display: flex; gap: 3rem;
      animation: scroll 22s linear infinite; white-space: nowrap;
    }
    .marquee span {
      font-size: 0.72rem; letter-spacing: 0.25em; text-transform: uppercase;
      color: var(--stone); flex-shrink: 0;
    }
    .marquee span.accent { color: var(--rust); }
    @keyframes scroll { from { transform: translateX(0); } to { transform: translateX(-50%); } }

    /* ── SECTION HEADER ── */
    .section { padding: 6rem 3rem; }
    .section-header { margin-bottom: 3.5rem; }
    .section-label {
      font-size: 0.72rem; letter-spacing: 0.3em; text-transform: uppercase;
      color: var(--rust); margin-bottom: 0.6rem;
    }
    .section-title {
      font-family: var(--display);
      font-size: clamp(2.2rem, 4vw, 3.2rem); font-weight: 300;
    }

    /* ── PRODUCT GRID ── */
    .product-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 2rem;
    }
    .product-card {
      cursor: pointer;
    }
    .product-card:hover .product-img { transform: scale(1.03); }
    .product-img-wrap {
      overflow: hidden; background: var(--mist);
      aspect-ratio: 3/4; margin-bottom: 1rem;
    }
    .product-img {
      width: 100%; height: 100%;
      display: flex; align-items: center; justify-content: center;
      transition: transform 0.5s cubic-bezier(.25,.46,.45,.94);
      font-size: 4.5rem;
    }
    .product-name {
      font-size: 0.9rem; letter-spacing: 0.04em; margin-bottom: 0.25rem;
    }
    .product-meta {
      display: flex; justify-content: space-between; align-items: center;
    }
    .product-price {
      font-family: var(--display); font-size: 1.1rem;
    }
    .product-tag {
      font-size: 0.68rem; letter-spacing: 0.12em; text-transform: uppercase;
      color: var(--rust);
    }

    /* ── EDITORIAL ── */
    .editorial {
      background: var(--ink); color: var(--cream);
      display: grid; grid-template-columns: 1fr 1fr;
      min-height: 50vh;
    }
    .editorial-text {
      padding: 5rem 4rem;
      display: flex; flex-direction: column; justify-content: center;
    }
    .editorial-text .section-label { color: var(--stone); }
    .editorial-text .section-title { color: var(--cream); margin-bottom: 1.2rem; }
    .editorial-text p { color: var(--stone); font-size: 0.95rem; line-height: 1.9; margin-bottom: 2rem; }
    .editorial-visual {
      background: #2a2a28;
      display: flex; align-items: center; justify-content: center;
      font-family: var(--display); font-size: 9rem;
      opacity: 0.15;
    }

    /* ── CATEGORIES ── */
    .categories { background: var(--mist); }
    .cat-grid {
      display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem;
    }
    .cat-card {
      background: var(--cream); padding: 2.5rem 2rem;
      border-bottom: 2px solid transparent;
      transition: border-color 0.2s, transform 0.2s;
      cursor: pointer;
    }
    .cat-card:hover { border-color: var(--rust); transform: translateY(-4px); }
    .cat-icon { font-size: 2.2rem; margin-bottom: 1rem; }
    .cat-name {
      font-family: var(--display);
      font-size: 1.5rem; font-weight: 300; margin-bottom: 0.4rem;
    }
    .cat-count { font-size: 0.78rem; color: #888; letter-spacing: 0.1em; }

    /* ── NEWSLETTER ── */
    .newsletter {
      text-align: center; padding: 6rem 3rem;
      border-top: 1px solid var(--mist);
    }
    .newsletter .section-title { margin-bottom: 0.8rem; }
    .newsletter p { color: #888; font-size: 0.92rem; margin-bottom: 2rem; }
    .email-form {
      display: flex; gap: 0; max-width: 440px; margin: 0 auto;
    }
    .email-form input {
      flex: 1; padding: 0.85rem 1.2rem;
      border: 1px solid var(--stone); border-right: none;
      background: transparent; font-family: var(--body); font-size: 0.88rem;
      outline: none; color: var(--ink);
    }
    .email-form input::placeholder { color: var(--stone); }
    .email-form button {
      padding: 0.85rem 1.8rem;
      background: var(--ink); color: var(--cream);
      border: 1px solid var(--ink); cursor: pointer;
      font-family: var(--body); font-size: 0.78rem;
      letter-spacing: 0.15em; text-transform: uppercase;
      transition: background 0.2s;
    }
    .email-form button:hover { background: var(--rust); border-color: var(--rust); }

    /* ── FOOTER ── */
    footer {
      background: var(--ink); color: var(--stone);
      padding: 3rem; text-align: center;
      font-size: 0.78rem; letter-spacing: 0.1em;
    }
    footer .footer-logo {
      font-family: var(--display); font-size: 1.8rem; color: var(--cream);
      letter-spacing: 0.25em; text-transform: uppercase;
      display: block; margin-bottom: 1rem;
    }

    /* ── RESPONSIVE ── */
    @media (max-width: 768px) {
      nav { padding: 1.2rem 1.5rem; }
      .nav-links { display: none; }
      .hero { grid-template-columns: 1fr; }
      .hero-image { min-height: 45vh; }
      .hero-text { padding: 3rem 1.5rem; }
      .section { padding: 4rem 1.5rem; }
      .editorial { grid-template-columns: 1fr; }
      .editorial-visual { display: none; }
      .cat-grid { grid-template-columns: 1fr 1fr; }
    }
  </style>
</head>
<body>

<!-- NAV -->
<nav>
  <a class="nav-logo" href="#">Thread</a>
  <ul class="nav-links">
    <li><a href="#new">New In</a></li>
    <li><a href="#categories">Categories</a></li>
    <li><a href="#editorial">Story</a></li>
    <li><a href="#newsletter">Contact</a></li>
  </ul>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-text">
    <p class="hero-eyebrow">SS 2025 Collection</p>
    <h1 class="hero-headline">Wear what<br/>you <em>mean</em><br/>to say.</h1>
    <p class="hero-sub">Considered clothing for people who dress with intention. Natural fabrics, enduring silhouettes, made to last decades not seasons.</p>
    <div style="display:flex; gap:1rem; flex-wrap:wrap;">
      <a href="#new" class="btn btn-fill">Shop New Arrivals</a>
      <a href="#categories" class="btn">Browse Categories</a>
    </div>
  </div>
  <div class="hero-image">
    <div class="hero-image-inner">
      <span class="hero-image-placeholder">✦</span>
    </div>
    <div class="hero-badge">
      <span>Free shipping over</span>
      <strong>₹2,000</strong>
    </div>
  </div>
</section>

<!-- MARQUEE -->
<div class="marquee-wrap">
  <div class="marquee">
    <span>New Collection</span><span class="accent">✦</span>
    <span>Free Returns</span><span class="accent">✦</span>
    <span>Sustainable Fabrics</span><span class="accent">✦</span>
    <span>Handcrafted Pieces</span><span class="accent">✦</span>
    <span>Limited Runs</span><span class="accent">✦</span>
    <span>Made Consciously</span><span class="accent">✦</span>
    <!-- repeat for seamless scroll -->
    <span>New Collection</span><span class="accent">✦</span>
    <span>Free Returns</span><span class="accent">✦</span>
    <span>Sustainable Fabrics</span><span class="accent">✦</span>
    <span>Handcrafted Pieces</span><span class="accent">✦</span>
    <span>Limited Runs</span><span class="accent">✦</span>
    <span>Made Consciously</span><span class="accent">✦</span>
  </div>
</div>

<!-- NEW ARRIVALS -->
<section class="section" id="new">
  <div class="section-header">
    <p class="section-label">Just Landed</p>
    <h2 class="section-title">New Arrivals</h2>
  </div>
  <div class="product-grid">
    {% for p in products %}
    <div class="product-card">
      <div class="product-img-wrap">
        <div class="product-img" style="background:{{ p.bg }}">{{ p.icon }}</div>
      </div>
      <p class="product-name">{{ p.name }}</p>
      <div class="product-meta">
        <span class="product-price">₹{{ p.price }}</span>
        <span class="product-tag">{{ p.tag }}</span>
      </div>
    </div>
    {% endfor %}
  </div>
</section>

<!-- CATEGORIES -->
<section class="section categories" id="categories">
  <div class="section-header">
    <p class="section-label">Explore</p>
    <h2 class="section-title">Shop by Category</h2>
  </div>
  <div class="cat-grid">
    {% for c in categories %}
    <div class="cat-card">
      <div class="cat-icon">{{ c.icon }}</div>
      <div class="cat-name">{{ c.name }}</div>
      <div class="cat-count">{{ c.count }} pieces</div>
    </div>
    {% endfor %}
  </div>
</section>

<!-- EDITORIAL -->
<section class="editorial" id="editorial">
  <div class="editorial-text">
    <p class="section-label">Our Philosophy</p>
    <h2 class="section-title">Fewer things,<br/>better made.</h2>
    <p>We work with small mills and family weavers across India to produce cloth that wears in, not out. Every piece in the Thread collection is designed to be the last one you'll ever need to buy of that kind.</p>
    <a href="#" class="btn" style="border-color:var(--stone); color:var(--stone); align-self:flex-start;">Read Our Story</a>
  </div>
  <div class="editorial-visual">✦</div>
</section>

<!-- NEWSLETTER -->
<section class="newsletter" id="newsletter">
  <p class="section-label" style="margin-bottom:0.6rem;">Stay Close</p>
  <h2 class="section-title">New drops, no noise.</h2>
  <p>Seasonal collections and studio notes — straight to your inbox.</p>
  <div class="email-form">
    <input type="email" placeholder="your@email.com" />
    <button type="button">Subscribe</button>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <span class="footer-logo">Thread</span>
  &copy; 2025 Thread Clothing Co. — Made with care in India.
</footer>

</body>
</html>
"""

PRODUCTS = [
    {"name": "Linen Overshirt", "price": "3,490", "tag": "New", "icon": "👕", "bg": "#ddd6cc"},
    {"name": "Wide Leg Trouser", "price": "4,290", "tag": "Bestseller", "icon": "👖", "bg": "#cfc8be"},
    {"name": "Cotton Midi Dress", "price": "5,190", "tag": "New", "icon": "👗", "bg": "#d8d2c8"},
    {"name": "Structured Blazer", "price": "7,890", "tag": "Limited", "icon": "🧥", "bg": "#c8c0b6"},
    {"name": "Relaxed Tee", "price": "1,890", "tag": "Essentials", "icon": "👕", "bg": "#e0d9d0"},
    {"name": "Kantha Jacket", "price": "9,490", "tag": "Handmade", "icon": "🧣", "bg": "#d0c9bf"},
    {"name": "Slip Skirt", "price": "2,990", "tag": "New", "icon": "👗", "bg": "#dcd5cb"},
    {"name": "Cargo Shorts", "price": "2,490", "tag": "Summer", "icon": "🩳", "bg": "#ccc4ba"},
]

CATEGORIES = [
    {"name": "Tops",       "icon": "👕", "count": 42},
    {"name": "Bottoms",    "icon": "👖", "count": 31},
    {"name": "Dresses",    "icon": "👗", "count": 28},
    {"name": "Outerwear",  "icon": "🧥", "count": 19},
    {"name": "Accessories","icon": "🧣", "count": 24},
    {"name": "Essentials", "icon": "✦",  "count": 15},
]


@app.route("/")
def index():
    return render_template_string(HTML, products=PRODUCTS, categories=CATEGORIES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
