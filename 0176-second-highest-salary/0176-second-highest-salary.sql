# Write your MySQL query statement below
SELECT Max(salary) AS SecondHighestSalary
FROM employee
WHERE salary < (SELECT Max(salary) From Employee);