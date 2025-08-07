window.addEventListener('DOMContentLoaded', () => {
    fetch('/clubs/ajax_fetch_all_clubs/')
    .then(res => res.text())
    .then(html => {
        document.getElementById('clubs-tbody').innerHTML = html;
    })
    .catch(err => {
        console.error('Failed to load clubs:', err);
    });
});
                    