// Define the backend URL
const backendUrl = 'http://localhost:8001'; // Update to match your backend port

// Fetch speed data every second and update the speedometer display
setInterval(async () => {
    try {
        const response = await fetch(`${backendUrl}/speedometer/data/`);
        if (response.ok) {
            const data = await response.json();
            document.getElementById('speed').innerText = data.speed.toFixed(2);
        } else {
            console.error('Failed to fetch speed data:', response.status);
        }
    } catch (error) {
        console.error('Error fetching speed data:', error);
    }
}, 1000);

