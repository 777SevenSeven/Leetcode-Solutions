# 0570 - Managers with at Least 5 Direct Reports

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Language:** MySQL (SQL)
- **Category:** Basic Joins
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/managers-with-at-least-5-direct-reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports)

## Problem Statement

Table: `Employee`

```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
```

 

Write a solution to find managers with at least **five direct reports**.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:

```text
Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+
```

## Approach & Key Insights

Group direct reports by `managerId` with `HAVING COUNT(*) >= 5`, then join with `Employee` to retrieve the manager names.

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`0570-managers-with-at-least-5-direct-reports.sql`](./0570-managers-with-at-least-5-direct-reports.sql).

```sql
# Write your MySQL query statement below
SELECT e.name
FROM Employee e
JOIN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) m
ON e.id = m.managerId;
```
