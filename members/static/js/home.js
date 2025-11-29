// Toggle dropdown menu
document.addEventListener("DOMContentLoaded", () => {
    const profileContainer = document.querySelector(".profile-container");
    const dropdownMenu = document.querySelector(".dropdown-menu");

    if (profileContainer && dropdownMenu) {
        profileContainer.addEventListener("click", () => {
            dropdownMenu.classList.toggle("hidden");
        });
    }

    // Hide dropdown when clicking outside
    document.addEventListener("click", (event) => {
        if (dropdownMenu && !profileContainer.contains(event.target)) {
            dropdownMenu.classList.add("hidden");
        }
    });
});
