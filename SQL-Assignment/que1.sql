SELECT p.manufacturer, COUNT(*) AS num_flights
FROM planes p
JOIN flights f ON p.tailnum = f.tailnum
GROUP BY p.manufacturer
ORDER BY num_flights DESC
LIMIT 1;