/* Smooth gradient background animation */
body {
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #a18cd1, #fbc2eb);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    transition: background 0.5s ease;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.container {
    background: rgba(255, 255, 255, 0.95);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 15px 30px rgba(0,0,0,0.2);
    width: 450px;
    max-width: 90%;
    text-align: center;
    animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
    0% {opacity:0; transform: translateY(-20px);}
    100% {opacity:1; transform: translateY(0);}
}

h1 {
    margin-bottom: 25px;
    color: #333;
    text-shadow: 1px 1px 2px #aaa;
}

textarea {
    width: 100%;
    height: 120px;
    margin-bottom: 20px;
    padding: 15px;
    font-size: 16px;
    border-radius: 12px;
    border: 2px solid #ddd;
    transition: 0.3s ease;
    resize: none;
}

textarea:focus {
    border-color: #4CAF50;
    box-shadow: 0 0 10px rgba(76, 175, 80, 0.5);
    outline: none;
}

.buttons {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

button {
    flex: 1;
    margin: 0 5px;
    padding: 12px 0;
    font-size: 16px;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    background: linear-gradient(45deg, #36D1DC, #5B86E5);
    color: white;
    font-weight: bold;
    transition: 0.4s;
}

button:hover {
    transform: scale(1.05);
    background: linear-gradient(45deg, #5B86E5, #36D1DC);
}

#result {
    height: 100px;
    background: #f0f0f0;
    border: 2px solid #ddd;
    border-radius: 12px;
    padding: 15px;
    font-size: 16px;
    color: #333;
    resize: none;
    transition: 0.3s ease;
}
