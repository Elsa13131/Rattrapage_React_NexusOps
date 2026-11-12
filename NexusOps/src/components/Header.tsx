
import { NavLink, useNavigate } from "react-router-dom";
import { useState } from "react";

const navClass = ({ isActive }: { isActive: boolean }) =>
  isActive ? "nav-button active" : "nav-button";

export default function Header() {
  const navigate = useNavigate();

  const [isConnected, setIsConnected] = useState(
    !!localStorage.getItem("token")
  );

  function handleLogout() {
    localStorage.removeItem("token");
    setIsConnected(false);
    navigate("/login");
  }

  return (
    <header className="site-header">
      <div>
        <p className="eyebrow">NEXUS OPS</p>
        <h1>NEXUS OPS</h1>
      </div>

      <nav className="nav">
        <NavLink to="/" end className={navClass}>
          DASHBOARD
        </NavLink>

        <NavLink to="/equipments" className={navClass}>
          EQUIPEMENTS
        </NavLink>

        <NavLink to="/incidents" className={navClass}>
          INCIDENTS
        </NavLink>

        <NavLink to="/users" className={navClass}>
          UTILISATEURS
        </NavLink>

        <NavLink to="/suggest" className={navClass}>
          SUGGESTIONS D'INCIDENTS
        </NavLink>

        {isConnected ? (
        <button className="nav-button nav-logout" onClick={handleLogout}>
            DÉCONNEXION
        </button>
        ) : (
          <NavLink to="/login" className={navClass}>
            CONNEXION
          </NavLink>
        )}
      </nav>
    </header>
  );
}
