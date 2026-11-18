# 1075 - Project Employees I

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Basic Aggregate Functions
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/project-employees-i](https://leetcode.com/problems/project-employees-i)

## Problem Statement

Table: `Project`

```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key of this table.
employee_id is a foreign key to `Employee` table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.
```

 

Table: `Employee`

```text
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
employee_id is the primary key of this table. It&#39;s guaranteed that experience_years is not NULL.
Each row of this table contains information about one employee.
```

 

Write an SQL query that reports the **average** experience years of all the employees for each project, **rounded to 2 digits**.

Return the result table in **any order**.

The query result format is in the following example.

 

Example 1:

```text
Input: 
Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+
Employee table:
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+
Output: 
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+
Explanation: The average experience years for the first project is (3 + 2 + 1) / 3 = 2.00 and for the second project is (3 + 2) / 2 = 2.50
```

## Approach & Key Insights

Join `Project` with `Employee` on `employee_id`, group by `project_id`, and calculate average experience rounded to two decimals: `ROUND(AVG(experience_years), 2)`.

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`1075-project-employees-i.sql`](./1075-project-employees-i.sql).

```sql
# Write your MySQL query statement below
SELECT
    p.project_id,
    ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
JOIN Employee e
    ON p.employee_id = e.employee_id
GROUP BY p.project_id;
```
