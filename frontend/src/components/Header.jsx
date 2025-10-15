export default function Header() {
    return (
        <header className="bg-white shadow-md py-4 px-6 flex justify-between items-center">
            <div className="flex items-center space-x-2">
                <img src="/logo.png" alt="Logo" className="h-10 w-10" />
                <span className="text-xl font-bold text-blue-800">PetZone</span>
            </div>

            <div>
                <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition">
                    Registration / Login
                </button>
            </div>
        </header>
    );
}