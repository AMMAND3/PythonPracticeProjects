-- Write an SQL query to report the first name, last name, city, and state of each person in the Person table.
-- If the address of a personId is not present in the Address table, report null instead.
-- Return the result table in any order.

SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT OUTER JOIN Address a
ON p.personId = a.personId;

-- Write an SQL query to report the second highest salary from the Employee table. If there is no second highest salary, the query should report null.

SELECT 
    MAX(salary) AS SecondHighestSalary
FROM 
    Employee
WHERE 
    salary < (SELECT MAX(salary) FROM Employee);

-- Write an SQL query to report the nth highest salary from the Employee table. If there is no nth highest salary, the query should report null.

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET n = N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct e.Salary
      from Employee e
      order by e.Salary desc
      limit n, 1
  );
END

-- Leetcode 178
-- Write an SQL query to rank the scores. The ranking should be calculated according to the following rules:

-- The scores should be ranked from the highest to the lowest.
-- If there is a tie between two scores, both should have the same ranking.
-- After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
-- Return the result table ordered by score in descending order.

SELECT s.score, DENSE_RANK() OVER (ORDER BY s.score DESC) AS "rank"
FROM Scores s
ORDER BY s.score DESC;

-- Write an SQL query to find all numbers that appear at least three times consecutively.

-- Return the result table in any order.


SELECT DISTINCT n1.num AS ConsecutiveNums
FROM Logs n1
JOIN Logs n2 ON n1.id + 1 = n2.id AND n1.num = n2.num
JOIN Logs n3 ON n1.id + 2 = n3.id AND n1.num = n3.num;


-- Leetcode 181
-- Write an SQL query to find the employees who earn more than their managers.

-- Return the result table in any order.

SELECT e.name AS "Employee"
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;


-- Write an SQL query to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

-- Return the result table in any order.

SELECT p.email
FROM Person p
GROUP BY email
HAVING COUNT(*) > 1;

-- Write an SQL query to report all customers who never order anything.

-- Return the result table in any order.

SELECT c.name AS "Customers"
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL;
