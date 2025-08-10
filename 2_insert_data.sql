--insert valuies to customers--
INSERT INTO customers VALUES (1, 'Ananya Sharma', 28, 'Female', 'Mumbai');
INSERT INTO customers VALUES (2, 'Ravi Verma', 35, 'Male', 'Delhi');
INSERT INTO customers VALUES (3, 'Priya Mehta', 23, 'Female', 'Bangalore');
INSERT INTO customers VALUES (4, 'Kunal Desai', 30, 'Male', 'Hyderabad');
INSERT INTO customers VALUES (5, 'Meera Iyer', 40, 'Female', 'Chennai');

--insert va;lues to products--
INSERT INTO products VALUES (101, 'iPhone 14', 'Electronics', 79999);
INSERT INTO products VALUES (102, 'Samsung Galaxy S22', 'Electronics', 74999);
INSERT INTO products VALUES (103, 'Sony Headphones', 'Accessories', 4999);
INSERT INTO products VALUES (104, 'Apple Watch', 'Wearables', 35999);
INSERT INTO products VALUES (105, 'Dell XPS 13', 'Laptops', 99999);

--insert into orderts--
INSERT INTO orders VALUES (1001, 1, TO_DATE('2023-06-01', 'YYYY-MM-DD'));
INSERT INTO orders VALUES (1002, 2, TO_DATE('2023-06-15', 'YYYY-MM-DD'));
INSERT INTO orders VALUES (1003, 1, TO_DATE('2023-07-03', 'YYYY-MM-DD'));
INSERT INTO orders VALUES (1004, 4, TO_DATE('2023-07-10', 'YYYY-MM-DD'));

--insert into order_items--
INSERT INTO order_items VALUES (1, 1001, 101, 1);
INSERT INTO order_items VALUES (2, 1001, 103, 2);
INSERT INTO order_items VALUES (3, 1002, 102, 1);
INSERT INTO order_items VALUES (4, 1003, 104, 1);
INSERT INTO order_items VALUES (5, 1004, 105, 1);

SELECT * FROM customers;

SELECT * FROM products;

SELECT * FROM orders;

SELECT * FROM order_items;

UPDATE orders
SET order_date = TO_DATE(
    '2025-' || TO_CHAR(order_date, 'MM-DD'),
    'YYYY-MM-DD'
);

SELECT * FROM orders;