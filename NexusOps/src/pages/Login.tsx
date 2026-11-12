
import { useState } from 'react';
import { login } from '../services/authService';

function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
        event.preventDefault();

        setError('');
        setLoading(true);

        try {
            const data = await login(email, password);

            localStorage.setItem('token', data.access_token);

            window.location.href = '/';
        } catch {
            setError('Email ou mot de passe incorrect');
        } finally {
            setLoading(false);
        }
    }

    return (
        <div>
            <h1>Connexion à NexusOps</h1>

            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="email">Adresse e-mail</label>
                    <input
                        id="email"
                        type="email"
                        value={email}
                        onChange={(event) => setEmail(event.target.value)}
                        required
                    />
                </div>

                <div>
                    <label htmlFor="password">Mot de passe</label>
                    <input
                        id="password"
                        type="password"
                        value={password}
                        onChange={(event) => setPassword(event.target.value)}
                        required
                    />
                </div>

                {error && <p>{error}</p>}

                <button type="submit" disabled={loading}>
                    {loading ? 'Connexion...' : 'Se connecter'}
                </button>
            </form>
        </div>
    );
}

export default Login;
