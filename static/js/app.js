// Function to toggle between light mode and dark mode
function toggleTheme() {
    const body = document.querySelector('body');
    body.classList.toggle('dark-mode');
}

// Call the toggleTheme function when the theme button is clicked
const themeButton = document.getElementById('theme-button');
themeButton.addEventListener('click', toggleTheme);
