-- Day 36: SQL Practice Problems


-- 1. Display all employees from the IT department
SELECT *
FROM placement_sql.employees
WHERE department = 'IT';


-- 2. Display employees earning more than 50000
SELECT *
FROM placement_sql.employees
WHERE salary > 50000;


-- 3. Display all employees sorted by salary from highest to lowest
SELECT *
FROM placement_sql.employees
ORDER BY salary DESC;


-- 4. Display the top 2 highest-paid employees
SELECT *
FROM placement_sql.employees
ORDER BY salary DESC
LIMIT 2;


-- 5. Find the average salary of all employees
SELECT AVG(salary) AS average_salary
FROM placement_sql.employees;


-- 6. Count the number of employees in each department
SELECT department, COUNT(*) AS employee_count
FROM placement_sql.employees
GROUP BY department;


-- 7. Find the average salary of each department
SELECT department, AVG(salary) AS average_salary
FROM placement_sql.employees
GROUP BY department;


-- 8. Find departments with an average salary greater than 50000
SELECT department, AVG(salary) AS average_salary
FROM placement_sql.employees
GROUP BY department
HAVING AVG(salary) > 50000;


-- 9. Find the highest salary in each department
SELECT department, MAX(salary) AS highest_salary
FROM placement_sql.employees
GROUP BY department;


-- 10. Find the total salary paid by each department
SELECT department, SUM(salary) AS total_salary
FROM placement_sql.employees
GROUP BY department;