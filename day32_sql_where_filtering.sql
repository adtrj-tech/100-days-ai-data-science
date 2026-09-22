-- Day 32: SQL WHERE & Filtering

-- 1. Employees from IT department
SELECT *
FROM placement_sql.employees
WHERE department = 'IT';


-- 2. Employees earning more than 50000
SELECT *
FROM placement_sql.employees
WHERE salary > 50000;


-- 3. Employees earning exactly 50000
SELECT *
FROM placement_sql.employees
WHERE salary = 50000;


-- 4. Employees not from IT department
SELECT *
FROM placement_sql.employees
WHERE department != 'IT';