import React, { useEffect, useContext } from "react";

// Import MVC Dependencies
import { Context } from "../store/appContext.js";

// Import Components
import PlanetsCard from "../component/PlanetsCard.jsx";

export const Planets = () => {
  const { store, actions } = useContext(Context);

  useEffect(() => {
    actions.getPlanets();
  }, [])

  return (
    <div className="container mb-5 pb-5 overflow-hidden">
      <div className="col-12 bg-dark">
        <h1 className="text-warning text-center text-uppercase">Planets</h1>
      </div>
      <div className="row">
        {store.planets.map((item, index) => {
          return (
            <div className="col-12 col-md-6 col-lg-4" key={index}>
              <PlanetsCard
                key={index}
                name={item.name}
                climate={item.climate}
                terrain={item.terrain}
                population={item.population}
                id={index}
              />
            </div>
          );
        })}
      </div>
    </div>
  );
};