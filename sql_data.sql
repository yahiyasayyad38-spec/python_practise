USE mydatabase; 

-- CREATE DATABASE mydata;

-- CREATE TABLE customers (
-- 	id INT PRIMARY KEY,
--     name VARCHAR(50) NOT NULL,
--     country VARCHAR(250)
-- )

INSERT INTO customers (id,name,country)
VALUES 
	(101,'charlie','USA'),
    (102,'belas','UK'),
    (103,'kate','germany')

SELECT *
FROM customers;

SELECT 
	id,
    first_name
FROM customers;

SELECT *
FROM customers
WHERE score > 500;

SELECT *
FROM customers
WHERE country = "USA";

SELECT * 
FROM customers AS c
INNER JOIN orders AS o
	ON c.id = o.customer_id
WHERE o.sales > 20;



-- SELECT
-- FROM 
-- WHERE
-- JOIN (inner,outer,full,) -- ON,USING
-- GROUP BY
-- HAVING
