
import type { Incident } from "../types";

const API_URL = "http://127.0.0.1:8000/incidents";

export async function getIncidents(): Promise<Incident[]> {
    const response = await fetch(API_URL);

    if (!response.ok) {
        throw new Error("Erreur lors de la récupération des incidents");
    }

    const data = await response.json();

    return data.map((incident: {
        id: number;
        title: string;
        severity: "low" | "medium" | "high";
        status: "open" | "in_progress" | "resolved" | "closed";
        equipment_id: number;
    }) => ({
        id: incident.id,
        title: incident.title,
        severity: incident.severity,
        status: incident.status,
        equipmentId: incident.equipment_id
    }));
}

export async function createIncident(incident: {
    title: string;
    severity: "low" | "medium" | "high";
    equipmentId: number;
}) {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            title: incident.title,
            severity: incident.severity,
            status: "open",
            equipment_id: incident.equipmentId
        }),
    });

    if (!response.ok) {
        const error = await response.json();
        throw new Error(
            error.detail || "Erreur lors de la création de l'incident"
        );
    }

    const data = await response.json();

    return {
        id: data.id,
        title: data.title,
        severity: data.severity,
        status: data.status,
        equipmentId: data.equipment_id
    } as Incident;
}
