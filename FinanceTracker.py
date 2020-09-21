from tkinter.ttk import Combobox
import sqlite3
from tkinter import *
import datetime
from tkinter import messagebox


# Welcome
class Welcome:
    def __init__(self, master):
        # Welcome windows
        self.master = master
        self.master.geometry('1000x700')
        # self.master.attributes("-fullscreen", True)
        self.master.title('Finance tracker by Enrico Garaiman 2020')
        self.master.config(bg='#80b3ff')
        self.frame = Frame(self.master, bg='#80b3ff')
        self.frame.pack()
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # Labels
        self.label1 = Label(self.frame, text='Hi! Your options:', fg='#ffffff', bg='#80b3ff', font=20, padx=20, pady=20)
        self.label1.grid(row=0, column=0)

        # Buttons
        self.add_transaction = Button(self.frame, text='Add your transaction', command=self.insert_into_database,
                                      bg='#0052cc', fg='#ffffff', padx=20, pady=20, font=20, width=30)
        self.add_transaction.grid(row=1, column=0, padx=20, pady=20)
        self.see_transaction = Button(self.frame, text='See last transaction', command=self.see_transaction_function,
                                      bg='#0052cc', fg='#ffffff', padx=20, pady=20, font=20, width=30)
        self.see_transaction.grid(row=2, column=0, padx=20, pady=20)
        self.see_balance = Button(self.frame, text='See your balance', command=self.balance,
                                  bg='#0052cc', fg='#ffffff', padx=20, pady=20, font=20, width=30)
        self.see_balance.grid(row=3, column=0, padx=20, pady=20)
        self.exit = Button(self.frame, text='Exit', command=self.exit,
                           bg='#e60000', fg='#ffffff', padx=20, pady=20, font=20, width=30)
        self.exit.grid(row=4, column=0, padx=20, pady=20)

    def exit(self):
        self.master.destroy()

    def insert_into_database(self):
        root2 = Toplevel(self.master)
        Insert(root2)

    def see_transaction_function(self):
        root2 = Toplevel(self.master)
        Transaction(root2)

    def balance(self):
        root2 = Toplevel(self.master)
        Balance(root2)


