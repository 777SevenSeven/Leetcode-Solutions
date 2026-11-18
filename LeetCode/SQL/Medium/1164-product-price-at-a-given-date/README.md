# 1164 - Product Price at a Given Date

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Language:** MySQL (SQL)
- **Category:** Advanced Select and Joins
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/product-price-at-a-given-date](https://leetcode.com/problems/product-price-at-a-given-date)

## Problem Statement

Table: `Products`

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.
```

Initially, all products have price 10.

Write a solution to find the prices of all products on the date `2019-08-16`.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:

```text
Input: 
Products table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+
Output: 
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+
```

## Approach & Key Insights

Union products with price updates on/before target date (picking the latest change via subquery) with products updated only after that date (assigned default price 10).

## Complexity Analysis

- **Time Complexity:** `O(N log N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`1164-product-price-at-a-given-date.sql`](./1164-product-price-at-a-given-date.sql).

```sql
# Write your MySQL query statement below
WITH latest_price AS (
    SELECT
        product_id,
        new_price,
        ROW_NUMBER() OVER (
            PARTITION BY product_id
            ORDER BY change_date DESC
        ) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)

SELECT
    p.product_id,
    COALESCE(lp.new_price, 10) AS price
FROM (
    SELECT DISTINCT product_id
    FROM Products
) p
LEFT JOIN latest_price lp
    ON p.product_id = lp.product_id
   AND lp.rn = 1;
```
