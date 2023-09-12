const codex = {
  'a': 1, 'j': 1, 's': 1,
  'b': 2, 'k': 2, 't': 2,
  'c': 3, 'l': 3, 'u': 3,
  'd': 4, 'm': 4, 'v': 4,
  'e': 5, 'n': 5, 'w': 5,
  'f': 6, 'o': 6, 'x': 6,
  'g': 7, 'p': 7, 'y': 7,
  'h': 8, 'q': 8, 'z': 8,
  'i': 9, 'r': 9
};

let sigilData = {};

function generateSigil() {
  const message = document.getElementById('messageInput').value.toLowerCase();
  let sigilCode = [];
  let uniqueLetters = [...new Set(message.replace(/[aeiou]/g, ''))];

  uniqueLetters.forEach(letter => {
    if (codex[letter]) {
      sigilCode.push(codex[letter]);
    }
  });

  sigilData = {
    message: message,
    sigilCode: sigilCode.sort(() => Math.random() - 0.5)
  };

  renderSigil();
}

function renderSigil() {
  const canvas = document.getElementById('sigilCanvas');
  const ctx = canvas.getContext('2d');
  const radius = canvas.width / 2;
  const angleStep = (2 * Math.PI) / sigilData.sigilCode.length;

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.beginPath();

  sigilData.sigilCode.forEach((number, index) => {
    const angle = index * angleStep;
    const x = radius + radius * Math.cos(angle);
    const y = radius + radius * Math.sin(angle);

    ctx.lineTo(x, y);
  });

  ctx.closePath();
  ctx.stroke();
}

document.getElementById('generateButton').addEventListener('click', generateSigil);