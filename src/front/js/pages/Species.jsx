import React, { useEffect, useContext } from "react";

// Import MVC Dependencies
import { Context } from "../store/appContext.js";

// Import Components
import SpeciesCard from "../component/SpeciesCard.jsx";

export const Species = () => {
  const { store, actions } = useContext(Context);

  useEffect(() => {
    actions.getSpecies();
  }, [])

  return (
    <div className="container mb-5 pb-5 overflow-hidden">
      <div className="col-12 bg-dark">
        <h1 className="text-warning text-center text-uppercase">Species</h1>
      </div>
      <div className="row">
        {store.species.map((item, index) => {
          return (
            <div className="col-12 col-md-6 col-lg-4" key={index}>
              <SpeciesCard
                key={index}
                name={item.name}
                designation={item.designation}
                average_lifespan={item.average_lifespan}
                language={item.language}
                id={index}
              />
            </div>
          );
        })}
      </div>
    </div>
  );
};