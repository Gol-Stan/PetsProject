import { Link } from "react-router-dom";

export default function NavBar() {
    return (
        <nav className="bg-orange-100 text-gray-800 py-3">
            <ul className="flex justify-center divide-x divide-gray-300">
                <li className="px-8">
                    <Link to="/breeds" className="hover:underline">
                        Breeds
                    </Link>
                </li>
                <li className="px-8">
                    <Link to="/mypets" className="hover:underline">
                        My Pet
                    </Link>
                </li>
                <li className="px-8">
                    <Link to="/adoption" className="hover:underline">
                        Adoption
                    </Link>
                </li>
                <li className="px-8">
                    <Link to="/training" className="hover:underline">
                        Training
                    </Link>
                </li>
            </ul>
        </nav>
    );
}