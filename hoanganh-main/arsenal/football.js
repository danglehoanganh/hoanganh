// Add any JavaScript logic here if needed in the future.
// Currently, no inline JavaScript was found in the provided HTML.

// Toggle brightness functionality
const toggleButton = document.getElementById('toggle-brightness');
toggleButton.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});

// Add a CSS class for dark mode
const style = document.createElement('style');
style.textContent = `
    .dark-mode {
        background-color: #121212;
        color: #ffffff;
    }
`;
document.head.appendChild(style);