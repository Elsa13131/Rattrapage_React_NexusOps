import { useEffect, useState } from 'react';
import { getUsers } from '../services/userService';
import type { User } from '../types';

function Users() {
  const [users, setUsers] = useState<User[]>([]);
  const [error, setError] = useState('');

  useEffect(() => {
    async function loadUsers() {
      try {
        const data = await getUsers();
        setUsers(data);
      } catch {
        setError('Impossible de récupérer les utilisateurs.');
      }
    }

    loadUsers();
  }, []);

  if (error) {
    return (
      <main>
        <h1>Utilisateurs</h1>
        <p>{error}</p>
      </main>
    );
  }

  return (
    <main>
      <h1>Utilisateurs</h1>

      {users.map((user) => (
        <div key={user.id}>
          <h2>{user.name}</h2>
          <p>Email : {user.email}</p>
          <p>Rôle : {user.role}</p>
        </div>
      ))}
    </main>
  );
}

export default Users;