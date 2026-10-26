import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

products = {
    "Wireless Mouse": {"Amazon": 599, "Flipkart": 549, "Meesho": 499},
    "Headphones": {"Amazon": 1499, "Flipkart": 1399, "Meesho": 1299},
    "Keyboard": {"Amazon": 899, "Flipkart": 849, "Meesho": 799},
    "Power Bank": {"Amazon": 1199, "Flipkart": 1099, "Meesho": 999}
}

bg = "#e8f4fd"
blue = "#0d47a1"


def compare():
    name = choice.get()
    prices = products[name]

    for row in table.get_children():
        table.delete(row)

    cheap_app = min(prices, key=prices.get)
    low = min(prices.values())
    high = max(prices.values())

    for app, price in prices.items():
        tag = "cheap" if app == cheap_app else "normal"
        table.insert("", "end", values=(app, "Rs. " + str(price)), tags=(tag,))

    result.config(text="Lowest price: " + cheap_app + " - Rs. " + str(low))
    saving.config(text="Price difference: Rs. " + str(high - low))


def sort_prices():
    name = choice.get()
    data = list(products[name].items())

    # Bubble sort
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j][1] > data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    for row in table.get_children():
        table.delete(row)

    for i, (app, price) in enumerate(data):
        tag = "cheap" if i == 0 else "normal"
        table.insert("", "end", values=(app, "Rs. " + str(price)), tags=(tag,))


def show_graph():
    name = choice.get()
    prices = products[name]

    win = tk.Toplevel(root)
    win.title("Price Comparison Graph")
    win.geometry("600x400")

    fig, ax = plt.subplots(figsize=(6, 4))

    apps = list(prices.keys())
    amounts = list(prices.values())

    bars = ax.bar(apps, amounts, color=["orange", "blue", "purple"])
    ax.set_title(name + " Price Comparison")
    ax.set_xlabel("Shopping Apps")
    ax.set_ylabel("Price in Rupees")
    ax.bar_label(bars)

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


root = tk.Tk()
root.title("Online Price Analyzer")
root.geometry("650x520")
root.configure(bg=bg)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", rowheight=30, font=("Arial", 11))
style.configure(
    "Treeview.Heading",
    background=blue,
    foreground="white",
    font=("Arial", 11, "bold")
)

heading = tk.Label(
    root,
    text="ONLINE PRICE ANALYZER",
    font=("Arial", 20, "bold"),
    bg=blue,
    fg="white",
    width=30
)
heading.pack(pady=15)

tk.Label(
    root,
    text="Select a product to compare prices",
    font=("Arial", 11),
    bg=bg
).pack()

choice = ttk.Combobox(
    root,
    values=list(products.keys()),
    state="readonly",
    width=25
)
choice.pack(pady=10)
choice.set("Wireless Mouse")
choice.bind("<<ComboboxSelected>>", lambda event: compare())

table = ttk.Treeview(
    root,
    columns=("app", "price"),
    show="headings",
    height=5
)
table.heading("app", text="Shopping App")
table.heading("price", text="Price")
table.column("app", width=250, anchor="center")
table.column("price", width=250, anchor="center")

table.tag_configure("cheap", background="#c8e6c9", foreground="#1b5e20")
table.tag_configure("normal", background="#fff9c4")
table.pack(pady=10)

result = tk.Label(
    root, text="", font=("Arial", 12, "bold"),
    bg=bg, fg="#2e7d32"
)
result.pack(pady=5)

saving = tk.Label(
    root, text="", font=("Arial", 11),
    bg=bg, fg="#c62828"
)
saving.pack(pady=3)

buttons = tk.Frame(root, bg=bg)
buttons.pack(pady=15)

tk.Button(
    buttons, text="Sort by Price",
    command=sort_prices, bg="orange",
    fg="white", width=14
).grid(row=0, column=0, padx=5)

tk.Button(
    buttons, text="Show Graph",
    command=show_graph, bg="#4caf50",
    fg="white", width=14
).grid(row=0, column=1, padx=5)

tk.Button(
    buttons, text="Compare Again",
    command=compare, bg="#2196f3",
    fg="white", width=14
).grid(row=0, column=2, padx=5)

compare()
root.mainloop()