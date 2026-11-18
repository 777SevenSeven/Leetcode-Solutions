# 1378 - Replace Employee ID With The Unique Identifier

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Basic Joins
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier)

## Problem Statement

Table: `Employees`

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.
```

 

Table: `EmployeeUNI`

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.
```

 

Write a solution to show the **unique ID **of each user, If a user does not have a unique ID replace just show `null`.

Return the result table in **any** order.

The result format is in the following example.

 

Example 1:

```text
Input: 
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
Output: 
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
Explanation: 
Alice and Bob do not have a unique ID, We will show null instead.
The unique ID of Meir is 2.
The unique ID of Winston is 3.
The unique ID of Jonathan is 1.
```

## Approach & Key Insights

Perform a `LEFT JOIN` between `Employees` and `EmployeeUNI` on `id` to retain all employee records even when no unique identifier exists (yielding NULL).

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`1378-replace-employee-id-with-the-unique-identifier.sql`](./1378-replace-employee-id-with-the-unique-identifier.sql).

```sql
# Write your MySQL query statement below
SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id;
```
