-- Day 31: SQL SELECT Statements

USE placement_sql;

-- 1. Display all columns and rows
SELECT *
FROM employees;


-- 2. Display specific columns
SELECT name, department
FROM employees;


-- 3. Display employee names and salaries
SELECT name, salary
FROM employees;


-- 4. Display unique departments
SELECT DISTINCT department
FROM employees;


-- 5. Rename columns using AS
SELECT
    name AS employee_name,
    salary AS monthly_salary
FROM employees;


-- 6. Select multiple columns
SELECT
    id,
    name,
    department,
    salary
FROM employees;


USE placement_sql;

DESCRIBE employees;