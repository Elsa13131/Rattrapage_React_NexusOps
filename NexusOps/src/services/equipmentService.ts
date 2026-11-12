
import type { Equipment } from "../types";

export async function getEquipments(): Promise<Equipment[]> {
    const token = localStorage.getItem("token");

    const response = await fetch("http://localhost:8000/equipments", {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    if (!response.ok) {
        throw new Error("Erreur lors de la récupération des équipements");
    }

    const data = await response.json();

    return data;
}
