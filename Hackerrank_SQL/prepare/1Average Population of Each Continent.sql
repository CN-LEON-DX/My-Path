SELECT co.continent, FLOOR(AVG(ct.population))
FROM CITY as ct
INNER JOIN COUNTRY as co ON co.code = ct.countrycode
GROUP BY co.continent
