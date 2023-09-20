const emailInput = document.getElementById('email-input');
const passwordInput = document.getElementById('password-input');
const submitButton = document.getElementById('submit-form');
const loginError = document.getElementById('login-error')

submitButton.addEventListener('click', function () {
    sendPost();
});

emailInput.addEventListener('input', function () {
    loginError.classList.add('hidden');

    if (emailInput.value.length > 0 &&
        passwordInput.value.length > 0 &&
        validateEmail(emailInput.value)
    ) {
        submitButton.disabled = false;
    }
    else {
        submitButton.disabled = true;
    }
});

passwordInput.addEventListener('input', function () {
    loginError.classList.add('hidden')

    if (emailInput.value.length > 0 &&
        passwordInput.value.length > 0 &&
        validateEmail(emailInput.value)
    ) {
        submitButton.disabled = false;
    }
    else {
        submitButton.disabled = true;
    }
});

emailInput.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        sendPost();
    }
});

passwordInput.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        sendPost();
    }
});

function validateEmail(email) {
    return String(email)
        .toLowerCase()
        .match(
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        );
};

function sendPost() {
    submitButton.disabled = true;
    submitButton.innerText = 'Logging in...'
    var email = emailInput.value;
    var password = passwordInput.value;

    fetch('/login/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'email': email,
            'password': password,
        })
    })
        .then(response => {
            if (response.status === 200) {
                window.location.href = response.url;
            }
            else if (response.status === 401) {
                loginError.classList.remove('hidden')
                submitButton.innerText = 'Log In'
            }
        })
}