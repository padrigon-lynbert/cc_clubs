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
    console.log("Selected club ID:", clubId);  // for debugging
    document.getElementById('club-name').textContent = clubName;
}
