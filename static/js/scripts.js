// JavaScript to show hover toast
function showHoverToast() {
    const toastContainer = document.getElementById('toast-container');

    // Create a new toast element
    const toast = document.createElement('div');
    toast.classList.add('toast', 'toast-info');
    toast.innerText = 'Click to add a new task';

    // Append the toast to the container
    toastContainer.appendChild(toast);

    // Remove the toast after 3 seconds
    setTimeout(() => {
        toast.remove();
    }, 3000); // 3 seconds
}
