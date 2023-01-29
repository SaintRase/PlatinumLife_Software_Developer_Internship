SELECT a.employee_name as Employee, b.employee_name as Manager
FROM employee_table a
LEFT JOIN employee_table b ON a.manager_id = b.id;
