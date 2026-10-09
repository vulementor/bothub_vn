/**
 * BOTHUB.VN - MARKETPLACE INTERACTIVE ENGINE
 * Cart System, Dynamic VietQR Checkout, Fast Search & Variant Selectors
 */

(function () {
  'use strict';

  // Master Catalog Data
  const CATALOG = {
    'muse-1b': {
      id: 'muse-1b',
      name: 'Muse AI · Gói 1 Tỷ Token',
      category: 'agent',
      price: 69000,
      originalPrice: 250000,
      icon: 'M',
      iconClass: 'icon-muse',
      badge: 'TIẾT KIỆM 72%',
      url: 'muse-ai.html',
      desc: '1 Tỷ Token Meta Muse Autonomous. Tự duyệt web, điền form, chạy nền 24/7.'
    },
    'muse-31b': {
      id: 'muse-31b',
      name: 'Muse AI · Gói 31 Tỷ Token',
      category: 'agent',
      price: 699000,
      originalPrice: 2200000,
      icon: 'M',
      iconClass: 'icon-muse',
      badge: 'BEST SELLER',
      url: 'muse-ai.html',
      desc: '31 Tỷ Token dung lượng cực lớn cho công việc tự động hoá workflow chuyên sâu.'
    },
    'muse-unlimited': {
      id: 'muse-unlimited',
      name: 'Muse AI · Gói VIP Doanh Nghiệp',
      category: 'business',
      price: 1890000,
      originalPrice: 4500000,
      icon: 'M',
      iconClass: 'icon-muse',
      badge: 'VIP PRO',
      url: 'muse-ai.html',
      desc: '100 Tỷ Token + Hỗ trợ thiết lập kịch bản Automation độc quyền từ kỹ thuật viên.'
    },
    'grok-cursor': {
      id: 'grok-cursor',
      name: 'Grok Bot qua Cursor AI Pro',
      category: 'agent',
      price: 299000,
      originalPrice: 500000,
      icon: 'G',
      iconClass: 'icon-grok',
      badge: 'HOT DEV',
      url: 'grok-bot.html',
      desc: 'Tích hợp Grok Autonomous vào Cursor IDE, Cloud Terminal & Agent lập trình tự động.'
    },
    'grok-supergrok': {
      id: 'grok-supergrok',
      name: 'SuperGrok AI VIP (xAI)',
      category: 'agent',
      price: 490000,
      originalPrice: 750000,
      icon: 'G',
      iconClass: 'icon-grok',
      badge: 'UNLIMITED',
      url: 'grok-bot.html',
      desc: 'Quyền truy cập trực tiếp mô hình Grok 3 / Grok Vision mới nhất không giới hạn.'
    },
    'chatgpt-plus': {
      id: 'chatgpt-plus',
      name: 'ChatGPT Plus (Chính chủ email)',
      category: 'assistant',
      price: 420000,
      originalPrice: 550000,
      icon: '✳',
      iconClass: 'icon-chatgpt',
      badge: 'PHỔ BIẾN',
      url: 'chatgpt.html',
      desc: 'Nâng cấp trực tiếp trên email của bạn. Dùng GPT-4o, GPT-o1, tạo ảnh Canvas, DALL-E 3.'
    },
    'chatgpt-ready': {
      id: 'chatgpt-ready',
      name: 'ChatGPT Plus (Tài khoản cấp sẵn)',
      category: 'assistant',
      price: 290000,
      originalPrice: 500000,
      icon: '✳',
      iconClass: 'icon-chatgpt',
      badge: 'GIÁ RẺ',
      url: 'chatgpt.html',
      desc: 'Tài khoản riêng tư 1 người dùng, kích hoạt tức thì, bảo hành 1 đổi 1 suốt 30 ngày.'
    },
    'claude-pro': {
      id: 'claude-pro',
      name: 'Claude AI Pro (Sonnet 3.7 & Opus)',
      category: 'assistant',
      price: 430000,
      originalPrice: 550000,
      icon: 'C',
      iconClass: 'icon-claude',
      badge: 'VUA CODE',
      url: 'claude-ai.html',
      desc: 'Trùm viết văn tự nhiên và lập trình phức tạp. Hỗ trợ Claude Artifacts, Claude Code.'
    },
    'gemini-advanced': {
      id: 'gemini-advanced',
      name: 'Gemini Advanced 2TB (Google One AI)',
      category: 'assistant',
      price: 180000,
      originalPrice: 490000,
      icon: '✦',
      iconClass: 'icon-gemini',
      badge: 'TIẾT KIỆM 65%',
      url: 'gemini-ai.html',
      desc: 'Mô hình Gemini 2.0 Pro đỉnh cao + 2000GB Google Drive tích hợp Gmail, Docs.'
    }
  };

  const CART_KEY = 'bothub_cart_v2';

  // Helpers
  function formatMoney(amount) {
    if (!amount) return 'Liên hệ';
    return new Intl.NumberFormat('vi-VN').format(amount) + 'đ';
  }

  function getCart() {
    try {
      const data = JSON.parse(localStorage.getItem(CART_KEY) || '[]');
      return Array.isArray(data) ? data : [];
    } catch (_) {
      return [];
    }
  }

  function saveCart(items) {
    localStorage.setItem(CART_KEY, JSON.stringify(items));
    updateCartBadge();
  }

  function updateCartBadge() {
    const cart = getCart();
    const count = cart.reduce((sum, item) => sum + (item.qty || 1), 0);
    document.querySelectorAll('.cart-badge, [data-saved-count]').forEach(el => {
      el.textContent = count;
    });
  }

  function showToast(msg) {
    let t = document.querySelector('.toast-msg');
    if (!t) {
      t = document.createElement('div');
      t.className = 'toast-msg';
      document.body.appendChild(t);
    }
    t.innerHTML = msg;
    t.classList.add('show');
    clearTimeout(window.__toastTimer);
    window.__toastTimer = setTimeout(() => {
      t.classList.remove('show');
    }, 3200);
  }

  // Cart Operations
  function addToCart(productId, qty = 1, showFeedback = true) {
    const item = CATALOG[productId];
    if (!item) return;

    let cart = getCart();
    const existing = cart.find(x => x.id === productId);
    if (existing) {
      existing.qty = (existing.qty || 1) + qty;
    } else {
      cart.push({ id: productId, qty: qty });
    }
    saveCart(cart);

    if (showFeedback) {
      showToast(`✓ Đã thêm <b>${item.name}</b> vào giỏ hàng! <a href="gio-hang.html" style="color:#06b6d4;text-decoration:underline;margin-left:8px;">Xem giỏ ↗</a>`);
    }
  }

  function removeFromCart(productId) {
    let cart = getCart().filter(x => x.id !== productId);
    saveCart(cart);
    renderCartPage();
    showToast('Đã xóa sản phẩm khỏi giỏ hàng.');
  }

  function updateItemQty(productId, delta) {
    let cart = getCart();
    const target = cart.find(x => x.id === productId);
    if (!target) return;
    target.qty = (target.qty || 1) + delta;
    if (target.qty <= 0) {
      cart = cart.filter(x => x.id !== productId);
    }
    saveCart(cart);
    renderCartPage();
  }

  // Fast Checkout Modal (VietQR)
  function openCheckoutModal(productOrCart, isSingle = true) {
    let modal = document.querySelector('#checkout-modal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'checkout-modal';
      modal.className = 'modal-overlay';
      document.body.appendChild(modal);
    }

    let productName = '';
    let totalAmount = 0;
    let orderCode = 'BH' + Math.floor(100000 + Math.random() * 900000);

    if (isSingle) {
      const prod = typeof productOrCart === 'string' ? CATALOG[productOrCart] : productOrCart;
      if (!prod) return;
      productName = prod.name;
      totalAmount = prod.price;
    } else {
      const cart = getCart();
      if (!cart.length) {
        showToast('Giỏ hàng đang trống!');
        return;
      }
      productName = `Đơn hàng (${cart.length} sản phẩm)`;
      totalAmount = cart.reduce((sum, c) => {
        const p = CATALOG[c.id];
        return sum + (p ? p.price * (c.qty || 1) : 0);
      }, 0);
    }

    const qrUrl = `https://img.vietqr.io/image/MB-0388888888-compact2.png?amount=${totalAmount}&addInfo=${orderCode}&accountName=VU%20VAN%20LE`;

    modal.innerHTML = `
      <div class="modal-box">
        <button type="button" class="modal-close" onclick="document.querySelector('#checkout-modal').classList.remove('open')">✕</button>
        <div style="text-align:center;margin-bottom:15px;">
          <span class="badge badge-hot">KÍCH HOẠT TỰ ĐỘNG 5 PHÚT</span>
          <h2 style="font-size:22px;margin:8px 0;color:#fff;">Thanh Toán Đơn Hàng</h2>
          <p style="font-size:13px;color:#94a3b8;">Gói: <strong style="color:#38bdf8">${productName}</strong></p>
        </div>

        <div class="qr-checkout-area">
          <div style="font-size:24px;font-weight:800;color:#10b981;margin-bottom:6px;">${formatMoney(totalAmount)}</div>
          <p style="font-size:12px;color:#cbd5e1;">Quét mã VietQR bằng app Ngân hàng hoặc MoMo để thanh toán tức thì</p>
          <img class="qr-code-img" src="${qrUrl}" alt="Mã VietQR thanh toán Bothub">
        </div>

        <div class="bank-info-box">
          <div class="info-row"><span>Ngân hàng:</span><strong>MB Bank (Quân Đội)</strong></div>
          <div class="info-row"><span>Số tài khoản:</span><strong class="copyable" onclick="navigator.clipboard.writeText('0388888888');alert('Đã chép STK: 0388888888')">0388888888 ⧉</strong></div>
          <div class="info-row"><span>Chủ tài khoản:</span><strong>VU VAN LE</strong></div>
          <div class="info-row"><span>Nội dung chuyển:</span><strong class="copyable" style="color:#f59e0b" onclick="navigator.clipboard.writeText('${orderCode}');alert('Đã chép nội dung: ${orderCode}')">${orderCode} ⧉</strong></div>
        </div>

        <form id="order-confirm-form" onsubmit="event.preventDefault(); window.__confirmOrder('${orderCode}');" style="margin-top:16px;">
          <div style="margin-bottom:12px;">
            <label style="font-size:12px;color:#cbd5e1;display:block;margin-bottom:5px;">Email nhận tài khoản AI <span style="color:#ef4444">*</span></label>
            <input type="email" required placeholder="Nhập email của bạn (vd: email@gmail.com)" style="width:100%;padding:10px 14px;border-radius:8px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.15);color:#fff;font-size:13px;" id="order-email">
          </div>
          <div style="margin-bottom:16px;">
            <label style="font-size:12px;color:#cbd5e1;display:block;margin-bottom:5px;">Số Zalo / Điện thoại hỗ trợ</label>
            <input type="tel" placeholder="Số điện thoại nhận thông báo Zalo" style="width:100%;padding:10px 14px;border-radius:8px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.15);color:#fff;font-size:13px;" id="order-phone">
          </div>
          <button type="submit" class="btn btn-emerald btn-block" style="padding:14px;font-size:15px;">
            ⚡ TÔI ĐÃ CHUYỂN KHOẢN - NHẬN TÀI KHOẢN NGAY
          </button>
        </form>

        <p style="font-size:11px;color:#64748b;text-align:center;margin-top:12px;line-height:1.5;">
          🛡️ Bảo hành 1 đổi 1 suốt thời gian sử dụng. Hỗ trợ kích hoạt trực tiếp qua Zalo 0388888888 (24/7).
        </p>
      </div>
    `;

    modal.classList.add('open');
  }

  window.__confirmOrder = function (code) {
    const email = document.getElementById('order-email')?.value || '';
    const modalBox = document.querySelector('#checkout-modal .modal-box');
    if (modalBox) {
      modalBox.innerHTML = `
        <div style="text-align:center;padding:25px 10px;">
          <div style="width:65px;height:65px;background:#10b981;border-radius:50%;display:grid;place-items:center;color:white;font-size:32px;margin:0 auto 18px;box-shadow:0 0 30px rgba(16,185,129,0.5);">✓</div>
          <h2 style="font-size:24px;color:#fff;margin-bottom:10px;">Đặt Hàng Thành Công!</h2>
          <p style="font-size:14px;color:#cbd5e1;line-height:1.7;margin-bottom:20px;">
            Hệ thống Bothub đã tiếp nhận mã đơn: <strong style="color:#f59e0b">${code}</strong>.<br>
            Thông tin tài khoản & hướng dẫn kích hoạt đang được gửi về email:<br>
            <strong style="color:#06b6d4;font-size:16px;">${email}</strong>
          </p>
          <div style="background:rgba(255,255,255,0.05);padding:14px;border-radius:10px;font-size:12.5px;color:#94a3b8;margin-bottom:24px;text-align:left;">
            ⏱ Thời gian xử lý tự động: <strong>3 - 5 phút</strong>.<br>
            📞 Nếu cần gấp, vui lòng chụp màn hình chuyển khoản gửi qua Zalo: <strong>0388888888</strong> để nhân viên cấp ngay lập tức!
          </div>
          <button class="btn btn-primary" onclick="document.querySelector('#checkout-modal').classList.remove('open');">Hoàn Tất & Tiếp Tục Mua Sắm</button>
        </div>
      `;
      // Clear cart if checkout from cart
      localStorage.removeItem(CART_KEY);
      updateCartBadge();
    }
  };

  // Render Cart Page
  function renderCartPage() {
    const container = document.querySelector('#cart-items-container');
    const totalEl = document.querySelector('#cart-total-price');
    const countEl = document.querySelector('#cart-total-count');
    if (!container) return;

    const cart = getCart();
    if (!cart.length) {
      container.innerHTML = `
        <div style="text-align:center;padding:50px 20px;">
          <div style="font-size:48px;margin-bottom:14px;">🛒</div>
          <h3 style="font-size:20px;color:#fff;margin-bottom:8px;">Giỏ hàng của bạn đang trống</h3>
          <p style="color:#94a3b8;font-size:14px;margin-bottom:22px;">Hãy khám phá các công cụ AI đỉnh cao và chọn cho mình gói phù hợp nhất!</p>
          <a href="ai-agent.html" class="btn btn-primary">Khám Phá AI Agent ↗</a>
        </div>
      `;
      if (totalEl) totalEl.textContent = '0đ';
      if (countEl) countEl.textContent = '0';
      return;
    }

    let grandTotal = 0;
    let totalItems = 0;

    container.innerHTML = cart.map(item => {
      const prod = CATALOG[item.id];
      if (!prod) return '';
      const qty = item.qty || 1;
      const subtotal = prod.price * qty;
      grandTotal += subtotal;
      totalItems += qty;

      return `
        <div class="cart-item-row">
          <div class="cart-item-img ${prod.iconClass}">${prod.icon}</div>
          <div class="cart-item-info">
            <h4>${prod.name}</h4>
            <p>${formatMoney(prod.price)} / gói</p>
          </div>
          <div style="display:flex;align-items:center;gap:8px;">
            <button class="btn btn-sm btn-outline" onclick="window.__updateCartQty('${prod.id}', -1)">-</button>
            <span style="font-weight:700;font-size:14px;min-width:20px;text-align:center;">${qty}</span>
            <button class="btn btn-sm btn-outline" onclick="window.__updateCartQty('${prod.id}', 1)">+</button>
          </div>
          <div class="cart-item-price">${formatMoney(subtotal)}</div>
          <button class="cart-remove-btn" title="Xóa" onclick="window.__removeCartItem('${prod.id}')">✕</button>
        </div>
      `;
    }).join('');

    if (totalEl) totalEl.textContent = formatMoney(grandTotal);
    if (countEl) countEl.textContent = totalItems;
  }

  window.__updateCartQty = (id, delta) => updateItemQty(id, delta);
  window.__removeCartItem = (id) => removeFromCart(id);
  window.__openCheckout = (id) => openCheckoutModal(id);
  window.__openCartCheckout = () => openCheckoutModal(null, false);
  window.__addToCart = (id) => addToCart(id);

  // Initialize UI Features
  function initNavigation() {
    const toggle = document.querySelector('#mobile-toggle');
    const drawer = document.querySelector('#mobile-drawer');
    if (toggle && drawer) {
      toggle.addEventListener('click', () => {
        drawer.classList.toggle('open');
      });
    }

    // Modal background click to close
    document.addEventListener('click', (e) => {
      if (e.target.classList.contains('modal-overlay')) {
        e.target.classList.remove('open');
      }
    });

    // Global buy buttons
    document.querySelectorAll('[data-buy]').forEach(btn => {
      btn.addEventListener('click', () => {
        const id = btn.dataset.buy;
        openCheckoutModal(id);
      });
    });

    // Global add cart buttons
    document.querySelectorAll('[data-add-cart]').forEach(btn => {
      btn.addEventListener('click', () => {
        const id = btn.dataset.addCart;
        addToCart(id);
      });
    });
  }

  // Live Search & Filter in Shop/Agent page
  function initShopFilters() {
    const searchInput = document.querySelector('#shop-search-input');
    const productCards = document.querySelectorAll('.product-card[data-category]');
    const categoryChecks = document.querySelectorAll('input[name="filter-cat"]');
    const countDisplay = document.querySelector('#shop-filtered-count');

    if (!productCards.length) return;

    function filterNow() {
      const q = (searchInput?.value || '').trim().toLowerCase();
      const checkedCats = Array.from(categoryChecks).filter(c => c.checked).map(c => c.value);

      let visibleCount = 0;
      productCards.forEach(card => {
        const title = (card.querySelector('h3')?.textContent || '').toLowerCase();
        const desc = (card.querySelector('.card-desc')?.textContent || '').toLowerCase();
        const cat = card.dataset.category;

        const matchSearch = !q || title.includes(q) || desc.includes(q);
        const matchCat = !checkedCats.length || checkedCats.includes(cat);

        if (matchSearch && matchCat) {
          card.style.display = '';
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });

      if (countDisplay) countDisplay.textContent = visibleCount;
    }

    if (searchInput) searchInput.addEventListener('input', filterNow);
    categoryChecks.forEach(c => c.addEventListener('change', filterNow));

    // Support URL param ?category=agent
    const params = new URLSearchParams(window.location.search);
    const catParam = params.get('category');
    if (catParam) {
      categoryChecks.forEach(c => {
        if (c.value === catParam) c.checked = true;
      });
      filterNow();
    }
  }

  // Copy Prompt 1-Click
  function initPromptCopy() {
    document.querySelectorAll('[data-copy-prompt]').forEach(btn => {
      btn.addEventListener('click', async () => {
        const card = btn.closest('.prompt-card');
        const code = card?.querySelector('.prompt-code')?.textContent.trim() || '';
        try {
          await navigator.clipboard.writeText(code);
          showToast('✓ Đã sao chép prompt vào bộ nhớ tạm!');
        } catch (_) {
          showToast('Vui lòng chọn và sao chép thủ công.');
        }
      });
    });

    // Prompt category filter
    const chips = document.querySelectorAll('.prompt-chip');
    const cards = document.querySelectorAll('.prompt-card[data-cat]');
    chips.forEach(chip => {
      chip.addEventListener('click', () => {
        chips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        const cat = chip.dataset.filter;
        cards.forEach(card => {
          if (cat === 'all' || card.dataset.cat === cat) {
            card.style.display = '';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // Interactive Variant Selectors on Landing Pages (Muse & Grok)
  function initVariantPickers() {
    document.querySelectorAll('.variant-selector-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const group = btn.closest('.variant-selector-group');
        if (!group) return;
        group.querySelectorAll('.variant-selector-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const price = btn.dataset.price;
        const targetPriceEl = document.querySelector(btn.dataset.targetPrice);
        if (targetPriceEl) {
          targetPriceEl.textContent = price;
        }

        const targetBuyBtn = document.querySelector(btn.dataset.targetBuy);
        if (targetBuyBtn && btn.dataset.productId) {
          targetBuyBtn.dataset.buy = btn.dataset.productId;
        }
      });
    });
  }

  // On DOM Ready
  document.addEventListener('DOMContentLoaded', () => {
    updateCartBadge();
    initNavigation();
    initShopFilters();
    initPromptCopy();
    initVariantPickers();
    renderCartPage();
  });

})();
