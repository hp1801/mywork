const updateSpeedDisplay = () => {
    fetch('/api/latest-speed/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('current-speed').innerText = data.speed + " km/h";
        });
};

// Update the display every second (1000 milliseconds)
setInterval(updateSpeedDisplay, 1000);