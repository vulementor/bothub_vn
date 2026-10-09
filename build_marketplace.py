import os
from pathlib import Path

ROOT = Path(__file__).parent

def get_header(active_key=''):
    nav_html = f'''
    <a class="nav-link {'active' if active_key == 'home' else ''}" href="index.html">Trang chủ</a>
    
    <!-- AI Agent Dropdown (chứa ChatGPT, Claude AI, Gemini AI) -->
    <div class="nav-dropdown">
      <a class="nav-link {'active' if active_key in ['agent', 'chatgpt', 'claude', 'gemini'] else ''}" href="ai-agent.html" style="display:inline-flex;align-items:center;gap:3px;">
        AI Agent <span style="font-size:10px;opacity:0.8;">▾</span>
      </a>
      <div class="nav-dropdown-menu">
        <a class="dropdown-item" href="ai-agent.html">
          <span class="dot" style="background:var(--cyan);"></span>
          <div><b>Tất Cả AI Agent</b><br><small style="color:#64748b;font-size:11px;">Xem toàn bộ danh mục công cụ</small></div>
        </a>
        <div style="height:1px;background:rgba(255,255,255,0.06);margin:4px 0;"></div>
        <a class="dropdown-item" href="chatgpt.html">
          <span class="dot" style="background:#10b981;"></span>
          <div><b>ChatGPT Plus & Team</b><br><small style="color:#64748b;font-size:11px;">Chính chủ email · o1/o3 reasoning</small></div>
        </a>
        <a class="dropdown-item" href="claude-ai.html">
          <span class="dot" style="background:#f59e0b;"></span>
          <div><b>Claude AI Pro</b><br><small style="color:#64748b;font-size:11px;">Sonnet 3.7 · Vua code & viết lách</small></div>
        </a>
        <a class="dropdown-item" href="gemini-ai.html">
          <span class="dot" style="background:#3b82f6;"></span>
          <div><b>Gemini Advanced 2TB</b><br><small style="color:#64748b;font-size:11px;">Google One AI Premium · 2000GB</small></div>
        </a>
      </div>
    </div>

    <a class="nav-link {'active' if active_key == 'muse' else ''}" href="muse-ai.html">Muse AI<span class="nav-badge-hot">69k</span></a>
    <a class="nav-link {'active' if active_key == 'grok' else ''}" href="grok-bot.html">Grok Bot</a>
    
    <!-- Trang Invite Code -->
    <a class="nav-link {'active' if active_key == 'invite' else ''}" href="ma-invite.html">Invite Code</a>

    <a class="nav-link {'active' if active_key == 'prompts' else ''}" href="thu-vien-prompt.html">Kho Prompt</a>
    <a class="nav-link {'active' if active_key == 'compare' else ''}" href="so-sanh.html">So sánh AI</a>
    '''

    drawer_html = f'''
    <a href="index.html">Trang chủ</a>
    <a href="ai-agent.html" style="font-weight:700;color:#fff;">AI Agent (Tất cả công cụ)</a>
    <div class="mobile-subnav">
      <a href="chatgpt.html">↳ ChatGPT Plus & Team</a>
      <a href="claude-ai.html">↳ Claude AI Pro (Sonnet 3.7)</a>
      <a href="gemini-ai.html">↳ Gemini Advanced 2TB</a>
    </div>
    <a href="muse-ai.html">Muse AI (Gói 1 Tỷ & 31 Tỷ Token) 🔥</a>
    <a href="grok-bot.html">Grok Bot Autonomous</a>
    <a href="ma-invite.html">Invite Code</a>
    <a href="thu-vien-prompt.html">Kho Prompt Mẫu</a>
    <a href="so-sanh.html">So Sánh AI</a>
    '''

    return f'''
    <!-- Top notification & guarantee -->
    <div class="top-bar">
      <div class="container">
        <div>
          <span class="flash-badge">FLASH SALE</span>
          <span>🔥 Siêu ưu đãi tháng này: Giảm đến 75% các gói <strong>Muse AI, Grok Bot, ChatGPT Plus</strong> · Kích hoạt siêu tốc trong 5 phút!</span>
        </div>
        <div class="top-links">
          <a href="ma-invite.html">🎁 Nhận 1 Tỷ Token Muse Free</a>
          <a href="chinh-sach.html">🛡️ Bảo hành 1 đổi 1</a>
          <a href="https://zalo.me/0388888888" target="_blank" rel="noopener">💬 Zalo: 0388.888.888</a>
        </div>
      </div>
    </div>

    <!-- Main Header -->
    <header class="header">
      <div class="container head-inner">
        <a href="index.html" class="logo" aria-label="BotHub.vn Marketplace">
          <div class="logo-icon">✦</div>
          <div class="logo-text">BotHub<span>.vn</span></div>
          <span class="logo-sub">MARKETPLACE</span>
        </a>

        <nav aria-label="Điều hướng chính">
          {nav_html}
        </nav>

        <div class="head-actions">
          <div class="search-bar">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.3-4.3"></path></svg>
            <input type="text" placeholder="Tìm kiếm AI, tool..." onkeydown="if(event.key==='Enter')window.location.href='ai-agent.html?q='+encodeURIComponent(this.value)">
          </div>

          <a href="gio-hang.html" class="cart-btn" aria-label="Giỏ hàng">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
            <span>Giỏ hàng</span>
            <span class="cart-badge">0</span>
          </a>

          <a href="https://zalo.me/0388888888" target="_blank" rel="noopener" class="btn-hotline">
            <span>💬 Hỗ Trợ Zalo</span>
          </a>

          <button type="button" class="mobile-toggle" id="mobile-toggle" aria-label="Menu">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12h16M4 6h16M4 18h16"/></svg>
          </button>
        </div>
      </div>
      <div class="mobile-drawer" id="mobile-drawer">
        {drawer_html}
        <a href="gio-hang.html">🛒 Giỏ hàng (<span class="cart-badge">0</span>)</a>
        <a href="https://zalo.me/0388888888" target="_blank">💬 Tư vấn Zalo 24/7</a>
      </div>
    </header>
    '''

def get_footer():
    return '''
    <!-- Guarantee Promise Strip -->
    <div class="container">
      <div class="promise-strip">
        <div class="promise-grid">
          <div class="promise-box">
            <div class="p-icon">⚡</div>
            <div>
              <h4>Kích Hoạt Siêu Tốc 5P</h4>
              <p>Hệ thống tự động kích hoạt tài khoản qua email của bạn chỉ sau 3-5 phút thanh toán.</p>
            </div>
          </div>
          <div class="promise-box">
            <div class="p-icon">🛡️</div>
            <div>
              <h4>Bảo Hành 1 Đổi 1 Trọn Đời</h4>
              <p>Cam kết bảo hành đầy đủ thời gian sử dụng. Đổi mới hoặc hoàn tiền 100% nếu có lỗi.</p>
            </div>
          </div>
          <div class="promise-box">
            <div class="p-icon">💰</div>
            <div>
              <h4>Tiết Kiệm Đến 80%</h4>
              <p>Mức giá đại lý tốt nhất thị trường, không cần thẻ visa quốc tế hay thủ tục rườm rà.</p>
            </div>
          </div>
          <div class="promise-box">
            <div class="p-icon">🤝</div>
            <div>
              <h4>Hỗ Trợ Kỹ Thuật 24/7</h4>
              <p>Đội ngũ chuyên gia AI hỗ trợ cài đặt, kết nối API và tối ưu prompt bất cứ lúc nào.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Footer -->
    <footer class="footer">
      <div class="container">
        <div class="footer-grid">
          <div class="footer-brand">
            <a href="index.html" class="logo">
              <div class="logo-icon">✦</div>
              <div class="logo-text">BotHub<span>.vn</span></div>
            </a>
            <p>BotHub.vn là nền tảng thương mại cung cấp công cụ & tài khoản AI hàng đầu Việt Nam. Giúp cá nhân và doanh nghiệp tiếp cận các siêu trí tuệ nhân tạo (Muse, Grok, Claude, ChatGPT, Gemini) với chi phí rẻ nhất và sự bảo đảm cao nhất.</p>
            <div style="font-size:13px;color:#94a3b8;display:grid;gap:6px;">
              <div>📍 <strong>Văn phòng:</strong> Tòa nhà Landmark 81, TP. Hồ Chí Minh</div>
              <div>📞 <strong>Hotline/Zalo:</strong> 0388.888.888 (Hỗ trợ 24/7)</div>
              <div>✉️ <strong>Email:</strong> hotro@bothub.vn</div>
            </div>
          </div>

          <div class="footer-col">
            <h4>Sản Phẩm Nổi Bật</h4>
            <ul>
              <li><a href="muse-ai.html">Muse AI (1 Tỷ & 31 Tỷ Token)</a></li>
              <li><a href="grok-bot.html">Grok Bot Autonomous</a></li>
              <li><a href="chatgpt.html">ChatGPT Plus & Team</a></li>
              <li><a href="claude-ai.html">Claude Pro Sonnet 3.7</a></li>
              <li><a href="gemini-ai.html">Gemini Advanced 2TB</a></li>
              <li><a href="ai-agent.html">Tất cả AI Agent ↗</a></li>
            </ul>
          </div>

          <div class="footer-col">
            <h4>Tài Nguyên & Công Cụ</h4>
            <ul>
              <li><a href="thu-vien-prompt.html">Kho 1000+ Prompt Miễn Phí</a></li>
              <li><a href="so-sanh.html">Bảng So Sánh Các AI Model</a></li>
              <li><a href="chinh-sach.html">Chính Sách Bảo Hành 1-1</a></li>
              <li><a href="gio-hang.html">Giỏ Hàng & Đơn Hàng</a></li>
              <li><a href="chinh-sach.html">Hướng Dẫn Thanh Toán VietQR</a></li>
            </ul>
          </div>

          <div class="footer-col">
            <h4>Phương Thức Thanh Toán</h4>
            <p style="font-size:12.5px;color:#94a3b8;margin-bottom:12px;">Hỗ trợ chuyển khoản ngân hàng tự động qua VietQR, thẻ nội địa, MoMo và ZaloPay.</p>
            <div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:15px;">
              <span class="badge badge-cyan">VietQR 24/7</span>
              <span class="badge badge-purple">MoMo Pay</span>
              <span class="badge badge-green">MB Bank</span>
              <span class="badge badge-hot">Thẻ Nội Địa</span>
            </div>
            <div style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);padding:12px;border-radius:10px;font-size:11.5px;color:#94a3b8;">
              🔒 Giao dịch được mã hóa an toàn 100%. Thông tin tài khoản được gửi tự động và bảo mật tuyệt đối.
            </div>
          </div>
        </div>

        <div class="footer-bottom">
          <div>© 2026 BotHub.vn - Nền Tảng Cung Cấp Tài Khoản & Công Cụ AI Số 1 Việt Nam. All rights reserved.</div>
          <div style="display:flex;gap:15px;">
            <a href="chinh-sach.html">Điều khoản sử dụng</a>
            <a href="chinh-sach.html">Chính sách bảo mật</a>
            <a href="chinh-sach.html">Quy định hoàn tiền</a>
          </div>
        </div>
      </div>
    </footer>

    <!-- Floating Contact Widgets -->
    <div class="floating-widget">
      <a href="https://zalo.me/0388888888" target="_blank" rel="noopener" class="floating-btn zalo" title="Chat Zalo ngay">Zalo</a>
      <a href="tel:0388888888" class="floating-btn hotline" title="Gọi Hotline: 0388.888.888">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      </a>
    </div>

    <script src="assets/app.js"></script>
    '''

