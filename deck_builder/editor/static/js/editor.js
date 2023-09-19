const uploadTextInput = document.getElementById('upload-text-input');

uploadTextInput.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = this.scrollHeight + 'px';
});

const selectImage = document.getElementById('select-image-upload');
const selectText = document.getElementById('select-text-input');
const uploadImageWrapper = document.getElementById('upload-image-wrapper');
const uploadTextWrapper = document.getElementById('upload-text-wrapper');

selectImage.addEventListener('click', function () {
    selectText.classList.remove('selected');
    selectImage.classList.add('selected');

    uploadTextWrapper.classList.add('hidden');
    uploadImageWrapper.classList.remove('hidden');
});

selectText.addEventListener('click', function () {
    selectText.classList.add('selected');
    selectImage.classList.remove('selected');

    uploadTextWrapper.classList.remove('hidden');
    uploadImageWrapper.classList.add('hidden');
});

const imageInput = document.getElementById('image-input');
const imageInputLabel = document.getElementById('image-input-label');

imageInputLabel.addEventListener('change', function () {
    sendImage();
});

function sendImage() {
    const uploadedFile = imageInput.files[0];

    if (uploadedFile) {
        const formData = new FormData();
        formData.append('image', uploadedFile);

        fetch('/upload/image', {
            method: 'POST',
            body: formData,
        })
            .then(response => response.json())
            .then(data => {
                window.location.href = `/edit/${data['id']}`
            });
    }
}

imageInputLabel.addEventListener('dragenter', function (event) {
    event.preventDefault();
    imageInputLabel.classList.add('active');
});

imageInputLabel.addEventListener('dragover', function (event) {
    event.preventDefault();
});

imageInputLabel.addEventListener('dragleave', function (event) {
    event.preventDefault();
    imageInputLabel.classList.remove('active');
});

imageInputLabel.addEventListener('drop', function (event) {
    event.preventDefault();
    imageInputLabel.classList.remove('active');
    sendImage();
});


const textInput = document.getElementById('upload-text-input');
const submitTextButton = document.getElementById('submit-text');
const buttonText = document.getElementById('submit-button-text');
const loadingIcon = document.getElementById('loading-icon');

textInput.addEventListener('input', function () {
    if (textInput.value.length > 0) {
        submitTextButton.disabled = false;
    } else {
        submitTextButton.disabled = true;
    }
});

submitTextButton.addEventListener('click', function () {
    submitTextButton.disabled = true;
    buttonText.classList.add('hidden');
    loadingIcon.classList.remove('hidden');
    const enteredText = textInput.value;

    fetch('/upload/text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: {
            text: enteredText,
        }
    })
        .then(response => response.json())
        .then(data => {
            window.location.href = `/edit/${data['id']}`
        });
});