const express = require('express');
const app = express();
const port = 3000;

// Serve static files (HTML, CSS, JavaScript)
app.use(express.static('public'));  // Assuming static files are in a 'public' folder

// Basic route to serve the homepage
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');  // Adjust this if index.html is in a different folder
});

// Start the server
app.listen(port, () => {
  console.log(`App running on http://localhost:${port}`);
});
