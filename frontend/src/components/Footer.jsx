export default function Footer() {
    return (
        <footer className="bg-gray-800 text-gray-200 py-4 mt-8">
            <div className="max-w-6xl mx-auto px-4 flex justify-between items-center">
                <p>© 2025 PetsProject.</p>
                <div className="flex gap-4">
                    <a href="#" className="hover:text-white">Instagram</a>
                    <a href="#" className="hover:text-white">Telegram</a>
                    <a href="#" className="hover:text-white">Youtube</a>
                </div>
            </div>
        </footer>
    );
}