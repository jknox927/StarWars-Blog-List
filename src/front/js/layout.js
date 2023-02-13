import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

// Import MVC dependencies
import ScrollToTop from "./component/scrollToTop";
import injectContext from "./store/appContext";

// Import Components
import { Navbar } from "./component/navbar";
import { Home } from "./pages/Home.jsx";
import { People } from "./pages/People.jsx";
import { Films } from "./pages/Films.jsx";
import { Starships } from "./pages/Starships.jsx";
import { Vehicles } from "./pages/Vehicles.jsx";
import { Species } from "./pages/Species.jsx";
import { Planets } from "./pages/Planets.jsx";
import { Footer } from "./component/footer";


const Layout = () => {

    const basename = process.env.BASENAME || "";

    return (
        <div>
            <BrowserRouter basename={basename}>
                <ScrollToTop>
                    <Navbar />
                    <Routes>
                        <Route element={<Home />} path="/" />
                        <Route element={<People />} path="/people" />
                        <Route element={<Films />} path="/films" />
                        <Route element={<Starships />} path="/starships" />
                        <Route element={<Vehicles />} path="/vehicles" />
                        <Route element={<Species />} path="/species" />
                        <Route element={<Planets />} path="/planets" />
                        <Route element={<h1>Not found!</h1>} />
                    </Routes>
                    <Footer />
                </ScrollToTop>
            </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);
