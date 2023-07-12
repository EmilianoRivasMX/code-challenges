-- Find the second highest salary from the Employee table. 
-- If there is no second highest salary, return null

SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee)
