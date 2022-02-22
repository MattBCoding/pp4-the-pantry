const doc = document.firstElementChild;
const nav = document.getElementById('primary-navigation');
const navToggle = document.getElementById('nav-toggle');
const navButtonText = document.getElementById('nav-button-text');
const accountToggle = document.getElementById('account-toggle');
const accountMenu = document.getElementById('account-menu');
  
// when someone clicks the hamburger menu button
// if the nav is closed, open it
// if the nav is open, close it
accountToggle.addEventListener('click', () => {
    const visibility = accountMenu.getAttribute('data-visible');
    if (visibility === 'false') {
        accountMenu.setAttribute('data-visible', true);
        accountToggle.setAttribute('aria-expanded', true);
    } else {
        accountMenu.setAttribute('data-visible', false);
        accountToggle.setAttribute('aria-expanded', false);
    }
})

navToggle.addEventListener('click', () => {
    const visibility = nav.getAttribute('data-visible');
    if (visibility === 'false') {
        nav.setAttribute('data-visible', true);
        navToggle.setAttribute('aria-expanded', true);
    } else {
        nav.setAttribute('data-visible', false);
        navToggle.setAttribute('aria-expanded', false);
    }
})

