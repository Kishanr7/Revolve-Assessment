SELECT f.tailnum, 
    SUM(CASE WHEN f.air_time ~ '^[0-9]+$' THEN (f.air_time::integer) ELSE 0 END) AS total_flying_hours
FROM flights f
GROUP BY f.tailnum
ORDER BY total_flying_hours DESC
LIMIT 1;