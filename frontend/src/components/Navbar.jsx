import { Link } from "react-router-dom";

export default function NavBar() {
    return (
        <nav className="bg-orange-100 text-gray-800 py-3">
            <ul className="flex justify-center space-x-16">
                <li><Link to="/breeds" className="hover:underline">Breed</Link></li>
                <li><Link to="/mypets" className="hover:underline">My Pets</Link></li>
                <li><Link to="/adoption" className="hover:underline">Adoption</Link></li>
                <li><Link to="/training" className="hover:underline">Training</Link></li>
            </ul>
        </nav>
    );
}