import React, { useEffect, useContext } from "react";

// Import MVC Dependencies
import { Context } from "../store/appContext.js";

// Import Components
import FilmCard from "../component/FilmCard.jsx";

export const Films = () => {
  const { store, actions } = useContext(Context);

  useEffect(() => {
    actions.getFilms();
  }, [])

  return (
    <div className="container mb-5 pb-5 overflow-hidden">
      <div className="col-12 bg-dark">
        <h1 className="text-warning text-center text-uppercase">Films</h1>
      </div>
      <div className="row">
        {store.films.map((item, index) => {
          return (
            <div className="col-12 col-md-6 col-lg-4" key={index}>
              <FilmCard
                key={index}
                title={item.title}
                episode_id={item.episode_id}
                director={item.director}
                release_date={item.release_date}
                id={index}
              />
            </div>
          );
        })}
      </div>
    </div>
  );
};