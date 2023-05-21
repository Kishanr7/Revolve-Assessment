SELECT Airports."AIRPORT", COUNT(*) AS FlightsCount
FROM Flights
JOIN Airports ON Flights.origin = Airports."IATA_CODE"
WHERE EXTRACT(DOW FROM DATE(Flights.year || '-' || Flights.month || '-' || Flights.day)) IN (0, 6)
GROUP BY Flights.origin, Airports."AIRPORT"
ORDER BY FlightsCount DESC
LIMIT 1;
