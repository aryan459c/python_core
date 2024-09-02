Ashok Tarai, [25-08-2024 3:38 PM]
"""SQL"""
SQL1. Explain about the DML, DDL, TCL, DQL commands?
DML (Data Manipulation Language): Used for manage data in  objects
Commands: INSERT, UPDATE, DELETE, MERGE.
DDL (Data Definition Language): Used for defining and managing all database objects.
Commands: CREATE, ALTER, DROP, TRUNCATE, COMMENT, RENAME.
TCL (Transaction Control Language): Manages changes made by DML statements.
Commands: COMMIT, ROLLBACK, SAVEPOINT, SET TRANSACTION.
DQL (Data Query Language): Used to query data from the database.
Commands: SELECT.

# 2. What is a join? Explain all joins.
Join: A SQL operation that combines rows from two or more tables based on a related column between them.
Inner Join: Returns records with matching values in both tables.
ON table1.common_column = table2.common_column;
Left Join (Left Outer Join): Returns all records from the left table and matched records from the right table; returns NULL for unmatched rows in the right table.

Right Join (Right Outer Join): Returns all records from the right table and matched records from the left table; returns NULL for unmatched rows in the left table.
Full Join (Full Outer Join): Returns records when there is a match in either left or right table records; returns NULL for unmatched rows in either table.
Cross Join: Returns the Cartesian product of the two tables.
Self Join: A table is joined with itself.
# 3. Difference between Joins vs Subquery?
Joins:combine data from multiple tables into a single result set by matching columns between them
Subqueries:are nested queries executed separately before the outer query uses the result. Subqueries can be used for complex filtering and calculation.

# 4. Find 3rd Highest Salary Of employee table ?
    select * from emp where salary=>(select max(sal) from salary where salary =>(select max(sal) from salary))
SELECT DISTINCT salary 
FROM employee 
ORDER BY salary DESC 
LIMIT 1 OFFSET 2;

Ashok Tarai, [25-08-2024 3:42 PM]
SELECT seller_id, SUM(amount) AS total_sales
FROM sales
WHERE MONTH(sale_date) = MONTH(CURRENT_DATE)
AND YEAR(sale_date) = YEAR(CURRENT_DATE)
GROUP BY seller_id
ORDER BY total_sales DESC;

# 6. Difference between Rank vs Dense_rank?
Rank: Provides ranks with gaps. If two rows are tied, the next rank will have a gap.
Dense_Rank: Provides ranks without gaps. If two rows are tied, the next rank will continue without a gap.