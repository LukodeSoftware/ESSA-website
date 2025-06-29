/**
 * ESSA - Emi's Swim School Academy
 * Main JavaScript File
 */

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    // Navbar shrink on scroll
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-shrink');
        } else {
            navbar.classList.remove('navbar-shrink');
        }
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            if (this.getAttribute('href') !== '#') {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                
                if (target) {
                    window.scrollTo({
                        top: target.offsetTop - 70,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Initialize toasts
    var toastElList = [].slice.call(document.querySelectorAll('.toast'));
    var toastList = toastElList.map(function(toastEl) {
        return new bootstrap.Toast(toastEl);
    });

    // Show toasts if they exist
    toastList.forEach(toast => toast.show());

    // Gallery Lightbox
    const galleryItems = document.querySelectorAll('.gallery-item img');
    const lightbox = document.querySelector('.lightbox');
    const lightboxImg = document.querySelector('.lightbox-img');
    const lightboxClose = document.querySelector('.lightbox-close');

    if (galleryItems.length > 0 && lightbox && lightboxImg && lightboxClose) {
        galleryItems.forEach(item => {
            item.addEventListener('click', function() {
                lightboxImg.src = this.src;
                lightbox.style.display = 'block';
                document.body.style.overflow = 'hidden';
            });
        });

        lightboxClose.addEventListener('click', function() {
            lightbox.style.display = 'none';
            document.body.style.overflow = 'auto';
        });

        lightbox.addEventListener('click', function(e) {
            if (e.target === lightbox) {
                lightbox.style.display = 'none';
                document.body.style.overflow = 'auto';
            }
        });
    }

    // Form validation
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            if (!contactForm.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            
            contactForm.classList.add('was-validated');
        });
    }

    // Animation on scroll
    const animatedElements = document.querySelectorAll('.animate__animated');
    
    function checkIfInView() {
        const windowHeight = window.innerHeight;
        const windowTopPosition = window.scrollY;
        const windowBottomPosition = windowTopPosition + windowHeight;
        
        animatedElements.forEach(function(element) {
            const elementHeight = element.offsetHeight;
            const elementTopPosition = element.offsetTop;
            const elementBottomPosition = elementTopPosition + elementHeight;
            
            // Check if element is in view
            if (
                (elementBottomPosition >= windowTopPosition) &&
                (elementTopPosition <= windowBottomPosition)
            ) {
                // Add the class that triggers the animation
                if (element.classList.contains('animate__fadeIn')) {
                    element.classList.add('animate__fadeIn');
                } else if (element.classList.contains('animate__fadeInUp')) {
                    element.classList.add('animate__fadeInUp');
                } else if (element.classList.contains('animate__fadeInDown')) {
                    element.classList.add('animate__fadeInDown');
                } else if (element.classList.contains('animate__fadeInLeft')) {
                    element.classList.add('animate__fadeInLeft');
                } else if (element.classList.contains('animate__fadeInRight')) {
                    element.classList.add('animate__fadeInRight');
                }
            }
        });
    }
    
    // Check if elements are in view on page load and scroll
    checkIfInView();
    window.addEventListener('scroll', checkIfInView);
});
