// Select DOM Elements
const carousel = document.querySelector('.carousel');
const nextButton = document.querySelector('.next-btn');
const prevButton = document.querySelector('.prev-btn');

// Number of pixels to scroll per click
const scrollAmount = 220;

// Scroll Forward
nextButton.addEventListener('click', () => {
  carousel.scrollBy({
    left: scrollAmount,
    behavior: 'smooth',
  });
});

// Scroll Backward
prevButton.addEventListener('click', () => {
  carousel.scrollBy({
    left: -scrollAmount,
    behavior: 'smooth',
  });
});
