# Write your MySQL query statement below
SELECT c.name AS customers
FROM customers AS c
LEFT JOIN orders AS o
    on c.id = o.customerId
WHERE o.customerId is NULL;