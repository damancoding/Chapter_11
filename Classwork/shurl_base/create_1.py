import sqlite3

conn = sqlite3.connect('shurl_base.db')

data = conn.cursor()

data.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')

stockName = input("Enter a stock name: ")
print(f"The stock you entered was {stockName}.")

data.execute("INSERT INTO stocks VALUES ('2024-04-10','BUY','RKLB',100,3.74)")

conn.commit()

data.execute('SELECT * FROM stocks')

for row in data.fetchall():
    print(row)

conn.close()