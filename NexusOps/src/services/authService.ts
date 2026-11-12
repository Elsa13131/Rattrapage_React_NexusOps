
export interface LoginResponse {
    access_token: string;
    token_type: string;
    user: {
        id: number;
        name: string;
        email: string;
        role: string;
    };
}

export async function login(
    email: string,
    password: string
): Promise<LoginResponse> {
    const response = await fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email,
            password: password
        })
    });

    if (!response.ok) {
        throw new Error("Email ou mot de passe incorrect");
    }

    const data: LoginResponse = await response.json();

    return data;
}
