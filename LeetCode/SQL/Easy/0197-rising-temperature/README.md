# 0197 - Rising Temperature

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Basic Joins
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/rising-temperature](https://leetcode.com/problems/rising-temperature)

## Problem Statement

Table: `Weather`

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
```

 

Write a solution to find all dates&#39; `id` with higher temperatures compared to its previous calendar dates (yesterday).

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:

```text
Input: 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output: 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation: 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).
```

## Approach & Key Insights

Self-join the `Weather` table where `DATEDIFF(w1.recordDate, w2.recordDate) = 1` and test `w1.temperature > w2.temperature` to identify rising temperature days.

## Complexity Analysis

- **Time Complexity:** `O(N log N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`0197-rising-temperature.sql`](./0197-rising-temperature.sql).

```sql
# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1
JOIN Weather w2
    ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
```
