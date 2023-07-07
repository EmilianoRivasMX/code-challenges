-- Write an SQL query to report all the duplicate emails. 
-- Note that it's guaranteed that the email field is not NULL.

-- Return the result table in any order.

-- MYSQL, SQL Server and Oracle
SELECT Email 
FROM Person 
GROUP BY Email 
HAVING COUNT(Email) > 1;

SELECT Email, count(Email) AS num
FROM Person
GROUP BY Email;
