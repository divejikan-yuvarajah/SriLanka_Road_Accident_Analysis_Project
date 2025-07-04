
-- Total Accidents per District
SELECT district, COUNT(*) AS total
FROM Accidents
GROUP BY district
ORDER BY total DESC;

-- Accidents by Hour of Day
SELECT strftime('%H', time) AS hour, COUNT(*) AS total
FROM Accidents
GROUP BY hour
ORDER BY total DESC;

-- Most Dangerous Roads
SELECT road, COUNT(*) AS total
FROM Accidents
GROUP BY road
ORDER BY total DESC
LIMIT 10;
