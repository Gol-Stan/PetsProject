import heroDog from "../assets/hero-dog.jpg";

export default function Home() {
    return (
        <div className="min-h-screen bg-amber-50 text-gray-800">
            {/* Hero section */}
            <section className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between px-6 py-16">
                <div className="md:w-1/2">
                    <h1 className="text-4xl md:text-5xl font-bold mb-6">
                        Welcome to <span className="text-orange-400">PetWorld</span>
                    </h1>
                    <p className="text-lg text-gray-700 mb-8 leading-relaxed">
                        Discover different dog breeds, learn their traits and personalities.
                        We help you find the perfect companion that matches your lifestyle.
                    </p>
                    <a
                        href="/breeds"
                        className="bg-orange-400 text-white px-6 py-3 rounded-lg font-semibold hover:bg-orange-500 transition-colors"
                    >
                        Explore Breeds
                    </a>
                </div>

                <div className="md:w-1/2 mt-10 md:mt-0 flex justify-center">
                    <img
                        src={heroDog}
                        alt="dog"
                        className="w-80 md:w-96 rounded-3xl shadow-lg object-cover"
                    />
                </div>
            </section>

            {/* About section */}
            <section className="bg-orange-100 py-16">
                <div className="max-w-6xl mx-auto px-6 text-center">
                    <h2 className="text-3xl font-bold mb-6">About the Project</h2>
                    <p className="text-gray-700 text-lg leading-relaxed max-w-3xl mx-auto">
                        This website is made for all dog lovers — whether you’re a first-time owner or a breeder.
                        We collect reliable information about breeds to help you understand which dog best fits your life.
                    </p>
                </div>
            </section>

            {/* Features */}
            <section className="max-w-6xl mx-auto px-6 py-16 grid grid-cols-1 md:grid-cols-3 gap-10 text-center">
                <div className="bg-orange-100 rounded-2xl shadow-md p-8">
                    <h3 className="text-xl font-semibold mb-4 text-orange-400">🐶 Breed Catalog</h3>
                    <p className="text-gray-700 leading-relaxed">
                        Learn everything about popular and rare dog breeds —
                        photos, descriptions, personality traits, and more.
                    </p>
                </div>

                <div className="bg-orange-100 rounded-2xl shadow-md p-8">
                    <h3 className="text-xl font-semibold mb-4 text-orange-400">📚 Useful Information</h3>
                    <p className="text-gray-700 leading-relaxed">
                        We regularly update articles on training, grooming, and nutrition
                        to help your pets live happy and healthy lives.
                    </p>
                </div>

                <div className="bg-orange-100 rounded-2xl shadow-md p-8">
                    <h3 className="text-xl font-semibold mb-4 text-orange-400">❤️ For All Animal Lovers</h3>
                    <p className="text-gray-700 leading-relaxed">
                        This website was created with love for animals —
                        to make the bond between humans and dogs even stronger.
                    </p>
                </div>
            </section>

        </div>
    );
}
