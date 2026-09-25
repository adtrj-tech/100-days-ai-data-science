-- Day 34: SQL Aggregate Functions


-- 1. Count the total number of employees
SELECT COUNT(*) AS total_employees
FROM placement_sql.employees;


-- 2. Find the total salary of all employees
SELECT SUM(salary) AS total_salary
FROM placement_sql.employees;


-- 3. Find the average salary
SELECT AVG(salary) AS average_salary
FROM placement_sql.employees;


-- 4. Find the highest salary
SELECT MAX(salary) AS highest_salary
FROM placement_sql.employees;


-- 5. Find the lowest salary
SELECT MIN(salary) AS lowest_salary
FROM placement_sql.employees;