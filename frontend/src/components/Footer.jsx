export default function Footer() {
    return (
        <footer className="bg-gray-800 text-gray-200 py-4 mt-8">
            <div className="max-w-6xl mx-auto px-4 flex justify-between items-center">
                <div className="w-1/3"></div>
                <p className="w-1/3 text-center">© 2025 PetsProject</p>
                <div className="w-1/3 flex justify-end gap-4">
                    <a href="#" className="hover:text-white">Instagram</a>
                    <a href="#" className="hover:text-white">Telegram</a>
                    <a href="#" className="hover:text-white">YouTube</a>
                </div>
            </div>
        </footer>
    );
}