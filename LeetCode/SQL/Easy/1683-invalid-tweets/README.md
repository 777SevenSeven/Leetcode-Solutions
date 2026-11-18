# 1683 - Invalid Tweets

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Select
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/invalid-tweets](https://leetcode.com/problems/invalid-tweets)

## Problem Statement

Table: `Tweets`

```text
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
content consists of alphanumeric characters, &#39;!&#39;, or &#39; &#39; and no other special characters.
This table contains all the tweets in a social media app.
```

 

Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is **strictly greater** than `15`.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:

```text
Input: 
Tweets table:
+----------+-----------------------------------+
| tweet_id | content                           |
+----------+-----------------------------------+
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |
+----------+-----------------------------------+
Output: 
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Explanation: 
Tweet 1 has length = 11. It is a valid tweet.
Tweet 2 has length = 33. It is an invalid tweet.
```

## Approach & Key Insights

Use MySQL `CHAR_LENGTH(content) > 15` rather than `LENGTH()` to correctly measure multi-byte character counts.

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(1)`

## Solution

The complete SQL query solution is available in [`1683-invalid-tweets.sql`](./1683-invalid-tweets.sql).

```sql
# Write your MySQL query statement below
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
```
