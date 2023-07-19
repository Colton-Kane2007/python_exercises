-- 1. Using the example from the lesson, create a temporary table called employees_with_departments 
-- that contains first_name, last_name, and dept_name for employees currently with that department.
-- Be absolutely sure to create this table on your own database. 
-- If you see "Access denied for user ...", it means that the query was attempting to write a new table to a database that you can only read.

USE robinson_2285;
CREATE TEMPORARY TABLE employees_with_departments 
(first_name VARCHAR(25) NOT NULL,
last_name VARCHAR(25) NOT NULL,
dept_name VARCHAR(25) NOT NULL);

SELECT * FROM employees_with_departments;

-- Add a column named full_name to this table. It should be a VARCHAR whose length is the sum of the lengths 
-- of the first name and last name columns.

ALTER TABLE employees_with_departments
MODIFY full_name VARCHAR(50);


-- Remove the first_name and last_name columns from the table.

ALTER TABLE employees_with_departments 
DROP first_name;
ALTER TABLE employees_with_departments 
DROP last_name;

-- What is another way you could have ended up with this same table?

-- CREATE TEMPORARY TABLE employees_with_departments 
-- (full_name VARCHAR(50) NOT NULL,
-- dept_name VARCHAR(25) NOT NULL);

-- 2. Create a temporary table based on the payment table from the sakila database.

CREATE TEMPORARY TABLE sakila_payments AS
(SELECT * FROM sakila.payment);

SELECT * FROM sakila_payments;

-- Write the SQL necessary to transform the amount column such that it is stored as 
-- an integer representing the number of cents of the payment. For example, 1.99 should become 199.


DESCRIBE sakila_payments;

ALTER TABLE sakila_payments
MODIFY amount DECIMAL(10,2);
UPDATE sakila_payments
SET amount = amount * 100;
ALTER TABLE sakila_payments
MODIFY amount INT UNSIGNED;

-- 3. Go back to the employees database. Find out how the current average pay in each department 
-- compares to the overall current pay for everyone at the company. 
-- For this comparison, you will calculate the z-score for each salary. 
-- In terms of salary, what is the best department right now to work for? The worst?
USE employees;

SELECT dept_name,
AVG(salary)
FROM departments d
JOIN dept_emp de USING(dept_no)
JOIN salaries s USING(emp_no)
WHERE de.to_date> NOW()
AND s.to_date> NOW()
GROUP BY dept_name;

USE robinson_2285;
CREATE TEMPORARY TABLE dept_avgs (
SELECT dept_name,
AVG(salary)
FROM employees.departments d
JOIN dept_emp de USING(dept_no)
JOIN salaries s USING(emp_no)
WHERE de.to_date> NOW()
AND s.to_date> NOW()
GROUP BY dept_name);








