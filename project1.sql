select * from HRData

-- 1. Employee Analysis
-- a) List all employees along with their positions and salaries.

select EmployeeName, Position, Salary from HRData
-- Explanation: This query fetches the names, positions, and salaries of all employees from the dataset.

-- b) Find the average salary of employees by department.

select Department, avg(Salary) as avgsal
from HRData
group by Department
-- Explanation: The AVG() function calculates the average salary for each department using the GROUP BY clause.

-- c) Retrieve the details of employees whose performance score is 'Exceeds'.

select * from HRData
where PerformanceScore = 'Exceeds'
-- Explanation: This query filters employees with a performance score of 'Exceeds' and returns all their details.


-- 2. Recruitment and Employment
-- a) Count the number of employees recruited from each recruitment source.

select RecruitmentSource, count(*) as Employeecount
from HRData
group by RecruitmentSource
-- Explanation: The query groups employees by recruitment source and counts them.

-- b) List the employees who are currently active.

select EmployeeName, Position, EmploymentStatus
from HRData
where EmploymentStatus = 'Active'
-- Explanation: Filters active employees based on the EmploymentStatus column.

-- c) Identify employees who have terminated and their termination dates.

select EmployeeName, TerminationDate
from HRData
where TerminationDate is not null
-- Explanation: Checks for non-null termination dates to find terminated employees.

-- 3. Demographics and Diversity
-- a) Get the count of employees based on gender.

select Gender, count(*) as employeegender
from HRData
group by Gender
-- Explanation: Groups employees by gender and counts them.

-- b) Find the number of married, single, and divorced employees.

select MaritalStatus, count(*) as count
from HRData
group by MaritalStatus
-- Explanation: Groups employees by their marital status and counts each group.

-- c) Retrieve the youngest and oldest employees in the company.

SELECT top 5 EmployeeName, DateOfBirth
FROM HRData
ORDER BY DateOfBirth ASC  -- Oldest Employee

SELECT top 5 EmployeeName, DateOfBirth
FROM HRData
ORDER BY DateOfBirth DESC  -- Youngest Employee
-- Explanation:
-- The TOP 5 keyword returns the five result.
-- The ordering (ASC or DESC) determines the oldest or youngest.

-- 4. Engagement and Satisfaction
-- a) List employees with an engagement survey score greater than 4.5.

select EmployeeName, EngagementSurvey
from HRData
where EngagementSurvey > 4.5
-- Explanation: Filters employees with high engagement survey scores.

-- b) Find the average employee satisfaction score by department.

SELECT Department, AVG(EmployeeSatisfaction) AS AvgSatisfaction
FROM HRData
GROUP BY Department;
-- Explanation: Computes the average satisfaction score for each department.

-- c) Identify employees with a satisfaction score of less than 3.

SELECT EmployeeName, EmployeeSatisfaction
FROM HRData
WHERE EmployeeSatisfaction < 3;
-- Explanation: Filters employees who have a satisfaction score below 3.

-- 5. Tenure and Experience
-- a) List employees who have been with the company for more than 5 years.

SELECT EmployeeName, HiringDate
FROM HRData
WHERE DATEDIFF(YEAR, CONVERT(DATE, HiringDate, 101), GETDATE()) > 5;
-- CONVERT(DATE, HiringDate, 101) — Converts the date in mm/dd/yyyy format (101 is the style code).

-- b) Find employees who were hired in the same year.

SELECT YEAR(CAST(HiringDate AS DATE)) AS HiringYear,
       STRING_AGG(EmployeeName, ', ') AS Employees
FROM HRData
GROUP BY YEAR(CAST(HiringDate AS DATE))
HAVING COUNT(*) > 1;
-- Explanation: Groups employees by their hiring year and shows names for those hired in the same year.

-- c) Calculate the total number of employees who joined each year.

SELECT YEAR(CAST(HiringDate AS DATE)) AS HiringYear,
       COUNT(*) AS EmployeeCount
FROM HRData
GROUP BY YEAR(CAST(HiringDate AS DATE));
-- Explanation: Groups employees by the year of hiring and counts them.





