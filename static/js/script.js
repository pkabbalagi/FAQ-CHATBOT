const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const history = document.getElementById("chat-history");
const clearButton = document.getElementById("clear-chat");

function scrollToBottom() {
  history.scrollTop = history.scrollHeight;
}

function addMessage(text, sender) {
  const row = document.createElement("div");
  row.className = `message-row ${sender === "user" ? "user-row" : "bot-row"}`;

  if (sender === "bot") {
    const avatar = document.createElement("div");
    avatar.className = "bot-avatar";
    avatar.textContent = "C";
    row.appendChild(avatar);
  }

  const bubble = document.createElement("div");
  bubble.className = `message ${sender === "user" ? "user-message" : "bot-message"}`;
  bubble.textContent = text;
  row.appendChild(bubble);
  history.appendChild(row);
  scrollToBottom();
}

function showTyping() {
  const row = document.createElement("div");
  row.id = "typing-indicator";
  row.className = "message-row bot-row";
  row.innerHTML = '<div class="bot-avatar">C</div><div class="message bot-message typing"><span></span><span></span><span></span></div>';
  history.appendChild(row);
  scrollToBottom();
}

function removeTyping() {
  document.getElementById("typing-indicator")?.remove();
}

async function sendMessage(text) {
  const message = text.trim();
  if (!message) return;

  addMessage(message, "user");
  input.value = "";
  sendButton.disabled = true;
  input.disabled = true;
  showTyping();

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    removeTyping();
    addMessage(data.reply || "Sorry, something went wrong. Please try again.", "bot");
  } catch (_error) {
    removeTyping();
    addMessage("Sorry, I couldn’t connect to the server. Please check your connection and try again.", "bot");
  } finally {
    sendButton.disabled = false;
    input.disabled = false;
    input.focus();
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  sendMessage(input.value);
});

clearButton.addEventListener("click", () => {
  history.innerHTML = "";
  addMessage("Chat cleared. How can I help you?", "bot");
  input.focus();
});

document.querySelectorAll(".quick-reply").forEach((button) => {
  button.addEventListener("click", () => sendMessage(button.textContent));
});

input.addEventListener("input", () => {
  sendButton.disabled = input.value.trim().length === 0;
});

sendButton.disabled = true;
