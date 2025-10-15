import { Link } from "react-router-dom";

export default function NavBar() {
    return (
        <nav className="bg-blue-800 text-white py-3">
            <ul className="flex justify-center space-x-8">
                <li><Link to="/" className="hover:underline">Главная</Link></li>
                <li><Link to="/breeds" className="hover:underline">Породы</Link></li>
                <li><Link to="/mypets" className="hover:underline">Мои питомцы</Link></li>
                <li><Link to="/adoption" className="hover:underline">Усыновление</Link></li>
                <li><Link to="/training" className="hover:underline">Дрессировка</Link></li>
            </ul>
        </nav>
    );
}