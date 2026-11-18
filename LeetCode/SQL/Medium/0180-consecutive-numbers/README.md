# 0180 - Consecutive Numbers

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Language:** MySQL (SQL)
- **Category:** Advanced Select and Joins
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/consecutive-numbers](https://leetcode.com/problems/consecutive-numbers)

## Problem Statement

Table: `Logs`

```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.
```

 

Find all numbers that appear at least three times consecutively.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:

```text
Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.
```

## Approach & Key Insights

Join three consecutive rows (`l1.id = l2.id - 1 AND l2.id = l3.id - 1`) verifying `l1.num = l2.num AND l2.num = l3.num` with `DISTINCT`.

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`0180-consecutive-numbers.sql`](./0180-consecutive-numbers.sql).

```sql
# Write your MySQL query statement below
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2
    ON l1.id = l2.id - 1
JOIN Logs l3
    ON l2.id = l3.id - 1
WHERE l1.num = l2.num
  AND l2.num = l3.num;
```
