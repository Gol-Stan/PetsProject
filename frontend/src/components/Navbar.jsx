import { Link } from "react-router-dom";

export default function NavBar() {
    return (
        <nav className="bg-blue-800 text-white py-3">
            <ul className="flex justify-center space-x-8">
                <li><Link to="/breeds" className="hover:underline">Breed</Link></li>
                <li><Link to="/mypets" className="hover:underline">My Pets</Link></li>
                <li><Link to="/adoption" className="hover:underline">Adoption</Link></li>
                <li><Link to="/training" className="hover:underline">Training</Link></li>
            </ul>
        </nav>
    );
}