import sqlite3
import os
import datetime

# create a menu so that the user can: choose to add or delete an entry from the database, review the entries, or find the total stocks bought/sold by this user/other users.

conn = sqlite3.connect('shurl_base.db')

data = conn.cursor()




data.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')

menu = [
    "a. Insert stock entry", 
    "b. View Total Entries", 
    "c. Search for an Entry", 
    "d. Delete an Entry",
    "e. Exit"
]
print(menu)
q = input("What would you like to do?")
print(q)

def catchselect(selection:str):
    match selection:
        case "a":
            buy_stock()
        case "b":
            viewing()
        case "c":
            ...
        case "d":
            ...
        case "e":
            quit
        case default:
            print("Please choose an option.")
            q

conn.commit()
def buy_stock():
    date_text = input('Enter date in YYYY-MM-DD format: ')                                       # I haven't figured out how to add the dashes (////-//-//) so I'll cut out the spaces
    year, month, day = map(int, date_text.split('-'))
    date1 = datetime.date(year, month, day)
    if len(date_text) == 10 and date_text[5] == "-" and date_text[7] == "-":
        date_text = True
    else:
        date_text = False
        print("Please enter the date in that exact format.")
        date_text

    if date1 == str:                                                                             # Validation if user inputs a str
        print("Invalid entry.")
        date_text = int(input("Enter date, YYYY-MM-DD: "))

    trans_text = input("Enter whether you are BUYing or SELLing this stock: ").upper()
    if trans_text != "BUY" or "SELL":                                                            # User has to input action as uppercase to stand out in database
        print("Invalid entry. Either BUY or SELL.")
        trans_text = input("Enter whether you are BUYing or SELLing this stock: ")


    stockName = input("Enter the stock name abbreviations: ")                                    # The maximum is at 9 because of stocks like NYSE:NEE and others in New York
    if len(stockName) < 1 or len(stockName) > 9:
        print("Invalid entry.")
        stockName = input("Enter the stock name abbreviations: ")

    qty_real = int(input("Enter how many stocks to be bought: "))                                # The maximum is at 1000 because this is a test of the database working properly. Later, I will add menu and option to delete previous entries.
    if qty_real < 1 or qty_real > 1000:
        print("Invalid entry.")
        qty_real = int(input("Enter how many stocks to be bought: "))

    price_real = float(input("Enter how much each stock cost: "))
    if price_real < 0:
        print("Invalid entry.")
        price_real = input("Enter how much each stock cost: ")
    elif price_real > 630000:
        print("Unless you bought from Berkshire Hathaway (BRK.A),")                              # This is a joke. In March 2023, Berkshire had the highest stock price of that year, $536,000 per share. 
        print("the stock price shouldn't exceed $500,000.")
        price_real = int(input("Enter how much each stock cost: "))

    print(f"The stock you entered was {stockName}, you are {trans_text}ing {qty_real} stocks. Each stock costs {price_real}.")
    print("*********************************************************************************")
    data.execute(f"INSERT INTO stocks VALUES ('{date1}','{trans_text}','{stockName}',{qty_real},{price_real})")


def viewing():
    men_view = [
        "a. stockName",
        "b. Sale",
        "c. price",
        "d. Sale date"
    ]
    view = input("What do you want to view in the database? ")
    if view == "a" or "A":
        view_n = input("Name: ")
        data.execute(f'SELECT {view_n} FROM stocks')
        print(data.fetchall())
        conn.commit()
        conn.close()
    elif view == "c" or "C":
	    view_p = input ("Price range: ")
		    num_1 = float(input("Enter the first price:"))
			num_2 = float(input("Enter the first price:"))
                def validate_data(record):
                    if view_p != isinstance(record):
                        return False, "Invalid record format."
                    else:
                        continue
			    price_r = range(num_1,num_2)
			    data.execute(f'SELECT {price_r} FROM stocks')
			    print(data.fetchall())
	elif view == "d" or "D":
		 view_q = input ("Time frame: ")
			 time_1 = float(input("Enter first time frame: "))
			 time_2 = float(input("Enter the second time frame: "))
			 if time_1 != #not on the list/in the database or time_2 != not on the list/in the database:
				 
    

    for row in data.fetchall():
        print(row)

menq = [
        "a. Entry Date",
        "b. Sale",
        "c. Name of stock",
        "d. cost range."
        "e. Homepage"
]
def searching():
    look = input("What do you want to search under? ")
    def lookselect(selection:str):
        match selection:
            case "a":
                time_r = float(input("Please input a range to under: "))                        # I intend to show the list by range via time frame vs YYYY for ease of access for the user and my laptop. 
                ...
                data.execute('SELECT date_text FROM stocks')
            case "b":
                ...
                data.execute('SELECT trans_text FROM stocks')
            case "c":
                name_r = input("Please enter the name of the stock: ")
                if len(name_r) < 1 or len(name_r) > 9:
                    print("Invalid entry.")
                    name_r                                                                      # I'm not sure if the stock name on file will be retrieved if the variable used here is under another name.
                data.execute('SELECT name_r FROM stocks')                                       # I'll use "temp" and swap the 2 variable values (unsure if swapping works with str)
            case "d":
                ...                                                                             # Same situation as the time_r variable, ease of access on user and my laptop
            case "e":
                ...
            case default:
                print("Please choose an option.")
    data.execute('SELECT * FROM stocks')
conn.close()
