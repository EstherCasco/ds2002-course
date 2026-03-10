USE thc8mr_db;

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
customer_id INT PRIMARY KEY,
name VARCHAR(50),
email VARCHAR(100),
city VARCHAR(50)
);

CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,
item VARCHAR(50),
quantity INT,
order_date DATE,
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
INSERT INTO customers VALUES
(1, 'Chris', 'chris@gmail.com','Arlington'),
(2, 'Kango', 'kango@gmail.com', 'Woodbridge'),
(3, 'Jalen', 'jalen@gmail.com', 'Amelia'),
(4, 'Maleah', 'maleah@gmail.com', 'Woodbridge'),
(5, 'Jaden', 'jaden@gmail.com', 'Fredericksburg'),
(6, 'Clarence', 'clarence@gmail.com', 'Cville'),
(7, 'Ruby', 'ruby@gmail.com', 'Virginia Beach'),
(8, 'Mekdess', 'mekdess@gmail.com', 'Woodbridge'),
(9, 'Elizabeth', 'elizabeth@gmail.com', 'Woodbridge'),
(10, 'Charlotte', 'charlotte@gmail.com', 'DC');
INSERT INTO orders VALUES
(101, 1, 'Sour Patch Kids', 1, '2026-02-01'),
(102, 2, 'Kit Kat', 2, '2026-02-02'),
(103, 3, 'Skittles', 1, '2026-02-03'),
(104, 4, 'Twix', 2, '2026-02-04'),
(105, 5, 'M&Ms', 1, '2026-02-05'),
(106, 6, 'Reeses', 1, '2026-02-06'),
(107, 7, 'Starburst', 2, '2026-02-07'),
(108, 8, 'Snickers', 1, '2026-02-08'),
(109, 9, 'Haribo Gummies', 1, '2026-02-09'),
(110, 10, 'Hershey Bar', 1, '2026-02-10');
