export default function Footer() {
    return (
        <footer className="bg-orange-100 text-gray-800 py-4 mt-8">
            <div className="max-w-6xl mx-auto px-4 flex justify-between items-center">
                <div className="w-1/3"></div>
                <p className="w-1/3 text-center">© 2025 PetsProject</p>
                <div className="w-1/3 flex justify-end gap-4">
                    <a href="#" className="hover:text-orange-800">Instagram</a>
                    <a href="#" className="hover:text-orange-800">Telegram</a>
                    <a href="#" className="hover:text-orange-800">YouTube</a>
                </div>
            </div>
        </footer>
    );
}