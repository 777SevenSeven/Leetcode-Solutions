# 0626 - Exchange Seats

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Language:** MySQL (SQL)
- **Category:** Subqueries
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/exchange-seats](https://leetcode.com/problems/exchange-seats)

## Problem Statement

Table: `Seat`

```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
The ID sequence always starts from 1 and increments continuously.
```

 

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by `id` **in ascending order**.

The result format is in the following example.

 

Example 1:

```text
Input: 
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
Output: 
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
Explanation: 
Note that if the number of students is odd, there is no need to change the last one&#39;s seat.
```

## Approach & Key Insights

Swap adjacent seat IDs using conditional `CASE WHEN` logic: odd IDs increase by 1 (except the final seat if total count is odd), while even IDs decrease by 1.

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(1)`

## Solution

The complete SQL query solution is available in [`0626-exchange-seats.sql`](./0626-exchange-seats.sql).

```sql
# Write your MySQL query statement below
SELECT
    CASE
        WHEN id % 2 = 1 AND id <> (SELECT MAX(id) FROM Seat)
            THEN id + 1
        WHEN id % 2 = 1
            THEN id
        ELSE id - 1
    END AS id,
    student
FROM Seat
ORDER BY id;
```
