const currentURL = window.location.href;

function redirect_login() {
  const redirect = currentURL.substring(0, currentURL.lastIndexOf('/') + 1) + 'login';
  window.location.href = redirect;
}

function redirect_signup() {
  const redirect = currentURL.substring(0, currentURL.lastIndexOf('/') + 1) + 'signup';
  window.location.href = redirect;
  console.log("what's happening");
}