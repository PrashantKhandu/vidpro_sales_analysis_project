-- Active: 1754214495102@@127.0.0.1@5432@interview

SELECT * FROM sales LIMIT 10;
SELECT * FROM customers LIMIT 10;
SELECT * FROM orders LIMIT 10;
SELECT * FROM items LIMIT 10;

-- 4. NULL quantity means not purchased — do not treat NULL as zero. Omit items where total quantity is zero.
SELECT 
    c.customer_name,
    c.age,
    i.item_name,
    SUM(s.quantity) AS quantity
FROM sales s
JOIN orders o 
    ON s.order_id = o.order_id
JOIN customer c 
    ON o.customer_id = c.customer_id
JOIN items i 
    ON s.item_id = i.item_id
GROUP BY c.customer_name, c.age, i.item_name
HAVING SUM(s.quantity) IS NOT NULL AND SUM(s.quantity) > 0
ORDER BY c.customer_name, i.item_name;