def render_page(title, desc, body_html, active_key=''):
    return f'''<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | BotHub.vn - Marketplace Công Cụ AI</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#070a13">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
  {get_header(active_key)}
  <main>
    {body_html}
  </main>
  {get_footer()}
</body>
</html>'''

# Product Card Component Generator
def product_card(prod_id, title, brand, tag, icon, icon_class, desc, specs, old_price, new_price, cat, badge_text, detail_url):
    specs_html = ''.join([f'<span class="spec-chip">{s}</span>' for s in specs])
    return f'''
    <article class="product-card" data-category="{cat}">
      <div class="card-top">
        <div class="prod-brand-icon {icon_class}">{icon}</div>
        <span class="badge badge-hot">{badge_text}</span>
      </div>
      <div class="card-content">
        <div class="card-tagline">{tag}</div>
        <h3><a href="{detail_url}">{title}</a></h3>
        <p class="card-desc">{desc}</p>
        <div class="prod-specs">
          {specs_html}
        </div>
        <div class="card-pricing-bar">
          <div class="price-col">
            <del>{old_price}</del>
            <span class="current-price">{new_price}</span>
          </div>
          <div class="card-actions">
            <button type="button" class="btn btn-outline btn-sm" onclick="window.__addToCart('{prod_id}')" title="Thêm vào giỏ">🛒</button>
            <button type="button" class="btn btn-primary btn-sm" onclick="window.__openCheckout('{prod_id}')">⚡ Mua Ngay</button>
          </div>
        </div>
      </div>
    </article>
    '''

# =========================================================================
# 1. INDEX.HTML (HOMEPAGE MARKETPLACE)
# =========================================================================
home_content = f'''
<div class="hero-section">
  <div class="container hero-grid">
    <div class="hero-left">
      <div class="hero-eyebrow">
        <span class="dot"></span>
        <span>SIÊU THỊ CÔNG CỤ & TÀI KHOẢN AI SỐ 1 VIỆT NAM</span>
      </div>
      <h1 class="hero-title">
        Giải Phóng Sức Lao Động.<br>
        <span class="gradient-text">X10 Hiệu Suất Cùng Siêu AI.</span>
      </h1>
      <p class="hero-desc">
        Sở hữu trọn bộ công cụ AI đỉnh cao: <strong>Muse AI, Grok Bot, ChatGPT Plus, Claude Pro, Gemini Advanced</strong>. Kích hoạt tự động sau 5 phút, bảo hành 1 đổi 1 trọn gói, tiết kiệm đến 80% chi phí.
      </p>
      <div class="hero-features">
        <div class="hero-feat-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
          <span>Kích hoạt tự động 3-5 phút</span>
        </div>
        <div class="hero-feat-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
          <span>Bảo hành 1 đổi 1 suốt thời gian dùng</span>
        </div>
        <div class="hero-feat-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
          <span>Thanh toán VietQR tiện lợi không cần visa</span>
        </div>
      </div>
      <div class="hero-ctas">
        <a href="#flagship-products" class="btn btn-primary btn-lg">Khám Phá Các Gói Hot ⚡</a>
        <a href="so-sanh.html" class="btn btn-outline btn-lg">So Sánh Nhanh Các AI ↗</a>
      </div>
    </div>

    <!-- Featured Spotlight: Muse AI Hero Card -->
    <div class="hero-highlight-card">
      <div class="card-header-flex">
        <div class="agent-brand">
          <div class="agent-logo">M</div>
          <div>
            <h3>Meta Muse AI</h3>
            <p>Autonomous Agent · Tự động làm việc</p>
          </div>
        </div>
        <span class="badge badge-hot">SIÊU HOT 🔥</span>
      </div>

      <h4>Không chỉ trò chuyện.<br><span>AI tự duyệt web, làm việc 24/7 thay bạn.</span></h4>
      <ul class="agent-bullets">
        <li>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
          <span>Có máy tính ảo & trình duyệt riêng: tự điền form, mua sắm, thu thập dữ liệu</span>
        </li>
        <li>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
          <span>Chạy nền ngay cả khi bạn tắt máy, tự xin phê duyệt trước thao tác nhạy cảm</span>
        </li>
        <li>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
          <span>Gói token siêu khủng: 1 tỷ token hoặc 31 tỷ token tha hồ dùng cả năm</span>
        </li>
      </ul>

      <div class="hero-pricing-box">
        <div class="price-row-item active" onclick="window.__openCheckout('muse-1b')">
          <div class="pkg-info">
            <b>Gói Khởi Động: 1 Tỷ Token</b>
            <small>Dùng thử mọi tính năng Autonomous</small>
          </div>
          <div class="pkg-price">
            <strong>69.000đ</strong>
            <del>250.000đ</del>
          </div>
        </div>
        <div class="price-row-item" onclick="window.__openCheckout('muse-31b')">
          <div class="pkg-info">
            <b>Gói Chuyên Nghiệp: 31 Tỷ Token</b>
            <small>Dung lượng cực lớn, tiết kiệm nhất</small>
          </div>
          <div class="pkg-price">
            <strong>699.000đ</strong>
            <del>2.200.000đ</del>
          </div>
        </div>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        <button type="button" class="btn btn-emerald btn-block" onclick="window.__openCheckout('muse-1b')">⚡ Mua Gói 69.000đ</button>
        <a href="muse-ai.html" class="btn btn-outline btn-block">Xem Chi Tiết Muse ↗</a>
      </div>
    </div>
  </div>
</div>

<!-- Stats Bar -->
<div class="stats-bar">
  <div class="container stats-grid">
    <div class="stat-item">
      <div class="stat-icon">👥</div>
      <div class="stat-text">
        <h4>5.200+ Khách Hàng</h4>
        <p>Freelancer, Developer, Doanh nghiệp</p>
      </div>
    </div>
    <div class="stat-item">
      <div class="stat-icon">⚡</div>
      <div class="stat-text">
        <h4>3 - 5 Phút</h4>
        <p>Thời gian kích hoạt tài khoản tự động</p>
      </div>
    </div>
    <div class="stat-item">
      <div class="stat-icon">🛡️</div>
      <div class="stat-text">
        <h4>1 Đổi 1 Trọn Gói</h4>
        <p>Bảo hành tuyệt đối suốt thời gian sử dụng</p>
      </div>
    </div>
    <div class="stat-item">
      <div class="stat-icon">🎁</div>
      <div class="stat-text">
        <h4>Kho 1.000+ Prompt</h4>
        <p>Tặng kèm độc quyền khi mua bất kỳ gói nào</p>
      </div>
    </div>
  </div>
</div>

<!-- Flagship Products Catalog Section -->
<section class="container" id="flagship-products" style="padding: 20px 0 50px;">
  <div class="section-header">
    <span class="section-eyebrow">SẢN PHẨM BÁN CHẠY NHẤT</span>
    <h2 class="section-title">Các Gói Công Cụ & Siêu AI Nổi Bật</h2>
    <p class="section-desc">Được hơn 5,000+ khách hàng lựa chọn để tự động hóa công việc viết lách, nghiên cứu, lập trình và sáng tạo nội dung hàng ngày.</p>
  </div>

  <div class="products-grid">
    {product_card('muse-1b', 'Muse AI · 1 Tỷ Token', 'Meta', 'Autonomous Agent', 'M', 'icon-muse', 'Agent tự chủ có máy tính riêng, tự duyệt web lấy dữ liệu, làm việc nền 24/7.', ['1 Tỷ Token', 'Browser Agent', 'Chạy nền 24/7'], '250.000đ', '69.000đ', 'agent', 'GIÁ SỐC -72%', 'muse-ai.html')}
    {product_card('muse-31b', 'Muse AI · 31 Tỷ Token', 'Meta', 'Token Pack Khủng', 'M', 'icon-muse', 'Dung lượng cực khủng cho chuyên gia và doanh nghiệp tự động hoá hàng trăm task.', ['31 Tỷ Token', 'Đa tác vụ song song', 'Tiết kiệm nhất'], '2.200.000đ', '699.000đ', 'agent', 'BEST SELLER 🔥', 'muse-ai.html')}
    {product_card('grok-cursor', 'Grok Bot qua Cursor Pro', 'xAI', 'AI Coder Đỉnh Cao', 'G', 'icon-grok', 'Trang bị Grok Autonomous vào Cursor IDE, Cloud Terminal và Agent sửa code tự động.', ['Cursor Pro', 'Cloud Terminal', 'Grok Autonomous'], '500.000đ', '299.000đ', 'agent', 'HOT DEV', 'grok-bot.html')}
    {product_card('chatgpt-plus', 'ChatGPT Plus Chính Chủ Email', 'OpenAI', 'Trợ Lý Toàn Năng', '✳', 'icon-chatgpt', 'Nâng cấp trực tiếp trên email của bạn. Dùng GPT-4o, GPT-o1, tạo ảnh Canvas, DALL-E.', ['Email chính chủ', 'Model GPT-4o / o1', 'Tạo ảnh & Code'], '550.000đ', '420.000đ', 'assistant', 'PHỔ BIẾN', 'chatgpt.html')}
    {product_card('claude-pro', 'Claude AI Pro Sonnet 3.7', 'Anthropic', 'Vua Viết & Lập Trình', 'C', 'icon-claude', 'Trùm giải quyết bài toán phức tạp, viết văn phong tự nhiên và phân tích tài liệu sâu.', ['Sonnet 3.7 & Opus', 'Claude Code', 'Context 200K'], '550.000đ', '430.000đ', 'assistant', 'CODE ĐỈNH', 'claude-ai.html')}
    {product_card('gemini-advanced', 'Gemini Advanced 2TB Storage', 'Google', 'Hệ Sinh Thái Google', '✦', 'icon-gemini', 'Gemini 2.0 Pro đỉnh cao + 2000GB Google One Drive, tích hợp toàn diện Gmail, Docs.', ['2000GB Drive', 'Gemini 2.0 Pro', 'Google Workspace'], '490.000đ', '180.000đ', 'assistant', 'TIẾT KIỆM 65%', 'gemini-ai.html')}
  </div>

  <div style="text-align:center;margin-top:20px;">
    <a href="ai-agent.html" class="btn btn-outline btn-lg">Xem Toàn Bộ 15+ Công Cụ AI Tại BotHub ↗</a>
  </div>
</section>

<!-- Comparison & Why Bothub -->
<section style="background: rgba(14,21,38,0.5);border-top:1px solid var(--border-color);border-bottom:1px solid var(--border-color);padding: 60px 0;">
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">LÝ DO NÊN CHỌN BOTHUB</span>
      <h2 class="section-title">Tại Sao Nên Mua Tại BotHub Thay Vì Mua Trực Tiếp?</h2>
      <p class="section-desc">Giải pháp tối ưu chi phí, loại bỏ mọi rào cản thanh toán quốc tế và được bảo vệ bởi chính sách bảo hành 1 đổi 1 tuyệt đối.</p>
    </div>

    <div class="matrix-table-wrap">
      <table class="matrix-table">
        <thead>
          <tr>
            <th>Tiêu Chí So Sánh</th>
            <th style="color:var(--emerald);">Mua Tại BotHub.vn</th>
            <th style="color:#94a3b8;">Tự Mua Thẻ Quốc Tế (Visa/Master)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Chi phí hàng tháng</strong></td>
            <td><strong style="color:var(--emerald);">Tiết kiệm 50% - 80%</strong> (Chỉ từ 69k/gói)</td>
            <td>Giá niêm yết $20 - $200 (500k - 5 triệu/tháng)</td>
          </tr>
          <tr>
            <td><strong>Phương thức thanh toán</strong></td>
            <td><span class="badge badge-green">VietQR / Chuyển khoản / MoMo (30 giây)</span></td>
            <td>Bắt buộc thẻ Visa/Master quốc tế, phí ngoại tệ cao</td>
          </tr>
          <tr>
            <td><strong>Rủi ro khóa thẻ / lỗi vùng</strong></td>
            <td><strong style="color:var(--emerald);">0% rủi ro</strong> — Tài khoản kích hoạt chuẩn sạch</td>
            <td>Thường xuyên bị từ chối thẻ, lỗi IP Việt Nam</td>
          </tr>
          <tr>
            <td><strong>Chính sách bảo hành</strong></td>
            <td><strong style="color:var(--emerald);">Bảo hành 1 đổi 1 suốt thời gian gói</strong></td>
            <td>Không có hỗ trợ tiếng Việt, khiếu nại khó khăn</td>
          </tr>
          <tr>
            <td><strong>Quà tặng kèm theo</strong></td>
            <td><span class="badge badge-cyan">Kho 1000+ Prompt độc quyền + Hỗ trợ 24/7</span></td>
            <td>Không có</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- Customer Reviews Section -->
<section class="container" style="padding: 60px 0;">
  <div class="section-header">
    <span class="section-eyebrow">KHÁCH HÀNG NÓI GÌ</span>
    <h2 class="section-title">Được Hơn 5.000+ Người Dùng Tin Tưởng</h2>
    <p class="section-desc">Cảm nhận thực tế từ các lập trình viên, marketer và chủ doanh nghiệp sau khi sử dụng công cụ AI tại BotHub.</p>
  </div>

  <div class="products-grid">
    <div style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:18px;padding:25px;">
      <div style="color:#f59e0b;margin-bottom:10px;font-size:16px;">★★★★★</div>
      <p style="font-size:13.5px;color:#cbd5e1;line-height:1.7;margin-bottom:15px;">“Mình mua gói Muse AI 31 tỷ token để tự động cào tin tức và theo dõi giá sản phẩm. Bot chạy ngầm trên cloud cực kỳ ổn định, tiết kiệm cho mình ít nhất 3 tiếng mỗi ngày!”</p>
      <div style="display:flex;align-items:center;gap:10px;">
        <div style="width:36px;height:36px;border-radius:50%;background:#4f46e5;display:grid;place-items:center;font-weight:700;">H</div>
        <div>
          <b style="font-size:13px;display:block;">Hoàng Minh Trí</b>
          <small style="color:#94a3b8;font-size:11px;">Senior Fullstack Dev · Hà Nội</small>
        </div>
      </div>
    </div>

    <div style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:18px;padding:25px;">
      <div style="color:#f59e0b;margin-bottom:10px;font-size:16px;">★★★★★</div>
      <p style="font-size:13.5px;color:#cbd5e1;line-height:1.7;margin-bottom:15px;">“Gói ChatGPT Plus nâng chính chủ trên email cá nhân chỉ mất chưa đầy 3 phút qua VietQR. Dùng mượt, có cả GPT-o1 giải toán và viết content marketing siêu nhàn.”</p>
      <div style="display:flex;align-items:center;gap:10px;">
        <div style="width:36px;height:36px;border-radius:50%;background:#06b6d4;display:grid;place-items:center;font-weight:700;">L</div>
        <div>
          <b style="font-size:13px;display:block;">Lê Thu Trang</b>
          <small style="color:#94a3b8;font-size:11px;">Agency Creative Lead · TP.HCM</small>
        </div>
      </div>
    </div>

    <div style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:18px;padding:25px;">
      <div style="color:#f59e0b;margin-bottom:10px;font-size:16px;">★★★★★</div>
      <p style="font-size:13.5px;color:#cbd5e1;line-height:1.7;margin-bottom:15px;">“Hỗ trợ nhiệt tình là điểm cộng lớn nhất ở Bothub. Mình bị quên mật khẩu lúc 11h đêm nhắn Zalo vẫn được các bạn hỗ trợ cấp lại ngay. Rất đáng đồng tiền!”</p>
      <div style="display:flex;align-items:center;gap:10px;">
        <div style="width:36px;height:36px;border-radius:50%;background:#10b981;display:grid;place-items:center;font-weight:700;">V</div>
        <div>
          <b style="font-size:13px;display:block;">Vũ Thành Nam</b>
          <small style="color:#94a3b8;font-size:11px;">Founder Startup Công Nghệ · Đà Nẵng</small>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Final CTA Section -->
<div class="container" style="margin-bottom: 30px;">
  <div style="background: linear-gradient(135deg, #1e1b4b, #312e81, #0f172a);border: 1px solid rgba(99,102,241,0.3);border-radius: 24px;padding: 50px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:25px;box-shadow: 0 20px 50px rgba(0,0,0,0.5);">
    <div>
      <span class="badge badge-hot" style="margin-bottom:10px;">ƯU ĐÃI CÓ HẠN</span>
      <h2 style="font-size:28px;color:#fff;margin:8px 0;">Bắt Đầu Tự Động Hóa Công Việc Cùng AI Ngay Hôm Nay</h2>
      <p style="color:#c7d2fe;font-size:14px;max-width:550px;">Đừng để đối thủ vượt lên trước. Trang bị những trợ lý AI mạnh nhất thế giới với chi phí chỉ bằng một bữa ăn sáng!</p>
    </div>
    <div style="display:flex;gap:12px;flex-wrap:wrap;">
      <button type="button" class="btn btn-emerald btn-lg" onclick="window.__openCheckout('muse-1b')">⚡ Mua Muse AI 69k</button>
      <a href="https://zalo.me/0388888888" target="_blank" class="btn btn-outline btn-lg">💬 Chat Zalo Tư Vấn</a>
    </div>
  </div>
</div>
'''

