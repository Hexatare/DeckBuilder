// Get all the image containers
const imageContainers = document.querySelectorAll('.image-text-wrapper');

// Add event listeners to each image container
imageContainers.forEach((container) => {
    const image = container.querySelector('img');
    const textbox = container.querySelector('.textbox');

    // Show the textbox on mouseover
    container.addEventListener('mouseover', () => {
        textbox.style.display = 'flex';
    });

    // Hide the textbox on mouseout
    container.addEventListener('mouseout', () => {
        textbox.style.display = 'none';
    });
});