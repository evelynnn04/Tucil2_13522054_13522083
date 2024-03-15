const canvas = document.getElementById("cartesian-canvas");
const ctx = canvas.getContext("2d");
const gridSize = 15;

// Define canvas width and height
const canvasWidth = canvas.width;
const canvasHeight = canvas.height;
numberOfVerticalLine = canvas.width / gridSize;
numberOfHorizontalLine = canvas.height / gridSize;

// Draw vertical grid lines
ctx.lineWidth = 1;
ctx.strokeStyle = "rgba(0, 0, 0, 1)";
for (let x = 0; x <= numberOfVerticalLine; x++) {
    if (x == numberOfVerticalLine / 2){
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(x * gridSize, 0);
        ctx.lineTo(x * gridSize, canvasHeight);
        ctx.stroke();
        continue;
    }
    ctx.lineWidth = 0.5;
    ctx.beginPath();
    ctx.moveTo(x * gridSize, 0);
    ctx.lineTo(x * gridSize, canvasHeight);
    ctx.stroke();
}

// Draw horizontal grid lines 
for (let y = 0; y <= numberOfHorizontalLine; y++) {
    if (y == numberOfHorizontalLine / 2){
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(0, y * gridSize);
        ctx.lineTo(canvasWidth, y * gridSize);
        ctx.stroke();
        continue;
    }
    ctx.lineWidth = 0.5;
    ctx.beginPath();
    ctx.moveTo(0, y * gridSize);
    ctx.lineTo(canvasWidth, y * gridSize);
    ctx.stroke();
}

// Define points for the additional line
const startPoint = { x: 1, y: 1 };
const endPoint = { x: -1, y: -1 };

// Draw line
ctx.strokeStyle = "black"; 
ctx.lineWidth = 0.5;
ctx.beginPath();
ctx.moveTo(startPoint.x * gridSize + canvasWidth / 2, -startPoint.y * gridSize + canvasHeight / 2);
ctx.lineTo(endPoint.x * gridSize + canvasWidth / 2, -endPoint.y * gridSize + canvasHeight / 2);
ctx.stroke();

// Display line coordinates
ctx.font = "10px Arial";
ctx.fillStyle = "black"; 
ctx.fillText(`(${startPoint.x}, ${startPoint.y})`, startPoint.x * gridSize + canvasWidth / 2, -startPoint.y * gridSize + canvasHeight / 2 - 5);
ctx.fillText(`(${endPoint.x}, ${endPoint.y})`, endPoint.x * gridSize + canvasWidth / 2, -endPoint.y * gridSize + canvasHeight / 2 - 5);

fetch('http://localhost:8080/api/beizer')
    .then(response => response.json())
    .then(data => {
        console.log(data); // Log the list data to the console
        // Use the list data as needed in your JavaScript code
    })
    .catch(error => console.error('Error:', error));