# =========================================================================
# 2. AI-AGENT.HTML (ALL TOOLS / CATALOG MARKETPLACE)
# =========================================================================
agent_content = f'''
<div class="container" style="padding-top:30px;">
  <div style="margin-bottom:25px;">
    <span class="section-eyebrow">DANH MỤC CÔNG CỤ AI</span>
    <h1 style="font-size:32px;margin:8px 0;font-weight:800;">Tất Cả Công Cụ & Autonomous AI Agent</h1>
    <p style="color:#94a3b8;font-size:14px;">Khám phá toàn bộ các tài khoản, gói token và dịch vụ AI chính hãng tại BotHub với mức giá ưu đãi nhất.</p>
  </div>

  <div class="shop-wrapper">
    <!-- Filter Sidebar -->
    <aside class="shop-filter-panel">
      <div class="filter-title">
        <span>Bộ Lọc Sản Phẩm</span>
        <button class="btn btn-sm btn-outline" onclick="document.querySelectorAll('input[name=filter-cat]').forEach(c=>c.checked=false);document.querySelector('#shop-search-input').value='';document.querySelector('#shop-search-input').dispatchEvent(new Event('input'));">Đặt lại</button>
      </div>

      <div class="filter-group">
        <h4>Tìm Kiếm</h4>
        <div style="background:rgba(255,255,255,0.05);border:1px solid var(--border-color);border-radius:8px;padding:8px 12px;display:flex;align-items:center;gap:6px;">
          <input type="text" id="shop-search-input" placeholder="Tên AI, tính năng..." style="background:none;border:none;color:#fff;font-size:13px;width:100%;">
        </div>
      </div>

      <div class="filter-group">
        <h4>Phân Loại</h4>
        <label class="filter-item">
          <span><input type="checkbox" name="filter-cat" value="agent"> AI Agent Tự Chủ</span>
          <span class="filter-count">3</span>
        </label>
        <label class="filter-item">
          <span><input type="checkbox" name="filter-cat" value="assistant"> AI Chat & Assistant</span>
          <span class="filter-count">4</span>
        </label>
        <label class="filter-item">
          <span><input type="checkbox" name="filter-cat" value="business"> Gói Doanh Nghiệp</span>
          <span class="filter-count">2</span>
        </label>
      </div>

      <div class="filter-group">
        <h4>Cam Kết Từ BotHub</h4>
        <div style="font-size:12px;color:#94a3b8;line-height:1.7;">
          ✓ Kích hoạt siêu tốc 3-5 phút<br>
          ✓ Bảo hành 1 đổi 1 trọn thời gian<br>
          ✓ Tài khoản chính chủ / riêng tư<br>
          ✓ Tặng kèm 1.000+ Prompt mẫu
        </div>
      </div>
    </aside>

    <!-- Main Products Area -->
    <section>
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;padding:12px 18px;background:var(--bg-card);border:1px solid var(--border-color);border-radius:12px;">
        <span style="font-size:13px;color:#94a3b8;">Đang hiển thị <strong style="color:#fff;" id="shop-filtered-count">8</strong> sản phẩm</span>
        <span style="font-size:12px;color:var(--emerald);">● Hệ thống kích hoạt tự động 24/7</span>
      </div>

      <div class="products-grid" style="grid-template-columns: repeat(2, 1fr);" id="shop-products-grid">
        {product_card('muse-1b', 'Muse AI · 1 Tỷ Token', 'Meta', 'Autonomous Agent', 'M', 'icon-muse', 'Agent tự chủ có máy tính riêng, tự duyệt web lấy dữ liệu, làm việc nền 24/7.', ['1 Tỷ Token', 'Browser Agent', 'Chạy nền 24/7'], '250.000đ', '69.000đ', 'agent', 'HOT NHẤT', 'muse-ai.html')}
        {product_card('muse-31b', 'Muse AI · 31 Tỷ Token', 'Meta', 'Token Pack Khủng', 'M', 'icon-muse', 'Dung lượng cực khủng cho chuyên gia và doanh nghiệp tự động hoá hàng trăm task.', ['31 Tỷ Token', 'Đa tác vụ song song', 'Tiết kiệm nhất'], '2.200.000đ', '699.000đ', 'agent', 'BEST SELLER 🔥', 'muse-ai.html')}
        {product_card('muse-unlimited', 'Muse AI · Gói VIP Doanh Nghiệp', 'Meta', 'Enterprise Agent', 'M', 'icon-muse', '100 Tỷ Token + Hỗ trợ thiết lập kịch bản automation độc quyền từ chuyên gia.', ['100 Tỷ Token', 'Kịch bản riêng', 'Ưu tiên hỗ trợ'], '4.500.000đ', '1.890.000đ', 'business', 'VIP ENTERPRISE', 'muse-ai.html')}
        {product_card('grok-cursor', 'Grok Bot qua Cursor AI Pro', 'xAI', 'AI Coder Đỉnh Cao', 'G', 'icon-grok', 'Trang bị Grok Autonomous vào Cursor IDE, Cloud Terminal và Agent sửa code tự động.', ['Cursor Pro', 'Cloud Terminal', 'Grok Autonomous'], '500.000đ', '299.000đ', 'agent', 'HOT DEV', 'grok-bot.html')}
        {product_card('grok-supergrok', 'SuperGrok AI VIP (xAI)', 'xAI', 'Grok 3 Trực Tiếp', 'G', 'icon-grok', 'Quyền truy cập trực tiếp mô hình Grok 3 / Vision không giới hạn.', ['Grok 3 Mới Nhất', 'Không giới hạn', 'Phân tích đa phương tiện'], '750.000đ', '490.000đ', 'agent', 'KHÔNG GIỚI HẠN', 'grok-bot.html')}
        {product_card('chatgpt-plus', 'ChatGPT Plus Chính Chủ Email', 'OpenAI', 'Trợ Lý Toàn Năng', '✳', 'icon-chatgpt', 'Nâng cấp trực tiếp trên email của bạn. Dùng GPT-4o, GPT-o1, tạo ảnh Canvas, DALL-E.', ['Email chính chủ', 'Model GPT-4o / o1', 'Tạo ảnh & Code'], '550.000đ', '420.000đ', 'assistant', 'PHỔ BIẾN', 'chatgpt.html')}
        {product_card('chatgpt-ready', 'ChatGPT Plus Cấp Sẵn', 'OpenAI', 'Tài Khoản Riêng Tư', '✳', 'icon-chatgpt', 'Tài khoản cấp sẵn 1 người dùng, kích hoạt tức thì, bảo hành 1 đổi 1 suốt 30 ngày.', ['1 Người dùng', 'Dùng ngay', 'Bảo hành 1-1'], '500.000đ', '290.000đ', 'assistant', 'GIÁ RẺ NHẤT', 'chatgpt.html')}
        {product_card('claude-pro', 'Claude AI Pro Sonnet 3.7', 'Anthropic', 'Vua Viết & Lập Trình', 'C', 'icon-claude', 'Trùm giải quyết bài toán phức tạp, viết văn phong tự nhiên và phân tích tài liệu sâu.', ['Sonnet 3.7 & Opus', 'Claude Code', 'Context 200K'], '550.000đ', '430.000đ', 'assistant', 'CODE ĐỈNH', 'claude-ai.html')}
        {product_card('gemini-advanced', 'Gemini Advanced 2TB Storage', 'Google', 'Hệ Sinh Thái Google', '✦', 'icon-gemini', 'Gemini 2.0 Pro đỉnh cao + 2000GB Google One Drive, tích hợp toàn diện Gmail, Docs.', ['2000GB Drive', 'Gemini 2.0 Pro', 'Google Workspace'], '490.000đ', '180.000đ', 'assistant', 'TIẾT KIỆM 65%', 'gemini-ai.html')}
      </div>
    </section>
  </div>
</div>
'''

