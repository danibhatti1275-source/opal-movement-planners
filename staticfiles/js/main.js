// static/js/main.js

// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    // Dropdown hover effect for mobile
    const dropbtns = document.querySelectorAll('.dropbtn');
    
    dropbtns.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const dropdown = this.closest('.dropdown');
            if (!dropdown) return;
            const content = dropdown.querySelector('.dropdown-content');
            document.querySelectorAll('.dropdown-content').forEach(menu => {
                if (menu !== content) {
                    menu.classList.remove('show');
                }
            });
            content.classList.toggle('show');
        });
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        if (anchor.classList.contains('dropbtn')) return;
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Navbar background on scroll
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(44, 24, 16, 0.95)';
        } else {
            navbar.style.background = 'var(--primary)';
        }
    });

    // Service card animation on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    document.querySelectorAll('.service-card, .vendor-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease';
        observer.observe(card);
    });
});

// Close dropdown when clicking outside
window.addEventListener('click', function(e) {
    if (!e.target.closest('.dropdown')) {
        const dropdowns = document.querySelectorAll('.dropdown-content');
        dropdowns.forEach(dropdown => {
            dropdown.classList.remove('show');
        });
    }
});