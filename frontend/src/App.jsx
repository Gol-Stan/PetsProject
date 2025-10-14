import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Footer from "./components/Footer";

import Home from "./pages/Home";
import Breeds from "./pages/Breeds";
import MyPets from "./pages/MyPets";
import Adoption from "./pages/Adoption";
import Training from "./pages/Training";

export default function App() {
    return (
        <Router>
            <div className="flex flex-col min-h-screen">
                <NavBar />
                <main className="flex-grow max-w-6xl mx-auto mt-8 px-4">
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/breeds" element={<Breeds />} />
                        <Route path="/mypets" element={<MyPets />} />
                        <Route path="/adoption" element={<Adoption />} />
                        <Route path="/training" element={<Training />} />
                    </Routes>
                </main>

                <Footer />
            </div>
        </Router>
    );
}
