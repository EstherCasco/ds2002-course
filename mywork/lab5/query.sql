USE thc8mr_db;

SELECT customers.name, customers.city, orders.item, orders.quantity, orders.order_date
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
WHERE orders.quantity > 1;
