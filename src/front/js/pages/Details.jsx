import React, { useEffect, useContext } from "react";
import { useParams } from "react-router-dom";

import { Context } from "../store/appContext";

export const Details = () => {
  const { actions, store } = useContext(Context);
  const { id } = useParams();

  useEffect(() => {
    actions.person(id);
  }, []);

  return <h1>Name: {store.person.name}</h1>;
};
