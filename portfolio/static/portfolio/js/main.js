/* ================================================
   Portfolio — Main JS
   ================================================ */

document.addEventListener('DOMContentLoaded', () => {

  // ── Navbar scroll effect ──────────────────────
  const nav = document.getElementById('main-nav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.style.borderBottomColor = window.scrollY > 40
        ? 'rgba(42,42,42,0.9)'
        : 'rgba(42,42,42,0.5)';
    }, { passive: true });
  }

  // ── Skill bar animation on scroll ────────────
  const skillBars = document.querySelectorAll('.skill-bar-fill');
  if (skillBars.length) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animated');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });

    skillBars.forEach(bar => observer.observe(bar));
  }

  // ── Entrance animations ───────────────────────
  const animateEls = document.querySelectorAll(
    '.hero-text, .project-card, .timeline-item, .skill-category, .about-info-card'
  );

  const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }, i * 80);
        fadeObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  animateEls.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(24px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    fadeObserver.observe(el);
  });

  // ── Auto-dismiss alerts ───────────────────────
  document.querySelectorAll('.alert').forEach(alert => {
    setTimeout(() => {
      const bsAlert = new bootstrap.Alert(alert);
      bsAlert.close();
    }, 5000);
  });

  // ── Contact form input styling ────────────────
  document.querySelectorAll('.form-group input, .form-group textarea').forEach(input => {
    input.addEventListener('focus', () => {
      input.closest('.form-group').classList.add('focused');
    });
    input.addEventListener('blur', () => {
      input.closest('.form-group').classList.remove('focused');
    });
  });

});
