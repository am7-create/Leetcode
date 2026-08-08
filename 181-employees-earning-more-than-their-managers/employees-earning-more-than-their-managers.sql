# Write your MySQL query statement below
SELECT e.name AS Employee
From Employee AS e
Join Employee AS m
    on e.managerId = m.Id
WHERE e.salary > m.salary;