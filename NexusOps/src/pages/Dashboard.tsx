import { useEffect, useState } from "react";
import { getEquipments } from "../services/equipmentService";
import { getIncidents } from "../services/incidentService";
import { getUsers } from "../services/userService";
import type { Equipment, Incident, User } from "../types";

function Dashboard() {
    const [equipments, setEquipments] = useState<Equipment[]>([]);
    const [incidents, setIncidents] = useState<Incident[]>([]);
    const [users, setUsers] = useState<User[]>([]);
    const [error, setError] = useState("");

    useEffect(() => {
        async function loadDashboard() {
            try {
                setError("");

                const equipmentsData = await getEquipments();
                const incidentsData = await getIncidents();
                const usersData = await getUsers();

                setEquipments(equipmentsData);
                setIncidents(incidentsData);
                setUsers(usersData);
            } catch (error) {
                setError("Impossible de charger les données du tableau de bord.");
            }
        }

        loadDashboard();
    }, []);

    const openIncidents = incidents.filter(
        (incident) => incident.status === "open"
    ).length;

    if (error) {
        return <p>{error}</p>;
    }

    return (
        <main>
            <h1>Tableau de bord</h1>

            <div>
                <div>
                    <h2>Équipements</h2>
                    <p>{equipments.length}</p>
                </div>

                <div>
                    <h2>Incidents ouverts</h2>
                    <p>{openIncidents}</p>
                </div>

                <div>
                    <h2>Utilisateurs</h2>
                    <p>{users.length}</p>
                </div>
            </div>
        </main>
    );
}

export default Dashboard;