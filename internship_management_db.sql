-- Drop database if it exists
DROP DATABASE IF EXISTS internship_management_db;
CREATE DATABASE internship_management_db;
USE internship_management_db;

-- Drop tables in reverse dependency order
DROP TABLE IF EXISTS internship_extensions;
DROP TABLE IF EXISTS validation_logs;
DROP TABLE IF EXISTS business_rules;
DROP TABLE IF EXISTS mentors;
DROP TABLE IF EXISTS intern_domain_assignments;
DROP TABLE IF EXISTS logs;
DROP TABLE IF EXISTS applications;
DROP TABLE IF EXISTS internships;
DROP TABLE IF EXISTS domains;
DROP TABLE IF EXISTS users;

-- Re-create users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255),
    role ENUM('admin', 'student') DEFAULT 'student',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Re-create domains table
CREATE TABLE domains (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);

-- Re-create internships table
CREATE TABLE internships (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(255),
    domain_id INT,
    start_date DATE,
    end_date DATE,
    duration INT,
    status ENUM('pending', 'approved', 'completed') DEFAULT 'pending',
    remarks TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (domain_id) REFERENCES domains(id)
);

-- Re-create applications table
CREATE TABLE applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    internship_id INT,
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
    applied_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (internship_id) REFERENCES internships(id)
);

-- Re-create logs table
CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Re-create intern_domain_assignments table
CREATE TABLE intern_domain_assignments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    domain_id INT,
    assigned_on DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (domain_id) REFERENCES domains(id)
);

-- Re-create mentors table
CREATE TABLE mentors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    expertise TEXT,
    assigned_user_id INT,
    FOREIGN KEY (assigned_user_id) REFERENCES users(id)
);

-- Re-create business_rules table
CREATE TABLE business_rules (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rule_name VARCHAR(100),
    rule_description TEXT,
    rule_type VARCHAR(50),
    value VARCHAR(255),
    domain_id INT,
    FOREIGN KEY (domain_id) REFERENCES domains(id)
);

-- Re-create validation_logs table
CREATE TABLE validation_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action TEXT,
    status VARCHAR(20),
    message TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Re-create internship_extensions table
CREATE TABLE internship_extensions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    internship_id INT,
    new_end_date DATE,
    reason TEXT,
    approved BOOLEAN DEFAULT FALSE,
    requested_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (internship_id) REFERENCES internships(id)
);