import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import NavBar from "./components/NavBar";
import Footer from "./components/Footer";

import Home from "./pages/Home";
import Breeds from "./pages/Breeds";
import MyPets from "./pages/MyPets";
import Adoption from "./pages/Adoption";
import Training from "./pages/Training";


import background from "./assets/background_main.png";
import Register from "./pages/Registration.jsx";

export default function App() {
    return (
        <Router>
            <div
                style={{
                    backgroundImage: `url(${background})`,
                    backgroundSize: "cover",
                    backgroundPosition: "center top",
                    backgroundRepeat: "no-repeat",
                    minHeight: "100vh",
                }}
            >
                <div className="flex flex-col min-h-screen bg-white/40 ">
                    <Header />
                    <NavBar />
                    <main className="flex-grow max-w-6xl mx-auto mt-8 px-4">
                        <Routes>
                            <Route path="/" element={<Home />} />
                            <Route path="/breeds" element={<Breeds />} />
                            <Route path="/mypets" element={<MyPets />} />
                            <Route path="/adoption" element={<Adoption />} />
                            <Route path="/training" element={<Training />} />
                            <Route path="register" element={<Register />} />
                        </Routes>
                    </main>
                    <Footer />
                </div>
            </div>
        </Router>
    );
}
