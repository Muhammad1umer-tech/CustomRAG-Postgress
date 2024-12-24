In order to add the new data,
add new csv to server.
compose down
remove pgvector image
up

Step 1: Check if PostgreSQL is Installed
Run the following command to see if PostgreSQL is installed:

bash
Copy code
psql --version
If PostgreSQL is installed, it will display the version (e.g., psql (PostgreSQL) 14.7).
If it is not installed, you'll see a message like psql: command not found.
Alternatively, you can check for PostgreSQL packages using:

bash
Copy code
dpkg -l | grep postgresql
Step 2: Install PostgreSQL
If PostgreSQL is not installed, follow these steps to install it:

Update the Package Index:

bash
Copy code
sudo apt update
Install PostgreSQL: Use the following command to install PostgreSQL:

bash
Copy code
sudo apt install -y postgresql postgresql-contrib
Check PostgreSQL Service Status: After installation, ensure the PostgreSQL service is running:

bash
Copy code
sudo systemctl status postgresql
Look for Active: active (running) to confirm the service is running.
