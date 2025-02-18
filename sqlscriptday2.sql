SHOW DATABASES;

USE org;

SHOW TABLES;

##Alter table

#Rename
ALTER TABLE BONUS RENAME TO Bonus;

ALTER TABLE TITLE RENAME TO Title;

SELECT * FROM Worker;

#Adding new column
ALTER TABLE Worker ADD age INT NOT NULL;

UPDATE Worker 
SET age = 27
WHERE WORKER_ID = 6;

#Modifying column's dtype
ALTER TABLE Worker MODIFY SALARY FLOAT NOT NULL DEFAULT 0;

DESCRIBE Worker;

#Change column name
ALTER TABLE Worker CHANGE COLUMN age AGE FLOAT NOT NULL DEFAULT 0;

ALTER TABLE Worker ADD test INT;

#Drop column
ALTER TABLE Worker DROP COLUMN test;

#Replace
REPLACE INTO Bonus (WORKER_REF_ID, BONUS_AMOUNT)
VALUES(3, 25000);

REPLACE INTO Worker (WORKER_ID, SALARY)
VALUES(1, 25000);

SELECT * FROM Bonus;

#LIMIT 

SELECT * FROM Worker 
LIMIT 3;

SELECT * FROM Worker
WHERE DEPARTMENT = 'AI/ML' 
LIMIT 2;

SELECT * FROM Worker 
LIMIT 3 OFFSET 2;

#JOINS

USE test;

CREATE TABLE Customer (
	cust_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    contact VARCHAR(15) NOT NULL,
    city VARCHAR(25)
);

CREATE TABLE Orders (
	order_id INT PRIMARY KEY AUTO_INCREMENT,
    cust_id INT,
    order_date DATE NOT NULL,
    order_amount FLOAT,
    FOREIGN KEY (cust_id) REFERENCES Customer(cust_id)
);

INSERT INTO Customer (name, contact, city) VALUES 
('John Doe', '555-1234', 'New York'),
('Jane Smith', '555-5678', 'Los Angeles'),
('Alice Johnson', '555-8765', 'Chicago'),
('Bob Brown', '555-4321', 'Houston'),
('Charlie White', '555-6789', 'San Francisco');

SELECT * FROM Customer;

INSERT INTO Orders (cust_id, order_date, order_amount) VALUES
(1, '2025-01-15', 100.50),
(2, '2025-02-05', 250.00),
(3, '2025-02-12', 75.99),
(1, '2025-02-18', 49.75),
(4, '2025-01-25', 300.00);

SELECT * FROM Orders;

#INNER JOIN
SELECT C.*, O.* FROM Customer AS C 
INNER JOIN Orders AS O ON O.cust_id = C.cust_id;

SELECT Orders.order_id, Customer.name, Orders.order_amount, Customer.contact FROM Orders
INNER JOIN Customer ON Orders.cust_id = Customer.cust_id;

#OUTER JOIN
#1.LEFT JOIN
SELECT Customer.cust_id, Customer.name, Orders.order_id, Orders.order_amount FROM Customer
LEFT JOIN Orders ON Customer.cust_id = Orders.cust_id;

#2.RIGHT JOIN
SELECT Orders.order_id, Customer.name FROM Customer
RIGHT JOIN Orders ON Customer.cust_id = Orders.cust_id;

#3. FULL JOIN
SELECT Customer.cust_id, Customer.name, Orders.order_id, Orders.order_amount
FROM Customer
LEFT JOIN Orders ON Customer.cust_id = Orders.cust_id
UNION
SELECT Customer.cust_id, Customer.name, Orders.order_id, Orders.order_amount
FROM Customer
RIGHT JOIN Orders ON Customer.cust_id = Orders.cust_id;

#4.CROSS JOIN
SELECT Customer.name, Orders.order_id FROM Customer
CROSS JOIN Orders;




