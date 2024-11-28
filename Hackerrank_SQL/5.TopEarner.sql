SET @max_earning = (SELECT MAX(months * salary)
FROM Employee);

SET @cnt = (SELECT COUNT(1)
FROM Employee as e
WHERE months * salary = @max_earning);

SELECT @max_earning, @cnt