
import { useEffect, useState } from "react";
import { getIncidents, updateIncident } from "../services/incidentService";
import type { Incident } from "../types";

function Incidents() {
    const [incidents, setIncidents] = useState<Incident[]>([]);
    const [error, setError] = useState("");
    const [editingIncident, setEditingIncident] = useState<Incident | null>(null);
    const [editError, setEditError] = useState("");
    const [saving, setSaving] = useState(false);

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

    function handleEdit(incident: Incident) {
        setEditingIncident({ ...incident });
        setEditError("");
    }

    function handleChange(
        field: keyof Incident,
        value: string | number
    ) {
        if (!editingIncident) {
            return;
        }

        setEditingIncident({
            ...editingIncident,
            [field]: value
        });
    }

    async function handleSave() {
        if (!editingIncident) {
            return;
        }

        setSaving(true);
        setEditError("");

        try {
            const updatedIncident = await updateIncident(editingIncident);

            setIncidents((currentIncidents) =>
                currentIncidents.map((incident) =>
                    incident.id === updatedIncident.id
                        ? updatedIncident
                        : incident
                )
            );

            setEditingIncident(null);
        } catch (error) {
            setEditError(
                error instanceof Error
                    ? error.message
                    : "Erreur lors de la modification."
            );
        } finally {
            setSaving(false);
        }
    }

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

                    <p>
                        Severity : {incident.severity === "low" ? "Faible" : incident.severity === "medium" ? "Moyenne" : "Élevée"}
                    </p>

                    <p>
                        Statut : {incident.status === "open" ? "Ouvert" : incident.status === "in_progress" ? "En cours" : incident.status === "resolved" ? "Résolu" : "Fermé"}
                    </p>

                    <p>Equipment ID : {incident.equipmentId}</p>

                    <button onClick={() => handleEdit(incident)}>
                        Modifier
                    </button>

                    {editingIncident?.id === incident.id && (
                        <div>
                            <h3>Modifier l'incident</h3>

                            <label>
                                Titre :
                                <input
                                    type="text"
                                    value={editingIncident.title}
                                    onChange={(event) =>
                                        handleChange("title", event.target.value)
                                    }
                                />
                            </label>

                            <label>
                                Sévérité :
                                <select
                                    value={editingIncident.severity}
                                    onChange={(event) =>
                                        handleChange("severity", event.target.value)
                                    }
                                >
                                    <option value="low">Faible</option>
                                    <option value="medium">Moyenne</option>
                                    <option value="high">Élevée</option>
                                </select>
                            </label>

                            <label>
                                Statut :
                                <select
                                    value={editingIncident.status}
                                    onChange={(event) =>
                                        handleChange("status", event.target.value)
                                    }
                                >
                                    <option value="open">Ouvert</option>
                                    <option value="in_progress">En cours</option>
                                    <option value="resolved">Résolu</option>
                                    <option value="closed">Fermé</option>
                                </select>
                            </label>

                            <label>
                                Equipment ID :
                                <input
                                    type="number"
                                    min="1"
                                    value={editingIncident.equipmentId}
                                    onChange={(event) =>
                                        handleChange("equipmentId", Number(event.target.value))
                                    }
                                />
                            </label>

                            {editError && <p>{editError}</p>}

                            <button onClick={handleSave} disabled={saving}>
                                {saving ? "Enregistrement..." : "Enregistrer"}
                            </button>

                            <button
                                onClick={() => setEditingIncident(null)}
                                disabled={saving}
                            >
                                Annuler
                            </button>
                        </div>
                    )}
                </div>
            ))}
        </main>
    );
}

export default Incidents;
