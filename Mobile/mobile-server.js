const express = require("express");
const path = require("path");

const app = express();

app.use(express.static(path.join(__dirname)));

app.listen(4000, "0.0.0.0", () => {
    console.log("Mobile Website Running on Port 4000");
});