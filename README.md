# BotHub.vn · HTML storefront prototype v1.0

**Tạo ngày:** 08/10/2026  
**Trạng thái:** HTML demo để duyệt giao diện, **không phải website đang nhận đơn hàng**.

## Mở bản demo

1. Giải nén tệp ZIP.
2. Mở `index.html` trong trình duyệt Chrome/Edge hoặc Firefox.
3. Bấm **Cửa hàng** để xem grid và bộ lọc. Bấm vào Muse AI / Grok Bot / ChatGPT để vào từng trang chi tiết.
4. Các trang HTML liên kết bằng đường dẫn tương đối nên cần giữ nguyên thư mục `assets/`.

Không cần cài WordPress, Node, React hay chạy máy chủ để xem giao diện. Font web Google là thành phần tùy chọn; trình duyệt sẽ fallback về sans-serif nếu offline.

## Cấu trúc dự án

```text
bothub-html-preview/
├── index.html                # Homepage
├── cua-hang.html             # Shop + tìm kiếm, lọc, sắp xếp
├── muse-ai.html              # Detail: biến thể 1 tỷ/31 tỷ token
├── grok-bot.html             # Detail: route Cursor / SuperGrok
├── chatgpt.html              # Detail: Go / Plus / Pro / Business
├── thu-vien-prompt.html      # Prompt cards, lọc và copy
├── so-sanh.html              # Trang so sánh
├── gio-hang.html             # Danh sách quan tâm, không checkout
├── chinh-sach.html           # Placeholder chính sách ở giai đoạn demo
├── assets/
│   ├── styles.css            # CSS responsive (shared)
│   ├── app.js                # JavaScript thuần, không dependency
│   └── favicon.svg
├── previews/                 # Ảnh chụp desktop và mobile
├── docs/
│   └── WORDPRESS-MIGRATION.md
└── build.py                  # Script tái tạo HTML gốc (không cần khi xem)
```

## Tương tác hoạt động trong demo

- Shop: tìm theo tên, chọn bộ lọc danh mục, sắp xếp giá/tên, trạng thái rỗng.
- Muse: chọn hai biến thể, cập nhật mức giá dự kiến và mã SKU.
- Grok Bot: chọn đường truy cập Cursor/SuperGrok và cấp gói nghiên cứu.
- ChatGPT: chọn Go/Plus/Pro/Business.
- Tất cả detail: tab thông tin, FAQ, lưu gói vào danh sách quan tâm.
- Prompt: lọc theo chủ đề, copy prompt vào clipboard.
- Header: điều hướng, tìm kiếm, menu mobile và bộ đếm gói đã lưu.
- Giỏ hàng: dùng `localStorage` **chỉ trong trình duyệt**, không có backend.
- Modal quan tâm: mô phỏng biểu mẫu. **Không gửi thông tin đăng ký đi đâu.**

## Lưu ý quan trọng

- Hai giá Muse **69.000đ/699.000đ** là **giá dự kiến chủ website đưa ra**; số dư, thời hạn và quyền phân phối chưa xác minh.
- Grok Bot và ChatGPT chỉ hiển thị các lựa chọn để tìm hiểu; không công bố giá BotHub hay quyền bán lại.
- Chưa mở giỏ hàng thanh toán, không giao tài khoản, không gửi email, không thu thập mật khẩu hay cookie.
- Không dùng ảnh/logo chính thức nhằm tránh ngụ ý là đại lý được ủy quyền. Các tile minh họa chỉ dùng chữ và hình học tự dựng.
- Giao diện hiện `noindex,nofollow` để tránh index nhầm staging HTML. Khi chuyển WordPress, đánh giá lại theo tình trạng từng sản phẩm, không tháo chặn cho toàn bộ trang tự động.

## Xây lại trang

`python build.py` tạo lại 9 file HTML từ template tĩnh. Tùy chỉnh bố cục trong `build.py`; CSS tại `assets/styles.css`; logic tại `assets/app.js`.

## Next step đề xuất

Duyệt giao diện trang chủ và shop → duyệt Muse / Grok / ChatGPT → chốt chính sách & SKU được phép bán → chuyển thành custom WordPress theme + WooCommerce templates.
