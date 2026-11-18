# 1341 - Movie Rating

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Language:** MySQL (SQL)
- **Category:** Subqueries
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/movie-rating](https://leetcode.com/problems/movie-rating)

## Problem Statement

Table: `Movies`

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key (column with unique values) for this table.
title is the name of the movie.
Each movie has a unique title.
```

Table: `Users`

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
The column &#39;name&#39; has unique values.
```

Table: `MovieRating`

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key (column with unique values) for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user&#39;s review date.
```

 

Write a solution to:

	Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
	Find the movie name with the **highest average** rating in `February 2020`. In case of a tie, return the lexicographically smaller movie name.

The result format is in the following example.

 

Example 1:

```text
Input: 
Movies table:
+-------------+--------------+
| movie_id    |  title       |
+-------------+--------------+
| 1           | Avengers     |
| 2           | Frozen 2     |
| 3           | Joker        |
+-------------+--------------+
Users table:
+-------------+--------------+
| user_id     |  name        |
+-------------+--------------+
| 1           | Daniel       |
| 2           | Monica       |
| 3           | Maria        |
| 4           | James        |
+-------------+--------------+
MovieRating table:
+-------------+--------------+--------------+-------------+
| movie_id    | user_id      | rating       | created_at  |
+-------------+--------------+--------------+-------------+
| 1           | 1            | 3            | 2020-01-12  |
| 1           | 2            | 4            | 2020-02-11  |
| 1           | 3            | 2            | 2020-02-12  |
| 1           | 4            | 1            | 2020-01-01  |
| 2           | 1            | 5            | 2020-02-17  | 
| 2           | 2            | 2            | 2020-02-01  | 
| 2           | 3            | 2            | 2020-03-01  |
| 3           | 1            | 3            | 2020-02-22  | 
| 3           | 2            | 4            | 2020-02-25  | 
+-------------+--------------+--------------+-------------+
Output: 
+--------------+
| results      |
+--------------+
| Daniel       |
| Frozen 2     |
+--------------+
Explanation: 
Daniel and Monica have rated 3 movies (&quot;Avengers&quot;, &quot;Frozen 2&quot; and &quot;Joker&quot;) but Daniel is smaller lexicographically.
Frozen 2 and Joker have a rating average of 3.5 in February but Frozen 2 is smaller lexicographically.
```

## Approach & Key Insights

Combine two independent subqueries via `UNION ALL`: the user with the most movie ratings and the highest average rated movie in February 2020.

## Complexity Analysis

- **Time Complexity:** `O(N log N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`1341-movie-rating.sql`](./1341-movie-rating.sql).

```sql
# Write your MySQL query statement below
(
    SELECT u.name AS results
    FROM Users u
    JOIN MovieRating mr
        ON u.user_id = mr.user_id
    GROUP BY u.user_id, u.name
    ORDER BY COUNT(*) DESC, u.name
    LIMIT 1
)

UNION ALL

(
    SELECT m.title AS results
    FROM Movies m
    JOIN MovieRating mr
        ON m.movie_id = mr.movie_id
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY m.movie_id, m.title
    ORDER BY AVG(mr.rating) DESC, m.title
    LIMIT 1
);
```
