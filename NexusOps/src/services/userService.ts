export async function getUsers() {
    const response = await fetch("http://localhost:3001/users");

    if (!response.ok) {
        throw new Error("Erreur lors de la récupération des utilisateurs");
    }

    const data = await response.json();

    return data;
}