# seo_articles.py - Module tạo các trang bài viết thủ thuật AI chuẩn SEO Google
from pathlib import Path

def get_related_links_html():
    return '''
    <a href="huong-dan-dang-ky-muse-ai-vpn.html" class="related-item-link">
      <strong>Hướng dẫn đăng ký Muse AI bằng VPN</strong>
      <small>Fake IP US nhận 1 tỷ token</small>
    </a>
    <a href="huong-dan-dang-ky-muse-ai-chatgpt-oauth.html" class="related-item-link">
      <strong>Đăng ký Muse AI bằng Google / ChatGPT</strong>
      <small>1-Click bảo mật không lo quên pass</small>
    </a>
    <a href="huong-dan-nuoi-da-nick-muse-ai-exmount.html" class="related-item-link">
      <strong>Nuôi đa nick Muse AI bằng Exmount Browser</strong>
      <small>Fake Fingerprint & Proxy cắm bot 24/7</small>
    </a>
    <a href="meo-toi-uu-token-muse-ai.html" class="related-item-link">
      <strong>Mẹo tối ưu phân bổ 31 tỷ token Muse AI</strong>
      <small>Tiết kiệm 40% chi phí sử dụng</small>
    </a>
    <a href="cach-sua-loi-403-forbidden-ai-cloudflare.html" class="related-item-link">
      <strong>Sửa lỗi 403 Forbidden & Cloudflare Captcha</strong>
      <small>Đổi IP sạch & xóa site storage</small>
    </a>
    '''

