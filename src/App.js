import React from "react";
import "./App.css";
import Timeline from "./Timeline";
import Cards from "./Cards";

const cardConfig = [
  {
    name: "metric1",
    description: "decription",
    dataSource: "api/thing",
  },
  {
    name: "metric2",
    description: "decription",
    dataSource: "api/thing",
  },
  {
    name: "metric3",
    description: "decription",
    dataSource: "api/thing",
  },
  {
    name: "metric4",
    description: "decription",
    dataSource: "api/thing",
  },
  {
    name: "metric5",
    description: "decription",
    dataSource: "api/thing",
  },
  {
    name: "metric6",
    description: "decription",
    dataSource: "api/thing",
  },
  {
    name: "metric7",
    description: "decription",
    dataSource: "api/thing",
  },
];

function App() {
  return (
    <div className="App">
      <div id="mainApp" className="container">
        <h1>BurnTracker</h1>
        <Timeline />
        <div class="row" id="detail">
          <Cards cardConfig={cardConfig} />
        </div>
      </div>
    </div>
  );
}

export default App;
