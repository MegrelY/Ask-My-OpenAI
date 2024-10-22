document.getElementById("send-button").addEventListener("click", sendMessage);

document.getElementById("question-input").addEventListener("keypress", function (e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

function appendMessage(sender, text) {
    const chatLog = document.getElementById("chat-log");
    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${sender}`;
    messageDiv.innerHTML = `<strong>${sender}:</strong> ${text.replace(/\n/g, '<br>')}`;
    chatLog.appendChild(messageDiv);
    chatLog.scrollTop = chatLog.scrollHeight; // Auto-scroll to bottom
}

async function sendMessage() {
    const questionInput = document.getElementById("question-input");
    const question = questionInput.value.trim();
    if (!question) return;  // Do nothing if input is empty

    appendMessage("user", question);
    questionInput.value = "";  // Clear the input field

    try {
        const response = await fetch("http://localhost:8000/query", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: question })
        });

        if (response.ok) {
            const data = await response.json();
            let answer = data.answer;
            if (data.references && data.references.length > 0) {
                answer += "\n\nReferences:\n" + data.references.join("\n");
            }
            appendMessage("openai", answer);
        } else {
            appendMessage("openai", "Error: Unable to get response from server.");
        }
    } catch (error) {
        appendMessage("openai", "Error: Network error.");
    }
}
