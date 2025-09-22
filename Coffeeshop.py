import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import datetime

# Database setup
conn = sqlite3.connect('coffee_shop.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    coffee_type TEXT,
    quantity INTEGER,
    price REAL,
    timestamp TEXT
)''')
conn.commit()

# Coffee menu
coffee_prices = {
    "Espresso": 80,
    "Doppio": 120,
    "Macchiato": 130,
    "Cappuccino": 100,
    "Latte": 120,
    "Flat White": 140,
    "Mocha": 150,
    "Affogato": 180,
    "Ice Coffee": 100,
    "Cold Brew": 140,
    "Nitro Coffee": 160,
    "Vietnamese Iced Coffee": 150,
    "Turkish Coffee": 160,
    "French Press": 130,
    "Drip Coffee": 90
}

# GUI setup
root = tk.Tk()
root.title("Coffee Management System")
root.attributes('-fullscreen', True)

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Load and resize image
image_path = "black.jpg"
try:
    img = Image.open(image_path)
except FileNotFoundError:
    messagebox.showerror("Image Error", f"Image file '{image_path}' not found.")
    root.destroy()
    exit()

img = img.resize((screen_width, screen_height), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)

# Set image as background
bg_label = tk.Label(root, image=photo)
bg_label.image = photo
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Overlay widgets
frame = tk.Frame(root, bg="black", bd=5)
frame.place(relx=0.5, rely=0.1, anchor="center")
tk.Label(frame, text="Welcome to Coffee Shop", font=("Arial", 24), fg="white", bg="black").pack()

tk.Label(root, text="Select Coffee Type", font=("Arial", 14), bg="black", fg="white").place(relx=0.5, rely=0.25, anchor="center")
coffee_var = tk.StringVar(root)
coffee_var.set("Espresso")
coffee_menu = tk.OptionMenu(root, coffee_var, *coffee_prices.keys())
coffee_menu.place(relx=0.5, rely=0.3, anchor="center")

tk.Label(root, text="Enter Quantity", font=("Arial", 14), bg="black", fg="white").place(relx=0.5, rely=0.35, anchor="center")
quantity_entry = tk.Entry(root)
quantity_entry.place(relx=0.5, rely=0.4, anchor="center")

# Toast Notification
def show_toast(msg):
    toast = tk.Toplevel(root)
    toast.overrideredirect(True)
    toast.configure(bg="black")
    toast.geometry(f"300x50+{screen_width//2 - 150}+{screen_height//2}")
    tk.Label(toast, text=msg, bg="black", fg="white", font=("Arial", 12)).pack(fill="both", expand=True)
    toast.after(2000, toast.destroy)

# Countdown Timer
def start_timer(seconds=5):
    countdown_label = tk.Label(root, text="", font=("Arial", 14), bg="black", fg="white")
    countdown_label.place(relx=0.5, rely=0.72, anchor="center")

    def update_timer(i):
        if i > 0:
            countdown_label.config(text=f"Preparing your coffee... {i}s")
            root.after(1000, update_timer, i - 1)
        else:
            countdown_label.config(text="Your coffee is ready!")

    update_timer(seconds)

# Receipt Generator
def generate_receipt(coffee, quantity, price, timestamp):
    receipt = f"--- Coffee Receipt ---\nCoffee: {coffee}\nQuantity: {quantity}\nTotal: ₹{price}\nTime: {timestamp}"
    messagebox.showinfo("Receipt", receipt)

# Place Order
def place_order():
    coffee = coffee_var.get()
    try:
        quantity = int(quantity_entry.get())
        price = coffee_prices[coffee] * quantity
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO orders (coffee_type, quantity, price, timestamp) VALUES (?, ?, ?, ?)",
                       (coffee, quantity, price, timestamp))
        conn.commit()
        messagebox.showinfo("Order Placed", f"{quantity} {coffee}(s) ordered.\nTotal: ₹{price}")
        show_toast(f"Order placed: {quantity} {coffee}(s)")
        start_timer()
        generate_receipt(coffee, quantity, price, timestamp)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid quantity.")

# View Orders
def view_orders():
    cursor.execute("SELECT * FROM orders")
    records = cursor.fetchall()
    output = "\n".join([f"{r[1]} x{r[2]} - ₹{r[3]} on {r[4]}" for r in records])
    messagebox.showinfo("Order History", output if output else "No orders yet.")

# View Summary
def show_summary():
    cursor.execute("SELECT SUM(price), SUM(quantity) FROM orders")
    total_sales, total_quantity = cursor.fetchone()
    cursor.execute("SELECT coffee_type, SUM(quantity) as total FROM orders GROUP BY coffee_type ORDER BY total DESC LIMIT 1")
    top_seller = cursor.fetchone()
    summary = f"Total Sales: ₹{total_sales or 0}\nTotal Cups Sold: {total_quantity or 0}"
    if top_seller:
        summary += f"\nTop Seller: {top_seller[0]} ({top_seller[1]} cups)"
    messagebox.showinfo("Sales Summary", summary)

# Buttons
tk.Button(root, text="Place Order", command=place_order, bg="#ff914d", fg="white").place(relx=0.5, rely=0.48, anchor="center")
tk.Button(root, text="View Orders", command=view_orders, bg="#4caf50", fg="white").place(relx=0.5, rely=0.54, anchor="center")
tk.Button(root, text="View Summary", command=show_summary, bg="#2196f3", fg="white").place(relx=0.5, rely=0.6, anchor="center")
tk.Button(root, text="Exit", command=root.destroy, bg="#f44336", fg="white").place(relx=0.5, rely=0.66, anchor="center")

root.mainloop()
conn.close()
