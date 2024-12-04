document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('speedCanvas');
    const ctx = canvas.getContext('2d');
    let currentSpeed = 0;

    // Function to fetch speed data every second
    setInterval(() => {
        fetch('http://localhost:8000/api/speed/')
            .then(response => response.json())
            .then(data => {
                currentSpeed = data.speed;
                drawSpeedometer(currentSpeed);
            })
            .catch(err => console.error('Error fetching speed data:', err));
    }, 1000);

    // Function to draw the speedometer
    function drawSpeedometer(speed) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw the outer circle
        ctx.beginPath();
        ctx.arc(200, 200, 150, 0, Math.PI * 2);
        ctx.strokeStyle = '#000';
        ctx.lineWidth = 5;
        ctx.stroke();
        ctx.closePath();

        // Draw the needle
        const angle = (speed / 120) * Math.PI - Math.PI / 2;
        const needleLength = 140;
        const needleX = 200 + needleLength * Math.cos(angle);
        const needleY = 200 + needleLength * Math.sin(angle);

        ctx.beginPath();
        ctx.moveTo(200, 200);
        ctx.lineTo(needleX, needleY);
        ctx.strokeStyle = 'red';
        ctx.lineWidth = 3;
        ctx.stroke();
        ctx.closePath();

        // Display speed value
        ctx.font = '24px Arial';
        ctx.fillStyle = '#000';
        ctx.fillText(`${Math.round(speed)} km/h`, 160, 200);
    }

    // Initial drawing
    drawSpeedometer(currentSpeed);
});
