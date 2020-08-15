import React from "react";

function Cards(props) {
  const cardConfig = props.cardConfig;

  cardConfig.sort((a, b) => a.priority - b.priority);
  return (
    <div className="carddeck row">
      {cardConfig.map((value, index) => {
        return (
          <div className="card-holder d-flex align-items-stretch p-2 col-lg-2 col-md-3 col-sm-4 col-6">
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
      <i className={"card-img-top flaticon " + props.card.icon}></i>
      <div class="card-body">
        <h5 class="card-title">{props.card.name}</h5>
        <p class="card-text">{props.card.description}</p>
        <a href={props.card.dataSource} className="btn btn-primary btn-sm">
          API Link
        </a>
      </div>
    </div>
  );
}

export default Cards;
