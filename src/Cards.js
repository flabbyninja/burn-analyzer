import React from "react";

function Cards(props) {
  const cardConfig = props.cardConfig;
  return (
    <div class="carddeck row">
      {cardConfig.map((value, index) => {
        return (
          <div class="card-holder p-2 col-xl-2 col-md-3 col-sm-6">
            <Card card={value} />
          </div>
        );
      })}
    </div>
  );
}

function Card(props) {
  return (
    <div class="card">
      <img src="..." class="card-img-top" alt="..."></img>
      <div class="card-body">
        <h5 class="card-title">{props.card.name}</h5>
        <p class="card-text">{props.card.description}</p>
        <a href={props.card.dataSource} class="btn btn-primary">
          API Link
        </a>
      </div>
    </div>
  );
}

export default Cards;
