
import { useEffect, useState } from "react";
import { getEquipments } from "../services/equipmentService";
import type { Equipment } from "../types";

function Equipments() {
    const [equipments, setEquipments] = useState<Equipment[]>([]);
    const [error, setError] = useState("");

    useEffect(() => {
        async function loadEquipments() {
            try {
                const data = await getEquipments();
                setEquipments(data);
            } catch {
                setError("Impossible de récupérer les équipements.");
            }
        }

        loadEquipments();
    }, []);

    if (error) {
        return (
            <main>
                <h1>Équipements</h1>
                <p>{error}</p>
            </main>
        );
    }

    return (
        <main>
            <h1>Équipements</h1>

            {equipments.map((equipment) => (
                <div key={equipment.id}>
                    <h2>{equipment.name}</h2>
                    <p>Type : {equipment.type}</p>
                    <p>Site : {equipment.site}</p>
                    <p>
                        Statut : {equipment.status === "online" ? "Online" : "Offline"}
                    </p>
                </div>
            ))}
        </main>
    );
}

export default Equipments;
