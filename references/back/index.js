const express = require("express");
const mysql2 = require("mysql2");
const cors = require("cors");

const app = express();
const db = mysql2.createConnection({
    user: "root",
    host: "localhost",
    password: "[thePassword]",
    database: "[myDatabaseName]",
});
const PORT = [addPortHere];

app.use(cors());
app.use(express.json());

// Route to get all posts
app.post("/routexd", (req, res) => {
    const name = req.body.name;

    db.query("INSERT INTO games VALUES (?)", [name], (err, result) => {
        if (err) console.log(err);
        else console.log('values inserted');
    });

});

app.listen(PORT, () => {
    console.log(`Server is running on ${PORT}`);
});
