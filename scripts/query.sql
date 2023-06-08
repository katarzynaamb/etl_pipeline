SELECT * from users;

SELECT * from global_statistics;

SELECT u.*, c.id AS compound_id, c.name, c.structure
FROM users u
JOIN compounds c ON c.id = ANY(u.most_common_compounds_ids)
ORDER BY u.id, c.id;