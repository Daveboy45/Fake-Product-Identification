// static/homepage.js
document.addEventListener('DOMContentLoaded', function() {
    // Code to run when the DOM is fully loaded
    // You can add your JavaScript code here
    // For example, you can add event listeners to the buttons

    // Select the buttons
    const adminButton = document.querySelector('.single-group-button:first-child');
    const userButton = document.querySelector('.single-group-button:last-child');

    // Add click event listeners to the buttons
    adminButton.addEventListener('click', function() {
        // Handle admin button click
        console.log('Admin button clicked');
    });

    userButton.addEventListener('click', function() {
        // Handle user button click
        console.log('User button clicked');
    });
});