# Insert transactions
class Insert:
    def __init__(self, master):
        # Window
        self.master = master
        self.master.geometry('1000x700')
        self.master.title('Insert your transaction | Finance Tracker by Enrico Garaiman 2020')
        self.frame = Frame(self.master, bg='#80b3ff')
        self.frame.pack()
        self.frame.place(relx=0.5, rely=0.5, anchor='center')
        self.master.config(bg='#80b3ff')

        # Initialisation
        self.type1 = StringVar()
        self.type2 = StringVar()
        self.val = StringVar()

        # Type frame
        self.type_label = Label(self.frame, text='Income/Cost', fg='#ffffff', bg='#80b3ff', font=20, padx=20, pady=20)
        self.type_label.grid(row=0, column=0)
        self.type_label = Label(self.frame, text='*', fg='#e60000', bg='#80b3ff', font=20, pady=20)
        self.type_label.grid(row=0, column=1)
        self.type_income = Radiobutton(self.frame, text='Income', value='Income', variable=self.type1, bg='#80b3ff',
                                       font=20, padx=20, pady=20, activebackground='#80b3ff', command=self.set_options)
        self.type_income.grid(row=0, column=2)
        self.type_cost = Radiobutton(self.frame, text='Cost', value='Cost', variable=self.type1, bg='#80b3ff', font=20,
                                     padx=20, pady=20, activebackground='#80b3ff', command=self.set_options)
        self.type_cost.grid(row=0, column=3)

        # Cash or Card frame
        self.cash_card_label = Label(self.frame, text='Cash/Card', fg='#ffffff', bg='#80b3ff', font=20, padx=20,
                                     pady=20)
        self.cash_card_label.grid(row=1, column=0)
        self.type_label = Label(self.frame, text='*', fg='#e60000', bg='#80b3ff', font=20, pady=20)
        self.type_label.grid(row=1, column=1)
        self.type_cash = Radiobutton(self.frame, text='Cash', value='Cash', variable=self.type2, bg='#80b3ff', font=20,
                                     padx=20, pady=20, activebackground='#80b3ff')
        self.type_cash.grid(row=1, column=2)
        self.type_card = Radiobutton(self.frame, text='Card', value='Card', variable=self.type2, bg='#80b3ff', font=20,
                                     padx=20, pady=20, activebackground='#80b3ff')
        self.type_card.grid(row=1, column=3)

        # Category frame
        self.value_label = Label(self.frame, text='Category', fg='#ffffff', bg='#80b3ff', font=20, padx=20,
                                 pady=20)
        self.value_label.grid(row=2, column=0)
        self.type_label = Label(self.frame, text='*', fg='#e60000', bg='#80b3ff', font=20, pady=20)
        self.type_label.grid(row=2, column=1)
        n = StringVar()
        self.categorychoosen = Combobox(self.frame, width=28, textvariable=n, font=20)
        self.categorychoosen['values'] = 'Choose_Income_or_Cost_first'
        self.categorychoosen.grid(row=2, column=2, columnspan=2)

        # Value frame
        self.value_label = Label(self.frame, text='Transaction value', fg='#ffffff', bg='#80b3ff', font=20, padx=20,
                                 pady=20)
        self.value_label.grid(row=3, column=0)
        self.type_label = Label(self.frame, text='*', fg='#e60000', bg='#80b3ff', font=20, pady=20)
        self.type_label.grid(row=3, column=1)
        self.value = Entry(self.frame, textvariable=self.val, bg='#80b3ff', font=20, width=30)
        self.value.grid(row=3, column=2, columnspan=2)

        # An optional comment frame
        self.optional_comment_label = Label(self.frame, text='Optional comment', fg='#ffffff', bg='#80b3ff', font=20,
                                            padx=20, pady=20)
        self.optional_comment_label.grid(row=4, column=0)
        self.optional_comment = Entry(self.frame, bg='#80b3ff', font=20, width=30)
        self.optional_comment.grid(row=4, column=2, columnspan=2)

        # Validate user inputs
        self.type1.trace("w", self.validate)
        self.type2.trace("w", self.validate)
        self.val.trace('w', self.validate)

        # Button frame
        self.return_button = Button(self.frame, text='Return to menu', command=self.master.destroy, fg='#ffffff',
                                    font=20, bg='#e60000', padx=20, pady=20)
        self.return_button.grid(row=5, column=0, columnspan=2, sticky='we')
        self.submit_button = Button(self.frame, text='Add your transaction', command=self.insert_into_database,
                                    fg='#ffffff', bg='#000000', font=20, padx=20, pady=20, state='disabled')
        self.submit_button.grid(row=5, column=2, columnspan=2, sticky='we')

    # Set options for category label
    def set_options(self):
        if self.type1.get() == 'Income':
            self.categorychoosen['values'] = (' Salary',
                                              ' Bonus',
                                              ' Gift',
                                              ' Another income')
        elif self.type1.get() == 'Cost':
            self.categorychoosen['values'] = (' Transport',
                                              ' Food',
                                              ' Clothes',
                                              ' Health',
                                              ' Electronics',
                                              ' Car',
                                              ' Utilities',
                                              ' Another cost')

    # Function for insert transaction into the database
    def insert_into_database(self):
        value = self.value.get()
        type1 = self.type1.get()
        type2 = self.type2.get()
        categorychoosen = self.categorychoosen.get()
        category = [' Salary', ' Bonus', ' Gift', ' Another income', ' Transport', ' Food', ' Clothes', ' Health',
                    ' Electronics', ' Car', ' Utilities', ' Another cost']

        # Connect to database and create tables if not exists
        conn = sqlite3.connect('transaction.db')
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS trans(ID n(6), date char(30), type char(6), card_cash char(4), category char("
            "30), "
            "value real, comment char(100));")
        cursor.execute("CREATE TABLE IF NOT EXISTS balance(total_income real, total_costs real);")
        cursor.execute("CREATE TABLE IF NOT EXISTS category_income(salary real, bonus real, gift real, another_income "
                       "real);")
        cursor.execute("CREATE TABLE IF NOT EXISTS category_costs(transport real, food real, clothes real, "
                       "health real, electronics real, car real, utilities real, another_cost real);")
        cursor.execute("CREATE TABLE IF NOT EXISTS total_card_cash(total_card, total_cash);")

        # Add a tranzaction
        cursor.execute("SELECT * from trans ORDER BY ID DESC")
        rows = cursor.fetchall()
        if len(rows) == 0:
            ID = 0
        else:
            ID = rows[0][0]
        cursor.execute("INSERT INTO trans(ID, date, type, card_cash, category, value, comment) VALUES (?,?,?,?,?,?,?)",
                       (ID + 1, datetime.datetime.now(), type1, type2, categorychoosen,
                        value, self.optional_comment.get()))
        conn.commit()

        # Update Balance for income and costs and for each category
        cursor.execute("SELECT * from balance")
        rows_balance = cursor.fetchall()
        cursor.execute("SELECT * from category_income")
        rows_category_income = cursor.fetchall()
        cursor.execute("SELECT * from category_costs")
        rows_category_costs = cursor.fetchall()
        cursor.execute("SELECT * from total_card_cash")
        rows_total_card_cash = cursor.fetchall()
        if len(rows_balance) == 0:
            conn.execute("INSERT INTO balance(total_income, total_costs) VALUES (?,?)", (0.00, 0.00))
            conn.execute("INSERT INTO category_income(salary, bonus, gift,"
                         "another_income) VALUES (?,?,?,?)", (0.00, 0.00, 0.00, 0.00))
            conn.execute("INSERT INTO category_costs(transport, food, clothes, health, electronics, car, utilities, "
                         "another_cost) VALUES (?,?,?,?,?,?,?,?)", (0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00))
            conn.execute("INSERT INTO total_card_cash(total_card, total_cash) VALUES (?,?)", (0.00, 0.00))
            total_income = total_costs = float(0.00)
            income_category = [0 for _ in range(4)]
            costs_category = [0 for _ in range(8)]
            total_card = total_cash = float(0.00)
        else:
            total_income = float(rows_balance[0][0])
            total_costs = float(rows_balance[0][1])
            income_category = [rows_category_income[0][i] for i in range(4)]
            costs_category = [rows_category_costs[0][i] for i in range(8)]
            total_card = float(rows_total_card_cash[0][0])
            total_cash = float(rows_total_card_cash[0][1])

        if type1 == 'Income':
            total_income += float(value)
            for i, catg in enumerate(category):
                if catg == categorychoosen:
                    income_category[i] += float(value)
                    break
            conn.execute("UPDATE balance SET total_income=?, total_costs=?", (float(total_income), float(total_costs)))
            conn.execute("UPDATE category_income SET salary=?, bonus=?, gift=?, another_income=?", income_category)
            conn.commit()
        elif type1 == 'Cost':
            total_costs += float(value)
            for i, catg in enumerate(category):
                if catg == categorychoosen:
                    costs_category[i - 4] += float(value)
                    break
            conn.execute("UPDATE balance SET total_costs=?, total_income=?", (float(total_costs), float(total_income)))
            conn.execute("UPDATE category_costs SET transport=?, food=?, clothes=?, health=?, electronics=?, car=?, "
                         "utilities=?, another_cost=?", costs_category)
            conn.commit()

        if type2 == 'Card':
            if type1 == 'Income':
                total_card += float(value)
            else:
                total_card -= float(value)
        elif type2 == 'Cash':
            if type1 == 'Income':
                total_cash += float(value)
            else:
                total_cash -= float(value)
        conn.execute("UPDATE total_card_cash SET total_card=?, total_cash=?", (float(total_card), float(total_cash)))
        conn.commit()

        # Close the database
        if conn:
            conn.close()
        self.empty_form()

    # Function for empty user input after transaction registration
    def empty_form(self):
        self.value.delete(0, 'end')
        self.categorychoosen.delete(0, 'end')

    # Function for input validation
    def validate(self, *args):
        if not self.value.get().isdigit():
            self.submit_button.config(state='disabled')
            return
        if self.type1.get() and self.type2.get() and self.value.get() and self.categorychoosen.get():
            self.submit_button.config(state='normal')
        else:
            self.submit_button.config(state='disabled')


# See or delete transactions
class Transaction:
    def __init__(self, master):
        # Window
        self.Checkbutton = IntVar()
        self.Checkbutton_list = list()
        self.Button_list = list()
        self.master = master
        self.master.geometry('1000x700')
        self.master.title('Your transaction | Finance Tracker by Enrico Garaiman 2020')
        self.principal_frame = Frame(self.master, bg='#80b3ff')
        self.buttons_frame = Frame(self.principal_frame, bg='#80b3ff')
        self.frame = ScrollableFrame(self.principal_frame)
        self.master.config(bg='#80b3ff')

        self.text_label = Label(self.buttons_frame, text='Choose the number of transactions',
                                font=20, bg='#80b3ff')
        self.text_label.grid(row=0, column=0, columnspan=3)
        self.number = Spinbox(self.buttons_frame, from_=0, to=self.get_number_of_transaction(),
                              font=20, bg='#80b3ff')
        self.number.grid(row=1, column=0, columnspan=3, pady=50)
        self.view_transaction_button = Button(self.buttons_frame, font=20, text='See last transactions',
                                              bg='#0052cc', fg='#ffffff', padx=20, pady=20,
                                              command=self.view_transaction, width=20)
        self.view_transaction_button.grid(row=2, column=0, sticky='we')
        self.clear = Button(self.buttons_frame, font=20, text='Clear', bg='#000000', fg='#ffffff',
                            padx=20, pady=20, command=self.clear, width=20)
        self.clear.grid(row=2, column=1, sticky='we')
        self.exit = Button(self.buttons_frame, font=20, text='Exit to menu', bg='#e60000', fg='#ffffff',
                           padx=20, pady=20, command=self.master.destroy, width=20)
        self.exit.grid(row=2, column=2, sticky='we')
        self.delete_button = Button(self.buttons_frame, font=20, bg='#0052cc', fg='#ffffff', padx=20, pady=20,
                                    command=self.delete_transactions, text='Delete selected transactions',
                                    state='disabled')
        self.delete_button.grid(row=3, column=0, columnspan=3, pady=10)
        self.principal_frame.pack()
        self.principal_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.buttons_frame.pack()
        self.frame.pack()

    # Clear checkbuttons function
    def clear(self):
        try:
            self.frame.destroy()
            self.frame = ScrollableFrame(self.principal_frame)
            self.frame.pack()
            self.view_transaction_button.config(state='normal')
            self.delete_button.config(state='disabled')
            self.succes_label.destroy()
            self.number.destroy()
            self.number = Spinbox(self.buttons_frame, from_=0, to=self.get_number_of_transaction(),
                                  font=20, bg='#80b3ff')
            self.number.grid(row=1, column=0, columnspan=3, pady=50)
        except:
            print()

    # Function return number of transaction
    def get_number_of_transaction(self):
        conn = sqlite3.connect('transaction.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * from trans ORDER BY date DESC")
        rows = cursor.fetchall()
        if conn:
            conn.close()
        return len(rows)

    # See last n transactions
    def view_transaction(self):
        self.view_transaction_button.config(state='disabled')
        self.delete_button.config(state='normal')
        conn = sqlite3.connect('transaction.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * from trans ORDER BY date DESC")
        rows = cursor.fetchall()
        number = self.number.get()

        for i in range(int(number)):
            sent_data = f"{rows[i][1][0:10]}: {rows[i][2]}, {rows[i][3]},\n{rows[i][4]}, VALUE: {rows[i][5]}\n"
            Btn = Checkbutton(self.frame.scrollable_frame, text=sent_data,
                              variable=self.Checkbutton,
                              onvalue=rows[i][0],
                              offvalue=0,
                              bg='#b3d9ff',
                              font=20)
            Btn.grid(row=i, column=0, columnspan=4)
            self.Button_list.append(Btn)
            self.Checkbutton_list.append(self.Checkbutton)

        if conn:
            conn.close()

    def delete_transactions(self):
        conn = sqlite3.connect('transaction.db')
        cursor = conn.cursor()
        succes = 0
        for c in self.Checkbutton_list:
            if c.get() != 0:
                ID = str(c.get())
                cursor.execute("DELETE from trans WHERE ID=?;", ID)
                conn.commit()
                succes += 1
        if succes:
            self.succes_label = Label(self.buttons_frame, text='The selected transactions was deleted successfully',
                                      font=20, bg='#80b3ff', fg='#00b33c')
            self.succes_label.grid(row=4, column=0, columnspan=3, pady=10)
        if conn:
            conn.close()


# See or reset balance
class Balance:
    def __init__(self, master):
        # Window
        self.master = master
        self.master.geometry('1000x900')
        self.master.title('Your balance | Finance Tracker by Enrico Garaiman 2020')
        self.frame = Frame(self.master, bg='#80b3ff')
        self.frame.pack()
        self.frame.place(relx=0.5, rely=0.5, anchor='center')
        self.master.config(bg='#80b3ff')

        total_income, total_costs = self.get_total_income_and_costs()
        salary, bonus, gift, another_income = self.get_income_each_category()
        transport, food, clothes, health, electronics, car, utilities, another_cost = self.get_costs_each_category()
        total_card, total_cash = self.get_card_cash_total()

        self.balance_label = Label(self.frame, text='Your balance:', bg='#80b3ff', font=20)
        self.balance_label.grid(row=0, column=0, columnspan=4)
        self.hr = Label(self.frame, text='____________________________________________', bg='#80b3ff', font=20)
        self.hr.grid(row=1, column=0, columnspan=4)
        self.total_income_label = Label(self.frame, text='Total income: ', bg='#80b3ff', font=20)
        self.total_income_label.grid(row=2, column=0)
        self.total_income = Label(self.frame, text=total_income, bg='#80b3ff', font=20, fg='#00b33c')
        self.total_income.grid(row=2, column=1)
        self.total_cost_label = Label(self.frame, text='Total costs: ', bg='#80b3ff', font=20)
        self.total_cost_label.grid(row=3, column=0)
        self.total_cost = Label(self.frame, text=total_costs, bg='#80b3ff', font=20, fg='#e60000')
        self.total_cost.grid(row=3, column=1)
        self.total_profit_label = Label(self.frame, text='Profit: ', bg='#80b3ff', font=20)
        self.total_profit_label.grid(row=4, column=0)
        self.total_profit = Label(self.frame, text=total_income - total_costs, bg='#80b3ff', font=20)
        self.total_profit.grid(row=4, column=1)
        self.total_card_label = Label(self.frame, text='CARD transactions: ', bg='#80b3ff', font=20)
        self.total_card_label.grid(row=2, column=3)
        self.total_card = Label(self.frame, text=total_card, bg='#80b3ff', font=20)
        self.total_card.grid(row=2, column=4)
        self.total_cash_label = Label(self.frame, text='CASH transactions: ', bg='#80b3ff', font=20)
        self.total_cash_label.grid(row=3, column=3)
        self.total_cash = Label(self.frame, text=total_cash, bg='#80b3ff', font=20)
        self.total_cash.grid(row=3, column=4)
        self.change_color()
        self.hr = Label(self.frame, text='____________________________________________', bg='#80b3ff', font=20)
        self.hr.grid(row=5, column=0, columnspan=4)
        self.income_label = Label(self.frame, text='Income for each category: ', bg='#80b3ff', font=20)
        self.income_label.grid(row=6, column=0, columnspan=4)
        self.hr = Label(self.frame, text='____________________________________________', bg='#80b3ff', font=20)
        self.hr.grid(row=7, column=0, columnspan=4)
        self.total_income_label = Label(self.frame, text='Salary: ', bg='#80b3ff', font=20)
        self.total_income_label.grid(row=8, column=0, columnspan=2)
        self.total_income = Label(self.frame, text=salary, bg='#80b3ff', font=20, fg='#00b33c')
        self.total_income.grid(row=8, column=2, columnspan=2)
        self.total_income_label = Label(self.frame, text='Bonus: ', bg='#80b3ff', font=20)
        self.total_income_label.grid(row=9, column=0, columnspan=2)
        self.total_income = Label(self.frame, text=bonus, bg='#80b3ff', font=20, fg='#00b33c')
        self.total_income.grid(row=9, column=2, columnspan=2)
        self.total_income_label = Label(self.frame, text='Gift: ', bg='#80b3ff', font=20)
        self.total_income_label.grid(row=10, column=0, columnspan=2)
        self.total_income = Label(self.frame, text=gift, bg='#80b3ff', font=20, fg='#00b33c')
        self.total_income.grid(row=10, column=2, columnspan=2)
        self.total_income_label = Label(self.frame, text='Another: ', bg='#80b3ff', font=20)
        self.total_income_label.grid(row=11, column=0, columnspan=2)
        self.total_income = Label(self.frame, text=another_income, bg='#80b3ff', font=20, fg='#00b33c')
        self.total_income.grid(row=11, column=2, columnspan=2)
        self.hr = Label(self.frame, text='____________________________________________', bg='#80b3ff', font=20)
        self.hr.grid(row=12, column=0, columnspan=4)
        self.costs_label = Label(self.frame, text='Costs for each category: ', bg='#80b3ff', font=20)
        self.costs_label.grid(row=13, column=0, columnspan=4)
        self.hr = Label(self.frame, text='____________________________________________', bg='#80b3ff', font=20)
        self.hr.grid(row=14, column=0, columnspan=4)
        self.total_costs_label = Label(self.frame, text='Transport: ', bg='#80b3ff', font=20)
        self.total_costs_label.grid(row=15, column=0, columnspan=2)
        self.total_costs = Label(self.frame, text=transport, bg='#80b3ff', font=20, fg='#e60000')
        self.total_costs.grid(row=15, column=2, columnspan=2)
        self.total_costs_label = Label(self.frame, text='Food: ', bg='#80b3ff', font=20)
        self.total_costs_label.grid(row=16, column=0, columnspan=2)
        self.total_costs = Label(self.frame, text=food, bg='#80b3ff', font=20, fg='#e60000')
        self.total_costs.grid(row=16, column=2, columnspan=2)
        self.total_costs_label = Label(self.frame, text='Clothes: ', bg='#80b3ff', font=20)
        self.total_costs_label.grid(row=17, column=0, columnspan=2)
        self.total_costs = Label(self.frame, text=clothes, bg='#80b3ff', font=20, fg='#e60000')
        self.total_costs.grid(row=17, column=2, columnspan=2)
        self.total_costs_label = Label(self.frame, text='Health: ', bg='#80b3ff', font=20)
        self.total_costs_label.grid(row=18, column=0, columnspan=2)
        self.total_costs = Label(self.frame, text=health, bg='#80b3ff', font=20, fg='#e60000')
        self.total_costs.grid(row=18, column=2, columnspan=2)
        self.total_costs_label = Label(self.frame, text='Electronics: ', bg='#80b3ff', font=20)
        self.total_costs_label.grid(row=19, column=0, columnspan=2)
        self.total_costs = Label(self.frame, text=electronics, bg='#80b3ff', font=20, fg='#e60000')
        self.total_costs.grid(row=19, column=2, columnspan=2)
        self.total_costs_label = Label(self.frame, text='Car: ', bg='#80b3ff', font=20)
        self.total_costs_label.grid(row=20, column=0, columnspan=2)
        self.total_costs = Label(self.frame, text=car, bg='#80b3ff', font=20, fg='#e60000')
        self.total_costs.grid(row=20, column=2, columnspan=2)
        self.total_costs_label = Label(self.frame, text='Utilities: ', bg='#80b3ff', font=20)
        self.total_costs_label.grid(row=21, column=0, columnspan=2)
        self.total_costs = Label(self.frame, text=utilities, bg='#80b3ff', font=20, fg='#e60000')
        self.total_costs.grid(row=21, column=2, columnspan=2)
        self.total_costs_label = Label(self.frame, text='Another: ', bg='#80b3ff', font=20)
        self.total_costs_label.grid(row=22, column=0, columnspan=2)
        self.total_costs = Label(self.frame, text=another_cost, bg='#80b3ff', font=20, fg='#e60000')
        self.total_costs.grid(row=22, column=2, columnspan=2)
        self.hr = Label(self.frame, text='____________________________________________', bg='#80b3ff', font=20)
        self.hr.grid(row=23, column=0, columnspan=4)
        self.reset = Button(self.frame, font=20, text='Reset Balance', bg='#0052cc', fg='#ffffff',
                           padx=20, pady=20, command=self.warning_delete_balance)
        self.reset.grid(row=24, column=0, sticky='we')
        self.exit = Button(self.frame, font=20, text='Exit to menu', bg='#e60000', fg='#ffffff',
                           padx=20, pady=20, command=self.master.destroy)
        self.exit.grid(row=24, column=1, columnspan=2, sticky='we')
        self.refresh = Button(self.frame, font=20, text='Refresh', bg='#0052cc', fg='#ffffff',
                           padx=20, pady=20, command=self.refresh_balance)
        self.refresh.grid(row=24, column=3, sticky='we')

    # Change color
    def change_color(self):
        total_income, total_costs = self.get_total_income_and_costs()
        total_card, total_cash = self.get_card_cash_total()
        if total_income - total_costs < 0:
            self.total_profit.config(fg='#e60000')
        else:
            self.total_profit.config(fg='#00b33c')
        if total_card < 0:
            self.total_card.config(fg='#e60000')
        else:
            self.total_card.config(fg='#00b33c')
        if total_cash < 0:
            self.total_cash.config(fg='#e60000')
        else:
            self.total_cash.config(fg='#00b33c')

    # Function return total income and costs
    def get_total_income_and_costs(self):
        conn = sqlite3.connect('transaction.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * from balance")
        rows = cursor.fetchall()

        if conn:
            conn.close()

        return rows[0][0], rows[0][1]

    # Function return income for each category
    def get_income_each_category(self):
        conn = sqlite3.connect('transaction.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * from category_income")
        rows = cursor.fetchall()

        if conn:
            conn.close()

        return rows[0][0], rows[0][1], rows[0][2], rows[0][3]

    # Function return income for each category
    def get_costs_each_category(self):
        conn = sqlite3.connect('transaction.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * from category_costs")
        rows = cursor.fetchall()

        if conn:
            conn.close()

        return rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4], rows[0][5], rows[0][6], rows[0][7]

    # Function return total cash/card transactions
    def get_card_cash_total(self):
        conn = sqlite3.connect('transaction.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * from total_card_cash")
        rows = cursor.fetchall()

        if conn:
            conn.close()

        return rows[0][0], rows[0][1]

    # Warning windows
    def warning_delete_balance(self):
        delete = messagebox.askquestion("Delete balance", "Are you sure?",
                                          icon='warning')
        if delete == "yes":
            self.delete_balance()
        else:
            return

    # Delete Balance (reset to 0)
    def delete_balance(self):
        conn = sqlite3.connect('transaction.db')
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS balance")
        cursor.execute("DROP TABLE IF EXISTS category_income")
        cursor.execute("DROP TABLE IF EXISTS category_costs")
        cursor.execute("DROP TABLE IF EXISTS total_card_cash")
        conn.commit()

        if conn:
            conn.close()

    # Refresh balance
    def refresh_balance(self):
        self.frame.destroy()
        self.__init__(self.master)


# Scrollable Frame
class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self, bg='#b3d9ff')
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas, bg='#b3d9ff')

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


def main():
    root = Tk()
    Welcome(root)
    root.mainloop()


if __name__ == '__main__':
    main()
