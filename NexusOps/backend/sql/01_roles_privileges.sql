
CREATE ROLE nexusops_lecture NOLOGIN;

CREATE ROLE nexusops_operateur NOLOGIN;

CREATE ROLE nexusops_admin NOLOGIN;

CREATE ROLE nexusops_audit NOLOGIN;


GRANT USAGE ON SCHEMA public TO
nexusops_lecture,
nexusops_operateur,
nexusops_admin,
nexusops_audit;


GRANT SELECT ON TABLE
public.equipments,
public.incidents
TO nexusops_lecture;


GRANT nexusops_lecture TO nexusops_operateur;


GRANT INSERT, UPDATE ON TABLE
public.incidents
TO nexusops_operateur;

GRANT USAGE, SELECT ON SEQUENCE
public.incidents_id_seq
TO nexusops_operateur;

REVOKE DELETE ON TABLE
public.incidents
FROM nexusops_operateur;


GRANT nexusops_operateur TO nexusops_admin;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public
TO nexusops_admin;

GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public
TO nexusops_admin;


GRANT SELECT ON TABLE
public.equipments,
public.incidents
TO nexusops_audit;
