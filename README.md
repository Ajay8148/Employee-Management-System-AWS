# Employee-Management-System-AWS

A simple **Employee Management System** built with **Python Flask**, **MySQL RDS**, and **AWS S3** for document storage.

## Features

- CRUD operations for Employees
- Leave management system
- Document uploads to AWS S3
- MySQL RDS as backend database
- Configurable via `config.py`

## Prerequisites

- Python 3.x
- MySQL Connector (`pip install mysql-connector-python`)
- AWS credentials with S3 access
- RDS MySQL database

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Ajay8148/Employee-Management-System-AWS.git
cd Employee-Management-System-AWS

employee-management/
│── app.py               # Main Flask app
│── requirements.txt     # Python dependencies
│── templates/           # HTML templates
│── static/              # CSS/JS files
│── config_example.py    # Sample config file (no secrets)
│── README.md
│── .gitignore

pip3 install -r requirements.txt

cp config_example.py config.py

Edit config.py with your RDS & S3 credentials:

DB_HOST = "<RDS endpoint>"
DB_USER = "appuser"
DB_PASSWORD = "<password>"
DB_NAME = "employee_db"

S3_BUCKET = "<your-bucket-name>"
AWS_ACCESS_KEY_ID = "<your-access-key>"
AWS_SECRET_ACCESS_KEY = "<your-secret-key>"

Sample app.py snippet to test DB

from flask import Flask
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

app = Flask(__name__)

try:
    db = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    print("Connected to database successfully!")
except mysql.connector.Error as err:
    print(" Error:", err)

@app.route("/")
def home():
    return "Employee Management System Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

--->python3 app.py

push to Github
cd employee-management
git init
git add .
git commit -m "Initial commit: Employee Management System"
git remote add origin https://github.com/username/Employee-Management-System-AWS.git
git branch -M main
git push -u origin main

