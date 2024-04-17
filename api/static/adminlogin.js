// admin_login.js
document.addEventListener('DOMContentLoaded', function() {
    const loginContainer = document.querySelector('.login-container');
    loginContainer.classList.remove('fade-in'); // Remove the fade-in class to reset the animation
    setTimeout(() => {
        loginContainer.classList.add('fade-in'); // Add the fade-in class to trigger the animation
    }, 100); // Delay the addition of the class to ensure the animation plays on page load
});
