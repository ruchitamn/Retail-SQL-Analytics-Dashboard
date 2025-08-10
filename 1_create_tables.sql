-- customers table
CREATE TABLE customers (
    customer_id NUMBER PRIMARY KEY,
    name VARCHAR2(100),
    age NUMBER,
    gender VARCHAR2(10),
    city VARCHAR2(50)
);

-- products table
CREATE TABLE products (
    product_id NUMBER PRIMARY KEY,
    product_name VARCHAR2(100),
    category VARCHAR2(50),
    price NUMBER(10,2)
);

-- orders table
CREATE TABLE orders (
    order_id NUMBER PRIMARY KEY,
    customer_id NUMBER,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- order_items table
CREATE TABLE order_items (
    item_id NUMBER PRIMARY KEY,
    order_id NUMBER,
    product_id NUMBER,
    quantity NUMBER,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
