const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			// store object values
			// root: {},
			favorites: [],
			people: [],
			films: [],
			starships: [],
			vehicles: [],
			species: [],
			planets: [],
		},

		actions: {
			
			getPeople: async () => {
				let url = "https://swapi.dev/api/people";
				
				try {
					const res = await fetch(url);
					const data = await res.json();
					console.log(data);
					setStore({ people: data.results });
				} catch (error) {
					throw Error(error);
				}
			},

			getFilms: async() => {
				let url = "https://swapi.dev/api/films";

				try {
					const res = await fetch(url);
					const data = await res.json();
					console.log(data);
					setStore({ films: data.results });
				} catch (error) {
					throw Error(error);
				}
				

				setStore({
					films: data.results,
				});
			},

			getPlanets: async () => {
				let url = "https://swapi.dev/api/planets";

				try {
					const res = await fetch(url);
					const data = await res.json();
					console.log(data);
					setStore({ planets: data.results });
				} catch (error) {
					throw Error(error);
				}
			},

			getSpecies: async () => {
				let url = "https://swapi.dev/api/species";

				try {
					const res = await fetch(url);
					const data = await res.json();
					console.log(data);
					setStore({ species: data.results });
				} catch (error) {
					throw Error(error);
				}	
			},

			getStarships: async () => {
				let url = "https://swapi.dev/api/starships";

				try {
					const res = await fetch(url);
					const data = await res.json();
					console.log(data);
					setStore({ starships: data.results });
				} catch (error) {
					throw Error(error);
				}	
			},

			getVehicles: async () => {
				let url = "https://swapi.dev/api/vehicles";

				try {
					const res = await fetch(url);
					const data = await res.json();
					console.log(data);
					setStore({ vehicles: data.results });
				} catch (error) {
					throw Error(error);
				}
			},

			addFavorite: (item) => {
				const store = getStore();
				let newFavorites = [ ...store.favorites, item];
				let uniqueFavorites = [ ...new Set(newFavorites) ];
				setStore({ favorites: uniqueFavorites });
			},

			deleteFavorite: (idx) => {
				const store = getStore();
				let newFavorites = store.favorites.filter(( item, index ) => index !== idx )
				setStore({ favorites: newFavorites });
			}
		}
	};
};

export default getState;
