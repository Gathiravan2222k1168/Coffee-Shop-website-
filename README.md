# Coffee-Shop-website-
Coffee shop - python + OpenCv that Renders Place Order, View Order, View Summary, Exit using image processing
Coffee Management System

A desktop-based Coffee Shop Management System built using Python (Tkinter), SQLite, and PIL (Pillow).
It allows coffee shop owners to manage orders, generate receipts, and track sales in a simple and interactive GUI.

🚀 Features

📋 Coffee Menu – Supports multiple coffee types with predefined prices

🛒 Place Orders – Select coffee type, enter quantity, and place orders

💾 Database Storage – Orders are stored persistently using SQLite

🧾 Receipt Generator – Generates a receipt with order details and timestamp

🔔 Toast Notification & Countdown – Displays notifications and preparation countdown

📜 Order History – View all past orders

📊 Sales Summary – Displays total sales, cups sold, and top-selling coffee

🎨 Full-Screen UI with Background Image

🖼️ Screenshots

(Add your screenshots here after running the project, e.g. screenshots/home.png, screenshots/order.png)

🛠️ Tech Stack

Python – Core programming language

Tkinter – GUI framework

SQLite3 – Lightweight database

Pillow (PIL) – Image handling

📂 Project Structure
Coffee-Management-System/
│── coffee_shop.py        # Main application file
│── coffee_shop.db        # SQLite database (auto-created)
│── black.jpg             # Background image
│── README.md             # Documentation
│── requirements.txt      # Project dependencies

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/Coffee-Management-System.git
cd Coffee-Management-System


Install dependencies:

pip install -r requirements.txt


(requirements.txt should contain:)

pillow


Run the application:

python coffee_shop.py

📊 Database

Database file: coffee_shop.db

Table: orders

id – Order ID

coffee_type – Type of coffee

quantity – Number of cups

price – Total price

timestamp – Order time

📌 Future Enhancements

🖨️ Print / Save receipt as PDF

👩‍💼 User authentication for staff

💳 Payment gateway integration

📱 Mobile-friendly version
