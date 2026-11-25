document.addEventListener('DOMContentLoaded', () => {
  // Auto-hide flash messages after a few seconds.
  document.querySelectorAll('.flash-message').forEach((message) => {
    window.setTimeout(() => {
      message.classList.add('fade-out');
      window.setTimeout(() => message.remove(), 400);
    }, 4500);
  });

  // Client-side enhancement for ticket quantity.
  const quantity = document.querySelector('#jumlah');
  const ticketSelect = document.querySelector('#jenis_tiket');
  const summary = document.querySelector('#ticket-summary');

  const updateSummary = () => {
    if (!quantity || !ticketSelect || !summary) return;
    const selected = ticketSelect.options[ticketSelect.selectedIndex];
    const qty = Number.parseInt(quantity.value || '0', 10);
    summary.textContent = selected && qty > 0
      ? `${selected.text} × ${qty} tiket`
      : 'Pilih tiket dan jumlahnya.';
  };

  ticketSelect?.addEventListener('change', updateSummary);
  quantity?.addEventListener('input', updateSummary);
  updateSummary();

  // Prevent accidental double submission while preserving normal Flask-WTF POST.
  document.querySelectorAll('form[data-disable-submit]').forEach((form) => {
    form.addEventListener('submit', () => {
      const button = form.querySelector('button[type="submit"], input[type="submit"]');
      if (button) {
        button.disabled = true;
        button.dataset.originalText = button.value || button.textContent;
        if ('value' in button) button.value = 'Memproses...';
        else button.textContent = 'Memproses...';
      }
    });
  });
});
