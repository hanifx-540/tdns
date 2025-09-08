const form = document.getElementById("encodeForm");
const resultContainer = document.getElementById("resultContainer");
const encodedText = document.getElementById("encodedText");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const text = document.getElementById("textInput").value;

    // Backend request (Flask)
    const response = await fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `text=${encodeURIComponent(text)}`
    });

    const data = await response.text(); // Flask returns rendered HTML
    // Extract encoded value from DOM (or use JSON API)
    // For demo, let's assume backend sends encoded in textarea
    encodedText.value = text + "-encoded"; // temporary placeholder

    resultContainer.classList.remove("hidden");
    gsap.fromTo(resultContainer, {opacity:0, y:-20}, {opacity:1, y:0, duration:0.5});
});
