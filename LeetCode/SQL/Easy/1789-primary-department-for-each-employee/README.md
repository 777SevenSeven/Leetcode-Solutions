# 1789 - Primary Department for Each Employee

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Advanced Select and Joins
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/primary-department-for-each-employee](https://leetcode.com/problems/primary-department-for-each-employee)

## Problem Statement

Table: `Employee`

```text
+---------------+---------+
| Column Name   |  Type   |
+---------------+---------+
| employee_id   | int     |
| department_id | int     |
| primary_flag  | varchar |
+---------------+---------+
(employee_id, department_id) is the primary key (combination of columns with unique values) for this table.
employee_id is the id of the employee.
department_id is the id of the department to which the employee belongs.
primary_flag is an ENUM (category) of type (&#39;Y&#39;, &#39;N&#39;). If the flag is &#39;Y&#39;, the department is the primary department for the employee. If the flag is &#39;N&#39;, the department is not the primary.
```

 

Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is `&#39;N&#39;`.

Write a solution to report all the employees with their primary department. For employees who belong to one department, report their only department.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:

```text
Input: 
Employee table:
+-------------+---------------+--------------+
| employee_id | department_id | primary_flag |
+-------------+---------------+--------------+
| 1           | 1             | N            |
| 2           | 1             | Y            |
| 2           | 2             | N            |
| 3           | 3             | N            |
| 4           | 2             | N            |
| 4           | 3             | Y            |
| 4           | 4             | N            |
+-------------+---------------+--------------+
Output: 
+-------------+---------------+
| employee_id | department_id |
+-------------+---------------+
| 1           | 1             |
| 2           | 1             |
| 3           | 3             |
| 4           | 3             |
+-------------+---------------+
Explanation: 
- The Primary department for employee 1 is 1.
- The Primary department for employee 2 is 1.
- The Primary department for employee 3 is 3.
- The Primary department for employee 4 is 3.
```

## Approach & Key Insights

Retrieve records where `primary_flag = "Y"` or employee belongs to only a single department (`HAVING COUNT(*) = 1`).

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`1789-primary-department-for-each-employee.sql`](./1789-primary-department-for-each-employee.sql).

```sql
# Write your MySQL query statement below
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'

UNION

SELECT employee_id, department_id
FROM Employee
GROUP BY employee_id
HAVING COUNT(*) = 1;
```
