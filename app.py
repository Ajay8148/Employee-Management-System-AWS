from flask import Flask, render_template, request, redirect
import boto3
import mysql.connector
import os
import config

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)

# S3 client
s3 = boto3.client("s3", region_name=config.AWS_REGION)

@app.route("/")
def home():
    cursor = db.cursor()
    cursor.execute("SELECT id, name, email FROM employees")
    employees = cursor.fetchall()
    return render_template("index.html", employees=employees)

@app.route("/add", methods=["POST"])
def add_employee():
    name = request.form["name"]
    email = request.form["email"]
    cursor = db.cursor()
    cursor.execute("INSERT INTO employees (name, email) VALUES (%s, %s)", (name, email))
    db.commit()
    return redirect("/")

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    if file:
        s3.upload_fileobj(file, config.S3_BUCKET, file.filename)
        return f"✅ File {file.filename} uploaded to S3 bucket {config.S3_BUCKET}"
    return "❌ No file selected!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
