import React from "react";
import "./App.css";
import Timeline from "./Timeline";
import Cards from "./Cards";
import staticCards from "./testdata";
import BurnNav from "./BurnNav";

const cardConfig = staticCards;

function App() {
  return (
    <div className="App">
      <BurnNav />
      <div id="mainApp" className="container">
        <h1>PowerTracker</h1>
        <Timeline />
        <div id="detail">
          <Cards cardConfig={cardConfig} />
        </div>
      </div>
      <footer className="footer">
        <span>
          Icons made by{" "}
          <a href="https://www.flaticon.com/authors/freepik" title="Freepik">
            Freepik
          </a>{" "}
          from{" "}
          <a href="https://www.flaticon.com/" title="Flaticon">
            www.flaticon.com
          </a>
        </span>
      </footer>
    </div>
  );
}

export default App;
