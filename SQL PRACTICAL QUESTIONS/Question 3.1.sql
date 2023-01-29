SELECT employee_name, Age
FROM employees
WHERE department_id = (SELECT department_id FROM employees ORDER BY Age DESC LIMIT 1)
ORDER BY Age DESC
LIMIT 3,1
