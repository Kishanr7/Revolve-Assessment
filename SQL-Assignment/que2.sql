SELECT p.manufacturer, 
       SUM(CASE WHEN f.air_time ~ '^[0-9]+$' THEN (f.air_time::integer) ELSE 0 END) AS total_flying_hours
FROM planes p
JOIN flights f ON p.tailnum = f.tailnum
GROUP BY p.manufacturer
ORDER BY total_flying_hours DESC
LIMIT 1;
