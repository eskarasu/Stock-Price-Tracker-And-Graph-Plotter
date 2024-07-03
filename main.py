import tkinter as tk
import yfinance as yf
import matplotlib.pyplot as plt

def current_data(st):
    stock_info = yf.Ticker(st)

    try:
        # Get 1 day data
        hist = stock_info.history(period="1d")
        current_price = hist['Close'].iloc[-1]
        previous_price = hist['Open'].iloc[0]
        print(f"Stock: {st}")
        print("Current Price:", current_price)

        # Calculate daily change percentage
        change_percent = ((current_price - previous_price) / previous_price) * 100
        print("Daily Change (%):", change_percent)

        # Show the price and daily change percentage with a label
        price_label.config(text=f"Current Price: {current_price:.2f} $")
        change_label.config(text=f"Daily Change: {change_percent:.2f} %")

    except Exception as e:
        print("An error occurred:", e)

def graph_mo(st):
    stock_info = yf.Ticker(st)
    try:
        # Get 1 month data
        hist = stock_info.history(period="1mo")
        # Draw the graph
        plt.figure(figsize=(10, 4))
        plt.plot(hist.index, hist['Close'], marker='o')
        plt.title(f"{st} Stock 1 Month Closing Prices")
        plt.xlabel("Date")
        plt.ylabel("Closing Price ($)")
        plt.grid(True)
        plt.show()

    except Exception as e:
        print("An error occurred:", e)

def graph_year(st):
    stock_info = yf.Ticker(st)
    try:
        # Get 1 year data
        hist = stock_info.history(period="1y")
        # Draw the graph
        plt.figure(figsize=(10, 4))
        plt.plot(hist.index, hist['Close'], marker='o')
        plt.title(f"{st} Stock 1 Year Closing Prices")
        plt.xlabel("Date")
        plt.ylabel("Closing Price ($)")
        plt.grid(True)
        plt.show()

    except Exception as e:
        print("An error occurred:", e)

def on_submit():
    st = stock_entry.get()
    current_data(st)

def on_graph_mo():
    st = stock_entry.get()
    graph_mo(st)

def on_graph_year():
    st = stock_entry.get()
    graph_year(st)    

def create_gui():
    global root, price_label, change_label, stock_entry
    root = tk.Tk()
    root.title("Stock Application")
    root.geometry("500x400")

    canvas = tk.Canvas(root)
    canvas.pack(fill="both", expand=True)

    bg = tk.PhotoImage(file="background_image.png")
    canvas.create_image(0, 0, image=bg, anchor="nw")

    stock_entry_label = tk.Label(root, text="Stock Code:", bg="white", fg="black")
    stock_entry_label_window = canvas.create_window(100, 20, window=stock_entry_label)

    stock_entry = tk.Entry(root)
    stock_entry_window = canvas.create_window(250, 20, window=stock_entry)

    button_submit = tk.Button(root, text="Submit", command=on_submit)
    button_submit_window = canvas.create_window(250, 50, window=button_submit)

    button_graph = tk.Button(root, text="Show one month graph", command=on_graph_mo)
    button_graph_window = canvas.create_window(100, 50, window=button_graph)

    button_graph = tk.Button(root, text="Show one year graph", command=on_graph_year)
    button_graph_window = canvas.create_window(100, 80, window=button_graph)

    price_label = tk.Label(root, text="Current Price: ", bg="white", fg="black")
    price_label_window = canvas.create_window(400, 20, window=price_label)

    change_label = tk.Label(root, text="Daily Change: ", bg="white", fg="black")
    change_label_window = canvas.create_window(400, 50, window=change_label)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
