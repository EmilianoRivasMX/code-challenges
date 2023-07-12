-- Find all customers who never order anything.
-- Return the result table in any order.

SELECT name AS Customers
FROM Customers
WHERE id NOT IN (SELECT CustomerId FROM Orders);

