CREATE DATABASE IF NOT EXISTS inventory_db;
USE inventory_db;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    stock INT
);

CREATE TABLE IF NOT EXISTS bills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bill_date DATE,
    total_amount DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS bill_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bill_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (bill_id) REFERENCES bills(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
