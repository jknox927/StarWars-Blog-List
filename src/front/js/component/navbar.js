import React, { useContext } from "react";
import { Link } from "react-router-dom";

// Import MVC Dependencies
import { Context } from "../store/appContext";

// Import Icons
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart, faTrashCan } from "@fortawesome/free-solid-svg-icons";

export const Navbar = () => {
  const { store, actions } = useContext(Context);

  return (
    <div className="container">
      <header className="blog-header 1h-1 py-3">
        <div className="row flex-nowrap justify-content-between align-items-center">
          <div className="col-4 d-flex justify-content-start align-items-center">
            <Link
              to="/"
              className="btn btn-warning text-uppercase fw-bold fs-6"
            >
              Home
            </Link>
          </div>
          <div className="col-4 text-center">
            <img
              src="https://lumiere-a.akamaihd.net/v1/images/sw_logo_stacked_2x-52b4f6d33087_7ef430af.png?region=0,0,586,254"
              height="80"
              width="185"
            />
          </div>
          <div className="col-4 d-flex justify-content-end align-items-center">
            <button
              type="button"
              className="btn btn-warning dropdown-toggle text-uppercase fw-bold fs-6"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Favorites <FontAwesomeIcon icon={faHeart} />
            </button>
            <ul className="dropdown-menu">
              {store.favorites.map((item, index) => (
                <li key={index} className="d-flex justify-content-between">
                  {item}{" "}
                  <FontAwesomeIcon
                    role="button"
                    icon={faTrashCan}
                    onClick={() => actions.deleteFavorite(index)}
                  />
                </li>
              ))}
            </ul>
          </div>
        </div>
      </header>
      <div className="nav-scroller py-1 mt-5 mb-2">
        <nav className="nav d-flex justify-content-between text-uppercase p-2 fs-4">
          <Link
            to="/people"
            className="text-secondary nav-link text-decoration-underline"
          >
            People
          </Link>
          <Link
            to="/films"
            className="text-secondary nav-link text-decoration-underline"
          >
            Films
          </Link>
          <Link
            to="/starships"
            className="text-secondary nav-link text-decoration-underline"
          >
            Starships
          </Link>
          <Link
            to="/vehicles"
            className="text-secondary nav-link text-decoration-underline"
          >
            Vehicles
          </Link>
          <Link
            to="/species"
            className="text-secondary nav-link text-decoration-underline"
          >
            Species
          </Link>
          <Link
            to="/planets"
            className="text-secondary nav-link text-decoration-underline"
          >
            Planets
          </Link>
        </nav>
      </div>
    </div>
  );
};
