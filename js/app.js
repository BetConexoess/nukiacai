(function () {
  var categories = [
    { id: 'all', label: 'Tudo' },
    { id: 'bases', label: 'Bases' },
    { id: 'frutas', label: 'Frutas' },
    { id: 'extras', label: 'Extras' },
    { id: 'combos', label: 'Combos' }
  ];

  var products = [
    {
      id: 'base-classica',
      category: 'bases',
      badge: 'Base',
      name: 'Açaí clássico',
      description: 'Textura cremosa e sabor equilibrado para uma montagem versátil.',
      note: 'Montagem livre',
      priceLabel: 'Preço a definir'
    },
    {
      id: 'base-zero',
      category: 'bases',
      badge: 'Base',
      name: 'Açaí zero',
      description: 'Opção mais leve para quem quer montar sem exagero.',
      note: 'Versão leve',
      priceLabel: 'Preço a definir'
    },
    {
      id: 'banana',
      category: 'frutas',
      badge: 'Fruta',
      name: 'Banana fresca',
      description: 'Rodelas para trazer doçura natural e textura ao copo.',
      note: 'Fruta clássica',
      priceLabel: 'Preço a definir'
    },
    {
      id: 'morango',
      category: 'frutas',
      badge: 'Fruta',
      name: 'Morango',
      description: 'Acidez equilibrada e visual que destaca a montagem.',
      note: 'Fruta destaque',
      priceLabel: 'Preço a definir'
    },
    {
      id: 'granola',
      category: 'extras',
      badge: 'Extra',
      name: 'Granola crocante',
      description: 'Camada de crocância para finalizar o açaí com contraste.',
      note: 'Top de crocância',
      priceLabel: 'Preço a definir'
    },
    {
      id: 'pacoca',
      category: 'extras',
      badge: 'Extra',
      name: 'Paçoca',
      description: 'Toque doce e nostálgico que combina com quase tudo.',
      note: 'Favorita da casa',
      priceLabel: 'Preço a definir'
    },
    {
      id: 'combo-casa',
      category: 'combos',
      badge: 'Combo',
      name: 'Combo da casa',
      description: 'Sugestão pronta com composição equilibrada.',
      note: 'Pedido rápido',
      priceLabel: 'Preço a definir'
    },
    {
      id: 'combo-familia',
      category: 'combos',
      badge: 'Combo',
      name: 'Combo família',
      description: 'Opção pensada para dividir e variar sabores.',
      note: 'Mais unidades',
      priceLabel: 'Preço a definir'
    }
  ];

  var storageKey = 'nukiacai-cart-v1';
  var state = {
    activeCategory: 'all',
    cart: loadCart()
  };

  var refs = {
    filterBar: document.querySelector('[data-filter-bar]'),
    catalog: document.querySelector('[data-catalog]'),
    cartList: document.querySelector('[data-cart-list]'),
    cartUnits: document.querySelector('[data-cart-units]'),
    cartSkus: document.querySelector('[data-cart-skus]'),
    heroUnits: document.querySelector('[data-total-units]'),
    heroSummary: document.querySelector('[data-hero-summary]'),
    activeCategoryLabel: document.querySelector('[data-active-category-label]'),
    summaryCategory: document.querySelector('[data-summary-category]'),
    whatsappButton: document.querySelector('[data-whatsapp-button]'),
    clearButton: document.querySelector('[data-clear-cart]')
  };

  if (!refs.filterBar || !refs.catalog || !refs.cartList) {
    return;
  }

  refs.catalog.addEventListener('click', handleAdjustmentClick);
  refs.cartList.addEventListener('click', handleAdjustmentClick);

  if (refs.filterBar) {
    refs.filterBar.addEventListener('click', function (event) {
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
    });
  }

  if (refs.clearButton) {
    refs.clearButton.addEventListener('click', function () {
      state.cart = {};
      saveCart();
      render();
    });
  }

  if (refs.whatsappButton) {
    refs.whatsappButton.addEventListener('click', function (event) {
      if (refs.whatsappButton.getAttribute('aria-disabled') === 'true') {
        event.preventDefault();
      }
    });
  }

  render();

  function loadCart() {
    try {
      var raw = window.localStorage.getItem(storageKey);
      if (!raw) {
        return {};
      }

      return normalizeCart(JSON.parse(raw));
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
      // Ignore storage failures and keep the interaction alive.
    }
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, function (character) {
      var map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      };

      return map[character];
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

    return {
      entries: entries,
      units: units,
      skus: entries.length
    };
  }

  function handleAdjustmentClick(event) {
    var button = event.target.closest('button[data-action]');
    if (!button) {
      return;
    }

    var card = button.closest('[data-product-id], [data-summary-product-id]');
    if (!card) {
      return;
    }

    var productId = card.dataset.productId || card.dataset.summaryProductId;
    if (!productId) {
      return;
    }

    var delta = button.getAttribute('data-action') === 'increase' ? 1 : -1;
    updateQuantity(productId, delta);
  }

  function updateQuantity(productId, delta) {
    var current = state.cart[productId] || 0;
    var next = current + delta;

    if (next <= 0) {
      delete state.cart[productId];
    } else {
      state.cart[productId] = next;
    }

    saveCart();
    render();
  }

  function buildWhatsappMessage(entries, units) {
    var lines = entries.map(function (entry) {
      return '- ' + entry.quantity + 'x ' + entry.product.name;
    });

    if (!lines.length) {
      return [
        'Olá! Quero montar meu pedido no Nu Ki Açaí.',
        '',
        'Poderia me enviar o cardápio atualizado?'
      ].join('\n');
    }

    return [
      'Olá! Quero fazer meu pedido no Nu Ki Açaí.',
      '',
      'Itens selecionados:',
      lines.join('\n'),
      '',
      'Total de unidades: ' + units,
      '',
      'Pode me confirmar o pedido?'
    ].join('\n');
  }

  function syncWhatsappButton(entries, units) {
    if (!refs.whatsappButton) {
      return;
    }

    var phoneNumber = (document.body.dataset.whatsappNumber || '').replace(/\D/g, '');
    var message = buildWhatsappMessage(entries, units);

    refs.whatsappButton.dataset.message = message;

    if (!phoneNumber) {
      refs.whatsappButton.href = '#contato';
      refs.whatsappButton.setAttribute('aria-disabled', 'true');
      refs.whatsappButton.tabIndex = -1;
      refs.whatsappButton.textContent = 'WhatsApp pendente';
      refs.whatsappButton.title = 'Defina o número do WhatsApp para ativar o envio';
      return;
    }

    refs.whatsappButton.removeAttribute('aria-disabled');
    refs.whatsappButton.tabIndex = 0;
    refs.whatsappButton.href = 'https://wa.me/' + phoneNumber + '?text=' + encodeURIComponent(message);
    refs.whatsappButton.target = '_blank';
    refs.whatsappButton.rel = 'noopener';
    refs.whatsappButton.textContent = units ? 'Enviar pedido (' + units + ')' : 'Enviar no WhatsApp';
    refs.whatsappButton.title = 'Abrir pedido no WhatsApp';
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

  function renderCatalog() {
    var visibleProducts = getVisibleProducts();

    refs.catalog.innerHTML = visibleProducts
      .map(function (product) {
        var quantity = state.cart[product.id] || 0;
        return (
          '<article class="product-card' +
          (quantity > 0 ? ' is-selected' : '') +
          '" data-product-id="' +
          product.id +
          '">' +
          '<div class="product-head">' +
          '<span class="product-badge">' +
          escapeHtml(product.badge) +
          '</span>' +
          '<span class="product-category">' +
          escapeHtml(getCategoryLabel(product.category)) +
          '</span>' +
          '</div>' +
          '<h3>' +
          escapeHtml(product.name) +
          '</h3>' +
          '<p>' +
          escapeHtml(product.description) +
          '</p>' +
          '<div class="product-meta">' +
          '<span>' +
          escapeHtml(product.note) +
          '</span>' +
          '<strong>' +
          escapeHtml(product.priceLabel) +
          '</strong>' +
          '</div>' +
          '<div class="quantity-picker" aria-label="Quantidade de ' +
          escapeHtml(product.name) +
          '">' +
          '<button type="button" data-action="decrease" aria-label="Diminuir ' +
          escapeHtml(product.name) +
          '">−</button>' +
          '<output>' +
          quantity +
          '</output>' +
          '<button type="button" data-action="increase" aria-label="Adicionar ' +
          escapeHtml(product.name) +
          '">+</button>' +
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
        '<div class="summary-empty"><strong>Nenhum item ainda.</strong><p>Toque em + em qualquer card para começar a montar.</p></div>';
    } else {
      refs.cartList.innerHTML = totals.entries
        .map(function (entry) {
          return (
            '<article class="summary-item" data-summary-product-id="' +
            entry.product.id +
            '">' +
            '<div>' +
            '<strong>' +
            escapeHtml(entry.product.name) +
            '</strong>' +
            '<p>' +
            entry.quantity +
            ' unidade' +
            (entry.quantity > 1 ? 's' : '') +
            ' · ' +
            escapeHtml(entry.product.note) +
            '</p>' +
            '</div>' +
            '<div class="summary-item-actions">' +
            '<button type="button" data-action="decrease" aria-label="Diminuir ' +
            escapeHtml(entry.product.name) +
            '">−</button>' +
            '<span>' +
            entry.quantity +
            '</span>' +
            '<button type="button" data-action="increase" aria-label="Adicionar ' +
            escapeHtml(entry.product.name) +
            '">+</button>' +
            '</div>' +
            '</article>'
          );
        })
        .join('');
    }

    if (refs.cartUnits) {
      refs.cartUnits.textContent = String(totals.units);
    }

    if (refs.cartSkus) {
      refs.cartSkus.textContent = String(totals.skus);
    }

    if (refs.heroUnits) {
      refs.heroUnits.textContent = String(totals.units);
    }

    if (refs.heroSummary) {
      refs.heroSummary.textContent = totals.units
        ? totals.skus + ' tipos e ' + totals.units + ' unidades prontos para o envio.'
        : 'Adicione produtos para ver a composição do pedido aqui.';
    }

    if (refs.activeCategoryLabel) {
      refs.activeCategoryLabel.textContent = getCategoryLabel(state.activeCategory);
    }

    if (refs.summaryCategory) {
      refs.summaryCategory.textContent = getCategoryLabel(state.activeCategory);
    }

    syncWhatsappButton(totals.entries, totals.units);
  }

  function render() {
    renderFilters();
    renderCatalog();
    renderCart();
  }
})();
