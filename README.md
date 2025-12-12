# Question 3 – Python Client-Server Application with Database

## Description
This system allows students to apply for admission using a TCP-based
Client-server application that validates and stores student details in a MySQL database.

## Architecture
- TCP client-server communication
- Multi-threaded server to handle multiple clients concurrently
- MySQL database for persistent data storage

## Components
- **Que3_server.py**  
  Creates a TCP server, handles multiple client connections using threads,
  validates input, stores data in the database, and generates unique
  application numbers.
  - **database.sql**  
  SQL script within Que3_server.py  to create the required database tables.

- **Que3_client.py**  
  Handles user input and sends it to the server over a TCP connection.

## Networking Protocol
- TCP was used to ensure reliable and ordered data transmission.

## How to Run
1. Create the tables  using `database.sql`
2. Start the server:
   ```bash
   python Que3_server.py
