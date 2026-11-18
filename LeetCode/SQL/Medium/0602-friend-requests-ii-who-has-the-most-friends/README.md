# 0602 - Friend Requests II: Who Has the Most Friends

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Language:** MySQL (SQL)
- **Category:** Subqueries
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends)

## Problem Statement

Table: `RequestAccepted`

```text
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.
```

 

Write a solution to find the people who have the most friends and the most friends number.

The test cases are generated so that only one person has the most friends.

The result format is in the following example.

 

Example 1:

```text
Input: 
RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
+--------------+-------------+-------------+
Output: 
+----+-----+
| id | num |
+----+-----+
| 3  | 3   |
+----+-----+
Explanation: 
The person with id 3 is a friend of people 1, 2, and 4, so he has three friends in total, which is the most number than any others.
```

 

**Follow up:** In the real world, multiple people could have the same most number of friends. Could you find all these people in this case?

## Approach & Key Insights

Combine `requester_id` and `accepter_id` using `UNION ALL`, group by ID, order by total count descending, and extract the top friend using `LIMIT 1`.

## Complexity Analysis

- **Time Complexity:** `O(N log N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`0602-friend-requests-ii-who-has-the-most-friends.sql`](./0602-friend-requests-ii-who-has-the-most-friends.sql).

```sql
SELECT
    id,
    COUNT(*) AS num
FROM (
    SELECT requester_id AS id
    FROM RequestAccepted

    UNION ALL

    SELECT accepter_id AS id
    FROM RequestAccepted
) t
GROUP BY id
ORDER BY num DESC
LIMIT 1;
```
