(function () {
  var categories = [
    { id: 'all', label: 'Todos' },
    { id: 'copos', label: 'Copos' },
    { id: 'especiais', label: 'Especiais' },
    { id: 'compartilhar', label: 'Para compartilhar' }
  ];

  var products = [
    {
      id: 'barca-premium',
      category: 'compartilhar',
      badge: 'Para dividir',
      name: 'Barca Premium',
      size: '',
      description: 'A escolha de mesa cheia: açaí cremoso com visual de celebração e espaço para caprichar nos acompanhamentos.',
      detail: 'Pensada para compartilhar, chegar no centro da mesa e virar assunto antes da primeira colherada.',
      price: null,
      priceLabel: 'Preço a definir',
      image: null,
      imagePending: true,
      imageAlt: '',
      tone: 'pink',
      featured: false
    },
    {
      id: 'gigante-770',
      category: 'copos',
      badge: 'Copo gigante',
      name: 'Gigante',
      size: '770 ml',
      description: 'O copo para vontade grande, fome séria e aquela camada extra que ninguém julga.',
      detail: 'Volume generoso para montar do seu jeito e segurar a vontade até o último gole de açaí.',
      price: null,
      priceLabel: 'Preço a definir',
      image: null,
      imagePending: true,
      imageAlt: '',
      tone: 'neon',
      featured: false
    },
    {
      id: 'grande-550',
      category: 'copos',
      badge: 'Favorito',
      name: 'Grande',
      size: '550 ml',
      description: 'Equilíbrio esperto entre quantidade, cremosidade e espaço para os toppings brilharem.',
      detail: 'Um clássico da vitrine Nu Ki: cabe fruta, crocância e aquela colherada funda de açaí.',
      price: null,
      priceLabel: 'Preço a definir',
      image: null,
      imagePending: true,
      imageAlt: '',
      tone: 'banana'
    },
    {
      id: 'medio-330',
      category: 'copos',
      badge: 'Na medida',
      name: 'Médio',
      size: '330 ml',
      description: 'Tamanho ágil para matar a vontade sem transformar o rolê em missão.',
      detail: 'Serve bem quando a ideia é um açaí direto, bonito e fácil de pedir de novo.',
      price: null,
      priceLabel: 'Preço a definir',
      image: null,
      imagePending: true,
      imageAlt: '',
      tone: 'cream'
    },
    {
      id: 'pequeno-200',
      category: 'copos',
      badge: 'Rapidinho',
      name: 'Pequeno',
      size: '200 ml',
      description: 'Pequeno no nome, direto na vontade. Ideal para uma pausa gelada.',
      detail: 'A dose compacta para experimentar, repetir ou encaixar no meio do dia.',
      price: null,
      priceLabel: 'Preço a definir',
      image: null,
      imagePending: true,
      imageAlt: '',
      tone: 'purple'
    },
    {
      id: 'especiais',
      category: 'especiais',
      badge: 'Da casa',
      name: 'Especiais',
      size: '',
      description: 'Combinações mais caprichadas, com cara de vitrine e montagem para sair bonita na foto.',
      detail: 'Uma seleção para quem quer sair do básico e deixar o açaí fazer presença.',
      price: null,
      priceLabel: 'Preço a definir',
      image: 'assets/products/produto-acai-kiwi.png',
      imageAlt: 'Bowl de açaí com kiwi, mirtilo, coco e chia',
      tone: 'kiwi',
      featured: false
    },
    {
      id: 'marmitao-1l',
      category: 'compartilhar',
      badge: '1 litro',
      name: 'Marmitão',
      size: '1 L',
      description: 'A opção de respeito para levar mais açaí, dividir ou guardar a próxima colherada.',
      detail: 'Formato grande para quem quer quantidade, presença e praticidade no mesmo pedido.',
      price: null,
      priceLabel: 'Preço a definir',
      image: null,
      imagePending: true,
      imageAlt: '',
      tone: 'deep'
    }
  ];

  var storageKey = 'nukiacai-menu-cart-v1';
  var state = {
    activeCategory: 'all',
    cart: loadCart(),
    activeDialogProduct: null,
    lastFocusedElement: null
  };

  var refs = {
    filterBar: document.querySelector('[data-filter-bar]'),
    catalog: document.querySelector('[data-catalog]'),
    summary: document.querySelector('.builder-summary'),
    cartList: document.querySelector('[data-cart-list]'),
    cartUnits: document.querySelector('[data-cart-units]'),
    cartSkus: document.querySelectorAll('[data-cart-skus]'),
    heroUnits: document.querySelector('[data-total-units]'),
    heroSummary: document.querySelector('[data-hero-summary]'),
    activeCategoryLabel: document.querySelector('[data-active-category-label]'),
    menuIntroUnits: document.querySelector('[data-menu-intro-units]'),
    summaryItems: document.querySelector('[data-summary-items]'),
    mobileBar: document.querySelector('[data-mobile-order-bar]'),
    mobileUnits: document.querySelector('[data-mobile-cart-units]'),
    mobileStatus: document.querySelector('[data-mobile-cart-status]'),
    clearButton: document.querySelector('[data-clear-cart]'),
    reviewButtons: document.querySelectorAll('[data-review-order], [data-mobile-review]'),
    dialog: document.querySelector('[data-product-dialog]'),
    dialogPanel: document.querySelector('.product-dialog__panel'),
    dialogContent: document.querySelector('[data-product-dialog-content]')
  };

  if (!refs.filterBar || !refs.catalog || !refs.cartList) {
    return;
  }

  refs.filterBar.addEventListener('click', handleFilterClick);
  refs.catalog.addEventListener('click', handleCatalogClick);
  refs.cartList.addEventListener('click', handleQuantityClick);

  if (refs.clearButton) {
    refs.clearButton.addEventListener('click', function () {
      state.cart = {};
      saveCart();
      render();
    });
  }

  refs.reviewButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      document.getElementById('montagem').scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  if (refs.dialog) {
    refs.dialog.addEventListener('click', function (event) {
      if (event.target.closest('[data-close-details]')) {
        closeDetails();
        return;
      }

      handleQuantityClick(event);
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && !refs.dialog.hidden) {
        closeDetails();
      }

      if (event.key === 'Tab' && !refs.dialog.hidden) {
        trapDialogFocus(event);
      }
    });
  }

  render();

  function loadCart() {
    try {
      var raw = window.localStorage.getItem(storageKey);
      return raw ? normalizeCart(JSON.parse(raw)) : {};
    } catch (error) {
      return {};
    }
  }

  function normalizeCart(source) {
    var cart = {};

    if (!source || typeof source !== 'object') {
      return cart;
    }

    products.forEach(function (product) {
      var value = Number(source[product.id]);
      if (Number.isFinite(value) && value > 0) {
        cart[product.id] = Math.floor(value);
      }
    });

    return cart;
  }

  function saveCart() {
    try {
      window.localStorage.setItem(storageKey, JSON.stringify(state.cart));
    } catch (error) {
      // Storage can fail in private contexts; the menu should still work.
    }
  }

  function escapeHtml(value) {
    return String(value || '').replace(/[&<>"']/g, function (character) {
      return {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      }[character];
    });
  }

  function getProduct(productId) {
    return products.find(function (product) {
      return product.id === productId;
    });
  }

  function getCategoryLabel(categoryId) {
    var category = categories.find(function (item) {
      return item.id === categoryId;
    });

    return category ? category.label : 'Todos';
  }

  function getVisibleProducts() {
    if (state.activeCategory === 'all') {
      return products;
    }

    return products.filter(function (product) {
      return product.category === state.activeCategory;
    });
  }

  function getEntries() {
    return products
      .map(function (product) {
        return {
          product: product,
          quantity: state.cart[product.id] || 0
        };
      })
      .filter(function (entry) {
        return entry.quantity > 0;
      });
  }

  function getTotals() {
    var entries = getEntries();
    var units = entries.reduce(function (sum, entry) {
      return sum + entry.quantity;
    }, 0);
    var hasAllPrices = entries.length > 0 && entries.every(function (entry) {
      return typeof entry.product.price === 'number';
    });
    var total = hasAllPrices
      ? entries.reduce(function (sum, entry) {
          return sum + entry.product.price * entry.quantity;
        }, 0)
      : null;

    return {
      entries: entries,
      units: units,
      skus: entries.length,
      total: total,
      totalLabel: total === null ? 'Preço a definir' : formatCurrency(total)
    };
  }

  function formatCurrency(value) {
    return value.toLocaleString('pt-BR', {
      style: 'currency',
      currency: 'BRL'
    });
  }

  function handleFilterClick(event) {
    var button = event.target.closest('[data-category]');
    if (!button) {
      return;
    }

    var categoryId = button.getAttribute('data-category');
    if (state.activeCategory === categoryId) {
      return;
    }

    state.activeCategory = categoryId;
    render();
  }

  function handleCatalogClick(event) {
    var detailButton = event.target.closest('[data-open-details]');
    if (detailButton) {
      openDetails(detailButton.getAttribute('data-open-details'), detailButton);
      return;
    }

    handleQuantityClick(event);
  }

  function handleQuantityClick(event) {
    var button = event.target.closest('button[data-action]');
    if (!button) {
      return;
    }

    var holder = button.closest('[data-product-id], [data-summary-product-id], [data-dialog-product-id]');
    if (!holder) {
      return;
    }

    var productId = holder.dataset.productId || holder.dataset.summaryProductId || holder.dataset.dialogProductId;
    var delta = button.getAttribute('data-action') === 'increase' ? 1 : -1;
    updateQuantity(productId, delta);
  }

  function updateQuantity(productId, delta) {
    var product = getProduct(productId);
    if (!product) {
      return;
    }

    var current = state.cart[productId] || 0;
    var next = current + delta;

    if (next <= 0) {
      delete state.cart[productId];
    } else {
      state.cart[productId] = next;
    }

    saveCart();
    render();
    pulseProduct(productId);

    if (state.activeDialogProduct === productId) {
      renderDialog(product);
    }
  }

  function pulseProduct(productId) {
    var card = refs.catalog.querySelector('[data-product-id="' + productId + '"]');
    if (!card) {
      return;
    }

    card.classList.remove('is-pulsing');
    window.requestAnimationFrame(function () {
      card.classList.add('is-pulsing');
    });
  }

  function renderFilters() {
    refs.filterBar.innerHTML = categories
      .map(function (category) {
        var active = category.id === state.activeCategory;
        return (
          '<button class="filter-chip" type="button" data-category="' +
          category.id +
          '" aria-pressed="' +
          String(active) +
          '">' +
          escapeHtml(category.label) +
          '</button>'
        );
      })
      .join('');
  }

  function renderProductMedia(product, context) {
    if (product.image) {
      return (
        '<div class="product-media product-media--' +
        escapeHtml(product.tone) +
        '">' +
        '<img src="' +
        escapeHtml(product.image) +
        '" alt="' +
        escapeHtml(product.imageAlt) +
        '" width="640" height="480" loading="lazy" decoding="async">' +
        '</div>'
      );
    }

    var placeholderTitle = product.size || product.name;

    return (
      '<div class="product-media product-media--placeholder product-media--' +
      escapeHtml(product.tone) +
      '" role="img" aria-label="Imagem final pendente para ' +
      escapeHtml(product.name) +
      '">' +
      '<span class="placeholder-glow" aria-hidden="true"></span>' +
      '<span class="placeholder-title">' +
      escapeHtml(placeholderTitle) +
      '</span>' +
      '<span class="placeholder-note">' +
      (context === 'dialog' ? 'Imagem final em preparação' : 'Imagem em preparação') +
      '</span>' +
      '</div>'
    );
  }

  function renderQuantityControls(product, quantity, compact) {
    if (!quantity) {
      return (
        '<button class="add-button" type="button" data-action="increase" aria-label="Adicionar ' +
        escapeHtml(product.name) +
        ' ao pedido">Adicionar</button>'
      );
    }

    return (
      '<div class="quantity-picker' +
      (compact ? ' quantity-picker--compact' : '') +
      '" aria-label="Quantidade de ' +
      escapeHtml(product.name) +
      '">' +
      '<button type="button" data-action="decrease" aria-label="Diminuir ' +
      escapeHtml(product.name) +
      '">−</button>' +
      '<output aria-live="polite">' +
      quantity +
      '</output>' +
      '<button type="button" data-action="increase" aria-label="Adicionar ' +
      escapeHtml(product.name) +
      '">+</button>' +
      '</div>'
    );
  }

  function renderCatalog() {
    refs.catalog.innerHTML = getVisibleProducts()
      .map(function (product, index) {
        var quantity = state.cart[product.id] || 0;
        var title = product.size ? product.name + ' ' + product.size : product.name;

        return (
          '<article class="product-card product-card--' +
          escapeHtml(product.tone) +
          (quantity > 0 ? ' is-selected' : '') +
          '" data-product-id="' +
          product.id +
          '" style="--card-index:' +
          index +
          '">' +
          renderProductMedia(product, 'card') +
          '<div class="product-body">' +
          '<div class="product-head">' +
          '<span class="product-badge">' +
          escapeHtml(product.badge) +
          '</span>' +
          '<span class="product-category">' +
          escapeHtml(getCategoryLabel(product.category)) +
          '</span>' +
          '</div>' +
          '<h3>' +
          escapeHtml(title) +
          '</h3>' +
          '<p>' +
          escapeHtml(product.description) +
          '</p>' +
          '<div class="product-meta">' +
          '<span>' +
          escapeHtml(product.size || 'Especial Nu Ki') +
          '</span>' +
          '</div>' +
          '<div class="product-actions">' +
          renderQuantityControls(product, quantity, false) +
          '<button class="details-button" type="button" data-open-details="' +
          product.id +
          '" aria-label="Ver detalhes de ' +
          escapeHtml(title) +
          '">Detalhes</button>' +
          '</div>' +
          '</div>' +
          '</article>'
        );
      })
      .join('');
  }

  function renderCart() {
    var totals = getTotals();

    if (!totals.entries.length) {
      refs.cartList.innerHTML =
        '<div class="summary-empty"><strong>Seu pedido está vazio</strong><p>Escolha um produto para começar a montar.</p></div>';
    } else {
      refs.cartList.innerHTML = totals.entries
        .map(function (entry) {
          var title = entry.product.size ? entry.product.name + ' ' + entry.product.size : entry.product.name;
          return (
            '<article class="summary-item" data-summary-product-id="' +
            entry.product.id +
            '">' +
            '<div>' +
            '<strong>' +
            escapeHtml(title) +
            '</strong>' +
            '<p>' +
            entry.quantity +
            ' item' +
            (entry.quantity > 1 ? 's' : '') +
            '</p>' +
            '</div>' +
            renderQuantityControls(entry.product, entry.quantity, true) +
            '</article>'
          );
        })
        .join('');
    }

    syncCounters(totals);
  }

  function syncCounters(totals) {
    if (refs.cartUnits) {
      refs.cartUnits.textContent = String(totals.units);
    }

    refs.cartSkus.forEach(function (item) {
      item.textContent = String(totals.skus);
    });

    if (refs.heroUnits) {
      refs.heroUnits.textContent = String(totals.units);
    }

    if (refs.heroSummary) {
      refs.heroSummary.textContent = totals.units
        ? totals.skus + ' escolhas e ' + totals.units + ' itens preparados para revisar.'
        : 'Adicione produtos para ver a composição do pedido aqui.';
    }

    if (refs.activeCategoryLabel) {
      refs.activeCategoryLabel.textContent = getCategoryLabel(state.activeCategory);
    }

    if (refs.menuIntroUnits) {
      refs.menuIntroUnits.textContent = String(totals.units);
    }

    if (refs.summaryItems) {
      refs.summaryItems.textContent = String(totals.units);
    }

    if (refs.mobileUnits) {
      refs.mobileUnits.textContent = String(totals.units);
    }

    if (refs.mobileStatus) {
      refs.mobileStatus.textContent = totals.units ? 'Revisar pedido' : 'Pedido vazio';
    }

    if (refs.mobileBar) {
      refs.mobileBar.hidden = totals.units === 0;
    }

    if (refs.summary) {
      refs.summary.classList.toggle('is-empty', totals.units === 0);
    }

    if (refs.clearButton) {
      refs.clearButton.disabled = totals.units === 0;
    }

    refs.reviewButtons.forEach(function (button) {
      button.disabled = totals.units === 0;
    });
  }

  function openDetails(productId, trigger) {
    var product = getProduct(productId);
    if (!product || !refs.dialog || !refs.dialogPanel || !refs.dialogContent) {
      return;
    }

    state.activeDialogProduct = productId;
    state.lastFocusedElement = trigger || document.activeElement;
    renderDialog(product);
    refs.dialog.hidden = false;
    document.body.classList.add('has-dialog-open');
    refs.dialogPanel.focus();
  }

  function closeDetails() {
    if (!refs.dialog) {
      return;
    }

    refs.dialog.hidden = true;
    document.body.classList.remove('has-dialog-open');
    state.activeDialogProduct = null;

    if (state.lastFocusedElement && typeof state.lastFocusedElement.focus === 'function') {
      state.lastFocusedElement.focus();
    }
  }

  function renderDialog(product) {
    var quantity = state.cart[product.id] || 0;
    var title = product.size ? product.name + ' ' + product.size : product.name;

    refs.dialogContent.innerHTML =
      '<div class="product-dialog__media">' +
      renderProductMedia(product, 'dialog') +
      '</div>' +
      '<div class="product-dialog__copy" data-dialog-product-id="' +
      product.id +
      '">' +
      '<p class="eyebrow">' +
      escapeHtml(product.badge) +
      '</p>' +
      '<h2 id="product-dialog-title">' +
      escapeHtml(title) +
      '</h2>' +
      '<p>' +
      escapeHtml(product.detail) +
      '</p>' +
      '<div class="product-meta">' +
      '<span>' +
      escapeHtml(product.size || 'Especial Nu Ki') +
      '</span>' +
      '</div>' +
      '<div class="product-dialog__actions">' +
      renderQuantityControls(product, quantity, false) +
      '</div>' +
      '</div>';
  }

  function trapDialogFocus(event) {
    var focusable = refs.dialog.querySelectorAll(
      'button:not([disabled]), [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );

    if (!focusable.length) {
      return;
    }

    var first = focusable[0];
    var last = focusable[focusable.length - 1];

    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }

  function render() {
    renderFilters();
    renderCatalog();
    renderCart();
  }
})();
