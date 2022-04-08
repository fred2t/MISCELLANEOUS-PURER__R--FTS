import React, { useState } from "react";
import "./App.css";

import Axios from "axios";

function App() {
    return (
        <div>
            <CreatePost />
        </div>
    );
}

function CreatePost() {
    const [name, setName] = useState("");

    const bruh = () => {
        Axios.post("http://localhost:3006/routexd", {
            name,
        }).then(() => console.log('success')).catch(() => console.log('caught'));
    };

    return (
        <div>
            <div>
                <label>Username: </label>
                <input
                    type="text"
                    onChange={(e) => {
                        setName(e.target.value);
                    }}
                />
                <label>Title: </label>

                <button onClick={bruh}>Submit Post</button>
            </div>
        </div>
    );
}

export default App;
