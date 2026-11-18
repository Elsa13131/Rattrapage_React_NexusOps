
CREATE INDEX IF NOT EXISTS idx_incidents_status
ON incidents(status);


CREATE INDEX IF NOT EXISTS idx_incidents_equipment_id
ON incidents(equipment_id);
