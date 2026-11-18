
CREATE OR REPLACE FUNCTION fn_count_open_incidents()
RETURNS INTEGER
LANGUAGE SQL
AS $$
    SELECT COUNT(*)::INTEGER
    FROM incidents
    WHERE status = 'open';
$$;




CREATE TABLE IF NOT EXISTS incident_audit (
    id SERIAL PRIMARY KEY,
    incident_id INTEGER,
    action VARCHAR(20) NOT NULL,
    old_status VARCHAR(50),
    new_status VARCHAR(50),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);




CREATE OR REPLACE FUNCTION fn_log_incident_changes()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO incident_audit (
            incident_id,
            action,
            new_status
        )
        VALUES (
            NEW.id,
            'INSERT',
            NEW.status
        );

        RETURN NEW;

    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO incident_audit (
            incident_id,
            action,
            old_status,
            new_status
        )
        VALUES (
            NEW.id,
            'UPDATE',
            OLD.status,
            NEW.status
        );

        RETURN NEW;

    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO incident_audit (
            incident_id,
            action,
            old_status
        )
        VALUES (
            OLD.id,
            'DELETE',
            OLD.status
        );

        RETURN OLD;
    END IF;

    RETURN NULL;
END;
$$;




CREATE TRIGGER trg_incidents_audit
AFTER INSERT OR UPDATE OR DELETE
ON incidents
FOR EACH ROW
EXECUTE FUNCTION fn_log_incident_changes();
