# 2356 - Number of Unique Subjects Taught by Each Teacher

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** MySQL (SQL)
- **Category:** Sorting and Grouping
- **Status:** Accepted
- **Original Problem:** [https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher)

## Problem Statement

Table: `Teacher`

```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
(subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.
```

 

Write a solution to calculate the number of unique subjects each teacher teaches in the university.

Return the result table in **any order**.

The result format is shown in the following example.

 

Example 1:

```text
Input: 
Teacher table:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+
Output:  
+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+
Explanation: 
Teacher 1:
  - They teach subject 2 in departments 3 and 4.
  - They teach subject 3 in department 3.
Teacher 2:
  - They teach subject 1 in department 1.
  - They teach subject 2 in department 1.
  - They teach subject 3 in department 1.
  - They teach subject 4 in department 1.
```

## Approach & Key Insights

Group records by `teacher_id` and count distinct subjects taught per teacher using `COUNT(DISTINCT subject_id)`.

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

## Solution

The complete SQL query solution is available in [`2356-number-of-unique-subjects-taught-by-each-teacher.sql`](./2356-number-of-unique-subjects-taught-by-each-teacher.sql).

```sql
# Write your MySQL query statement below
SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
```
