# 0596 - Classes With at Least 5 Students

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Sorting and Grouping
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/classes-with-at-least-5-students](https://leetcode.com/problems/classes-with-at-least-5-students)

## Problem Statement

Table: `Courses`

```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.
```

 

Write a solution to find all the classes that have **at least five students**.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:

```text
Input: 
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
Output: 
+---------+
| class   |
+---------+
| Math    |
+---------+
Explanation: 
- Math has 6 students, so we include it.
- English has 1 student, so we do not include it.
- Biology has 1 student, so we do not include it.
- Computer has 1 student, so we do not include it.
```

## Approach & Key Insights

Group by `class` and filter for classes with five or more registered students using `HAVING COUNT(student) >= 5`.

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`0596-classes-with-at-least-5-students.sql`](./0596-classes-with-at-least-5-students.sql).

```sql
# Write your MySQL query statement below
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;
```
