# Amanda M.
# validation for each user input
# date is 2024-04-12, test stock is NYSE:NEE, current price: 63.08, BUY, qty = 10 
import sqlite3
import datetime

# create a menu so that the user can: choose to add or delete an entry from the database, review the entries, or find the total stocks bought/sold by this user/other users.

conn = sqlite3.connect('shurl_base.db')

data = conn.cursor()

data.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')


date_text = input('Enter date in YYYY-MM-DD format: ')                                       # I haven't figured out how to add the dashes (////-//-//) so I'll cut out the spaces
year, month, day = map(int, date_text.split('-'))
date1 = datetime.date(year, month, day)

if date1 == str:
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
elif price_real > 5000000:
    print("Unless you bought from Berkshire Hathaway (BRK.A),")                              # This is a joke. In March 2023, Berkshire had the highest stock price of that year, $536,000 per share. 
    print("the stock price shouldn't exceed $500,000.")
    price_real = int(input("Enter how much each stock cost: "))

print(f"The stock you entered was {stockName}, you are {trans_text}ing {qty_real} stocks. Each stock costs {price_real}.")
print("*********************************************************************************")
data.execute(f"INSERT INTO stocks VALUES ('{date1}','{trans_text}','{stockName}',{qty_real},{price_real})")



conn.commit()

data.execute('SELECT * FROM stocks')

for row in data.fetchall():
    print(row)

conn.close()
