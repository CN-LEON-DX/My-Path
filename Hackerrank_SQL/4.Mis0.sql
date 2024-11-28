WITH mis as (
    SELECT AVG(
        CAST(REPLACE(CAST(e.salary AS CHAR), '0', '') AS FLOAT)) as mis_salary,
        AVG(e.salary) as org_salary
    FROM EMPLOYEES as e
)
SELECT CEIL(mis.org_salary - mis.mis_salary)
FROM mis
