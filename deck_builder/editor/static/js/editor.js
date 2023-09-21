function download_deck(id) {
  fetch("/editor/download/"+id)
    .then(response => response.blob())
    .then(blob => {
      const blobURL = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = blobURL;
      link.download = 'deck.txt';
      link.style.display = 'none';
      document.body.appendChild(link)
      link.click();
      window.URL.revokeObjectURL(blobURL);
      document.body.removeChild(link);
  });
  console.log(id)
}
