import type { Incident } from "../types";


export async function getIncidents(): Promise<Incident[]> {
    const response = await fetch("http://localhost:3001/incidents");


    if (!response.ok) {
        throw new Error("Erreur lors de la récupération des incidents");
    }

     return response.json();
    }

export async function createIncident(incident: {
    title: string;
    severity: 'low' | 'medium' | 'high';
    equipmentId: number;
}) {
    const response = await fetch("http://localhost:3001/incidents", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            ...incident,
            status: "open",
        }),
    });

    if (!response.ok) {
        throw new Error("Erreur lors de la création de l'incident");
    }

    return response.json();
}