// Auto-hide flash messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(function(message, index) {
        setTimeout(function() {
            message.classList.add('fade-out');
            setTimeout(function() {
                message.remove();
            }, 500);
        }, 5000);
    });
}); 