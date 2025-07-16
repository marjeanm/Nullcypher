const injectComponent = async (id, path) => {
  const res = await fetch(path);
  let  html = await res.text();
  document.getElementById(id).innerHTML = html;
};

injectComponent("memory-feed", "/src/components/MemoryFeed.html");
injectComponent("council-display", "/src/components/CouncilPanel.html");




async function sendMessage(userInput) {
  const response = await fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: userInput })
  });

  const reader = response.body.getReader();
  const decoder = new TextDecoder("utf-8");
  let message = "";

  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    const chunk = decoder.decode(value);
    message += chunk;
    updateTerminal(message);  // Replace this with your terminal’s display function
  }
}
document.getElementById("submitBtn").addEventListener("click", () => {
  const userInput = document.getElementById("userInput").value;
  sendMessage(userInput);
});
function updateTerminal(message) {
  document.getElementById("terminalOutput").innerText = message;
}
