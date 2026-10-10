
import { useEffect, useState } from "react";
import { getIncidents } from "../services/incidentService";
import type { Incident } from "../types";

function Incidents() {
    const [incidents, setIncidents] = useState<Incident[]>([]);
    const [error, setError] = useState("");

    useEffect(() => {
        async function loadIncidents() {
            try {
                const data = await getIncidents();
                setIncidents(data);
            } catch {
                setError("Impossible de récupérer les incidents.");
            }
        }

        loadIncidents();
    }, []);

    if (error) {
        return (
            <main>
                <h1>Incidents</h1>
                <p>{error}</p>
            </main>
        );
    }

    return (
        <main>
            <h1>Incidents</h1>

            {incidents.map((incident) => (
                <div key={incident.id}>
                    <h2>{incident.title}</h2>
                    <p>Severity : {incident.severity === "low" ? "Faible" : incident.severity === "medium" ? "Moyenne" : "Élevée"}</p>
                    <p>
                        Statut : {incident.status === "open" ? "Ouvert" : incident.status === "in_progress" ? "En cours" : incident.status === "resolved" ? "Résolu" : "Fermé"}
                    </p>
                    <p>Equipment ID : {incident.equipmentId}</p>
                </div>
            ))}
        </main>
    );
}

export default Incidents;
