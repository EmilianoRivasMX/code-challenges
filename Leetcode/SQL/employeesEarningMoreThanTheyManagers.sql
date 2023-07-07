-- Write an SQL query to find the employees who earn more than their managers.
-- Return the result table in any order.

# MYSQL, SQL Server and Oracle
SELECT E.name AS Employee FROM Employee E
WHERE E.salary > (SELECT salary FROM Employee WHERE id = e.managerId);

SELECT E1.name AS Employee FROM Employee E1, Employee E2
WHERE E1.managerId = E2.id AND E1.salary > E2.salary;

SELECT E1.name AS Employee FROM Employee E1
JOIN Employee E2 ON E1.managerId = E2.id
WHERE E1.salary > E2.salary;