# =========================================================================
# 3. MUSE-AI.HTML (LANDING PAGE MUSE AI)
# =========================================================================
muse_content = f'''
<div class="container">
  <div style="font-size:13px;color:#94a3b8;padding:15px 0;">
    <a href="index.html">Trang chủ</a> › <a href="ai-agent.html">AI Agent</a> › <span style="color:#fff;">Muse AI</span>
  </div>

  <div class="lp-hero-custom">
    <div style="max-width:760px;">
      <span class="badge badge-hot" style="margin-bottom:12px;">META MUSE · AUTONOMOUS AGENT THẾ HỆ MỚI</span>
      <h1 style="font-size:clamp(32px, 4vw, 48px);font-weight:800;line-height:1.2;margin:12px 0;">
        Giao Việc Cho Muse AI.<br>
        <span style="color:var(--cyan);">Để AI Tự Thao Tác Và Hoàn Thành Thay Bạn.</span>
      </h1>
      <p style="font-size:16px;color:#cbd5e1;line-height:1.8;margin-bottom:24px;">
        Muse không chỉ trả lời câu hỏi như chatbot thông thường. Muse là <strong>Autonomous Agent</strong> sở hữu trình duyệt và máy tính ảo riêng để tự duyệt web, điền form, phân tích số liệu và làm việc 24/7 ngay cả khi bạn tắt ứng dụng.
      </p>
      <div style="display:flex;gap:15px;flex-wrap:wrap;margin-bottom:28px;">
        <span style="display:flex;align-items:center;gap:6px;font-size:13.5px;color:#10b981;font-weight:700;">✓ Có máy tính & trình duyệt riêng</span>
        <span style="display:flex;align-items:center;gap:6px;font-size:13.5px;color:#10b981;font-weight:700;">✓ Tác vụ tự động chạy ngầm 24/7</span>
        <span style="display:flex;align-items:center;gap:6px;font-size:13.5px;color:#10b981;font-weight:700;">✓ Xin duyệt trước thao tác nhạy cảm</span>
      </div>
      <div style="display:flex;gap:15px;flex-wrap:wrap;">
        <a href="#bang-gia-muse" class="btn btn-primary btn-lg">Xem Bảng Giá & Mua Ngay (Từ 69k) ⚡</a>
        <a href="#huong-dan-muse" class="btn btn-outline btn-lg">Xem Hướng Dẫn Sử Dụng ↗</a>
      </div>
    </div>
  </div>

  <!-- Features Grid -->
  <div class="section-header" style="margin-top:40px;">
    <span class="section-eyebrow">TÍNH NĂNG ĐỘT PHÁ</span>
    <h2 class="section-title">Muse AI Có Thể Làm Gì Cho Bạn?</h2>
    <p class="section-desc">Thay vì tự mở 10 tab trình duyệt và copy-paste thủ công, hãy giao mục tiêu cho Muse.</p>
  </div>

  <div class="lp-features-grid">
    <div class="lp-feat-card">
      <div class="lp-feat-icon">🌐</div>
      <h3>Trình Duyệt & Máy Tính Riêng</h3>
      <p>Tự động mở website, tương tác với giao diện, điền biểu mẫu, đặt lịch hẹn và xử lý dữ liệu phức tạp mà bạn không cần chạm tay.</p>
    </div>
    <div class="lp-feat-card">
      <div class="lp-feat-icon">⚡</div>
      <h3>Thực Thi Tác Vụ Nhiều Bước</h3>
      <p>Hiểu mục tiêu lớn, tự chia nhỏ thành các nhiệm vụ con, tự kiểm tra sai sót và trả về kết quả hoàn chỉnh có thể nghiệm thu.</p>
    </div>
    <div class="lp-feat-card">
      <div class="lp-feat-icon">🌙</div>
      <h3>Chạy Ngầm 24/7 Khi Tắt Máy</h3>
      <p>Sau khi nhận nhiệm vụ, Muse hoạt động độc lập trên máy chủ cloud. Bạn có thể tắt máy tính đi ngủ, sáng hôm sau nhận báo cáo.</p>
    </div>
    <div class="lp-feat-card">
      <div class="lp-feat-icon">🔒</div>
      <h3>Xin Phê Duyệt Thông Minh</h3>
      <p>Tuyệt đối an toàn: Muse sẽ tự động dừng lại và gửi thông báo xin xác nhận trước các hành động như thanh toán, gửi email quan trọng.</p>
    </div>
    <div class="lp-feat-card">
      <div class="lp-feat-icon">📊</div>
      <h3>Theo Dõi Đối Thủ & Săn Giá</h3>
      <p>Tự động theo dõi biến động giá cả của đối thủ cạnh tranh trên Shopee, Lazada, Amazon và gửi báo cáo phân tích vào mỗi buổi sáng.</p>
    </div>
    <div class="lp-feat-card">
      <div class="lp-feat-icon">🔗</div>
      <h3>Kết Nối Ứng Dụng Đa Nền Tảng</h3>
      <p>Tích hợp trực tiếp với Google Workspace, Notion, Trello, Slack để cập nhật tiến độ công việc tự động.</p>
    </div>
  </div>

  <!-- Pricing Section -->
  <div class="section-header" id="bang-gia-muse" style="margin-top:60px;">
    <span class="section-eyebrow">BẢNG GIÁ ƯU ĐÃI</span>
    <h2 class="section-title">Chọn Gói Muse AI Phù Hợp</h2>
    <p class="section-desc">Giá siêu hời độc quyền tại BotHub. Kích hoạt trong 5 phút, bảo hành trọn đời gói.</p>
  </div>

  <div class="lp-pricing-grid">
    <!-- Pack 1B -->
    <div class="lp-price-card">
      <h3>Gói Khởi Động</h3>
      <p class="plan-subtitle">Phù hợp trải nghiệm cá nhân & học tập</p>
      <div class="lp-price-amount">
        <del>250.000đ</del>
        <span class="num">69.000đ</span>
        <span class="unit">/ 1 Tỷ Token</span>
      </div>
      <ul class="lp-plan-features">
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> 1.000.000.000 Token dung lượng</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Đầy đủ tính năng Browser & Machine Agent</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Tác vụ chạy ngầm độc lập</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Tặng kèm kho 1000+ Prompt độc quyền</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Bảo hành 1 đổi 1 suốt 30 ngày</li>
      </ul>
      <button type="button" class="btn btn-outline btn-block" onclick="window.__openCheckout('muse-1b')">⚡ Mua Gói 1 Tỷ (69k)</button>
    </div>

    <!-- Pack 31B (Featured) -->
    <div class="lp-price-card featured">
      <span class="badge-popular">BÁN CHẠY NHẤT 🔥</span>
      <h3>Gói Chuyên Nghiệp</h3>
      <p class="plan-subtitle">Dung lượng cực lớn cho công việc hàng ngày</p>
      <div class="lp-price-amount">
        <del>2.200.000đ</del>
        <span class="num">699.000đ</span>
        <span class="unit">/ 31 Tỷ Token</span>
      </div>
      <ul class="lp-plan-features">
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> <strong>31.000.000.000 Token</strong> dung lượng khủng</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Tối đa 5 tác vụ chạy song song cùng lúc</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Tốc độ phản hồi ưu tiên cao nhất</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Tặng tài liệu & video hướng dẫn Automation</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Bảo hành 1 đổi 1 suốt thời gian dùng</li>
      </ul>
      <button type="button" class="btn btn-primary btn-block btn-lg" onclick="window.__openCheckout('muse-31b')">⚡ Mua Gói 31 Tỷ (699k)</button>
    </div>

    <!-- Pack VIP -->
    <div class="lp-price-card">
      <h3>Gói Doanh Nghiệp VIP</h3>
      <p class="plan-subtitle">Giải pháp cho Agency & Nhóm phát triển</p>
      <div class="lp-price-amount">
        <del>4.500.000đ</del>
        <span class="num">1.890.000đ</span>
        <span class="unit">/ 100 Tỷ Token</span>
      </div>
      <ul class="lp-plan-features">
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> <strong>100 Tỷ Token</strong> không lo giới hạn</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Setup kịch bản tự động hóa 1-1 cùng kỹ thuật</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Hỗ trợ nhóm làm việc đa thành viên</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Hỗ trợ riêng qua nhóm Telegram/Zalo VIP</li>
      </ul>
      <button type="button" class="btn btn-outline btn-block" onclick="window.__openCheckout('muse-unlimited')">⚡ Mua Gói VIP (1.890k)</button>
    </div>
  </div>

  <!-- How to start section -->
  <div class="container" id="huong-dan-muse" style="margin:60px 0 30px;">
    <div style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:20px;padding:40px;">
      <h3 style="font-size:22px;margin-bottom:15px;color:#fff;">3 Bước Bắt Đầu Với Muse AI Cực Kỳ Đơn Giản:</h3>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:20px;">
        <div style="background:rgba(255,255,255,0.03);padding:20px;border-radius:12px;">
          <div style="color:var(--cyan);font-weight:800;font-size:16px;margin-bottom:8px;">01. Đặt Mua & Quét QR</div>
          <p style="font-size:13px;color:#cbd5e1;">Chọn gói token phù hợp, quét mã VietQR chuyển khoản. Nhập email nhận tài khoản.</p>
        </div>
        <div style="background:rgba(255,255,255,0.03);padding:20px;border-radius:12px;">
          <div style="color:var(--cyan);font-weight:800;font-size:16px;margin-bottom:8px;">02. Nhận Tài Khoản 5P</div>
          <p style="font-size:13px;color:#cbd5e1;">Hệ thống tự động kích hoạt tài khoản có đủ token vào email của bạn trong 3-5 phút.</p>
        </div>
        <div style="background:rgba(255,255,255,0.03);padding:20px;border-radius:12px;">
          <div style="color:var(--cyan);font-weight:800;font-size:16px;margin-bottom:8px;">03. Giao Việc & Thư Giãn</div>
          <p style="font-size:13px;color:#cbd5e1;">Đăng nhập, nhập mục tiêu công việc và để Muse AI tự động thao tác trên trình duyệt.</p>
        </div>
      </div>
    </div>
  </div>
</div>
'''

