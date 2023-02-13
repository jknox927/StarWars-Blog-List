import React, { useContext } from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

// Import MVC Dependencies
import { Context } from "../store/appContext";

// Import Icons
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart } from "@fortawesome/free-solid-svg-icons";

const SpeciesCard = (props) => {
  const { actions } = useContext(Context);

  return (
    <div className="col">
      <div className="card shadow my-3">
        <img src="https://lumiere-a.akamaihd.net/v1/images/omega-s2-a-main_0216f1de.jpeg?region=280%2C0%2C720%2C720" className="card-img-top" alt="..." />
        <div className="body text-dark">
          <h4 className="card-title text-center p-3">{props.name}</h4>
          <ul className="list-group list-group-flush">
            <li className="list-group-item">Designation: <span className="text-capitalize">{props.designation}</span></li>
            <li className="list-group-item">Avg. Lifespan: <span className="text-capitalize">{props.average_lifespan}</span></li>
            <li className="list-group-item">Language: <span className="text-capitalize">{props.language}</span></li>
          </ul>
          <div className="d-flex justify-content-between p-3">
            <div className="">
              <Link to={`/single/${props.id}`}>
                <div className="btn btn-outline-warning">Details</div>
              </Link>
            </div>
            <div className="">
              <button className="btn btn-outline-warning" onClick={() => actions.addFavorite(props.name)}>
                <FontAwesomeIcon icon={faHeart} />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

SpeciesCard.propTypes = {
  name: PropTypes.string,
  designation: PropTypes.string,
  average_lifespan: PropTypes.string,
  language: PropTypes.string,
  id: PropTypes.number,
  url: PropTypes.string
};

export default SpeciesCard;
