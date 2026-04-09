USE thc8mr_db;

INSERT INTO customers (customer_id, name, email, city)
VALUES
(11, 'Maria Lopez', 'maria.lopez@email.com', 'Charlottesville'),
(12, 'Daniel Cruz', 'daniel.cruz@email.com', 'Richmond');

INSERT INTO orders (order_id, customer_id, item, quantity, order_date)
VALUES
(111, 11, 'Notebook', 2, '2026-04-08'),
(112, 11, 'Backpack', 1, '2026-04-08'),
(113, 12, 'Water Bottle', 3, '2026-04-08');
