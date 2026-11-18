
CREATE OR REPLACE VIEW v_audit_incidents AS
SELECT
    a.id AS audit_id,
    a.incident_id,
    a.action,
    a.old_status,
    a.new_status,
    a.changed_at
FROM incident_audit a;


GRANT SELECT ON v_audit_incidents
TO nexusops_audit;
