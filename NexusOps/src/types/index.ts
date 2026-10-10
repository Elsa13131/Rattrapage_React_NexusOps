export interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'operator' | 'viewer';
}

export interface Equipment {
  id: string;
  name: string;
  type: string;
  site: string;
  status: 'online' | 'offline';
}

export interface Incident {
    id: string;
    title: string;
    severity: 'low' | 'medium' | 'high';
    status: 'open' | 'in_progress' | 'resolved' | 'closed';
    equipmentId: number;
}