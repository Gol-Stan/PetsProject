import { NavLink} from "react-router-dom";
import {Component} from "react";

export default function Navbar() {
    const links = [
        {path: "/", label: "Home"},
        {path: "/mypets", label: "MyPets"},
        {path: "/breeds", label: "Breeds"},
        {path: "/adoption", label: "Adoption"},
        {path: "/training", label: "Training"},
    ];

    return (
        <nav className="bg-blue-900 text-white py-4">
            <div className="max-w-6xl mx-auto flex justify-between items-center px-4">
                <h1 className="text-2xl font-bold">PetWorld</h1>
                <div className="flex gap-6">
                    {links.map(({path, label}) => (
                        <NavLink
                            key={path}
                            to={path}
                            className={({isActive}) =>
                                isActive
                                    ? "font-semibold underline"
                                    : "hover:underline text-gray-200"
                            }
                        >
                            {label}
                        </NavLink>
                    ))}
                </div>
            </div>
        </nav>
    );
}