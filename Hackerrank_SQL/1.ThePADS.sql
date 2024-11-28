/*
Enter your query here.
*/
CREATE TEMPORARY TABLE map(
    occ_count INT,
    occupation VARCHAR(50)
);

INSERT INTO map(occ_count, occupation)
SELECT COUNT(1) as t, oc.occupation
FROM OCCUPATIONS oc
GROUP BY oc.occupation
ORDER BY t ASC, oc.occupation;


SELECT 
    CONCAT(oc.name, '(', LEFT(oc.occupation, 1), ')') AS n
FROM OCCUPATIONS oc
ORDER BY n;

SELECT CONCAT('There are a total of ', map.occ_count , ' ', LOWER(map.occupation), 's.') FROM map;