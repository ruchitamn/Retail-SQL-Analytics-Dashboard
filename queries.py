queries = {
    "Total Revenue": """
        SELECT SUM(p.price * oi.quantity) AS total_revenue
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
    """,

    "Top 3 Cities by Orders": """
        SELECT c.city, COUNT(o.order_id) AS total_orders
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY c.city
        ORDER BY total_orders DESC
        FETCH FIRST 3 ROWS ONLY
    """,

    "MOST POPULAR PRODUCT": """
        SELECT p.product_name, SUM(oi.quantity) AS total_sold
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY p.product_name
        ORDER BY total_sold DESC
        FETCH FIRST 1 ROWS ONLY
    """,

    "REVENUE OF EACH CATEGORY/PRODUCT": """
        SELECT 
    p.product_name,
    SUM(p.price * oi.quantity) AS revenue
FROM 
    products p
JOIN 
    order_items oi ON p.product_id = oi.product_id
GROUP BY 
    p.product_name
ORDER BY 
    revenue DESC
    """,

    "CUSTOMER WHO SPENT MOST": """
        SELECT 
    c.name,
    SUM(p.price * oi.quantity) AS total_spent
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
JOIN 
    order_items oi ON o.order_id = oi.order_id
JOIN 
    products p ON oi.product_id = p.product_id
GROUP BY 
    c.name
ORDER BY 
    total_spent DESC
FETCH FIRST 1 ROWS ONLY
    """,


    "MONTHLY SALES TREND": """
        SELECT 
    TO_CHAR(o.order_date, 'YYYY-MM') AS month,
    SUM(p.price * oi.quantity) AS revenue
FROM 
    orders o
JOIN 
    order_items oi ON o.order_id = oi.order_id
JOIN 
    products p ON oi.product_id = p.product_id
GROUP BY 
    TO_CHAR(o.order_date, 'YYYY-MM')
ORDER BY 
    month
    """,



    "AVERAGE ORDER VALUE": """
        SELECT 
    ROUND(SUM(p.price * oi.quantity) / COUNT(DISTINCT o.order_id), 2) AS avg_order_value
FROM 
    order_items oi
JOIN 
    products p ON oi.product_id = p.product_id
JOIN 
    orders o ON oi.order_id = o.order_id
    """,


    "Product Categories with More Than 1 Product": """
        SELECT 
    category, COUNT(*) AS product_count
FROM 
    products
GROUP BY 
    category
HAVING 
    COUNT(*) > 1
    """,

    "ORDER DETAILS": """
        SELECT 
    o.order_id, c.name AS customer_name, p.product_name, oi.quantity, o.order_date
FROM 
    orders o
JOIN 
    customers c ON o.customer_id = c.customer_id
JOIN 
    order_items oi ON o.order_id = oi.order_id
JOIN 
    products p ON oi.product_id = p.product_id
ORDER BY 
    o.order_id
    """,


    "CUSTOMER ORDER FREQUENCY": """
        SELECT 
    c.name, COUNT(o.order_id) AS num_orders
FROM 
    customers c
LEFT JOIN 
    orders o ON c.customer_id = o.customer_id
GROUP BY 
    c.name
ORDER BY 
    num_orders DESC
    """,



    "PRODUCTS NEVER ORDERED": """
        SELECT 
    product_name
FROM 
    products
WHERE 
    product_id NOT IN (
        SELECT DISTINCT product_id FROM order_items
    )
    """,



    "REPEATED CUSTROMER": """
        SELECT 
    c.name, COUNT(o.order_id) AS total_orders
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
GROUP BY 
    c.name
HAVING 
    COUNT(o.order_id) > 1
    """
}
