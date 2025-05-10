-- SELECT COUNT(*) AS total_managers, SUM(salary) AS total_salary FROM Staff WHERE oPosition = 'Manager';

-- SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary, AVG(salary) AS avg_salary FROM Staff;

-- SELECT branchNo, COUNT(*) AS staff_count, SUM(salary) AS total_salary FROM Staff GROUP BY branchNo HAVING COUNT(*) > 1;

-- SELECT city FROM Branch UNION SELECT city FROM PropertyForRent ORDER BY city;

-- SELECT DISTINCT b.city FROM Branch b WHERE EXISTS ( SELECT 1 FROM PropertyForRent p WHERE p.city = b.city ) ORDER BY b.city;

-- SELECT COUNT(*) AS total_assistants, SUM(salary) AS total_salary, AVG(salary) AS average_salary FROM Staff WHERE oPosition = 'Assistant';

SELECT 
    b.branchNo,
    b.city AS branchCity,
    s.staffNo AS memberStaffNo,
    s.fName || ' ' || s.lName AS memberName,
    p.staffNo AS managerStaffNo,
    mgr.fName || ' ' || mgr.lName AS managerName,
    p.propertyNo,
    p.street AS propertyAddress,
    p.city AS propertyCity,
    p.rent
FROM 
    Branch b
JOIN 
    Staff s ON b.branchNo = s.branchNo
LEFT JOIN 
    PropertyForRent p ON s.staffNo = p.staffNo
LEFT JOIN 
    Staff mgr ON p.staffNo = mgr.staffNo
ORDER BY 
    b.branchNo, s.staffNo, p.propertyNo;