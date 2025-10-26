import center1 from "../assets/centers/center1.jpg";
import center2 from "../assets/centers/center2.jpg";
import center3 from "../assets/centers/center3.jpg";
import center4 from "../assets/centers/center4.jpg";
import center5 from "../assets/centers/center5.jpg";


const adoptionCenters = [
    {
        id: 1,
        name: "Happy Paws Shelter",
        phone: "+373 68 555 21",
        address: "Str. Mihai Viteazul , Chișinău",
        photo: center1,
    },
    {
        id: 2,
        name: "Animal Hope Center",
        phone: "+373 69 888 32",
        address: "Bd. Dacia , Chișinău",
        photo: center2,
    },
    {
        id: 3,
        name: "Safe Home Pets",
        phone: "+373 60 321 90",
        address: "Str. Ștefan cel Mare , Chișinău",
        photo: center3,
    },
    {
        id: 4,
        name: "LoveTail Rescue",
        phone: "+373 78 404 11",
        address: "Str. Independenței , Bălți",
        photo: center4,
    },
    {
        id: 5,
        name: "Paw Friends Foundation",
        phone: "+373 67 700 56",
        address: "Str. București , Chișinău",
        photo: center5,
    },
];



function CenterCard({ center }) {
    return (
        <div className="w-[500px] bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition p-4 flex flex-col items-center text-center">
            <img
                src={center.photo}
                alt={center.name}
                className="w-full h-40 object-cover rounded-md mb-4"
            />
            <h3 className="text-xl font-semibold mb-2 text-gray-800">{center.name}</h3>
            <p className="text-gray-600 text-sm mb-1">
                <strong>Phone:</strong> {center.phone}
            </p>
            <p className="text-gray-600 text-sm">
                <strong>Address:</strong> {center.address}
            </p>
        </div>
    );
}


export default function Adoption() {
    return (
        <div className="max-w-6xl mx-auto px-4 py-8">
            <h2 className="text-3xl font-bold mb-6 text-center text-gray-800">
                Adoption Centers
            </h2>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-8">
                {adoptionCenters.map((center) => (
                    <CenterCard key={center.id} center={center} />
                ))}
            </div>
        </div>
    );
}