# =========================================================================
# 4. GROK-BOT.HTML (LANDING PAGE GROK BOT)
# =========================================================================
grok_content = f'''
<div class="container">
  <div style="font-size:13px;color:#94a3b8;padding:15px 0;">
    <a href="index.html">Trang chủ</a> › <a href="ai-agent.html">AI Agent</a> › <span style="color:#fff;">Grok Bot</span>
  </div>

  <div class="lp-hero-custom" style="background:radial-gradient(circle at 70% 30%, rgba(30,41,59,0.8), transparent 60%), var(--bg-card);">
    <div style="max-width:760px;">
      <span class="badge badge-hot" style="margin-bottom:12px;">xAI · GROK AUTONOMOUS AGENT</span>
      <h1 style="font-size:clamp(32px, 4vw, 48px);font-weight:800;line-height:1.2;margin:12px 0;">
        Grok Bot Autonomous.<br>
        <span style="color:#38bdf8;">Siêu Trí Tuệ Không Giới Hạn Của Elon Musk.</span>
      </h1>
      <p style="font-size:16px;color:#cbd5e1;line-height:1.8;margin-bottom:24px;">
        Đồng đội AI lập trình và tự động hoá công việc kỹ thuật đỉnh cao. Tích hợp trực tiếp máy tính Cloud Terminal riêng, Browser Agent và khả năng làm việc liên tục ngay cả khi bạn tắt máy.
      </p>
      <div style="display:flex;gap:15px;flex-wrap:wrap;margin-bottom:28px;">
        <span style="display:flex;align-items:center;gap:6px;font-size:13.5px;color:#10b981;font-weight:700;">✓ Tích hợp Cursor AI IDE Pro</span>
        <span style="display:flex;align-items:center;gap:6px;font-size:13.5px;color:#10b981;font-weight:700;">✓ Cloud Terminal độc lập</span>
        <span style="display:flex;align-items:center;gap:6px;font-size:13.5px;color:#10b981;font-weight:700;">✓ Tự động debug và deploy dự án</span>
      </div>
      <div style="display:flex;gap:15px;flex-wrap:wrap;">
        <button type="button" class="btn btn-primary btn-lg" onclick="window.__openCheckout('grok-cursor')">⚡ Mua Grok qua Cursor (299k/tháng)</button>
        <button type="button" class="btn btn-outline btn-lg" onclick="window.__openCheckout('grok-supergrok')">SuperGrok VIP (490k) ↗</button>
      </div>
    </div>
  </div>

  <div class="section-header" style="margin-top:40px;">
    <span class="section-eyebrow">KHẢ NĂNG KỸ THUẬT</span>
    <h2 class="section-title">Tại Sao Developer Chọn Grok Bot?</h2>
    <p class="section-desc">Không chỉ trả lời lý thuyết, Grok Bot có thể trực tiếp viết code, chạy lệnh terminal và kiểm thử phần mềm.</p>
  </div>

  <div class="lp-features-grid">
    <div class="lp-feat-card">
      <div class="lp-feat-icon">💻</div>
      <h3>Cloud Terminal Riêng Biệt</h3>
      <p>Cung cấp môi trường Linux ảo an toàn để bot tự chạy lệnh shell, kiểm tra log lỗi và cài đặt thư viện cần thiết.</p>
    </div>
    <div class="lp-feat-card">
      <div class="lp-feat-icon">⚡</div>
      <h3>Tự Động Tìm & Sửa Bug</h3>
      <p>Grok Bot đọc toàn bộ repository, phát hiện nguyên nhân lỗi logic và tạo git patch hoàn chỉnh cho bạn review.</p>
    </div>
    <div class="lp-feat-card">
      <div class="lp-feat-icon">🌐</div>
      <h3>Browser Agent Khảo Sát Web</h3>
      <p>Tự động duyệt tài liệu API mới nhất trên internet, tránh tình trạng viết code dựa trên kiến thức lỗi thời.</p>
    </div>
  </div>

  <!-- Pricing -->
  <div class="lp-pricing-grid" style="margin-top:40px;">
    <div class="lp-price-card featured">
      <span class="badge-popular">LẬP TRÌNH VIÊN KHUYÊN DÙNG</span>
      <h3>Grok qua Cursor Pro</h3>
      <p class="plan-subtitle">Tích hợp thẳng vào Cursor IDE chỉnh sửa code</p>
      <div class="lp-price-amount">
        <del>500.000đ</del>
        <span class="num">299.000đ</span>
        <span class="unit">/ Tháng</span>
      </div>
      <ul class="lp-plan-features">
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Quyền truy cập Cursor Pro tốc độ cao</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Sử dụng Grok Autonomous & Claude 3.5 Sonnet</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Auto-complete code thông minh trên toàn repo</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Bảo hành 1 đổi 1 suốt 30 ngày</li>
      </ul>
      <button type="button" class="btn btn-primary btn-block btn-lg" onclick="window.__openCheckout('grok-cursor')">⚡ Mua Ngay (299.000đ)</button>
    </div>

    <div class="lp-price-card">
      <h3>SuperGrok AI VIP</h3>
      <p class="plan-subtitle">Truy cập trực tiếp nền tảng xAI cao cấp</p>
      <div class="lp-price-amount">
        <del>750.000đ</del>
        <span class="num">490.000đ</span>
        <span class="unit">/ Tháng</span>
      </div>
      <ul class="lp-plan-features">
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Sử dụng mô hình Grok 3 mới nhất</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Phân tích dữ liệu thời gian thực trên mạng X</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Khả năng suy luận tư duy không bị kiểm duyệt</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Bảo hành 1 đổi 1 chính hãng</li>
      </ul>
      <button type="button" class="btn btn-outline btn-block" onclick="window.__openCheckout('grok-supergrok')">⚡ Mua SuperGrok (490.000đ)</button>
    </div>
  </div>
</div>
'''

# =========================================================================
# 5. CHATGPT.HTML
# =========================================================================
chatgpt_content = f'''
<div class="container" style="padding-top:20px;">
  <div style="font-size:13px;color:#94a3b8;padding:15px 0;">
    <a href="index.html">Trang chủ</a> › <a href="ai-agent.html">AI Agent</a> › <span style="color:#fff;">ChatGPT</span>
  </div>

  <div class="lp-hero-custom" style="background:radial-gradient(circle at 70% 30%, rgba(16,185,129,0.3), transparent 60%), var(--bg-card);">
    <div style="max-width:760px;">
      <span class="badge badge-hot" style="margin-bottom:12px;">OPENAI · TRỢ LÝ HÀNG ĐẦU THẾ GIỚI</span>
      <h1 style="font-size:clamp(32px, 4vw, 48px);font-weight:800;line-height:1.2;margin:12px 0;">
        ChatGPT Plus Chính Chủ.<br>
        <span style="color:#34d399;">Nâng Cấp Trực Tiếp Trên Email Của Bạn.</span>
      </h1>
      <p style="font-size:16px;color:#cbd5e1;line-height:1.8;margin-bottom:24px;">
        Truy cập mô hình mạnh nhất: <strong>GPT-4o, GPT-o1 suy luận logic cao</strong>, tạo ảnh DALL-E 3 không giới hạn, phân tích dữ liệu bảng tính Excel và kho 3 triệu Custom GPTs phục vụ mọi ngành nghề.
      </p>
      <div style="display:flex;gap:15px;flex-wrap:wrap;">
        <button type="button" class="btn btn-emerald btn-lg" onclick="window.__openCheckout('chatgpt-plus')">⚡ Nâng Cấp Email Chính Chủ (420k/tháng)</button>
        <button type="button" class="btn btn-outline btn-lg" onclick="window.__openCheckout('chatgpt-ready')">Mua Tài Khoản Cấp Sẵn (290k) ↗</button>
      </div>
    </div>
  </div>

  <div class="lp-pricing-grid" style="margin-top:40px;">
    <div class="lp-price-card featured">
      <span class="badge-popular">KHUYÊN DÙNG NHẤT</span>
      <h3>Plus Nâng Chính Chủ</h3>
      <p class="plan-subtitle">Kích hoạt trực tiếp trên email cá nhân của bạn</p>
      <div class="lp-price-amount">
        <del>550.000đ</del>
        <span class="num">420.000đ</span>
        <span class="unit">/ Tháng</span>
      </div>
      <ul class="lp-plan-features">
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Email chính chủ, giữ nguyên lịch sử chat</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Quyền sử dụng GPT-4o, GPT-o1 mới nhất</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Tạo ảnh DALL-E 3, Canvas, Code Interpreter</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Bảo hành 1 đổi 1 suốt 30 ngày</li>
      </ul>
      <button type="button" class="btn btn-emerald btn-block btn-lg" onclick="window.__openCheckout('chatgpt-plus')">⚡ Mua Gói Chính Chủ (420k)</button>
    </div>

    <div class="lp-price-card">
      <h3>Plus Cấp Sẵn Riêng Tư</h3>
      <p class="plan-subtitle">Tài khoản cấp sẵn 1 người dùng riêng biệt</p>
      <div class="lp-price-amount">
        <del>500.000đ</del>
        <span class="num">290.000đ</span>
        <span class="unit">/ Tháng</span>
      </div>
      <ul class="lp-plan-features">
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Tài khoản cấp riêng, đổi được mật khẩu</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Đầy đủ tính năng GPT-4o Plus</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Kích hoạt tức thì trong 3 phút</li>
        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Bảo hành 1 đổi 1 suốt 30 ngày</li>
      </ul>
      <button type="button" class="btn btn-outline btn-block" onclick="window.__openCheckout('chatgpt-ready')">⚡ Mua Tài Khoản Cấp Sẵn (290k)</button>
    </div>
  </div>
</div>
'''

# =========================================================================
# 6. CLAUDE-AI.HTML
# =========================================================================
claude_content = f'''
<div class="container" style="padding-top:20px;">
  <div style="font-size:13px;color:#94a3b8;padding:15px 0;">
    <a href="index.html">Trang chủ</a> › <a href="ai-agent.html">AI Agent</a> › <span style="color:#fff;">Claude AI</span>
  </div>

  <div class="lp-hero-custom" style="background:radial-gradient(circle at 70% 30%, rgba(217,119,6,0.3), transparent 60%), var(--bg-card);">
    <div style="max-width:760px;">
      <span class="badge badge-hot" style="margin-bottom:12px;">ANTHROPIC · CLAUDE AI PRO</span>
      <h1 style="font-size:clamp(32px, 4vw, 48px);font-weight:800;line-height:1.2;margin:12px 0;">
        Claude AI Pro (Sonnet 3.7).<br>
        <span style="color:#fbbf24;">Vua Lập Trình & Viết Văn Phong Tự Nhiên.</span>
      </h1>
      <p style="font-size:16px;color:#cbd5e1;line-height:1.8;margin-bottom:24px;">
        Được đánh giá là mô hình AI lập trình và tư duy logic tốt nhất hiện nay. Hỗ trợ <strong>Claude Artifacts</strong> tương tác trực tiếp giao diện, cửa sổ ngữ cảnh cực khủng 200,000 token đọc hiểu toàn bộ tài liệu dày cộm.
      </p>
      <div style="display:flex;gap:15px;flex-wrap:wrap;">
        <button type="button" class="btn btn-primary btn-lg" onclick="window.__openCheckout('claude-pro')">⚡ Mua Claude Pro (430.000đ/tháng)</button>
        <a href="https://zalo.me/0388888888" target="_blank" class="btn btn-outline btn-lg">Tư Vấn Zalo 24/7 ↗</a>
      </div>
    </div>
  </div>

  <div class="lp-features-grid" style="margin-top:40px;">
    <div class="lp-feat-card">
      <div class="lp-feat-icon">⚡</div>
      <h3>Claude Sonnet 3.7 & Opus</h3>
      <p>Mô hình tiên tiến nhất giải quyết các bài toán code khó, thuật toán phức tạp mà các AI khác bó tay.</p>
    </div>
    <div class="lp-feat-card">
      <div class="lp-feat-icon">📄</div>
      <h3>Context Window 200K Token</h3>
      <p>Thả cả một cuốn sách, hàng trăm file PDF hợp đồng hoặc toàn bộ source code vào để Claude tóm tắt và phân tích.</p>
    </div>
    <div class="lp-feat-card">
      <div class="lp-feat-icon">🎨</div>
      <h3>Claude Artifacts</h3>
      <p>Xem trước website, ứng dụng React, biểu đồ dữ liệu và game mini trực tiếp ngay trong cửa sổ chat.</p>
    </div>
  </div>
</div>
'''