def render_article_page(header_html, footer_html, art):
    slug = art['slug']
    title = art['title']
    meta_desc = art['meta_desc']
    keywords = art['keywords']
    category = art['category']
    read_time = art['read_time']
    date_pub = art['date_pub']
    date_mod = art['date_mod']
    lead = art['lead']
    steps = art['steps']
    tip_text = art['tip_text']
    cta_title = art['cta_title']
    cta_link = art['cta_link']
    cta_btn = art['cta_btn']
    video_info = art.get('video_info')

    # Build steps HTML & Schema
    step_items_html = ""
    schema_steps_list = []
    
    for idx, s in enumerate(steps, 1):
        clean_text = s['desc'].replace('<strong>', '').replace('</strong>', '').replace('<code>', '').replace('</code>', '')
        step_name = s['title'].replace('"', '\\"')
        clean_text_escaped = clean_text.replace('"', '\\"')
        
        schema_steps_list.append(f'''{{
          "@type": "HowToStep",
          "name": "{step_name}",
          "text": "{clean_text_escaped}",
          "url": "https://bothub.vn/{slug}#step-{idx}"
        }}''')
        
        code_html = ""
        if s.get('code'):
            c = s['code'].replace("'", "\\'")
            code_html = f'''
            <div class="code-command-box">
              <span>{s['code']}</span>
              <button type="button" onclick="navigator.clipboard.writeText('{c}');alert('Đã sao chép vào bộ nhớ tạm!');">Copy</button>
            </div>
            '''

        step_items_html += f'''
        <div class="article-step-block" id="step-{idx}">
          <div class="article-step-header">
            <div class="article-step-badge">{idx}</div>
            <h3 class="article-step-title">{s['title']}</h3>
          </div>
          <div class="article-step-desc">{s['desc']}</div>
          {code_html}
        </div>
        '''

    schema_steps_json = ",\n        ".join(schema_steps_list)

    video_html = ""
    video_schema = ""
    if video_info:
        chips = "".join([f'<span class="video-chapter-chip">⏱️ {ch}</span>' for ch in video_info.get('chapters', [])])
        v_title = video_info.get('title', '')
        v_dur = video_info.get('duration', '03:30')
        video_html = f'''
        <div class="guide-video-player-wrap">
          <div class="video-screen-container">
            <div class="video-screen-mockup-graphic">
              <div class="play-btn-pulse" style="margin:0 auto 12px;cursor:pointer;" onclick="alert('Đang phát video demo HD: {v_title}');">▶</div>
              <h4 style="font-size:18px;color:#fff;font-weight:800;margin-bottom:6px;">{v_title}</h4>
              <p style="font-size:13px;color:#94a3b8;margin:0;">Video thực hành chuẩn HD 1080P · Thời lượng: {v_dur} · BotHub Studio</p>
            </div>
          </div>
          <div class="video-controls-bar">
            <span style="font-size:12px;color:#38bdf8;font-weight:700;">🎬 MỐC THỜI GIAN VIDEO:</span>
            <div class="video-chapters-chips">
              {chips}
            </div>
          </div>
        </div>
        '''
        video_schema = f''',
      {{
        "@type": "VideoObject",
        "name": "{v_title}",
        "description": "{meta_desc}",
        "thumbnailUrl": "https://bothub.vn/assets/logo.png",
        "uploadDate": "{date_pub}T08:00:00+07:00",
        "duration": "PT4M"
      }}'''

    related_links_html = get_related_links_html()

    full_html = f'''<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | BotHub.vn</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="{keywords}">
  <link rel="canonical" href="https://bothub.vn/{slug}">
  <meta name="theme-color" content="#070a13">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/styles.css">

  <!-- Open Graph / Facebook / Zalo -->
  <meta property="og:locale" content="vi_VN">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="https://bothub.vn/{slug}">
  <meta property="og:site_name" content="BotHub.vn - Marketplace Công Cụ AI">
  <meta property="article:published_time" content="{date_pub}T08:00:00+07:00">
  <meta property="article:modified_time" content="{date_mod}T09:00:00+07:00">
  <meta property="article:section" content="{category}">

  <!-- Schema.org Markup for Google SEO -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "Trang Chủ", "item": "https://bothub.vn/" }},
          {{ "@type": "ListItem", "position": 2, "name": "Thủ Thuật AI", "item": "https://bothub.vn/so-sanh.html" }},
          {{ "@type": "ListItem", "position": 3, "name": "{title}", "item": "https://bothub.vn/{slug}" }}
        ]
      }},
      {{
        "@type": "HowTo",
        "name": "{title}",
        "description": "{meta_desc}",
        "totalTime": "PT4M",
        "step": [
        {schema_steps_json}
        ]
      }}{video_schema}
    ]
  }}
  </script>
</head>
<body>
  {header_html}
  
  <main>
    <div class="container article-page-wrap">
      <!-- Breadcrumbs -->
      <nav class="article-breadcrumbs" aria-label="Breadcrumb">
        <a href="index.html">Trang chủ</a>
        <span class="sep">/</span>
        <a href="so-sanh.html">Thủ Thuật AI</a>
        <span class="sep">/</span>
        <span style="color:#fff;">{title}</span>
      </nav>

      <!-- 2-Column SEO Article Layout -->
      <div class="article-layout-grid">
        <!-- Main Article Content -->
        <article class="article-main-content">
          <header class="article-meta-header">
            <div class="article-meta-row">
              <span class="guide-tag hot">{category}</span>
              <span>⏱️ {read_time}</span>
              <span>👤 BotHub Tech Team</span>
              <span>📅 Cập nhật: {date_mod}</span>
            </div>
            <h1 class="article-page-title">{title}</h1>
            <p class="article-lead">{lead}</p>
          </header>

          <!-- Interactive Video Player -->
          {video_html}

          <!-- Step-by-Step Practical Guide -->
          <div class="article-rich-body">
            <h2>Các Bước Thực Hành Chi Tiết (Step-by-Step)</h2>
            {step_items_html}

            <!-- Pro Tip Box -->
            <div class="pro-tip-box" style="margin-top:25px;padding:16px 20px;">
              <strong>⚠️ LƯU Ý TỪ CHUYÊN GIA:</strong> {tip_text}
            </div>

            <!-- In-Article CTA Banner -->
            <div class="article-cta-box">
              <div>
                <h3 style="font-size:18px;font-weight:800;color:#fff;margin-bottom:6px;">{cta_title}</h3>
                <p style="font-size:13.5px;color:#94a3b8;margin:0;">Kỹ thuật viên BotHub hỗ trợ cài đặt cấu hình VPN / Exmount qua Ultraview 1-1 hoàn toàn miễn phí!</p>
              </div>
              <div style="display:flex;gap:10px;flex-wrap:wrap;">
                <a href="{cta_link}" class="btn btn-emerald btn-lg">{cta_btn}</a>
                <a href="https://zalo.me/0388888888" target="_blank" rel="noopener" class="btn btn-outline btn-lg">💬 Zalo Kỹ Thuật 24/7</a>
              </div>
            </div>
          </div>
        </article>

        <!-- Right Sticky Sidebar -->
        <aside class="article-sidebar">
          <!-- Author Card -->
          <div class="sidebar-card">
            <h4>👤 Tác Giả & Kiểm Duyệt</h4>
            <div class="sidebar-author-box">
              <div class="sidebar-author-avatar">✦</div>
              <div>
                <strong style="color:#fff;font-size:14px;display:block;">BotHub Tech Team</strong>
                <span style="color:#10b981;font-size:12px;font-weight:700;">✓ Đã kiểm duyệt 100% hoạt động</span>
              </div>
            </div>
          </div>

          <!-- Free Token Promo Card -->
          <div class="sidebar-card" style="background:linear-gradient(135deg,rgba(6,182,212,0.1),rgba(99,102,241,0.1));border-color:rgba(6,182,212,0.3);">
            <h4 style="color:var(--cyan);">🎁 Kho Invite Code Free</h4>
            <p style="font-size:13px;color:#cbd5e1;line-height:1.6;margin-bottom:14px;">
              Lấy ngay mã mời Muse AI nhận <strong>1.000.000.000 Token</strong> miễn phí vào ví hôm nay!
            </p>
            <a href="ma-invite.html" class="btn btn-cyan btn-block">Nhận Mã 1 Tỷ Token →</a>
          </div>

          <!-- Related Posts -->
          <div class="sidebar-card">
            <h4>📚 Bài Viết Cùng Chuyên Mục</h4>
            <div class="sidebar-related-list">
              {related_links_html}
            </div>
          </div>

          <!-- Quick Matrix Compare Link -->
          <div class="sidebar-card">
            <h4>⚖️ Đối Chiếu Công Cụ</h4>
            <p style="font-size:13px;color:#94a3b8;margin-bottom:12px;">Xem bảng so sánh giá và tính năng giữa Muse AI, Grok Bot, ChatGPT Plus và Claude Pro.</p>
            <a href="so-sanh.html#bang-so-sanh" class="btn btn-outline btn-block btn-sm">Xem Bảng So Sánh AI →</a>
          </div>
        </aside>
      </div>
    </div>
  </main>

  {footer_html}
</body>
</html>'''
    return full_html


