-- Day 33: SQL ORDER BY & LIMIT


-- 1. Sort employees by salary in ascending order
SELECT *
FROM placement_sql.employees
ORDER BY salary ASC;


-- 2. Sort employees by salary in descending order
SELECT *
FROM placement_sql.employees
ORDER BY salary DESC;


-- 3. Display the employee with the highest salary
SELECT *
FROM placement_sql.employees
ORDER BY salary DESC
LIMIT 1;


-- 4. Display the employee with the lowest salary
SELECT *
FROM placement_sql.employees
ORDER BY salary ASC
LIMIT 1;


-- 5. Display the top 3 highest-paid employees
SELECT *
FROM placement_sql.employees
ORDER BY salary DESC
LIMIT 3;