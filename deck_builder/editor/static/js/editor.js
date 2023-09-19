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

imageInput.addEventListener('change', function () {
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
                console.log(data);
            });
    }
});

/*
const textInput = document.getElementById('text-input');
const submitTextButton = document.getElementById('submit-text');

submitTextButton.addEventListener('click', function () {
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
            fileContents = data['file_contents'];

            console.log(fileContents);
        });
});
*/