// frontend/src/main.js

// Load CouncilPanel.html into #council-panel
async function loadCouncilPanel() {
  try {
    const res = await fetch('/components/CouncilPanel.html');
    const html = await res.text();
    document.getElementById('council-panel').innerHTML = html;
  } catch (error) {
    console.error("Failed to load CouncilPanel:", error);
  }
}

loadCouncilPanel();





document.getElementById('send-btn').addEventListener('click', async () => {
  const input = document.getElementById('user-input');
  const output = document.getElementById('terminal-output');

  if (input.value.trim() === '') return;

  const userBlock = document.createElement('div');
  userBlock.textContent = `> ${input.value}`;
  output.appendChild(userBlock);

  const res = await fetch('http://localhost:8000/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: input.value }),
  });

  const data = await res.json();

  const aiBlock = document.createElement('div');
  aiBlock.textContent = data.response || '[No reply]';
  aiBlock.classList.add('text-purple-400', 'mt-2');
  output.appendChild(aiBlock);

  input.value = '';
  output.scrollTop = output.scrollHeight;
});
