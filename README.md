# 📊 Sales Data Processing Project (SQL & Pandas Implementation)

## 📌 Project Overview

This project implements a complete data processing workflow based on a predefined ER diagram consisting of four relational tables:

- Customer
- Orders
- Sales
- Items

Sales Data Processing Project is a structured data engineering workflow based on an ER diagram with four tables: Customer, Orders, Sales, and Items. The schema strictly follows defined relationships and foreign key constraints to maintain relational integrity.

The goal is to generate a customer-item level purchase summary in a strictly formatted CSV file. The output must use a semicolon delimiter and the exact header: Customer;Age;Item;Quantity. Quantity must not contain decimals, NULL must represent not purchased, zero totals must be excluded, and column order must remain unchanged.

The project includes two independent implementations: a pure SQL solution that performs joins and aggregation inside the database, and a Pandas-based Python solution that processes data at the application layer. Both approaches produce identical validated output.

The implementation follows modular design, reusable functions, proper error handling, clean structure, and professional version control practices, resulting in a production-ready repository.

### Author

Prashant Bhoje
Data Engineer
