// js/script.js - For mobile menu only
document.addEventListener('DOMContentLoaded', function () {
    // Mobile menu toggle
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileDeptToggle = document.getElementById('mobile-dept-toggle');
    const mobileDeptMenu = document.getElementById('mobile-dept-menu');

    if (mobileMenuButton) {
        mobileMenuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }

    if (mobileDeptToggle) {
        mobileDeptToggle.addEventListener('click', () => {
            mobileDeptMenu.classList.toggle('hidden');
        });
    }
});