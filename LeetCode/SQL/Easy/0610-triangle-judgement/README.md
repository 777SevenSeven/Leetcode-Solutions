# 0610 - Triangle Judgement

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Advanced Select and Joins
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/triangle-judgement](https://leetcode.com/problems/triangle-judgement)

## Problem Statement

Table: `Triangle`

```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.
```

 

Report for every three line segments whether they can form a triangle.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:

```text
Input: 
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
Output: 
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+
```

## Approach & Key Insights

Evaluate triangle inequality theorem via `CASE WHEN x + y > z AND x + z > y AND y + z > x THEN "Yes" ELSE "No" END`.

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(1)`

## Solution

The complete SQL query solution is available in [`0610-triangle-judgement.sql`](./0610-triangle-judgement.sql).

```sql
# Write your MySQL query statement below
SELECT
    x,
    y,
    z,
    CASE
        WHEN x + y > z
         AND x + z > y
         AND y + z > x
        THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;
```
