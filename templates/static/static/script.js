async function sendRequest(action) {
    const text = document.getElementById('text').value.trim();
    const resultBox = document.getElementById('result');

    if (!text) {
        resultBox.value = "Please type some text!";
        return;
    }

    resultBox.value = "Processing...";

    try {
        const response = await fetch(`/${action}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });

        const data = await response.json();

        if (response.ok) {
            resultBox.value = data.result;
        } else {
            resultBox.value = "Error: " + data.error;
        }
    } catch (err) {
        resultBox.value = "Error: Unable to connect!";
    }
}

// Optional: real-time encode as user types
document.getElementById('text').addEventListener('input', () => {
    sendRequest('encode');
});
