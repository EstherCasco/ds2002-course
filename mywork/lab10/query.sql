USE thc8mr_db;

SELECT c.customer_id, c.name, c.city, o.order_id, o.item, o.quantity, o.order_date
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.quantity >= 2;
