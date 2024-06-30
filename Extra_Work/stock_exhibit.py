# Amanda Mam.
# 4/23/2024
# Final Project draft
import sqlite3
import datetime


# menu is c.r.u.d or  Create, Read, Update, Delete
# create a menu so that the user can: choose to add or delete an entry from the database, review the entries, or find the total stocks bought/sold by this user/other users.

conn = sqlite3.connect('shurl_base.db')

data = conn.cursor()

data.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, sale text, symbol text, qty real, price real, yield real)''')

conn.commit()

def buy_stock():
    date_text = input('Enter date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_text.split('-'))

    if len(date_text) != 10:
        print("Invalid entry.2")
        date_text

    sale_text = str.upper(input("Enter whether you are buying or selling this stock: "))
    if sale_text == "BUY" or "SELL":
        print("Valid Entry.")
        pass

    stockName = str.upper(input("Enter the stock name abbreviations: "))                          # The maximum is at 9 because of stocks like NYSE:NEE and others based in New York
    if len(stockName) < 1 or len(stockName) > 9:
        print("Invalid entry.1")
        stockName = input("Enter the stock name abbreviations: ")
    elif stockName != str:
        print("Invalid entry.2")
        stockName = input("Enter the stock name abbreviations: ")
    elif stockName[5] == ":":                                                                     # This pass is specifically for the semicolons in NYSE based companies           
        pass

    qty_real = int(input("Enter how many stocks to be bought: "))
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

    print(f"The stock you entered was {stockName}, you are {sale_text}ing {qty_real} stocks. Each stock costs {price_real}.")
    print("*********************************************************************************")
    data.execute(f"INSERT INTO stocks VALUES ('{date_text}','{sale_text}','{stockName}',{qty_real},{price_real}, yield.)")
    conn.commit()
    for row in data.fetchall():
        print(row)
    main()


def viewing():                                                                                    # Update: fix the viewing system by displaying everything
    men_u = [
        "a. Trades",
        "b. Stock name",
        "c. Homepage",
    ]
    print(men_u)
    u = input("Choose options (a, b, c): ")
    print(u)
    match u:
        case "a":
            sedarT = input("Enter whether you bought or sold (buy or sell): ")                    # New problem: "no such column". Doesn't matter if you entered buy or sell.  
            trade = (f'SELECT {sedarT} FROM stocks WHERE sale_text = {sedarT}')                   # Add-on: Changed name of column to sale, splitting sale column into 2 columns: buy or sell
            data.execute(trade)
            print(f"Trades: {sedarT}")
            output = data.fetchall()
            for row in output:
                print(row)

        case "b":
            eman = input("Enter name of stock: ")
            name = (f'SELECT {eman} FROM stocks WHERE stockName = {eman}')
            data.execute(name)
            output = data.fetchall()
            for row in output:
                print(row)

        case "c":
            main()                

   # for row in data.fetchall():
   #     print(row)
    main()

def updating():                                                                                 # I need to work on everything in this section.
    menq = [
        "a. Entry Date",
        "b. Trades",
        "c. Name of stock",
        "d. Homepage"
    ]
    print(menq)
    look = input("What do you want to search under? ")
    def lookselect(selection:str):
        match selection:
            case "a":
                mm = [('January' or 'january'), ('February' or 'february'), ('March' or 'march'), ('April' or 'april'), ('May'), ('June' or 'june'), ('August'), ('September' or 'september'), ('October'), ('November' or 'november'), ('December')]
                time_r = float(input("Choose year, month, or week to enter: "))
                if time_r == "year":
                    time_s = int(input("Enter year: "))
                    if time_s in range(2023, 2025):
                        print(data.execute(f'SELECT {time_s} FROM date_text'))
                    else:
                        print("Entry not found. Please enter another year.")
                        time_s = int(input("Enter year: "))
                elif time_r == "month":
                    for time_s in range(1,12) or mm:
                        if time_s is range(1,12) or mm:
                            for i, item in enumerate(time_s):
                                mm_sql = 'SELECT time_s FROM date_text'
                                data.execute(mm_sql)
                                mmresult = data.fetchall()
                                for x in mmresult:
                                    print(x)
                                    updating()
                        else:
                            print("No items in that month.")
                            mm
                            time_r
                            updating()
                elif time_r == "week":
                    mm
                    p_month = input("Please enter a month to search under: ")
                    men_w = men_w()
                    while True:
                        print("1. Week 1")
                        print("2. Week 2")
                        print("3. Week 3")
                        print("4. Week 4")                    
                        p_week = input("Please whick week to search under: ")
                        q_wk1 = (1,7)
                        q_wk2 = (8,14)
                        q_wk3 = (15,21)
                        q_wk4 = (22,30)
                        if p_week == 1:
                            data.execute(f'SELECT * FROM date_text where {p_week} == {q_wk1}')
                        elif p_week == 2:
                            data.execute(f'SELECT * FROM date_text where {p_week} == {q_wk2}')
                        elif p_week == 3:
                            data.execute(f'SELECT * FROM date_text where {p_week} == {q_wk3}')
                        elif p_week == 4:
                            data.execute(f'SELECT * FROM date_text where {p_week} == {q_wk4}')
                        else:
                            print("Please choose an option from Menu.")
            case "b":
                trades_q = input("Did you buy or sell item: ")
                sql = 'SELECT trades_q FROM sale_text'
                data.execute(sql)
                myresult = data.fetchall()
                for x in myresult:
                    print(x)
                    updating()
            case "c":
                name_r = input("Please enter the name of the stock: ")
                if len(name_r) < 1 or len(name_r) > 9:
                    print("Invalid entry.")
                    name_r                                                                      # I'm not sure if the stock name on file will be retrieved if the variable used here is under another name.
                else:
                    data.execute('SELECT name_r FROM stocks')
                    updating()
            case "d":
                main()
            case default:
                print("Please choose an option.")
                updating()

def deleting():                                                                                 # I need to work on this after updating()
    print("deleting...")
    main()

def main():
    menu = [
        "a. Create a stock entry", 
        "b. View Total Entries", 
        "c. Update an Entry", 
        "d. Delete an Entry",
        "e. Exit"
        ]
    print(menu)
    q = input("What would you like to do? ")

    def catchselect(selection:str):
        match selection:
            case "a":
                buy_stock()
            case "b":
                viewing()
            case "c":
                updating()
            case "d":
                deleting()
            case "e":
                quit
            case default:
                print("Please choose an option.")
                print(menu)
                q = input("What would you like to do? ")
    catchselect(q)


main()
conn.close()
# next add-on: Probable yields. This is based off of NASDAQ system and will be multiplying current cost/ P/E Ratio to yield.
