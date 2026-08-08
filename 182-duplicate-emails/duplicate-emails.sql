# Write your MySQL query statement below
SELECT email
FROM person
group by email
HAVING COUNT(email) > 1;
