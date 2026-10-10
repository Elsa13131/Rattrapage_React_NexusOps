import type { Equipment } from "../types";

export async function getEquipments(): Promise<Equipment[]> {
    const response = await fetch("http://localhost:3001/equipments");

    if (!response.ok) {
        throw new Error("Erreur lors de la récupération des équipements");
    }

    const data = await response.json();

    return data;
}