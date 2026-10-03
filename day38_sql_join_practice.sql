-- Day 38: SQL JOIN Practice


-- 1. Display employee name, department, salary, and location
SELECT
    e.name,
    e.department,
    e.salary,
    d.location
FROM placement_sql.employees e
INNER JOIN placement_sql.departments d
    ON e.department = d.department;


-- 2. Display employees working in Kochi
SELECT
    e.name,
    e.department,
    e.salary,
    d.location
FROM placement_sql.employees e
INNER JOIN placement_sql.departments d
    ON e.department = d.department
WHERE d.location = 'Kochi';


-- 3. Display employees earning more than 50000 with their location
SELECT
    e.name,
    e.department,
    e.salary,
    d.location
FROM placement_sql.employees e
INNER JOIN placement_sql.departments d
    ON e.department = d.department
WHERE e.salary > 50000;


-- 4. Display employees sorted by salary from highest to lowest
SELECT
    e.name,
    e.department,
    e.salary,
    d.location
FROM placement_sql.employees e
INNER JOIN placement_sql.departments d
    ON e.department = d.department
ORDER BY e.salary DESC;


-- 5. Find the average salary for each department
SELECT
    e.department,
    d.location,
    AVG(e.salary) AS average_salary
FROM placement_sql.employees e
INNER JOIN placement_sql.departments d
    ON e.department = d.department
GROUP BY e.department, d.location;


-- 6. Find the total salary for each department
SELECT
    e.department,
    d.location,
    SUM(e.salary) AS total_salary
FROM placement_sql.employees e
INNER JOIN placement_sql.departments d
    ON e.department = d.department
GROUP BY e.department, d.location;


-- 7. Find departments with more than one employee
SELECT
    e.department,
    d.location,
    COUNT(*) AS employee_count
FROM placement_sql.employees e
INNER JOIN placement_sql.departments d
    ON e.department = d.department
GROUP BY e.department, d.location
HAVING COUNT(*) > 1;


-- 8. Display the top 2 highest-paid employees with their location
SELECT
    e.name,
    e.department,
    e.salary,
    d.location
FROM placement_sql.employees e
INNER JOIN placement_sql.departments d
    ON e.department = d.department
ORDER BY e.salary DESC
LIMIT 2;