# 1729 - Find Followers Count

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Sorting and Grouping
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/find-followers-count](https://leetcode.com/problems/find-followers-count)

## Problem Statement

Table: `Followers`

```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| follower_id | int  |
+-------------+------+
(user_id, follower_id) is the primary key (combination of columns with unique values) for this table.
This table contains the IDs of a user and a follower in a social media app where the follower follows the user.
```

 

Write a solution that will, for each user, return the number of followers.

Return the result table ordered by `user_id` in ascending order.

The result format is in the following example.

 

Example 1:

```text
Input: 
Followers table:
+---------+-------------+
| user_id | follower_id |
+---------+-------------+
| 0       | 1           |
| 1       | 0           |
| 2       | 0           |
| 2       | 1           |
+---------+-------------+
Output: 
+---------+----------------+
| user_id | followers_count|
+---------+----------------+
| 0       | 1              |
| 1       | 1              |
| 2       | 2              |
+---------+----------------+
Explanation: 
The followers of 0 are {1}
The followers of 1 are {0}
The followers of 2 are {0,1}
```

## Approach & Key Insights

Group by `user_id`, tally followers with `COUNT(follower_id)`, and sort the results by `user_id ASC`.

## Complexity Analysis

- **Time Complexity:** `O(N log N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`1729-find-followers-count.sql`](./1729-find-followers-count.sql).

```sql
# Write your MySQL query statement below
SELECT
    user_id,
    COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;
```
