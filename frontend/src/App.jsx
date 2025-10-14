import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Breeds from "./pages/Breeds";
import MyPets from "./pages/MyPets";
import Adoption from "./pages/Adoption";
import Training from "./pages/Training";

export default function App() {
    return (
        <Router>
            <NavBar />
            <div className="max-w-6xl mx-auto mt-8">
                <Routes>
                    <Route exact path="/breeds" element={<Breeds />} />
                    <Route exact path="/mypets" element={<MyPets />} />
                    <Route exact path="/adoption" element={<Adoption />} />
                    <Route exact path="/training" element={<Training />} />
                </Routes>
            </div>
        </Router>
    );
}