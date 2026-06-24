CREATE TABLE customers (
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    email      VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE products (
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    price      NUMERIC(10, 2) NOT NULL,
    stock      INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE orders (
    id          SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    product_id  INTEGER REFERENCES products(id),
    quantity    INTEGER NOT NULL,
    total       NUMERIC(10, 2) NOT NULL,
    status      VARCHAR(20) DEFAULT 'pending',
    created_at  TIMESTAMP DEFAULT NOW()
);