# =========================================================================
# 7. GEMINI-AI.HTML
# =========================================================================
gemini_content = f'''
<div class="container" style="padding-top:20px;">
  <div style="font-size:13px;color:#94a3b8;padding:15px 0;">
    <a href="index.html">Trang chủ</a> › <a href="ai-agent.html">AI Agent</a> › <span style="color:#fff;">Gemini AI</span>
  </div>

  <div class="lp-hero-custom" style="background:radial-gradient(circle at 70% 30%, rgba(37,99,235,0.3), transparent 60%), var(--bg-card);">
    <div style="max-width:760px;">
      <span class="badge badge-hot" style="margin-bottom:12px;">GOOGLE · GEMINI ADVANCED</span>
      <h1 style="font-size:clamp(32px, 4vw, 48px);font-weight:800;line-height:1.2;margin:12px 0;">
        Gemini Advanced + 2TB Drive.<br>
        <span style="color:#60a5fa;">Tích Hợp Sâu Vào Toàn Bộ Hệ Sinh Thái Google.</span>
      </h1>
      <p style="font-size:16px;color:#cbd5e1;line-height:1.8;margin-bottom:24px;">
        Mô hình Gemini 2.0 Pro mới nhất kết hợp gói dung lượng 2.000GB Google One. Tự động soạn thảo văn bản trong Google Docs, phân tích bảng tính Google Sheets và lọc email thông minh trong Gmail.
      </p>
      <div style="display:flex;gap:15px;flex-wrap:wrap;">
        <button type="button" class="btn btn-cyan btn-lg" onclick="window.__openCheckout('gemini-advanced')">⚡ Mua Gemini Advanced 2TB (180.000đ/tháng)</button>
        <a href="https://zalo.me/0388888888" target="_blank" class="btn btn-outline btn-lg">Tư Vấn Zalo 24/7 ↗</a>
      </div>
    </div>
  </div>

  <div class="lp-features-grid" style="margin-top:40px;">
    <div class="lp-feat-card">
      <div class="lp-feat-icon">💾</div>
      <h3>2.000GB Dung Lượng Google One</h3>
      <p>Lưu trữ hình ảnh chất lượng gốc, video, tài liệu và chia sẻ dung lượng cho tối đa 5 người thân trong gia đình.</p>
    </div>
    <div class="lp-feat-card">
      <div class="lp-feat-icon">🚀</div>
      <h3>Gemini 2.0 Pro Siêu Tốc</h3>
      <p>Cửa sổ xử lý lên tới 1 triệu token, hiểu video dài hàng giờ, phân tích âm thanh và hình ảnh chi tiết.</p>
    </div>
    <div class="lp-feat-card">
      <div class="lp-feat-icon">📂</div>
      <h3>Tích Hợp Docs, Gmail, Sheets</h3>
      <p>Trợ lý viết văn bản trực tiếp trong Docs, tự động tạo bài thuyết trình trong Slides chỉ với 1 câu lệnh.</p>
    </div>
  </div>
</div>
'''

# =========================================================================
# 8. THU-VIEN-PROMPT.HTML (PROMPT LIBRARY)
# =========================================================================
prompts_data = [
    ('agent', 'AI Agent Lập Kế Hoạch 5 Bước', 'Chia nhỏ mục tiêu lớn thành các task con có mốc nghiệm thu và tiêu chuẩn kiểm chứng.',
     '''Bạn là Autonomous Project Agent chuyên nghiệp.
Mục tiêu dự án: [NHẬP MỤC TIÊU CỦA BẠN].
Hãy thiết lập kế hoạch thực thi 5 giai đoạn:
1. Giai đoạn: Tên, mục tiêu cốt lõi
2. Input yêu cầu & Tài nguyên đầu vào
3. Các hành động cụ thể (Action Steps)
4. Tiêu chí nghiệm thu định lượng (Acceptance Criteria)
5. Rủi ro tiềm ẩn & Biện pháp xử lý ngoại lệ
Chỉ sử dụng công cụ được phép, không tự ý giả định dữ liệu chưa kiểm chứng.'''),

    ('coding', 'Coding Agent: Refactor & Vá Bug An Toàn', 'Phân tích mã nguồn, phát hiện lỗi ngầm và viết test case kiểm thử.',
     '''Bạn là Senior Software Engineer.
Ngôn ngữ: [NGÔN NGỮ/FRAMEWORK].
Source code hiện tại:
[DÁN CODE CỦA BẠN VÀO ĐÂY]
Nhiệm vụ:
1. Phát hiện tất cả lỗ hổng bảo mật, lỗi logic và memory leak.
2. Tối ưu performance và clean code theo nguyên lý SOLID.
3. Viết lại đoạn code đã tối ưu có chú thích giải thích chi tiết.
4. Cung cấp bộ Unit Test đầy đủ các trường hợp edge case.'''),

    ('marketing', 'Chiến Lược Content 30 Ngày Tăng Traffic', 'Lập lịch nội dung theo hành trình khách hàng và cụm chủ đề SEO.',
     '''Bạn là Content Marketing & SEO Strategist.
Sản phẩm/Dịch vụ: [SẢN PHẨM CỦA BẠN].
Đối tượng mục tiêu: [CHÂN DUNG KHÁCH HÀNG].
Hãy lập bảng kế hoạch nội dung 30 ngày gồm:
- Tuần 1: Nhận thức vấn đề (Pain Point & Awareness)
- Tuần 2: So sánh & Cân nhắc giải pháp (Consideration)
- Tuần 3: Chuyển đổi & Trải nghiệm thực tế (Decision & Proof)
- Tuần 4: Giữ chân & Bán thêm (Retention)
Mỗi bài viết gồm: Tiêu đề hook, Search Intent, Dàn ý 3 ý chính, Kêu gọi hành động (CTA).'''),

    ('image', 'Character Sheet 11 Góc Mặt Nhất Quán', 'Tạo bộ ảnh nhân vật 11 góc quay chi tiết giữ nguyên nhận diện khuôn mặt.',
     '''Ultra-realistic character turnaround sheet, full face consistency.
Subject: [MÔ TẢ NHÂN VẬT, ĐỘ TUỔI, GIỚI TÍNH, TRANG PHỤC].
11 angles on a single canvas in 4-4-3 arrangement:
Front view, 45 degree left, 90 degree profile left, 45 degree right, 90 degree profile right, looking up, looking down, 3/4 left smiling, 3/4 right neutral, intense expression, laughing.
Neutral studio soft lighting, consistent eye color and hair texture, high detail 8k photography, 85mm lens f/1.8, cinematic.'''),

    ('agent', 'Research Agent: Khảo Sát & So Sánh Thị Trường', 'Nghiên cứu sâu các đối thủ cạnh tranh trên thị trường và lập ma trận SWOT.',
     '''Bạn là Market Research Agent.
Thị trường cần nghiên cứu: [LĨNH VỰC/SẢN PHẨM].
Hãy thực hiện báo cáo chuyên sâu:
1. Top 5 đối thủ hàng đầu đang dẫn đầu thị trường.
2. Phân tích mô hình định giá (Pricing model) và điểm mạnh/yếu của từng bên.
3. Khoảng trống thị trường (Unmet Needs) mà chưa ai giải quyết tốt.
4. Đề xuất chiến lược định vị và thông điệp cạnh tranh độc nhất (USP).'''),

    ('coding', 'Tạo Kịch Bản Video Ngắn Triệu View TikTok/Reels', 'Khung kịch bản video 30-45 giây giữ chân người xem từ giây đầu tiên.',
     '''Bạn là Viral Video Scriptwriter chuyên nghiệp.
Chủ đề video: [CHỦ ĐỀ/SẢN PHẨM].
Thời lượng: 30 - 45 giây.
Hãy viết kịch bản chi tiết:
- Giây 0-3 (Hook hình ảnh & âm thanh): Gây sốc, phá vỡ định kiến hoặc đặt câu hỏi tò mò.
- Giây 4-15 (Xoáy sâu nỗi đau): Diễn tả tình huống khách hàng gặp phải.
- Giây 16-30 (Bẻ khóa giải pháp): Giới thiệu cách giải quyết thông minh bằng sản phẩm.
- Giây 31-40 (Call to Action): Kêu gọi hành động ngắn gọn, kích thích comment.''')
]

prompts_cards_html = ''.join([
    f'''
    <div class="prompt-card" data-cat="{cat}">
      <div class="prompt-card-top">
        <span class="badge badge-purple">{cat.upper()}</span>
        <span class="badge badge-green">MIỄN PHÍ</span>
      </div>
      <h3>{title}</h3>
      <p style="font-size:12.5px;color:#94a3b8;line-height:1.6;margin-bottom:12px;">{desc}</p>
      <div class="prompt-box">
        <pre class="prompt-code" style="font-family:inherit;white-space:pre-wrap;margin:0;">{body}</pre>
      </div>
      <button type="button" class="btn btn-outline btn-sm btn-block" data-copy-prompt style="margin-top:auto;">
        📋 Sao Chép Prompt
      </button>
    </div>
    '''
    for cat, title, desc, body in prompts_data
])

prompt_content = f'''
<div class="container" style="padding-top:30px;">
  <div style="margin-bottom:25px;">
    <span class="section-eyebrow">TÀI NGUYÊN ĐỘC QUYỀN BOTHUB</span>
    <h1 style="font-size:32px;margin:8px 0;font-weight:800;">Kho Thư Viện Prompt AI Thực Chiến</h1>
    <p style="color:#94a3b8;font-size:14px;">Tuyển tập các câu lệnh mẫu chất lượng cao cho AI Agent, Lập trình, Marketing, Viết nội dung và Tạo ảnh. Nhấn sao chép 1-click để sử dụng ngay.</p>
  </div>

  <div class="prompt-filter-bar">
    <button type="button" class="prompt-chip active" data-filter="all">Tất Cả Prompt</button>
    <button type="button" class="prompt-chip" data-filter="agent">AI Agent & Workflow</button>
    <button type="button" class="prompt-chip" data-filter="coding">Lập Trình & Sửa Code</button>
    <button type="button" class="prompt-chip" data-filter="marketing">Marketing & SEO</button>
    <button type="button" class="prompt-chip" data-filter="image">Tạo Ảnh & Video</button>
  </div>

  <div class="prompts-grid">
    {prompts_cards_html}
  </div>
</div>
'''

