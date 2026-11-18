# 1907 - Count Salary Categories

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Language:** MySQL (SQL)
- **Category:** Advanced Select and Joins
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/count-salary-categories](https://leetcode.com/problems/count-salary-categories)

## Problem Statement

Table: `Accounts`

```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.
```

 

Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

	`&quot;Low Salary&quot;`: All the salaries **strictly less** than `$20000`.
	`&quot;Average Salary&quot;`: All the salaries in the **inclusive** range `[$20000, $50000]`.
	`&quot;High Salary&quot;`: All the salaries **strictly greater** than `$50000`.

The result table **must** contain all three categories. If there are no accounts in a category, return `0`.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:

```text
Input: 
Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
Output: 
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+
Explanation: 
Low Salary: Account 2.
Average Salary: No accounts.
High Salary: Accounts 3, 6, and 8.
```

## Approach & Key Insights

Construct fixed category rows ("Low Salary", "Average Salary", "High Salary") via `UNION ALL` to guarantee all categories appear even with zero counts.

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(1)`

## Solution

The complete SQL query solution is available in [`1907-count-salary-categories.sql`](./1907-count-salary-categories.sql).

```sql
# Write your MySQL query statement below
SELECT
    'Low Salary' AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income < 20000

UNION

SELECT
    'Average Salary',
    COUNT(*)
FROM Accounts
WHERE income BETWEEN 20000 AND 50000

UNION

SELECT
    'High Salary',
    COUNT(*)
FROM Accounts
WHERE income > 50000;
```
