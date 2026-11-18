# 1757 - Recyclable and Low Fat Products

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Select
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/recyclable-and-low-fat-products](https://leetcode.com/problems/recyclable-and-low-fat-products)

## Problem Statement

Table: `Products`

```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type (&#39;Y&#39;, &#39;N&#39;) where &#39;Y&#39; means this product is low fat and &#39;N&#39; means it is not.
recyclable is an ENUM (category) of types (&#39;Y&#39;, &#39;N&#39;) where &#39;Y&#39; means this product is recyclable and &#39;N&#39; means it is not.
```

 

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:

```text
Input: 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output: 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: Only products 1 and 3 are both low fat and recyclable.
```

## Approach & Key Insights

Filter records where both `low_fats` and `recyclable` are flagged as "Y" using a direct WHERE clause condition.

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(1)`

## Solution

The complete SQL query solution is available in [`1757-recyclable-and-low-fat-products.sql`](./1757-recyclable-and-low-fat-products.sql).

```sql
# Write your MySQL query statement below
SELECT product_id
FROM Products
WHERE low_fats = 'Y' 
    AND recyclable = 'Y';
```
