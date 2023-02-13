import React, { useContext } from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

// Import MVC Dependencies
import { Context } from "../store/appContext";

// Import Icons
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart } from "@fortawesome/free-solid-svg-icons";

const FilmCard = (props) => {
  const { store, actions } = useContext(Context);

  return (
    <div className="col">
      <div className="card shadow my-3">
        <img
          src="https://lumiere-a.akamaihd.net/v1/images/omega-s2-a-main_0216f1de.jpeg?region=280%2C0%2C720%2C720"
          className="card-img-top"
          alt="..."
        />
        <div className="body text-dark">
          <h4 className="card-title text-center p-3">{props.title}</h4>
          <ul className="list-group list-group-flush">
            <li className="list-group-item">
              Episode:
              <span className="text-capitalize">{props.episode_id}</span>
            </li>
            <li className="list-group-item">
              Director:
              <span className="text-capitalize">{props.director}</span>
            </li>
            <li className="list-group-item">
              Release Date:
              <span className="text-capitalize">{props.release_date}</span>
            </li>
          </ul>
          <div className="d-flex justify-content-between p-3">
            <div className="">
              <Link to={`/single/${props.id}`}>
                <div className="btn btn-outline-warning">Details</div>
              </Link>
            </div>
            <div className="">
              <button
                className="btn btn-outline-warning"
                onClick={() => actions.addFavorites(props.title)}
              >
                <FontAwesomeIcon icon={faHeart} />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

Card.propTypes = {
  title: PropTypes.string,
  episode_id: PropTypes.number,
  director: PropTypes.string,
  release_date: PropTypes.string,
  id: PropTypes.number,
  url: PropTypes.string,
};

export default FilmCard;
