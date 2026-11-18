# 1667 - Fix Names in a Table

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Advanced String Functions / Regex / Clause
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/fix-names-in-a-table](https://leetcode.com/problems/fix-names-in-a-table)

## Problem Statement

Table: `Users`

```text
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
```

 

Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by `user_id`.

The result format is in the following example.

 

Example 1:

```text
Input: 
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
Output: 
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+
```

## Approach & Key Insights

Capitalize names using `CONCAT(UPPER(SUBSTR(name, 1, 1)), LOWER(SUBSTR(name, 2)))` and sort by `user_id`.

## Complexity Analysis

- **Time Complexity:** `O(N log N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`1667-fix-names-in-a-table.sql`](./1667-fix-names-in-a-table.sql).

```sql
# Write your MySQL query statement below
SELECT
    user_id,
    CONCAT(
        UPPER(LEFT(name, 1)),
        LOWER(SUBSTRING(name, 2))
    ) AS name
FROM Users
ORDER BY user_id;
```
