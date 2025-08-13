document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    // Initialize EmailJS
    emailjs.init("hjbFuooL8G36rR4N9");

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

    // Form validation + EmailJS integration
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault(); // Prevent normal form submit

            if (!contactForm.checkValidity()) {
                e.stopPropagation();
                contactForm.classList.add('was-validated');
                return;
            }

            contactForm.classList.add('was-validated');

            // EmailJS send
            emailjs.sendForm("service_0bg4umd", "template_fqzrvv8", this)
                .then(function() {
                    const msgBox = document.getElementById('formMessage');
                    msgBox.style.display = 'block';
                    msgBox.className = 'alert alert-success mt-3'; // Bootstrap green alert
                    msgBox.textContent = window.translations.successMessage;
                    
                    contactForm.reset();
                    contactForm.classList.remove('was-validated');
                }, function(error) {
                    const msgBox = document.getElementById('formMessage');
                    msgBox.style.display = 'block';
                    msgBox.className = 'alert alert-danger mt-3'; // Bootstrap red alert
                    msgBox.textContent = window.translations.errorMessage;
                });
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
            
            if (
                (elementBottomPosition >= windowTopPosition) &&
                (elementTopPosition <= windowBottomPosition)
            ) {
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
    
    checkIfInView();
    window.addEventListener('scroll', checkIfInView);
});