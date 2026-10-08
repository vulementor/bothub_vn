# BotHub HTML → WordPress/WooCommerce mapping

## 1. Sitemap mapping

| HTML preview | URL WordPress dự kiến | Template |
|---|---|---|
| `index.html` | `/` | front-page.php |
| `cua-hang.html` | `/cua-hang/` | archive-product.php |
| `muse-ai.html` | `/cong-cu/muse-ai/` | single-ai_tool.php + WooCommerce variant chỉ khi đủ điều kiện |
| `grok-bot.html` | `/cong-cu/grok-bot/` | single-ai_tool.php |
| `chatgpt.html` | `/cong-cu/chatgpt/` | single-ai_tool.php |
| `thu-vien-prompt.html` | `/thu-vien-prompt/` | archive-prompt.php |
| `so-sanh.html` | `/so-sanh/muse-grok-bot-chatgpt/` | single-comparison.php |
| `gio-hang.html` | `/gio-hang/` | Woo cart, chỉ khi có SKU LIVE |
| `chinh-sach.html` | `/chinh-sach/` | WordPress page, thay bằng nội dung pháp lý thực |

**Quan trọng:** Giao diện Muse/Grok/ChatGPT hiện là hồ sơ công cụ để preview. Khi chuyển WordPress, route `/cong-cu/` nhắm mục đích khám phá, còn route `/san-pham/` dành riêng cho trang giao dịch sản phẩm đủ điều kiện. Đừng triển khai hai trang cùng H1 và nội dung gần trùng nhau.

## 2. Data architecture

### WordPress post types

- `ai_tool`: các hồ sơ Muse/Grok/ChatGPT; có tên hãng, mô tả, FAQ, link guide, `last_verified_at`.
- `prompt`: tên prompt, chủ đề, văn bản, hướng dẫn, độ khó và công cụ tương thích.
- `comparison`: bài so sánh có phương pháp và ngày đối chiếu.
- `post`: bài viết SEO và hướng dẫn.

### WooCommerce

- Product parent (nếu được phê duyệt): `muse-ai-token`, variations `MUSE-1B`, `MUSE-31B`.
- `grok-bot-cursor`, `grok-bot-supergrok` và `chatgpt-*`: không sinh public product SKU cho tới khi xác minh đủ điều kiện cung ứng.
- Price/stock/activation/refund fields do WooCommerce quản lý, không hardcode trong template.
- Custom meta tối thiểu: `source_verified_at`, `terms_checked_at`, `resale_authorization_status`, `fulfillment_test_at`, `valid_until`, `purchase_cta_allowed`.

## 3. Gating sản phẩm

1. RESEARCH: thu thập thông tin, chưa cho mua.
2. SUPPLIER_VERIFIED: nguồn cung có bằng chứng.
3. RIGHTS_VERIFIED: điều khoản/ủy quyền cho phép hình thức phân phối.
4. FULFILLMENT_TESTED: kiểm chứng quy trình giao/activate, balance/expiry thực tế.
5. APPROVED: pháp lý, giá và nội dung được duyệt.
6. LIVE: chỉ lúc này mở offer, thanh toán, giao file/key/seat hợp lệ.

Nếu không hợp lệ: chuyển sang bài hướng dẫn + affiliate chính thức hoặc dịch vụ hỗ trợ độc lập. Không gửi credential để vượt qua hạn chế tài khoản cá nhân.

## 4. Code migration

- Tách `header()` / `footer()` thành WordPress header.php / footer.php.
- `assets/styles.css` được enqueue qua `wp_enqueue_style`, `assets/app.js` qua `wp_enqueue_script`.
- Tìm kiếm/filter shop dùng Woo product query với server-side pagination/caching; không dùng array DOM khi lên 240 URL.
- Giỏ hàng `localStorage` chỉ dành cho HTML demo; khi có SKU LIVE thay bằng session/cookie và WooCommerce cart nonce.
- Mẫu đăng ký quan tâm cần backend thật, opt-in rõ ràng, consent và chống spam.
- Điều hướng shop/category chuyển từ `.html` sang permalink hoàn chỉnh.
- Thêm schema phù hợp dữ liệu thực, breadcrumb, canonical, sitemap XML cho URL đã publish; staging phải noindex.
- Không đưa website live khi chưa bổ sung thông tin pháp nhân, điều khoản sử dụng, chính sách dữ liệu, hoàn tiền và hỗ trợ.

## 5. SEO content plan

Pillar `ai-agent/` → Tool `/cong-cu/` → Plan explainer `/goi/` → Product `/san-pham/` chỉ khi LIVE. Prompt `/prompt/` → Tool và hướng dẫn. Tách search intent cho từng URL để tránh cannibalization.

## 6. User journeys để QA sau khi chuyển

- Trang chủ → shop → category → hồ sơ Muse → chọn biến thể → giỏ Woo → checkout thật (chỉ SKU LIVE).
- Shop → tìm Grok → so sánh hai route → nội dung hướng dẫn; không thể mua khi HOLD.
- Prompt library → lọc → copy → trang công cụ liên quan.
- Mobile: menu, điều hướng, sticky cart không che nội dung, thanh toán không bị cache.
