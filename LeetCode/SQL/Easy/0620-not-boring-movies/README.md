# 0620 - Not Boring Movies

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Basic Aggregate Functions
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/not-boring-movies](https://leetcode.com/problems/not-boring-movies)

## Problem Statement

Table: `Cinema`

```text
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |
+----------------+----------+
id is the primary key (column with unique values) for this table.
Each row contains information about the name of a movie, its genre, and its rating.
rating is a 2 decimal places float in the range [0, 10]
```

 

Write a solution to report the movies with an odd-numbered ID and a description that is not `&quot;boring&quot;`.

Return the result table ordered by `rating` **in descending order**.

The result format is in the following example.

 

Example 1:

```text
Input: 
Cinema table:
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 1  | War        | great 3D    | 8.9    |
| 2  | Science    | fiction     | 8.5    |
| 3  | irish      | boring      | 6.2    |
| 4  | Ice song   | Fantacy     | 8.6    |
| 5  | House card | Interesting | 9.1    |
+----+------------+-------------+--------+
Output: 
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 5  | House card | Interesting | 9.1    |
| 1  | War        | great 3D    | 8.9    |
+----+------------+-------------+--------+
Explanation: 
We have three movies with odd-numbered IDs: 1, 3, and 5. The movie with ID = 3 is boring so we do not include it in the answer.
```

## Approach & Key Insights

Select odd-numbered IDs using `id % 2 = 1` with `description != "boring"`, ordering the output by rating in descending order.

## Complexity Analysis

- **Time Complexity:** `O(N log N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`0620-not-boring-movies.sql`](./0620-not-boring-movies.sql).

```sql
# Write your MySQL query statement below
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description <> 'boring'
ORDER BY rating DESC;
```
