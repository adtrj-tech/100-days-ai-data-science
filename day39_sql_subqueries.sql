-- Day 39: SQL Subqueries


-- 1. Find employees earning more than the average salary
SELECT *
FROM placement_sql.employees
WHERE salary > (
    SELECT AVG(salary)
    FROM placement_sql.employees
);


-- 2. Find the employee with the highest salary
SELECT *
FROM placement_sql.employees
WHERE salary = (
    SELECT MAX(salary)
    FROM placement_sql.employees
);


-- 3. Find employees earning the lowest salary
SELECT *
FROM placement_sql.employees
WHERE salary = (
    SELECT MIN(salary)
    FROM placement_sql.employees
);


-- 4. Find employees working in the department
-- that has the highest average salary
SELECT *
FROM placement_sql.employees
WHERE department = (
    SELECT department
    FROM placement_sql.employees
    GROUP BY department
    ORDER BY AVG(salary) DESC
    LIMIT 1
);


-- 5. Find employees earning more than
-- the average salary of the IT department
SELECT *
FROM placement_sql.employees
WHERE salary > (
    SELECT AVG(salary)
    FROM placement_sql.employees
    WHERE department = 'IT'
);


-- 6. Find employees who work in departments
-- having more than one employee
SELECT *
FROM placement_sql.employees
WHERE department IN (
    SELECT department
    FROM placement_sql.employees
    GROUP BY department
    HAVING COUNT(*) > 1
);


-- 7. Find the second-highest salary
SELECT MAX(salary) AS second_highest_salary
FROM placement_sql.employees
WHERE salary < (
    SELECT MAX(salary)
    FROM placement_sql.employees
);