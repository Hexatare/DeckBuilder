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

function delete_card(elem) {
  const id = elem.parentElement.id;
  fetch("/editor/remove/"+id, {
    method: 'POST',
  });
  const parent = elem.parentElement;
  parent.parentNode.removeChild(parent);
}

function save_deck() {
  const content = document.querySelector('.page-content');
  const deck = content.querySelectorAll('.page-content-card');
  const cards = [];
  deck.forEach(function(elem) {
    let id = elem.id;
    let front =  elem.querySelector('.page-content-card-front').value;
    let back = elem.querySelector('.page-content-card-back').value;
    cards.push({id:id, front:front, back:back});
  });

  let send = {
    cards: cards,
  };

  const headers = {
  'Content-Type': 'application/json',
  };
  
  fetch("/editor/save", {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(send),
  });
}