# =========================================================================
# 9. SO-SANH.HTML (COMPARISON MATRIX)
# =========================================================================
compare_content = f'''
<div class="container" style="padding-top:30px;">
  <div style="margin-bottom:25px;">
    <span class="section-eyebrow">BẢNG PHÂN TÍCH & ĐỐI CHIẾU</span>
    <h1 style="font-size:32px;margin:8px 0;font-weight:800;">So Sánh Các Dòng Siêu AI: Chọn Đúng Công Cụ</h1>
    <p style="color:#94a3b8;font-size:14px;">Mỗi mô hình AI có một thế mạnh riêng biệt. Đối chiếu bảng dưới đây để đầu tư đúng công cụ cho công việc của bạn.</p>
  </div>

  <div class="matrix-table-wrap">
    <table class="matrix-table">
      <thead>
        <tr>
          <th>Tiêu Chí</th>
          <th>Muse AI (Meta)</th>
          <th>Grok Bot (xAI)</th>
          <th>ChatGPT Plus</th>
          <th>Claude AI Pro</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Phân loại chính</strong></td>
          <td><span class="badge badge-hot">Autonomous Agent</span></td>
          <td><span class="badge badge-cyan">Cloud Terminal & Coding</span></td>
          <td><span class="badge badge-green">Trợ lý toàn năng</span></td>
          <td><span class="badge badge-purple">Viết văn & Lập trình sâu</span></td>
        </tr>
        <tr>
          <td><strong>Khả năng tự thao tác</strong></td>
          <td>Tự mở trình duyệt, điền biểu mẫu, làm việc 24/7</td>
          <td>Chạy lệnh Linux Terminal, tương tác API</td>
          <td>Duyệt web tra cứu (Browse with Bing)</td>
          <td>Claude Code tương tác file dự án</td>
        </tr>
        <tr>
          <td><strong>Mô hình cốt lõi</strong></td>
          <td>Meta Muse Agent Model</td>
          <td>Grok 3 / Vision</td>
          <td>GPT-4o, GPT-o1</td>
          <td>Claude 3.7 Sonnet, Opus</td>
        </tr>
        <tr>
          <td><strong>Dung lượng / Hạn mức</strong></td>
          <td><strong>1 Tỷ - 31 Tỷ Token</strong></td>
          <td>Gói tháng Cursor Pro / SuperGrok</td>
          <td>Không giới hạn theo tin nhắn</td>
          <td>Cửa sổ ngữ cảnh 200.000 Token</td>
        </tr>
        <tr>
          <td><strong>Giá tại BotHub</strong></td>
          <td><strong style="color:var(--emerald);">Từ 69.000đ</strong></td>
          <td><strong style="color:var(--emerald);">Từ 299.000đ/tháng</strong></td>
          <td><strong style="color:var(--emerald);">Từ 290.000đ/tháng</strong></td>
          <td><strong style="color:var(--emerald);">430.000đ/tháng</strong></td>
        </tr>
        <tr>
          <td><strong>Phù hợp cho ai?</strong></td>
          <td>Người cần tự động hoá task lặp đi lặp lại</td>
          <td>Lập trình viên, kỹ sư phần mềm</td>
          <td>Nhân viên văn phòng, sinh viên, creator</td>
          <td>Chuyên gia nội dung, lập trình viên cao cấp</td>
        </tr>
        <tr>
          <td><strong>Hành động</strong></td>
          <td><button class="btn btn-primary btn-sm" onclick="window.__openCheckout('muse-1b')">⚡ Mua Muse 69k</button></td>
          <td><button class="btn btn-primary btn-sm" onclick="window.__openCheckout('grok-cursor')">⚡ Mua Grok 299k</button></td>
          <td><button class="btn btn-primary btn-sm" onclick="window.__openCheckout('chatgpt-plus')">⚡ Mua GPT 420k</button></td>
          <td><button class="btn btn-primary btn-sm" onclick="window.__openCheckout('claude-pro')">⚡ Mua Claude 430k</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
'''

# =========================================================================
# 10. GIO-HANG.HTML (CART & CHECKOUT)
# =========================================================================
cart_content = f'''
<div class="container" style="padding-top:30px;">
  <div style="margin-bottom:20px;">
    <span class="section-eyebrow">GIỎ HÀNG CỦA BẠN</span>
    <h1 style="font-size:30px;margin:6px 0;font-weight:800;">Danh Sách Gói AI Đã Chọn</h1>
  </div>

  <div class="cart-layout">
    <div class="cart-items-box" id="cart-items-container">
      <!-- Injected by JavaScript -->
    </div>

    <aside class="cart-summary">
      <h3>Tóm Tắt Đơn Hàng</h3>
      <div class="summary-row">
        <span>Tổng số gói:</span>
        <strong id="cart-total-count">0</strong>
      </div>
      <div class="summary-row">
        <span>Hình thức kích hoạt:</span>
        <strong style="color:var(--cyan);">Tự động qua Email (5P)</strong>
      </div>
      <div class="summary-row">
        <span>Chính sách bảo hành:</span>
        <strong style="color:var(--emerald);">1 Đổi 1 Trọn Gói</strong>
      </div>
      <div class="summary-row total">
        <span>Tổng thanh toán:</span>
        <span style="color:var(--emerald);" id="cart-total-price">0đ</span>
      </div>

      <button type="button" class="btn btn-emerald btn-block btn-lg" style="margin-top:20px;" onclick="window.__openCartCheckout()">
        ⚡ TIẾN HÀNH THANH TOÁN (VIETQR)
      </button>

      <div style="margin-top:16px;font-size:12px;color:#94a3b8;line-height:1.6;text-align:center;">
        🔒 Quét mã VietQR chuyển khoản ngân hàng hoặc ví MoMo. Tài khoản sẽ được gửi tự động sau khi thanh toán.
      </div>
    </aside>
  </div>
</div>
'''

# =========================================================================
# 11. CHINH-SACH.HTML
# =========================================================================
policy_content = f'''
<div class="container" style="padding-top:30px;max-width:900px;">
  <div style="margin-bottom:30px;">
    <span class="section-eyebrow">CHÍNH SÁCH BÁN HÀNG & BẢO HÀNH</span>
    <h1 style="font-size:32px;margin:8px 0;font-weight:800;">Chính Sách Bảo Hành & Cam Kết Dịch Vụ</h1>
    <p style="color:#94a3b8;font-size:14px;">BotHub.vn cam kết đem lại trải nghiệm mua sắm công nghệ an toàn, bảo mật và minh bạch 100%.</p>
  </div>

  <div style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:18px;padding:30px;display:grid;gap:25px;margin-bottom:40px;">
    <div>
      <h3 style="color:#fff;font-size:18px;margin-bottom:8px;">1. Chính Sách Bảo Hành 1 Đổi 1</h3>
      <p style="color:#cbd5e1;font-size:13.5px;line-height:1.8;">Mọi tài khoản và gói token mua tại BotHub.vn đều được bảo hành 1 đổi 1 trong suốt thời gian sử dụng đã cam kết. Nếu gặp bất kỳ sự cố nào như lỗi đăng nhập, mất quota hay gián đoạn dịch vụ, quý khách chỉ cần nhắn tin cho đội ngũ hỗ trợ qua Zalo 0388.888.888 để được cấp lại tài khoản mới trong vòng 10-15 phút.</p>
    </div>

    <div>
      <h3 style="color:#fff;font-size:18px;margin-bottom:8px;">2. Thời Gian Kích Hoạt & Bàn Giao</h3>
      <p style="color:#cbd5e1;font-size:13.5px;line-height:1.8;">- Đối với tài khoản cấp sẵn: Bàn giao tự động qua Email trong 3 - 5 phút sau khi hệ thống nhận được chuyển khoản VietQR.<br>
      - Đối với gói nâng cấp chính chủ trên email: Kỹ thuật viên sẽ hỗ trợ nâng cấp trong 5 - 15 phút.</p>
    </div>

    <div>
      <h3 style="color:#fff;font-size:18px;margin-bottom:8px;">3. Chính Sách Hoàn Tiền</h3>
      <p style="color:#cbd5e1;font-size:13.5px;line-height:1.8;">BotHub hoàn tiền 100% trong vòng 24 giờ đầu tiên nếu sản phẩm không đúng với mô tả hoặc lỗi kỹ thuật từ hệ thống mà không thể khắc phục được.</p>
    </div>

    <div>
      <h3 style="color:#fff;font-size:18px;margin-bottom:8px;">4. Bảo Mật Thông Tin Khách Hàng</h3>
      <p style="color:#cbd5e1;font-size:13.5px;line-height:1.8;">BotHub tuyệt đối không chia sẻ thông tin email, số điện thoại hay dữ liệu sử dụng của khách hàng cho bất kỳ bên thứ ba nào. Mọi giao dịch chuyển khoản ngân hàng đều được thực hiện trực tiếp qua mã VietQR an toàn.</p>
    </div>
  </div>
</div>
'''

# =========================================================================
# 12. MA-INVITE.HTML (INVITE CODES & PROMO HUB)
# =========================================================================
muse_invite_list = [
    ('ZACDIA', 27, 'Mã mời chính thức nhận ngay 1 Tỷ Token trải nghiệm đầy đủ tính năng.'),
    ('6WVLSZ', 29, 'Mã mời nhận 1 Tỷ Token Autonomous Agent cho tài khoản mới.'),
    ('PYWR4C', 29, 'Kích hoạt 1 Tỷ Token Meta Muse ngay sau khi đăng ký.'),
    ('5CVT4Y', 29, 'Mã nhận quota 1 Tỷ Token tốc độ cao không giới hạn.'),
    ('Q2E6IN', 29, 'Thêm 1 Tỷ Token vào tài khoản Muse để tự động hóa công việc.'),
    ('NY07IM', 29, 'Mã giới thiệu kích hoạt tính năng browser agent & 1B token.'),
    ('QUOSLL', 29, 'Cấp quyền 1 Tỷ Token cho cá nhân và nhóm trải nghiệm.'),
    ('TEP0WR', 29, 'Mã mời đặc quyền từ đại lý BotHub nhận 1 Tỷ Token.'),
    ('93W5WA', 29, 'Mã nhận 1 Tỷ Token miễn phí kiểm tra hoạt động cloud agent.'),
    ('13XC4P', 29, 'Quota 1 Tỷ Token Meta Muse chính thức còn lượt dùng cao.'),
    ('ARGX86', 29, 'Mã dự phòng dung lượng 1 Tỷ Token hợp lệ hôm nay.')
]

invite_cards_html = ''.join([
    f'''
    <div class="invite-card" data-tool="muse">
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div style="display:flex;align-items:center;gap:8px;">
          <div class="prod-brand-icon icon-muse" style="width:34px;height:34px;font-size:16px;">M</div>
          <span style="font-weight:700;font-size:13px;color:#fff;">Muse AI · 1 Tỷ Token</span>
        </div>
        <span class="remaining-badge">● Còn {slots} lượt</span>
      </div>

      <div class="invite-code-box" data-copy-invite="{code}" title="Nhấn để sao chép mã {code}">
        <span style="font-size:11px;color:#94a3b8;display:block;margin-bottom:4px;">MÃ INVITE CODE (CLICK ĐỂ COPY)</span>
        <span class="invite-code-text">{code}</span>
      </div>

      <p style="font-size:12px;color:#94a3b8;line-height:1.6;margin-bottom:14px;flex:1;">{desc}</p>

      <div style="display:grid;grid-template-columns:1fr auto;gap:8px;margin-top:auto;">
        <button type="button" class="btn btn-cyan btn-sm" data-copy-invite="{code}">
          📋 Sao Chép Mã
        </button>
        <a href="https://ai.meta.com/muse/" target="_blank" rel="noopener" class="btn btn-outline btn-sm" title="Mở trang Muse đăng ký">
          Dùng Mã ↗
        </a>
      </div>
    </div>
    '''
    for code, slots, desc in muse_invite_list
])

