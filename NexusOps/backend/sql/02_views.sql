
CREATE OR REPLACE VIEW v_operator_incidents AS
SELECT
    i.id AS incident_id,
    i.title,
    i.severity,
    i.status,
    e.name AS equipment_name,
    e.status AS equipment_status
FROM incidents i
INNER JOIN equipments e
    ON i.equipment_id = e.id;


GRANT SELECT ON v_operator_incidents
TO nexusops_operateur;
