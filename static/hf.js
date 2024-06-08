document.getElementById('send-btn').addEventListener('click', () => {
    const userInput = document.getElementById('user-input').value;
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_id: 1, message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        const messageContainer = document.getElementById('messages');
        const userMessage = document.createElement('div');
        userMessage.innerText = `You: ${userInput}`;
        messageContainer.appendChild(userMessage);
        
        const botResponse = document.createElement('div');
        botResponse.innerText = `Bot: ${data.response}`;
        messageContainer.appendChild(botResponse);
        
        document.getElementById('user-input').value = '';
    });
});
