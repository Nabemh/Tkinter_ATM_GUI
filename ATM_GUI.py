from tkinter import *
from tkinter import font

root = Tk()
root.title('ATM')
# root.attributes('-fullscreen', True)
root.geometry("400x240")


# *withdrawal window*

def balance():
    user_operation.new_root.withdraw()

    balance.new_root = Toplevel(root)
    balance.new_root.geometry('460x390')

    account_balance = 100000
    lbl_font_settings = "MS Sans Serif", 35, "bold"
    text_title = Label(
        balance.new_root, text='BALANCE ENQUIRY', font=lbl_font_settings)
    note_lbl = Label(balance.new_root,
                     text=f'YOUR ACCOUNT BALANCE IS:  {account_balance}')
    exit_btn = Button(balance.new_root, text='EXIT',
                      width=14, height=3, fg='red')

    text_title.pack()
    note_lbl.pack(side=TOP, padx=15, pady=15)
    exit_btn.pack(side=BOTTOM, padx=10, pady=10)


def no():
    root.destroy()


def confirmation():

    withdrawal.new_root.withdraw()

    confirmation.new_root = Toplevel(root)
    confirmation.new_root.geometry('460x390')

    msg_box = Message(confirmation.new_root, text='\nYour transaction has been successful\n\nPlease collect your money\n\nYou can remove your card\n\nDo you want to check your balance?', justify='center', fg='blue')
    yes_btn = Button(confirmation.new_root, width=7, height=2,
                     text='YES', fg='green', command=balance)
    no_btn = Button(confirmation.new_root, width=7, height=2,
                    text=' NO ', fg='red', command=no)

    # On screen
    no_btn.pack(side=RIGHT, pady=10, padx=10)
    yes_btn.pack(side=RIGHT, pady=10)
    msg_box.pack()


def withdrawal():
    user_operation.new_root.withdraw()

    withdrawal.new_root = Toplevel(root)
    withdrawal.new_root.geometry('460x390')

    # labels and entry
    prompt_lbl = Label(withdrawal.new_root,
                       text='\nPlease enter amount\n', fg="red")
    amount_entry = Entry(withdrawal.new_root, justify='center')

    # Buttons

    bf = Frame(withdrawal.new_root)
    bf.pack(side=BOTTOM)

    bf4 = Frame(withdrawal.new_root)
    bf4.pack(side=BOTTOM)

    bf3 = Frame(withdrawal.new_root)
    bf3.pack(side=BOTTOM)

    bf3 = Frame(withdrawal.new_root)
    bf3.pack(side=BOTTOM)

    bf2 = Frame(withdrawal.new_root)
    bf2.pack(side=BOTTOM)

    bf1 = Frame(withdrawal.new_root)
    bf1.pack(side=BOTTOM)

    b1 = Button(bf1, text='1', width=12, height=2,
                command=lambda: amount_entry.insert('end', '1'))
    b2 = Button(bf1, text='2', width=12, height=2,
                command=lambda: amount_entry.insert('end', '2'))
    b3 = Button(bf1, text='3', width=12, height=2,
                command=lambda: amount_entry.insert('end', '3'))
    b4 = Button(bf2, text='4', width=12, height=2,
                command=lambda: amount_entry.insert('end', '4'))
    b5 = Button(bf2, text='5', width=12, height=2,
                command=lambda: amount_entry.insert('end', '5'))
    b6 = Button(bf2, text='6', width=12, height=2,
                command=lambda: amount_entry.insert('end', '6'))
    b7 = Button(bf3, text='7', width=12, height=2,
                command=lambda: amount_entry.insert('end', '7'))
    b8 = Button(bf3, text='8', width=12, height=2,
                command=lambda: amount_entry.insert('end', '8'))
    b9 = Button(bf3, text='9', width=12, height=2,
                command=lambda: amount_entry.insert('end', '9'))
    b0 = Button(bf4, text='0', width=12, height=2,
                command=lambda: amount_entry.insert('end', '0'))
    btn_enter = Button(bf4, text='↵', width=12, height=2,
                       fg='green', command=confirmation)
    clear_btn = Button(bf4, text='⌫', fg='orange', width=12,
                       height=2,  command=lambda: amount_entry.delete(1))

    # On-screen placement
    amount_entry.pack()
    prompt_lbl.pack()
    b1.pack(side=LEFT, pady=10)
    b2.pack(side=LEFT, padx=10)
    b3.pack(side=LEFT)
    b4.pack(side=LEFT)
    b5.pack(side=LEFT, padx=10)
    b6.pack(side=LEFT)
    b7.pack(side=LEFT, pady=10)
    b8.pack(side=LEFT, padx=10)
    b9.pack(side=LEFT)
    clear_btn.pack(side=LEFT)
    b0.pack(side=LEFT, padx=10)
    btn_enter.pack(side=LEFT)


