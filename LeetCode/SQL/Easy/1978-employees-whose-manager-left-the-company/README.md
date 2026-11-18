# 1978 - Employees Whose Manager Left the Company

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Subqueries
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/employees-whose-manager-left-the-company](https://leetcode.com/problems/employees-whose-manager-left-the-company)

## Problem Statement

Table: `Employees`

```text
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| manager_id  | int      |
| salary      | int      |
+-------------+----------+
In SQL, employee_id is the primary key for this table.
This table contains information about the employees, their salary, and the ID of their manager. Some employees do not have a manager (manager_id is null).
```

 

Find the IDs of the employees whose salary is strictly less than `$30000` and whose manager left the company. When a manager leaves the company, their information is deleted from the `Employees` table, but the reports still have their `manager_id` set to the manager that left.

Return the result table ordered by `employee_id`.

The result format is in the following example.

 

Example 1:

```text
Input:  
Employees table:
+-------------+-----------+------------+--------+
| employee_id | name      | manager_id | salary |
+-------------+-----------+------------+--------+
| 3           | Mila      | 9          | 60301  |
| 12          | Antonella | null       | 31000  |
| 13          | Emery     | null       | 67084  |
| 1           | Kalel     | 11         | 21241  |
| 9           | Mikaela   | null       | 50937  |
| 11          | Joziah    | 6          | 28485  |
+-------------+-----------+------------+--------+
Output: 
+-------------+
| employee_id |
+-------------+
| 11          |
+-------------+

Explanation: 
The employees with a salary less than $30000 are 1 (Kalel) and 11 (Joziah).
Kalel&#39;s manager is employee 11, who is still in the company (Joziah).
Joziah&#39;s manager is employee 6, who left the company because there is no row for employee 6 as it was deleted.
```

## Approach & Key Insights

Filter low-salary employees (< $30,000) whose `manager_id` is NOT NULL and `NOT IN (SELECT employee_id FROM Employees)`.

## Complexity Analysis

- **Time Complexity:** `O(N log N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`1978-employees-whose-manager-left-the-company.sql`](./1978-employees-whose-manager-left-the-company.sql).

```sql
# Write your MySQL query statement below
SELECT employee_id
FROM Employees
WHERE salary < 30000
  AND manager_id IS NOT NULL
  AND manager_id NOT IN (
      SELECT employee_id
      FROM Employees
  )
ORDER BY employee_id;
```
