# 0176 - Second Highest Salary

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Language:** MySQL (SQL)
- **Category:** Advanced String Functions / Regex / Clause
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/second-highest-salary](https://leetcode.com/problems/second-highest-salary)

## Problem Statement

Table: `Employee`

```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
```

 

Write a solution to find the second highest **distinct** salary from the `Employee` table. If there is no second highest salary, return `null (return None in Pandas)`.

The result format is in the following example.

 

Example 1:

```text
Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```

Example 2:

```text
Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
```

## Approach & Key Insights

Query distinct salaries ordered descending with `LIMIT 1 OFFSET 1` wrapped in an outer scalar `SELECT (...) AS SecondHighestSalary` to return NULL if non-existent.

## Complexity Analysis

- **Time Complexity:** `O(N log N)`
- **Space Complexity:** `O(1)`

## Solution

The complete SQL query solution is available in [`0176-second-highest-salary.sql`](./0176-second-highest-salary.sql).

```sql
# Write your MySQL query statement below
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
```
