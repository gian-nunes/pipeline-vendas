CREATE TABLE orders_analytics (
    order_id     INTEGER PRIMARY KEY,
    customer_id  INTEGER,
    product_id   INTEGER,
    quantity     INTEGER,
    total        NUMERIC(10, 2),
    status       VARCHAR(20),
    processed_at TIMESTAMP DEFAULT NOW()
);
