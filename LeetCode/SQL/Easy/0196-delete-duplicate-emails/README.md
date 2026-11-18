# 0196 - Delete Duplicate Emails

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Advanced String Functions / Regex / Clause
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/delete-duplicate-emails](https://leetcode.com/problems/delete-duplicate-emails)

## Problem Statement

Table: `Person`

```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
```

 

Write a solution to** delete** all duplicate emails, keeping only one unique email with the smallest `id`.

For SQL users, please note that you are supposed to write a `DELETE` statement and not a `SELECT` one.

For Pandas users, please note that you are supposed to modify `Person` in place.

After running your script, the answer shown is the `Person` table. The driver will first compile and run your piece of code and then show the `Person` table. The final order of the `Person` table **does not matter**.

The result format is in the following example.

 

Example 1:

```text
Input: 
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Output: 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.
```

## Approach & Key Insights

Delete duplicate emails using a self-join `DELETE p1 FROM Person p1, Person p2 WHERE p1.email = p2.email AND p1.id > p2.id`.

## Complexity Analysis

- **Time Complexity:** `O(N^2)`
- **Space Complexity:** `O(1)`

## Solution

The complete SQL query solution is available in [`0196-delete-duplicate-emails.sql`](./0196-delete-duplicate-emails.sql).

```sql
# Write your MySQL query statement below
DELETE p1
FROM Person p1
JOIN Person p2
    ON p1.email = p2.email
WHERE p1.id > p2.id;
```
