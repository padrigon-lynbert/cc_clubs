window.addEventListener('DOMContentLoaded', () => {
    fetch('/clubs/ajax_fetch_all_clubs/')
        .then(res => res.text())
        .then(html => {
            const tbody = document.getElementById('clubs-tbody');
            tbody.innerHTML = html;

            // Bind click after loading
            tbody.querySelectorAll('.club-row').forEach(function(row) {
                row.addEventListener('click', function () {
                    const clubId = this.dataset.id;
                    const clubName = this.querySelector('td').textContent.trim();
                    selectClub(clubId, clubName);
                });
            });
        })
        .catch(err => {
            console.error('Failed to load clubs:', err);
        });
});

// This updates the club name in the view
function selectClub(clubId, clubName) {
    console.log("Selected club ID:", clubId);
    document.getElementById('club-name').textContent = clubName;

    // Optional toast (used for testing)
    // const toast = document.createElement('div');
    // toast.textContent = `Selected: ${clubName}`;
    // toast.style.position = 'fixed';
    // toast.style.bottom = '30px';
    // toast.style.left = '50%';
    // toast.style.transform = 'translateX(-50%)';
    // toast.style.background = '#333';
    // toast.style.color = '#fff';
    // toast.style.padding = '10px 20px';
    // toast.style.borderRadius = '8px';
    // toast.style.boxShadow = '0 2px 6px rgba(0,0,0,0.2)';
    // toast.style.zIndex = '9999';
    // toast.style.opacity = '0';
    // toast.style.transition = 'opacity 0.3s ease';

    // document.body.appendChild(toast);

    // Fade in
    requestAnimationFrame(() => {
        toast.style.opacity = '1';
    });

    // Remove after 2.5s
    setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => document.body.removeChild(toast), 300);
    }, 2500);
}