# User Operation window
def user_operation():
    enter_pin.new_root.withdraw()

    user_operation.new_root = Toplevel(root)
    user_operation.new_root.geometry('460x390')

    # labels and buttons
    lbl_font_settings = "MS Sans Serif", 35, "bold"
    text_title = Label(user_operation.new_root,
                       text='ATM', font=lbl_font_settings)
    note_lbl = Label(user_operation.new_root,
                     text='Select desired operation', fg='red')
    withdraw_btn = Button(user_operation.new_root, text='WITHDRAWAL',
                          width=12, height=2, fg='red', bg='sky blue', command=withdrawal)
    bal_btn = Button(user_operation.new_root, text='BALANCE INQ',
                     width=12, height=2, fg='red', bg='sky blue')
    exit_btn = Button(user_operation.new_root, text='EXIT',
                      width=12, height=2, fg='red')

    # Putting buttons and screen
    text_title.pack()
    note_lbl.pack(side=BOTTOM, pady=10)
    exit_btn.pack(side=RIGHT, padx=10)
    withdraw_btn.pack(side=RIGHT, padx=10, pady=80)
    bal_btn.pack(side=RIGHT, padx=10, pady=80)


# *Pin verification window*
def enter_pin():
    root.withdraw()

    enter_pin.new_root = Toplevel(root)

    # enter_pin.geometry('460x390')

    # Button functions
    def input_text(text):
        entry_box.insert('end', text)

    def back_space():
        entry_box.delete(0)

    # labels and buttons
    lbl = Label(enter_pin.new_root, text='Enter your PIN', fg="red")
    entry_box = Entry(enter_pin.new_root, show="*")

    btn1 = Button(enter_pin.new_root, text='1', pady=15, padx=30,
                  font='cour15', command=lambda: input_text('1'))
    btn2 = Button(enter_pin.new_root, text='2', pady=15, padx=30,
                  font='cour15', command=lambda: input_text('2'))
    btn3 = Button(enter_pin.new_root, text='3', pady=15, padx=30,
                  font='cour15', command=lambda: input_text('3'))
    btn4 = Button(enter_pin.new_root, text='4', pady=15, padx=30,
                  font='cour15', command=lambda: input_text('4'))
    btn5 = Button(enter_pin.new_root, text='5', pady=15, padx=30,
                  font='cour15', command=lambda: input_text('5'))
    btn6 = Button(enter_pin.new_root, text='6', pady=15, padx=30,
                  font='cour15', command=lambda: input_text('6'))
    btn7 = Button(enter_pin.new_root, text='7', pady=15, padx=30,
                  font='cour15', command=lambda: input_text('7'))
    btn8 = Button(enter_pin.new_root, text='8', pady=15, padx=30,
                  font='cour15', command=lambda: input_text('8'))
    btn9 = Button(enter_pin.new_root, text='9', pady=15, padx=30,
                  font='cour15', command=lambda: input_text('9'))
    btn0 = Button(enter_pin.new_root, text='0', pady=15, padx=30,
                  font='cour15', command=lambda: input_text('0'))
    btn_clear = Button(enter_pin.new_root, pady=15, padx=30,
                       font='cour15', text='⌫', command=back_space)
    btn_enter = Button(enter_pin.new_root, pady=15, padx=30,
                       font='cour15', text='↵', command=user_operation)

    # Labels and buttons on screen
    lbl.grid(row=1, columnspan=3, column=0)
    entry_box.grid(row=2, columnspan=3, column=0)

    btn1.grid(row=3, column=0)
    btn2.grid(row=3, column=1)
    btn3.grid(row=3, column=2)

    btn4.grid(row=4, column=0)
    btn5.grid(row=4, column=1)
    btn6.grid(row=4, column=2)

    btn7.grid(row=5, column=0)
    btn8.grid(row=5, column=1)
    btn9.grid(row=5, column=2)

    btn_clear.grid(row=6, column=0)
    btn0.grid(row=6, column=1)
    btn_enter.grid(row=6, column=2)


# *Opening window*

# labels

font_settings = "MS Sans Serif", 20, "bold"
title_label = Label(root, text="ATM Terminal", font=font_settings, fg='red')
intro = Label(root, text="Welcome", fg='blue')
option_text = Label(root, text='Select your account type', fg='blue')


# defining functions
def exit_func():
    root.destroy()


# buttons
saving = Button(root, text="Savings", width=7, height=2,
                bg="#87CEEB", fg='red', command=enter_pin)
current = Button(root, text="Current", width=7, height=2,
                 bg='#87CEEB', fg='red', command=enter_pin)
exit = Button(root, text='EXIT', width=7, height=2,
              fg="red", command=exit_func)

# On-screen positioning - buttons
exit.pack(side=RIGHT, padx=10)
saving.pack(side=RIGHT, padx=10, pady=80)
current.pack(side=RIGHT, padx=10, pady=80)

# On-screen positioning - labels
intro.pack()
title_label.pack(pady=10)

root.mainloop()
