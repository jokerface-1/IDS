import express from "express";
import pg from "pg";
import cors from "cors";

const app = express();
app.use(cors());

const db = new pg.Client({
    user: "postgres",
    password: "jokerface",
    database: "IDS",
    host: "localhost",
    port: 5432
});

await db.connect();

app.get("/data", async (req, res) => {

    try {

        const result = await db.query(
            "SELECT * FROM alerts"
        );

        res.json(result.rows);

    } catch (err) {

        console.log(err);

        res.status(500).send("Database Error");

    }

});

app.listen(3000, () => {
    console.log("Listening...");
});