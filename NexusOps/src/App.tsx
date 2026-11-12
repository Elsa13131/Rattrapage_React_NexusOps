
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Header from './components/Header';

import Dashboard from './pages/Dashboard';
import Equipments from './pages/Equipments';
import Incidents from './pages/Incidents';
import Users from './pages/Users';
import Suggest from './pages/Suggest';
import Login from './pages/Login';

function App() {
  return (
    <BrowserRouter>
      <Header />

      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/login" element={<Login />} />
        <Route path="/equipments" element={<Equipments />} />
        <Route path="/incidents" element={<Incidents />} />
        <Route path="/users" element={<Users />} />
        <Route path="/suggest" element={<Suggest />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
