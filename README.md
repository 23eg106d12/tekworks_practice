# Online Complaint Management System

## Description
A Streamlit-based web application where users can submit complaints and an admin can track and update complaint status.

## Features
- User complaint registration
- Auto-generated complaint ID
- Admin dashboard
- Update complaint status (Open / In Progress / Closed)
- Search complaint by ID

## Tech Stack
- Python
- Streamlit
- MySQL

## Database Schema
Table: complaints  
- id
- name
- email
- category
- description
- status
- created_at

## How to Run

### 1. Create Database
```sql
SOURCE schema.sql;
