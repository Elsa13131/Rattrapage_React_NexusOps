# NexusOps — Justification des choix SQL

## 1. Gestion des rôles et des permissions (DCL)

Plusieurs rôles PostgreSQL ont été créés afin de séparer les droits selon les responsabilités des utilisateurs.

- **nexusops_lecture** : permet de consulter les équipements et les incidents.
- **nexusops_operateur** : hérite des droits de lecture et peut ajouter ou modifier des incidents, mais ne peut pas les supprimer.
- **nexusops_admin** : dispose de droits étendus sur les tables et les séquences.
- **nexusops_audit** : permet de consulter les informations nécessaires aux audits.

Les commandes `CREATE ROLE`, `GRANT` et `REVOKE` permettent de gérer ces autorisations.

Les rôles ont été créés avec `NOLOGIN` afin de les utiliser comme groupes de permissions.

## 2. Création des vues SQL

Deux vues ont été créées pour simplifier l'accès aux données.

- **v_operator_incidents** : affiche les incidents ainsi que les informations des équipements associés. Elle utilise une jointure `INNER JOIN` entre les tables `incidents` et `equipments`.
- **v_audit_incidents** : affiche l'historique des opérations effectuées sur les incidents, avec l'ancien et le nouveau statut ainsi que la date de modification.

Ces vues permettent de présenter uniquement les informations utiles à chaque profil.

## 3. Index et performances

Deux index ont été créés :

- **idx_incidents_status** : facilite les recherches d'incidents selon leur statut.
- **idx_incidents_equipment_id** : facilite les recherches et les jointures à partir de l'identifiant d'un équipement.

Ces index ont été choisis en fonction des recherches et des relations utilisées dans l'application NexusOps.

## 4. Fonction SQL

La fonction `fn_count_open_incidents()` permet de compter automatiquement le nombre d'incidents dont le statut est `open`.

Elle utilise `COUNT(*)` pour retourner un nombre entier.

Cette fonction peut notamment servir à alimenter une statistique du tableau de bord.

## 5. Audit et trigger

Une table `incident_audit` a été créée pour conserver l'historique des opérations effectuées sur les incidents.

La fonction `fn_log_incident_changes()` enregistre automatiquement les opérations suivantes :

- `INSERT` : création d'un incident.
- `UPDATE` : modification d'un incident, avec conservation de l'ancien et du nouveau statut.
- `DELETE` : suppression d'un incident, avec conservation de son ancien statut.

Le trigger `trg_incidents_audit` appelle automatiquement cette fonction après chaque opération sur la table `inc