# Danh sách 5 bài viết chuẩn SEO chi tiết
seo_articles_list = [
    {
        'slug': 'huong-dan-dang-ky-muse-ai-vpn.html',
        'title': 'Hướng Dẫn Đăng Ký Muse AI Bằng VPN Nhận 1 Tỷ Token (Chống Chặn IP 2026)',
        'meta_desc': 'Hướng dẫn chi tiết cách đăng ký tài khoản Meta Muse AI bằng VPN không bị chặn IP tại Việt Nam. Kích hoạt trọn vẹn 1 tỷ token miễn phí, video thực hành từng bước.',
        'keywords': 'đăng ký muse ai bằng vpn, hướng dẫn đăng ký muse ai, nhận 1 tỷ token muse ai, fake ip đăng ký muse ai, invite code muse ai',
        'category': 'MUSE AI · VPN FAKE IP',
        'read_time': '4 Phút Đọc',
        'date_pub': '2026-10-09',
        'date_mod': '2026-10-09',
        'lead': 'Nền tảng Meta Muse AI thường giới hạn IP tại Việt Nam hoặc chặn cấp phát gói 1 Tỷ Token miễn phí. Hướng dẫn chi tiết cách dùng VPN sạch (US/Singapore) để đăng ký thành công 100% và nhận ngay 1.000.000.000 Token vào ví tài khoản.',
        'video_info': {
            'title': 'Video Demo: Đăng Ký Muse AI Bằng Proton VPN & Nhập Invite Code 1 Tỷ Token',
            'duration': '03:45',
            'chapters': ['00:15 - Bật VPN Server US', '01:05 - Mở Tab Ẩn Danh', '01:50 - Nhập Invite Code', '02:40 - Kích Hoạt Ví 1 Tỷ Token']
        },
        'steps': [
            {
                'title': 'Cài đặt phần mềm VPN uy tín có dải IP sạch',
                'desc': 'Khuyên dùng các phần mềm VPN chất lượng cao: <strong>Proton VPN</strong> (bản free có server US/NL/JP tốc độ cao), <strong>Cloudflare 1.1.1.1 WARP</strong>, hoặc <strong>NordVPN / ExpressVPN</strong>. Tránh dùng các tiện ích VPN extension miễn phí tràn lan dễ bị Cloudflare đưa vào Blacklist.'
            },
            {
                'title': 'Kết nối máy chủ United States hoặc Singapore',
                'desc': 'Chọn server US (San Jose, California hoặc New York) hoặc Singapore. Sau khi kết nối, truy cập <code>whoer.net</code> hoặc <code>ipinfo.io</code> để kiểm tra độ ẩn danh đạt từ <strong>80% - 100%</strong> (màu xanh lá).'
            },
            {
                'title': 'Mở cửa sổ trình duyệt ẩn danh (Incognito Mode)',
                'desc': 'Nhấn tổ hợp phím <code>Ctrl + Shift + N</code> (hoặc <code>Cmd + Shift + N</code> trên macOS). Bước này cách ly hoàn toàn cookies và cache cũ, ngăn Muse AI nhận diện vị trí địa lý trước đó.'
            },
            {
                'title': 'Mở trang đăng ký Muse AI & Dán mã Invite Code',
                'desc': 'Mở trang đăng ký chính thức của Muse AI. Điền email và dán một trong các mã mời độc quyền còn lượt từ BotHub vào ô <em>Invite / Referral Code</em>:',
                'code': 'Mã Invite Code đang hoạt động: ZACDIA  |  6WVLSZ  |  PYWR4C  |  5CVT4Y'
            },
            {
                'title': 'Xác thực Email OTP & Nhận ngay 1 Tỷ Token',
                'desc': 'Mở hòm thư email, lấy mã xác nhận OTP và hoàn tất tạo mật khẩu. Đăng nhập vào bảng điều khiển Muse AI: Kiểm tra số dư ví thấy ngay <strong>1.000.000.000 Token (1 Tỷ Token)</strong> sẵn sàng làm việc!'
            }
        ],
        'tip_text': 'Tuyệt đối giữ nguyên kết nối VPN trong suốt quá trình điền form và xác nhận mã email OTP. Không ngắt kết nối giữa chừng để tránh hệ thống hủy phiên đăng ký.',
        'cta_title': 'Chưa Có Mã Invite Code? Lấy Ngay Miễn Phí Tại BotHub',
        'cta_link': 'ma-invite.html',
        'cta_btn': '🎁 Lấy Mã Invite Code 1 Tỷ Token'
    },
    {
        'slug': 'huong-dan-dang-ky-muse-ai-chatgpt-oauth.html',
        'title': 'Hướng Dẫn Đăng Ký Muse AI Bằng Google & ChatGPT Auth 1-Click Nhận 1 Tỷ Token',
        'meta_desc': 'Cách tạo tài khoản Muse AI bằng Google OAuth và OpenAI ChatGPT 1-click an toàn, không lo quên pass, hạn chế checkpoint và nhận ngay 1 tỷ token vào ví.',
        'keywords': 'đăng ký muse ai bằng chatgpt, đăng ký muse ai bằng google, tạo tài khoản muse ai, oauth muse ai',
        'category': 'OAUTH 2.0 · FAST PASS',
        'read_time': '2 Phút Đọc',
        'date_pub': '2026-10-09',
        'date_mod': '2026-10-09',
        'lead': 'Phương thức đăng ký nhanh gọn và an toàn nhất: Không cần tạo mật khẩu riêng, không lo email OTP bị rơi vào Spam/Rác. Tài khoản tạo bằng Google/ChatGPT OAuth có Trust Score cao hơn rất nhiều, hạn chế tối đa nguy cơ checkpoint.',
        'video_info': {
            'title': 'Video Demo: Đăng Ký 1-Click Liên Kết Google & OpenAI Nhận Ngay 1 Tỷ Token',
            'duration': '02:15',
            'chapters': ['00:10 - Đăng nhập sẵn Google/OpenAI', '00:45 - Nhấp Login with OAuth', '01:20 - Điền Invite Code']
        },
        'steps': [
            {
                'title': 'Đăng nhập sẵn tài khoản Gmail hoặc OpenAI',
                'desc': 'Mở trình duyệt chính và đăng nhập sẵn tài khoản Google Gmail hoặc tài khoản OpenAI ChatGPT bạn đang sử dụng.'
            },
            {
                'title': 'Chọn phương thức liên kết OAuth 2.0',
                'desc': 'Tại trang Sign-up của Muse AI, nhấp nút <strong>"Continue with Google"</strong> hoặc <strong>"Login via OpenID/ChatGPT Auth"</strong>. Hệ thống chỉ yêu cầu quyền định danh cơ bản (Email & Tên), tuyệt đối bảo mật.'
            },
            {
                'title': 'Điền mã Invite Code kích hoạt 1 Tỷ Token',
                'desc': 'Ở bước hoàn tất hồ sơ, nhập mã Invite Code từ BotHub vào ô Referral Code để hệ thống tự động cộng 1 Tỷ Token miễn phí.',
                'code': 'Mã Invite Code độc quyền: ZACDIA'
            },
            {
                'title': 'Sử dụng ngay lập tức',
                'desc': 'Tài khoản kích hoạt hoàn tất trong 30 giây. Bạn có thể sử dụng trực tiếp trên giao diện web hoặc trích xuất API Key để kết nối vào phần mềm.'
            }
        ],
        'tip_text': 'Tài khoản liên kết Google Auth có độ tin cậy cực cao, gần như không bao giờ bị hệ thống gắn cờ bot hoặc yêu cầu xác minh danh tính rườm rà.',
        'cta_title': 'Nhận Danh Sách Mã Invite Code Còn Lượt Tại BotHub',
        'cta_link': 'ma-invite.html',
        'cta_btn': '🎁 Lấy Mã Invite Code Mới Nhất'
    },
    {
        'slug': 'huong-dan-nuoi-da-nick-muse-ai-exmount.html',
        'title': 'Hướng Dẫn Nuôi Đa Nick Muse AI Bằng Trình Duyệt Antidetect Exmount Chạy Bot 24/7',
        'meta_desc': 'Bí quyết tạo hàng chục profile Muse AI cách ly vân tay (fingerprint) trên Exmount Browser, gán Proxy dân cư tĩnh cắm Agent cào data tự động không lo bị khóa.',
        'keywords': 'nuôi nick muse ai, trình duyệt antidetect exmount, fake fingerprint muse ai, proxy dân cư muse ai, automation agent',
        'category': 'CHUYÊN SÂU DEV · ANTIDETECT BROWSER',
        'read_time': '5 Phút Đọc',
        'date_pub': '2026-10-09',
        'date_mod': '2026-10-09',
        'lead': 'Dành cho anh em Dev, Automation & Affiliate cần cắm hàng chục Agent tự hành 24/7 cào dữ liệu, xử lý hàng trăm tác vụ mà không sợ bị trùng vân tay (fingerprint) trình duyệt hay bị khóa tài khoản hàng loạt.',
        'video_info': {
            'title': 'Video Demo: Cấu Hình Exmount Browser & Gán Proxy Dân Cư Nuôi Đa Nick',
            'duration': '05:20',
            'chapters': ['00:20 - Cài đặt Exmount Browser', '01:15 - Fake Fingerprint độc lập', '02:30 - Gán Proxy dân cư tĩnh', '04:10 - Đăng ký & Xuất Cookie JSON']
        },
        'steps': [
            {
                'title': 'Cài đặt phần mềm Trình duyệt Antidetect Exmount',
                'desc': 'Khuyên dùng <strong>Exmount Browser</strong> (tối ưu hóa chuyên sâu cho AI & Automation, nhẹ nhàng, chạy song song nhiều profile mượt mà) hoặc AdsPower / GoLogin.'
            },
            {
                'title': 'Tạo Profile độc lập và Fake Fingerprint sạch',
                'desc': 'Tạo profile mới (ví dụ <code>Muse-Bot-01</code>). Chọn giả lập OS (Windows 11 / macOS), tự động sinh thông số mới: Canvas Fingerprint, WebGL Vendor, AudioContext, Font List, CPU cores, RAM và bật WebRTC chống rò rỉ IP thật.'
            },
            {
                'title': 'Gán Proxy dân cư (Residential Proxy SOCKS5/HTTP)',
                'desc': 'Mỗi Profile gán một Proxy riêng biệt (IP tĩnh sạch). Sau khi mở profile, truy cập <code>browserleaks.com</code> hoặc <code>pixelscan.net</code> kiểm tra độ sạch đạt 100% màu xanh.'
            },
            {
                'title': 'Mở Profile & Tiến hành đăng ký tài khoản',
                'desc': 'Mỗi profile mở lên tương đương một máy tính độc lập tại một quốc gia khác. Đăng ký Muse AI và nhập Invite Code từ BotHub để mỗi profile đều sở hữu 1 Tỷ Token riêng biệt.',
                'code': 'Mã Invite Code: 6WVLSZ  |  PYWR4C  |  Q2E6IN'
            },
            {
                'title': 'Xuất Cookie JSON cắm bot tự động chạy 24/7',
                'desc': 'Cài extension Cookie-Editor trong profile Exmount, xuất file cookies dạng JSON. Bạn có thể nạp file cookie này vào script NodeJS/Python để bot làm việc liên tục không cần đăng nhập lại!'
            }
        ],
        'tip_text': 'BÍ KÍP CHỐNG CHECKPOINT: Tuyệt đối không đăng nhập chéo tài khoản giữa các Profile. Luôn xuất file Cookies dự phòng định kỳ hàng tuần.',
        'cta_title': 'Cần Hỗ Trợ Cấu Hình Exmount & Cung Cấp Proxy Sạch?',
        'cta_link': 'https://zalo.me/0388888888',
        'cta_btn': '💬 Nhắn Zalo Hỗ Trợ Kỹ Thuật 1-1'
    },
    {
        'slug': 'meo-toi-uu-token-muse-ai.html',
        'title': 'Bí Quyết Săn Invite Code & Tối Ưu Phân Bổ 31 Tỷ Token Muse AI Tiết Kiệm 70%',
        'meta_desc': 'Kỹ thuật tối ưu hóa context prompt dạng JSON nén giúp tiết kiệm 40% token Muse AI. Mẹo săn Invite Code hàng ngày và nâng cấp gói 31 tỷ token giá rẻ tại BotHub.',
        'keywords': 'tối ưu token muse ai, săn invite code muse ai, gói 31 tỷ token muse ai, tiết kiệm token agent',
        'category': 'TỐI ƯU CHI PHÍ · TOKEN MANAGEMENT',
        'read_time': '3 Phút Đọc',
        'date_pub': '2026-10-09',
        'date_mod': '2026-10-09',
        'lead': 'Làm sao để 1 Tỷ Token không bị tiêu hao vô ích trong vài ngày? Hướng dẫn thiết lập tham số Agent, tối ưu độ dài context prompt và thời điểm nên nâng cấp gói 31 Tỷ Token tại BotHub để tối ưu chi phí.',
        'video_info': {
            'title': 'Video Demo: Chiến Lược Viết Prompt Chuẩn Minified Tiết Kiệm 40% Token',
            'duration': '03:10',
            'chapters': ['00:15 - Giới hạn Max Output Tokens', '01:00 - Kỹ thuật Prompt ép JSON nén', '02:10 - Khi nào nâng cấp gói 31 Tỷ']
        },
        'steps': [
            {
                'title': 'Giới hạn Max Tokens trong cấu hình Agent',
                'desc': 'Với các tác vụ phân loại hoặc trích xuất dữ liệu, luôn đặt <code>max_tokens: 500 - 1000</code>. Tránh để mặc định làm Agent tự sinh giải thích dài dòng tốn token.'
            },
            {
                'title': 'Yêu cầu trả kết quả dạng JSON Minified',
                'desc': 'Cấu hình System Prompt: <em>"Respond only with minified JSON, no preamble, no markdown backticks"</em>. Kỹ thuật này giúp tiết kiệm từ 35% đến 50% lượng token truyền tải.',
                'code': 'System Prompt Tip: {"format": "json_compact", "explain": false}'
            },
            {
                'title': 'Săn mã Invite Code mới hàng ngày',
                'desc': 'Truy cập trang <a href="ma-invite.html" style="color:var(--cyan);font-weight:700;">Kho Invite Code BotHub</a> mỗi ngày để lấy các mã mới khi cần bổ sung token cho tài khoản phụ.'
            },
            {
                'title': 'Nâng cấp gói 31 Tỷ Token giá chỉ 249.000đ',
                'desc': 'Nếu triển khai dự án doanh nghiệp dài hạn, gói 31 Tỷ Token tại BotHub là giải pháp tối ưu nhất, rẻ hơn 85% so với mua credit lẻ và được bảo hành 1 đổi 1 suốt thời gian sử dụng.'
            }
        ],
        'tip_text': 'Khi chạy bot cào web lớn, hãy tách nhỏ các batch công việc để nếu có task bị lỗi mạng sẽ không làm hao tổn toàn bộ context token.',
        'cta_title': 'Khám Phá Gói Muse AI 31 Tỷ Token Giá Cực Ưu Đãi',
        'cta_link': 'muse-ai.html',
        'cta_btn': '⚡ Xem Gói 31 Tỷ Token (699k)'
    },
    {
        'slug': 'cach-sua-loi-403-forbidden-ai-cloudflare.html',
        'title': 'Cách Sửa Lỗi 403 Forbidden & Kẹt Captcha Cloudflare Khi Dùng AI Quốc Tế',
        'meta_desc': 'Tổng hợp cách sửa lỗi 403 Forbidden, Access Denied, IP Blocked và vòng lặp xác minh Cloudflare Turnstile khi truy cập các công cụ AI từ Việt Nam.',
        'keywords': 'sửa lỗi 403 forbidden ai, kẹt captcha cloudflare muse ai, fix lỗi access denied, đổi ip vpn sạch',
        'category': 'TROUBLESHOOTING · FIX LỖI 403',
        'read_time': '3 Phút Đọc',
        'date_pub': '2026-10-09',
        'date_mod': '2026-10-09',
        'lead': 'Tổng hợp bí quyết xử lý các lỗi thường gặp nhất khi anh em dùng AI quốc tế: "Access Denied", "Rate Limit Exceeded", "Verification Loop" và cách đổi IP sạch trong 30 giây.',
        'video_info': {
            'title': 'Video Demo: Xử Lý Dứt Điểm Lỗi Access Denied Và Cloudflare Loop',
            'duration': '02:40',
            'chapters': ['00:20 - Xóa Site Data trong Application', '01:05 - Đổi Server VPN sạch', '01:50 - Tắt Extension chặn script']
        },
        'steps': [
            {
                'title': 'Xóa Cache & Cookies cục bộ của trang (Clear Site Data)',
                'desc': 'Nhấn <code>F12</code> -> Chuyển sang tab <strong>Application</strong> -> Chọn <strong>Storage</strong> bên trái -> Nhấp nút <strong>Clear site data</strong>. Thao tác này xóa sạch cờ nhận diện cũ.'
            },
            {
                'title': 'Đổi máy chủ VPN sang server sạch hơn',
                'desc': 'Nếu server US East bị chặn, đổi sang US West (San Jose, Los Angeles) hoặc server Châu Âu (Frankfurt, Amsterdam). Các server này có dải IP ít bị Cloudflare gắn cờ đen.'
            },
            {
                'title': 'Chuyển DNS máy tính sang Cloudflare 1.1.1.1',
                'desc': 'Chuyển DNS mạng máy tính sang <code>1.1.1.1</code> và <code>1.0.0.1</code> (Cloudflare DNS) hoặc <code>8.8.8.8</code> (Google DNS) để giải quyết lỗi phân giải tên miền bị nhà mạng chặn.'
            },
            {
                'title': 'Tắt các Extension xung đột với Cloudflare Turnstile',
                'desc': 'Tạm thời tắt các tiện ích AdBlock, uBlock Origin hoặc Privacy Badger vì chúng có thể vô tình chặn các script xác thực của Cloudflare gây ra vòng lặp vô tận.'
            }
        ],
        'tip_text': 'Nếu vẫn bị chặn IP, hãy dùng chế độ chia sẻ 4G từ điện thoại qua máy tính và kết nối VPN, dải IP mạng di động có độ sạch rất cao.',
        'cta_title': 'Vẫn Bị Lỗi Mạng? Liên Hệ Kỹ Thuật Viên Hỗ Trợ Trực Tiếp',
        'cta_link': 'https://zalo.me/0388888888',
        'cta_btn': '💬 Nhắn Zalo Hỗ Trợ Kỹ Thuật'
    }
]
