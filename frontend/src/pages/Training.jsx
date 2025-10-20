const trainers = [
    {
        id: 1,
        name: "Alex Greff",
        role: "Dog Trainer",
        photo: "/assets/trainer1.jpg",
        description: "10 years of experience training dogs and cats."
    },
    {
        id: 2,
        name: "Mary Beth",
        role: "Animal Behaviorist",
        photo: "/assets/trainer2.jpg",
        description: "Specializes in animal behavior correction and training."
    },
    {
        id: 3,
        name: "John Smith",
        role: "Dog Trainer",
        photo: "/assets/trainer3.jpg",
        description: "Expert in obedience training and agility."
    },
];

function TrainerCard({ trainer }) {
    return (
        <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition p-4 flex flex-col items-center text-center">
            <img
                src={trainer.photo}
                alt={trainer.name}
                className="w-32 h-32 rounded-full object-cover mb-4"
            />
            <h3 className="text-xl font-semibold mb-1">{trainer.name}</h3>
            <p className="text-orange-500 font-medium mb-2">{trainer.role}</p>
            <p className="text-gray-600 text-sm">{trainer.description}</p>
        </div>
    );
}


export default function Training() {
    return (
        <div className="max-w-6xl mx-auto px-4 py-8">
            <h2 className="text-3xl font-bold mb-6 text-center text-gray-800">Our Trainers & Experts</h2>

            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                {trainers.map((trainer) => (
                    <TrainerCard key={trainer.id} trainer={trainer} />
                    ))}
            </div>
        </div>
    );
}