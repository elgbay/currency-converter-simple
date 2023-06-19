# import necessary libraries
import requests
from tkinter import Tk, Label, Entry, StringVar, Button, OptionMenu, ttk

# A list of common currencies.
currencies = [
    'AUD',
    'CAD',
    'EUR',
    'GBP',
    'JPY',
    'USD',
    'Other...'
]

# Function to get exchange rate from an API
def get_exchange_rate(source_currency, target_currency):
    api_key = 'your-api-key'  # replace with your actual API key
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{source_currency}/{target_currency}'

    response = requests.get(url)  # make GET request to the API
    data = response.json()  # get the JSON data from the response

    # Check if the request was successful
    if data['result'] == 'success':
        # Return the conversion rate
        return data['conversion_rate']
    else:
        # If there was an error, print it and return None
        print(f"Error: {data['error-type']}")
        return None


# Function to get user input from the console
def get_user_input():
    source_currency = input("Enter the source currency code: ")
    target_currency = input("Enter the target currency code: ")
    amount = float(input("Enter the amount you want to convert: "))
    return source_currency, target_currency, amount

# Function to convert the currency
def convert_currency():
    source_currency, target_currency, amount = get_user_input()
    exchange_rate = get_exchange_rate(source_currency, target_currency)

    # If the exchange rate was successfully fetched, do the conversion
    if exchange_rate:
        converted_amount = amount * exchange_rate
        print(f"{amount} {source_currency} is equivalent to {converted_amount} {target_currency}.")
    else:
        print("Conversion failed. Please check the provided currency codes and try again.")


# Function to convert the currency using GUI
def convert_currency_gui():
    # Get the user input from the GUI
    source_currency = source_currency_var.get()
    target_currency = target_currency_var.get()
    amount = float(amount_var.get())
    
    # Check if the user selected 'Other...', if so, get the entered currency code
    if source_currency == "Other...":
        source_currency = input_source_currency_var.get()
    if target_currency == "Other...":
        target_currency = input_target_currency_var.get()

    # Fetch the exchange rate
    exchange_rate = get_exchange_rate(source_currency, target_currency)

    # If the exchange rate was successfully fetched, do the conversion and display the result in the GUI
    if exchange_rate:
        converted_amount = amount * exchange_rate
        result_var.set(f"{amount} {source_currency} is equivalent to {converted_amount} {target_currency}.")
    else:
        result_var.set("Conversion failed. Please check the provided currency codes and try again.")


# Initialize the Tkinter GUI
root = Tk()
root.title("Currency Converter")

style = ttk.Style(root)
style.theme_use('clam')  # Use the 'clam' theme. You can experiment with 'default', 'classic', 'alt', etc.

# Initialize the variables for the GUI
source_currency_var = StringVar()
target_currency_var = StringVar()
input_source_currency_var = StringVar()
input_target_currency_var = StringVar()
amount_var = StringVar()
result_var = StringVar()
# Set up the GUI
ttk.Label(root, text="Source Currency").grid(row=0, column=0)
# Dropdown menu for source currency selection
source_currency_option = ttk.OptionMenu(root, source_currency_var, *currencies)
source_currency_option.grid(row=0, column=1)
# Entry field for source currency if 'Other...' is selected
source_currency_entry = ttk.Entry(root, textvariable=input_source_currency_var)
source_currency_entry.grid(row=0, column=2)

ttk.Label(root, text="Target Currency").grid(row=1, column=0)
# Dropdown menu for target currency selection
target_currency_option = ttk.OptionMenu(root, target_currency_var, *currencies)
target_currency_option.grid(row=1, column=1)
# Entry field for target currency if 'Other...' is selected
target_currency_entry = ttk.Entry(root, textvariable=input_target_currency_var)
target_currency_entry.grid(row=1, column=2)

ttk.Label(root, text="Amount").grid(row=2, column=0)
# Entry field for the amount to be converted
ttk.Entry(root, textvariable=amount_var).grid(row=2, column=1)

# Convert button which triggers the conversion function when clicked
ttk.Button(root, text="Convert", command=convert_currency_gui).grid(row=3, column=0, columnspan=2)

ttk.Label(root, text="Result").grid(row=4, column=0)
# Label to display the conversion result
ttk.Label(root, textvariable=result_var).grid(row=4, column=1)

# Start the GUI event loop
root.mainloop()
