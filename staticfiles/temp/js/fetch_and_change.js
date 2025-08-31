window.addEventListener('DOMContentLoaded', () => {
    const tbody = document.getElementById('clubs-tbody');

    fetch('/clubs/ajax_fetch_all_clubs/')
        .then(res => res.text())
        .then(html => {
            tbody.innerHTML = html;

            // Bind click to each row after loading
            tbody.querySelectorAll('.club-row').forEach(row => {
                row.addEventListener('click', () => {
                    const clubId = row.dataset.id;
                    const clubName = row.querySelector('td').textContent.trim();
                    console.log('Selected:', clubId, clubName);
                    document.getElementById('club-name').textContent = clubName;
                });
            });
        })
        .catch(err => {
            console.error('Failed to load clubs:', err);
        });
});
