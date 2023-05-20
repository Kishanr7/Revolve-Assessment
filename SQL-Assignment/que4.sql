SELECT dest, SUM(CASE WHEN arr_delay ~ '^-?[0-9]+(\.[0-9]+)?$' THEN arr_delay::numeric ELSE 0 END) AS total_delay
FROM flights
GROUP BY dest
ORDER BY total_delay DESC
LIMIT 1;