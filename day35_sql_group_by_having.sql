-- Day 35: SQL GROUP BY & HAVING


-- 1. Count employees in each department
SELECT department, COUNT(*) AS employee_count
FROM placement_sql.employees
GROUP BY department;


-- 2. Find the total salary for each department
SELECT department, SUM(salary) AS total_salary
FROM placement_sql.employees
GROUP BY department;


-- 3. Find the average salary for each department
SELECT department, AVG(salary) AS average_salary
FROM placement_sql.employees
GROUP BY department;


-- 4. Find the highest salary in each department
SELECT department, MAX(salary) AS highest_salary
FROM placement_sql.employees
GROUP BY department;


-- 5. Show departments having more than 1 employee
SELECT department, COUNT(*) AS employee_count
FROM placement_sql.employees
GROUP BY department
HAVING COUNT(*) > 1;