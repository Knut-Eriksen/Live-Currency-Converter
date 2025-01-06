import tkinter as tk
from tkinter import ttk
import requests

def convert_currency():
    amount = float(amount_entry.get())
    base_currency = from_currency.get()
    target_currency = to_currency.get()

    rate = fetch_exchange_rate(api_key, base_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        result_label.config(text=f"{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        result_label.config(text="Error fetching exchange rate!")


def fetch_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    return data["conversion_rates"].get(target_currency)


# API key
api_key = "7cf6fa21a788ffb5d4f249a5"

# GUI
root = tk.Tk()
root.geometry("400x300")

root.title("Live Currency Converter")

# Input
tk.Label(root, text="Amount:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="From:").grid(row=1, column=0)
from_currency = ttk.Combobox(root, values=["USD", "EUR", "GBP", "INR", "NOK"])
from_currency.grid(row=1, column=1)
from_currency.set("USD")

tk.Label(root, text="To:").grid(row=2, column=0)
to_currency = ttk.Combobox(root, values=["USD", "EUR", "GBP", "INR", "NOK"])
to_currency.grid(row=2, column=1)
to_currency.set("EUR")

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2)

# Result
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
