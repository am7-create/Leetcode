# Write your MySQL query statement below
SELECT 
     d.name AS Department,
     e.name AS employee,
     e.salary AS Salary
From Employee e
join Department d
    ON e.departmentId = d.Id
WHERE e.salary = (
    select MAX(e2.salary)
    FROM Employee e2
    where e2.departmentId = e.departmentId

);