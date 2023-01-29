SELECT client_name, client_gender, client_age, department, client_occupation
FROM Client_Info
JOIN Company
ON Client_Info.client_id = Company.client_id
WHERE department IS NOT NULL
ORDER BY client_id;