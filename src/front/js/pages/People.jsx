import React, { useEffect, useContext } from "react";
import { useParams } from "react-router-dom";

// Import MVC Dependencies
import { Context } from "../store/appContext.js";

// Import Components
import Card from "../component/Card.jsx";

export const People = () => {
  const { store, actions } = useContext(Context);
  const { id } = useParams();

  useEffect(() => {
    actions.getPeople();
    // actions.person(id);
  }, []);

  return (
    <div className="container mb-5 pb-5 overflow-hidden">
      <div className="col-12 bg-dark">
        <h1 className="text-warning text-center text-uppercase">People</h1>
      </div>
      <div className="row">
        {store.people.map((item, index) => {
          return (
            <div className="col-12 col-md-6 col-lg-4" key={index}>
              <Card
                key={index}
                name={item.name}
                gender={item.gender}
                hair_color={item.hair_color}
                birth_year={item.birth_year}
                id={index + 1}
              />
            </div>
          );
        })}
      </div>
    </div>
  );
};
