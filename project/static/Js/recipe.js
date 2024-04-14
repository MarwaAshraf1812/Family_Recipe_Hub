/* recipe_script */

document.addEventListener("DOMContentLoaded", function() {
    // Favorite Button
    const favoriteButton = document.querySelector('.favorite-button');
    favoriteButton.addEventListener('click', function() {
        // Add logic for adding to favorites
        console.log('Added to favorites');
    });

    // Rating Button
    const rateButton = document.querySelector('.rate-button');
    const ratingSelect = document.querySelector('.rating-select');
    rateButton.addEventListener('click', function() {
        const selectedRating = ratingSelect.value;
        // Add logic for rating
        console.log('Rated:', selectedRating);
    });

    // Share Button
    const shareButton = document.querySelector('.share-button');
    const shareInput = document.querySelector('input[type="text"]');
    shareButton.addEventListener('click', function() {
        shareInput.select();
        document.execCommand('copy');
        console.log('Copied to clipboard:', shareInput.value);
        // Add feedback to the user that link is copied
    });
});
