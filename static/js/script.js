const doc = document.firstElementChild;
const nav = document.getElementById('primary-navigation');
const navToggle = document.getElementById('nav-toggle');
const navButtonText = document.getElementById('nav-button-text');
const accountToggle = document.getElementById('account-toggle');
const accountMenu = document.getElementById('account-menu');
const storageKey = 'theme-preference';
const colorModeToggle = document.getElementById('color-mode');
  
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

// color scheme preference code adapted from 
// https://github.com/argyleink/gui-challenges
const changeTheme = () => {
    // flip current value
    theme.value = theme.value === 'light' ? 'dark' : 'light'
    setPreference()
}
  
const getColorPreference = () => {
    if (localStorage.getItem(storageKey))
        return localStorage.getItem(storageKey)
    else
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
}
  
const setPreference = () => {
    localStorage.setItem(storageKey, theme.value)
    reflectPreference()
}
  
const reflectPreference = () => {
    doc.setAttribute('data-theme', theme.value)
    colorModeToggle ?.setAttribute('aria-label', theme.value)
    if (theme.value === 'light') {
        colorModeToggle.checked = false;
    } else {
        colorModeToggle.checked = true;
    }
}
  
const theme = {
    value: getColorPreference(),
}
  
// set early so no page flashes / CSS is made aware
reflectPreference()
  
window.onload = () => {
    // set on load so screen readers can see latest value on the button
    reflectPreference()
  
    // now this script can find and listen for clicks on the control
    colorModeToggle.addEventListener('click', changeTheme)
}
  
// sync with system changes
window
    .matchMedia('(prefers-color-scheme: dark)')
    .addEventListener('change', ({matches:isDark}) => {
        theme.value = isDark ? 'dark' : 'light'
        setPreference()
})
