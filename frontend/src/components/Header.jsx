import Nav from './Navbar';
import logo from '../assets/logo.png';
import background from '../assets/background.jpg';

export default function Header() {
    return (
        <header
            className="relative bg-cover bg-[position:50%_80%] h-32 flex items-center"
            style={{
                backgroundImage: `linear-gradient(rgba(245, 222, 179, 0.2), rgba(245, 222, 179, 0.2)),  url(${background})`,
            }}
        >

            <div className="w-full max-w-6xl mx-auto flex justify-between items-center px-6">
                <div className="flex items-center gap-3">
                    <img
                        src={logo}
                        alt="PetZone Logo"
                        className="w-16 h-16 object-contain"
                    />
                    <h1 className="text-3xl font-bold text-shadow-green-400">PetWorld</h1>
                </div>

            </div>
        </header>
    );
}