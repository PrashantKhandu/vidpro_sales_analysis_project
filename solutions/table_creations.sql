'''
    Table creation codes
    Database Name: interview (we can put any name)
    Table Names: customer, orders, items, sales
    Description:
        -- We  have 4 tables
        -- sales is a fact table
        -- Remaining all the dimention tables

'''

-- 1. customer table
CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    age INTEGER NOT NULL CHECK (age > 0)
);

-- 2. orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,

    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES customer(customer_id)
        ON DELETE CASCADE
);

-- 3. items table
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) NOT NULL CHECK (price >= 0)
);

-- 4. sales table
CREATE TABLE sales (
    sales_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NULL CHECK (quantity >= 0),

    CONSTRAINT fk_sales_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_sales_item
        FOREIGN KEY (item_id)
        REFERENCES items(item_id)
        ON DELETE CASCADE
);
