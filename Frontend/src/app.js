import React, { useState } from "react";
import axios from "axios";

function App() {
  const [prompt, setPrompt] = useState("");
  const [image, setImage] = useState(null);
  const [bimFile, setBimFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateModel = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:5000/generate", { prompt });
      setImage(response.data["2D_model"]);
      setBimFile(response.data["BIM_model"]);
    } catch (error) {
      console.error("Error generating model:", error);
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Text-to-2D & BIM Generator</h1>
      <input
        type="text"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your prompt..."
      />
      <button onClick={generateModel} disabled={loading}>
        {loading ? "Generating..." : "Generate"}
      </button>

      {image && <img src={`http://127.0.0.1:5000/${image}`} alt="2D Model" />}
      {bimFile && <a href={`http://127.0.0.1:5000/${bimFile}`} download>Download BIM Model</a>}
    </div>
  );
}

export default App;
