# 0584 - Find Customer Referee

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Select
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/find-customer-referee](https://leetcode.com/problems/find-customer-referee)

## Problem Statement

Table: `Customer`

```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.
```

 

Find the names of the customer that are either:

	**referred by** any customer with `id != 2`.
	**not referred by** any customer.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:

```text
Input: 
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
Output: 
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
```

## Approach & Key Insights

Query customer names handling three-valued logic (NULL) by explicitly checking `referee_id != 2 OR referee_id IS NULL`.

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(1)`

## Solution

The complete SQL query solution is available in [`0584-find-customer-referee.sql`](./0584-find-customer-referee.sql).

```sql
# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_id != 2 
    OR referee_id IS NULL;
```
