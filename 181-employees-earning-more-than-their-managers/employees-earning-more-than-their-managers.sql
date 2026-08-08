# Write your MySQL query statement below
SELECT e.name AS employee
FROM employee e
join employee m
    on e.managerId = m.Id
WHERE e.salary > m.salary;