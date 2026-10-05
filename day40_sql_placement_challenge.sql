-- Day 39: SQL Placement Challenge
-- #100DaysOfAIwithAdhi


-- Q1. Display all employees from the IT department.
SELECT *
FROM placement_sql.employees
WHERE department = 'IT';


-- Q2. Display employees earning more than 55000,
-- sorted from highest salary to lowest.
SELECT *
FROM placement_sql.employees
WHERE salary > 55000
ORDER BY salary DESC;


-- Q3. Find the top 2 highest-paid employees.
SELECT *
FROM placement_sql.employees
ORDER BY salary DESC
LIMIT 2;


-- Q4. Find the total number of employees.
SELECT COUNT(*) AS total_employees
FROM placement_sql.employees;


-- Q5. Find the average salary of all employees.
SELECT AVG(salary) AS average_salary
FROM placement_sql.employees;


-- Q6. Find the number of employees in each department.
SELECT department, COUNT(*) AS employee_count
FROM placement_sql.employees
GROUP BY department;


-- Q7. Find the average salary for each department.
SELECT department, AVG(salary) AS average_salary
FROM placement_sql.employees
GROUP BY department;


-- Q8. Display only departments having more than 1 employee.
SELECT department, COUNT(*) AS employee_count
FROM placement_sql.employees
GROUP BY department
HAVING COUNT(*) > 1;


-- Q9. Display employee name, department, salary,
-- and department location using a JOIN.
SELECT
    e.name,
    e.department,
    e.salary,
    d.location
FROM placement_sql.employees e
INNER JOIN placement_sql.departments d
    ON e.department = d.department;


-- Q10. Display employees earning more than
-- the average salary of all employees.
SELECT *
FROM placement_sql.employees
WHERE salary > (
    SELECT AVG(salary)
    FROM placement_sql.employees
);


-- Q11. Find the employee(s) with the highest salary.
SELECT *
FROM placement_sql.employees
WHERE salary = (
    SELECT MAX(salary)
    FROM placement_sql.employees
);


-- Q12. Find the second-highest salary.
SELECT MAX(salary) AS second_highest_salary
FROM placement_sql.employees
WHERE salary < (
    SELECT MAX(salary)
    FROM placement_sql.employees
);


-- Q13. Find the department with the highest average salary.
SELECT department, AVG(salary) AS average_salary
FROM placement_sql.employees
GROUP BY department
ORDER BY average_salary DESC
LIMIT 1;


-- Q14. Display the top 2 highest-paid employees
-- along with their department location.
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


-- Q15. Find departments whose total salary
-- is greater than 100000.
SELECT department, SUM(salary) AS total_salary
FROM placement_sql.employees
GROUP BY department
HAVING SUM(salary) > 100000;