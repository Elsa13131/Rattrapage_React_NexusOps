
import type { User } from "../types";

export async function getUsers(): Promise<User[]> {
    const response = await fetch("http://127.0.0.1:8000/users");

    if (!response.ok) {
        throw new Error("Erreur lors de la récupération des utilisateurs");
    }

    const data: User[] = await response.json();

    return data;
}
