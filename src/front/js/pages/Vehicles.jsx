import React, { useEffect, useContext } from "react";

// Import MVC Dependencies
import { Context } from "../store/appContext.js";

// Import Components
import StarshipsCard from "../component/StarshipsCard.jsx";

export const Vehicles = () => {
  const { store, actions } = useContext(Context);

  useEffect(() => {
    actions.getVehicles();
  }, [])

  return (
    <div className="container mb-5 pb-5 overflow-hidden">
      <div className="col-12 bg-dark">
        <h1 className="text-warning text-center text-uppercase">Vehicles</h1>
      </div>
      <div className="row">
        {store.vehicles.map((item, index) => {
          return (
            <div className="col-12 col-md-6 col-lg-4" key={index}>
              <StarshipsCard
                key={index}
                name={item.name}
                manufacturer={item.manufacturer}
                max_atmosphering_speed={item.max_atmosphering_speed}
                hyperdrive_rating={item.hyperdrive_rating}
                id={index}
              />
            </div>
          );
        })}
      </div>
    </div>
  );
};