invite_content = f'''
<div class="container" style="padding-top:30px;">
  <div style="margin-bottom:25px;">
    <span class="section-eyebrow">KHO MÃ MỜI & ƯU ĐÃI ĐỘC QUYỀN</span>
    <h1 style="font-size:32px;margin:8px 0;font-weight:800;">Kho Mã Invite Code & Mã Giảm Giá AI Miễn Phí</h1>
    <p style="color:#94a3b8;font-size:14px;max-width:750px;">
      Cập nhật danh sách mã mời (Invite Code) nhận <strong>1 Tỷ Token Muse AI miễn phí</strong> và các voucher độc quyền cho Grok, Cursor, ChatGPT. Sao chép 1-click để nhận tài nguyên AI ngay!
    </p>
  </div>

  <!-- Live Status Notice -->
  <div style="background:rgba(6,182,212,0.1);border:1px solid rgba(6,182,212,0.25);border-radius:14px;padding:16px 20px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:30px;">
    <div style="display:flex;align-items:center;gap:10px;">
      <span style="width:10px;height:10px;border-radius:50%;background:#10b981;box-shadow:0 0 10px #10b981;display:inline-block;"></span>
      <span style="font-size:13.5px;color:#e2e8f0;font-weight:600;">Trạng thái: <strong>11 Mã Muse AI 1 Tỷ Token</strong> đang hoạt động và còn lượt sử dụng.</span>
    </div>
    <span class="badge badge-hot">CẬP NHẬT MỖI NGÀY</span>
  </div>

  <!-- Filter Chips -->
  <div class="prompt-filter-bar">
    <button type="button" class="invite-chip prompt-chip active" data-filter="all">Tất Cả Mã ({len(muse_invite_list)}+)</button>
    <button type="button" class="invite-chip prompt-chip" data-filter="muse">Muse AI (Mã 1 Tỷ Token Free)</button>
    <button type="button" class="invite-chip prompt-chip" data-filter="grok">Grok & Cursor AI (Sắp cập nhật)</button>
    <button type="button" class="invite-chip prompt-chip" data-filter="discount">Mã Giảm Giá BotHub</button>
  </div>

  <!-- Invite Codes Grid -->
  <div class="invite-grid">
    {invite_cards_html}

    <!-- Future Expansion Card: Grok & Cursor -->
    <div class="invite-card" data-tool="grok">
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div style="display:flex;align-items:center;gap:8px;">
          <div class="prod-brand-icon icon-grok" style="width:34px;height:34px;font-size:16px;">G</div>
          <span style="font-weight:700;font-size:13px;color:#fff;">Grok Bot / Cursor Pro</span>
        </div>
        <span class="badge badge-purple">SẮP MỞ</span>
      </div>

      <div class="invite-code-box" style="border-style:dotted;opacity:0.8;">
        <span style="font-size:11px;color:#94a3b8;display:block;margin-bottom:4px;">MÃ MỜI ĐỘC QUYỀN</span>
        <span class="invite-code-text" style="color:#94a3b8;font-size:18px;">ĐANG CẬP NHẬT...</span>
      </div>

      <p style="font-size:12px;color:#94a3b8;line-height:1.6;margin-bottom:14px;flex:1;">
        Đăng ký nhận thông báo mã mời hoặc mã giảm giá cho Grok Bot và Cursor AI Pro sớm nhất.
      </p>

      <a href="https://zalo.me/0388888888" target="_blank" rel="noopener" class="btn btn-outline btn-sm btn-block">
        💬 Đăng Ký Nhận Mã Qua Zalo
      </a>
    </div>

    <!-- Future Expansion Card: BotHub Promo Code -->
    <div class="invite-card" data-tool="discount">
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div style="display:flex;align-items:center;gap:8px;">
          <div class="prod-brand-icon icon-chatgpt" style="width:34px;height:34px;font-size:16px;">✦</div>
          <span style="font-weight:700;font-size:13px;color:#fff;">Voucher Giảm 10% Bothub</span>
        </div>
        <span class="badge badge-green">VOUCHER</span>
      </div>

      <div class="invite-code-box" data-copy-invite="BOTHUB2026" title="Nhấn để copy mã BOTHUB2026">
        <span style="font-size:11px;color:#94a3b8;display:block;margin-bottom:4px;">MÃ GIẢM GIÁ ĐƠN HÀNG</span>
        <span class="invite-code-text" style="color:#10b981;">BOTHUB2026</span>
      </div>

      <p style="font-size:12px;color:#94a3b8;line-height:1.6;margin-bottom:14px;flex:1;">
        Giảm ngay 10% khi mua bất kỳ tài khoản ChatGPT Plus, Claude Pro hoặc Muse AI 31 Tỷ Token.
      </p>

      <button type="button" class="btn btn-emerald btn-sm btn-block" data-copy-invite="BOTHUB2026">
        📋 Sao Chép Mã Giảm Giá
      </button>
    </div>
  </div>

  <!-- Instructions Guide -->
  <div style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:20px;padding:35px;margin:50px 0;">
    <h3 style="font-size:22px;color:#fff;margin-bottom:16px;">📖 Hướng Dẫn 3 Bước Nhập Mã Invite Nhận 1 Tỷ Token Muse AI:</h3>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;">
      <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);padding:20px;border-radius:12px;">
        <div style="color:var(--cyan);font-weight:800;font-size:16px;margin-bottom:8px;">Bước 1. Sao Chép Mã</div>
        <p style="font-size:13px;color:#cbd5e1;line-height:1.7;">Chọn 1 mã bất kỳ ở danh sách trên (ưu tiên mã còn 29 lượt) và bấm nút <strong>"Sao Chép Mã"</strong>.</p>
      </div>
      <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);padding:20px;border-radius:12px;">
        <div style="color:var(--cyan);font-weight:800;font-size:16px;margin-bottom:8px;">Bước 2. Truy Cập Muse AI</div>
        <p style="font-size:13px;color:#cbd5e1;line-height:1.7;">Mở trang đăng ký Meta Muse AI và dán mã invite vào ô <em>Invite Code / Referral Code</em>.</p>
      </div>
      <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);padding:20px;border-radius:12px;">
        <div style="color:var(--cyan);font-weight:800;font-size:16px;margin-bottom:8px;">Bước 3. Nhận 1 Tỷ Token</div>
        <p style="font-size:13px;color:#cbd5e1;line-height:1.7;">Hoàn tất tạo tài khoản. Kiểm tra số dư sẽ thấy ngay 1.000.000.000 token miễn phí sẵn sàng làm việc!</p>
      </div>
    </div>
  </div>

  <!-- Upsell Banner: Need more tokens? -->
  <div style="background:linear-gradient(135deg,#1e1b4b,#0e1526);border:1px solid rgba(99,102,241,0.3);border-radius:20px;padding:35px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:20px;margin-bottom:40px;">
    <div>
      <span class="badge badge-hot" style="margin-bottom:8px;">CẦN DUNG LƯỢNG LỚN HƠN?</span>
      <h3 style="font-size:22px;color:#fff;margin:6px 0;">Dùng Hết 1 Tỷ Token Miễn Phí? Nâng Cấp Gói 31 Tỷ Token!</h3>
      <p style="color:#cbd5e1;font-size:13.5px;max-width:600px;">Gói 31 Tỷ Token chỉ <strong>699.000đ</strong> (giá gốc 2.200.000đ) giúp bạn chạy hàng trăm tác vụ cào web, tổng hợp báo cáo và tự động hoá liên tục cả năm.</p>
    </div>
    <div style="display:flex;gap:10px;">
      <button type="button" class="btn btn-emerald btn-lg" onclick="window.__openCheckout('muse-31b')">⚡ Mua Gói 31 Tỷ Token (699k)</button>
      <a href="muse-ai.html" class="btn btn-outline btn-lg">Xem Chi Tiết ↗</a>
    </div>
  </div>
</div>
'''

# =========================================================================
# WRITE ALL PAGES
# =========================================================================
pages = [
    ('index.html', 'Chợ Công Cụ & Tài Khoản AI Số 1 Việt Nam', 'Sở hữu Muse AI, Grok Bot, ChatGPT Plus, Claude Pro với chi phí rẻ nhất. Kích hoạt tự động 5 phút, bảo hành 1 đổi 1.', home_content, 'home'),
    ('ai-agent.html', 'Tất Cả Công Cụ AI & Autonomous Agents', 'Danh mục tài khoản AI Agent, Muse AI, Grok Bot, ChatGPT, Claude Pro, Gemini. Mua ngay nhận mã VietQR.', agent_content, 'agent'),
    ('muse-ai.html', 'Muse AI: Gói 1 Tỷ & 31 Tỷ Token Giá Rẻ', 'Muse AI Autonomous Agent có máy tính riêng, tự duyệt web, làm việc 24/7. Giá từ 69.000đ.', muse_content, 'muse'),
    ('grok-bot.html', 'Grok Bot: Quyền Truy Cập Grok Autonomous', 'Tích hợp Grok vào Cursor AI Pro và SuperGrok VIP. Máy tính cloud terminal riêng.', grok_content, 'grok'),
    ('ma-invite.html', 'Kho Mã Invite Code Muse AI 1 Tỷ Token & Công Cụ AI Miễn Phí', 'Cập nhật danh sách mã invite code Muse AI nhận 1 tỷ token miễn phí, mã mời Grok Bot, Cursor, voucher giảm giá.', invite_content, 'invite'),
    ('chatgpt.html', 'ChatGPT Plus Chính Chủ Email & Team', 'Nâng cấp ChatGPT Plus chính chủ trên email của bạn. GPT-4o, GPT-o1, tạo ảnh Canvas.', chatgpt_content, 'chatgpt'),
    ('claude-ai.html', 'Claude AI Pro Sonnet 3.7 & Opus', 'Mua tài khoản Claude Pro chính hãng. Siêu trí tuệ lập trình và viết văn tự nhiên.', claude_content, 'claude'),
    ('gemini-ai.html', 'Gemini Advanced 2TB Google One AI', 'Gemini 2.0 Pro đỉnh cao + 2000GB Google Drive tích hợp Gmail, Docs.', gemini_content, 'gemini'),
    ('thu-vien-prompt.html', 'Kho Thư Viện Prompt AI Thực Chiến Miễn Phí', 'Tuyển tập 1000+ prompt hay cho AI Agent, Marketing, Coding, Midjourney.', prompt_content, 'prompts'),
    ('so-sanh.html', 'So Sánh Các Dòng Siêu AI Chi Tiết', 'Bảng ma trận so sánh tính năng và giá giữa Muse, Grok, ChatGPT, Claude, Gemini.', compare_content, 'compare'),
    ('gio-hang.html', 'Giỏ Hàng & Thanh Toán VietQR', 'Danh sách gói AI đã lưu, thanh toán VietQR tự động nhận tài khoản sau 5 phút.', cart_content, 'cart'),
    ('chinh-sach.html', 'Chính Sách Bảo Hành & Cam Kết Dịch Vụ', 'Cam kết bảo hành 1 đổi 1 trọn gói, kích hoạt siêu tốc và hoàn tiền 100%.', policy_content, 'policy'),
    ('cua-hang.html', 'Danh Mục Sản Phẩm AI Agent', 'Tổng hợp tất cả công cụ AI và Autonomous Agent tại BotHub.vn.', agent_content, 'agent')
]

for filename, title, desc, content, active_key in pages:
    filepath = ROOT / filename
    html = render_page(title, desc, content, active_key)
    filepath.write_text(html, encoding='utf-8')
    print(f"Generated {filename} ({round(len(html)/1024, 1)} KB)")

print("All marketplace pages generated successfully!")
