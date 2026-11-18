# 0619 - Biggest Single Number

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Sorting and Grouping
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/biggest-single-number](https://leetcode.com/problems/biggest-single-number)

## Problem Statement

Table: `MyNumbers`

```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.
```

 

A **single number** is a number that appeared only once in the `MyNumbers` table.

Find the largest **single number**. If there is no **single number**, report `null`.

The result format is in the following example.

 
 

Example 1:

```text
Input: 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+
Output: 
+-----+
| num |
+-----+
| 6   |
+-----+
Explanation: The single numbers are 1, 4, 5, and 6.
Since 6 is the largest single number, we return it.
```

Example 2:

```text
Input: 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 7   |
| 7   |
| 3   |
| 3   |
| 3   |
+-----+
Output: 
+------+
| num  |
+------+
| null |
+------+
Explanation: There are no single numbers in the input table so we return null.
```

## Approach & Key Insights

Use a subquery grouping by `num` with `HAVING COUNT(*) = 1` to isolate unique numbers, then wrap with `SELECT MAX(num)`.

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`0619-biggest-single-number.sql`](./0619-biggest-single-number.sql).

```sql
# Write your MySQL query statement below
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) t;
```
