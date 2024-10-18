-- View the students who need a meeting
CREATE VIEW need_meeting AS
SELECT u.name
FROM users u
JOIN corrections c ON u.id = c.user_id
LEFT JOIN meetings m ON u.id = m.user_id
WHERE c.score < 80
AND (m.last_meeting IS NULL OR m.last_meeting < NOW() - INTERVAL 1 MONTH);
