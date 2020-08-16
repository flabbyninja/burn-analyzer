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
    <div className="card">
      <i className={"card-img-top flaticon " + props.card.icon}></i>
      <div className="card-body">
        <h5 className="card-title">{props.card.name}</h5>
        <p className="card-text">{props.card.description}</p>
        <a href={props.card.dataSource} className="btn btn-primary btn-sm mb-2">
          API Link
        </a>
      </div>
    </div>
  );
}

export default Cards;
