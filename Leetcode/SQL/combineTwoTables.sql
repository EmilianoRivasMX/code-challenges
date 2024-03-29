-- Write an SQL query to report the first name, last name, city, and state of each person in the Person table. 
-- If the address of a personId is not present in the Address table, report null instead.
-- Return the result table in any order.

# MYSQL
SELECT p.firstName, p.lastName, a.city, a.state 
FROM Person p LEFT JOIN Address a 
ON p.personId = a.personId;

SELECT p.firstName, p.lastName, a.city, a.state 
FROM Person p LEFT JOIN Address a 
USING (personId);

# SQL SERVER
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p LEFT JOIN Address a
ON p.personId = a.personId;

# ORACLE
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p, Address a
WHERE p.personId = a.personId(+);