from tkinter import *
from tkinter import ttk, messagebox
import webbrowser
import Python.DEV_project.Payload_json as payload
import Python.DEV_project.Variables as vari
import openpyxl

"""

The brands pulled from the below path (Local) and converted to dictionary with 3 values
a.value = brands names
b.value = domain
c.value = WP/API

"""

loc = 'C:\\Users\\inter\\PycharmProjects\\Projects\\Python\\DEV_project\\WP_brands.xlsx'  # the path to the sheet
# file of the brands
book = openpyxl.load_workbook(loc)
sh = book.active
locations = {}
test_loc = {}
my_list=[]
for a, b, c in sh:  # a: brand name, b: brand URL, c: WP or API
    locations[a.value] = b.value, c.value
    test_loc[a.value] = c.value
    my_dict_brand = dict(locations.items())  # Dictionary
    my_test = dict(test_loc.items())
    my_list.append(my_test)
    x = dict(my_test).keys()

for f in my_list:
    print("First: ", f)

############################
########## G U I ###########
############################

root = Tk()
root.geometry('700x700+600+100')

tab_parent = ttk.Notebook(root)

register_tab = ttk.Frame(tab_parent)
qa_tab = ttk.Frame(tab_parent)

tab_parent.add(register_tab, text='Register')
tab_parent.add(qa_tab, text='Auto QA')

tab_parent.pack(expand=1, fill=BOTH)
"""

Top Labels

"""
username_label = Label(register_tab, text='Username: ')  # User name Label
username_label.grid(row=0, column=0, sticky=SW)

entryText_name = StringVar()
username_input = Entry(register_tab, textvariable=entryText_name)
username_input.grid(row=0, column=1)  # User name Entry

password_label = Label(register_tab, text='Password: ')  # Password Label
password_label.grid(row=1, column=0, sticky=SW)

entryText_pass = StringVar()
password_input = Entry(register_tab, textvariable=entryText_pass)
password_input.grid(row=1, column=1)  # Password Entry
entryText_pass.set('Aa123456')

mail_label = Label(register_tab, text='Email: ')  # Email Label
mail_label.grid(row=2, column=0, sticky=SW)

mail_var = StringVar()
mail_input = Entry(register_tab, textvariable=mail_var)
mail_input.grid(row=2, column=1)  # Email Entry

mailinator_label = Label(register_tab, text='@mailinator.com')  # Mailinator Label
mailinator_label.grid(row=2, column=2, sticky=SW)

dropbox_brands_label = ttk.Label(register_tab, text='Brands: ')  # Brands Label
dropbox_brands_label.grid(row=1, column=3, sticky=E)

dropBox_var = StringVar()
dropbox_brands = ttk.Combobox(register_tab, values=my_list, textvariable=dropBox_var,
                              state=DISABLED)  # Brands Dropbox
dropbox_brands.grid(row=1, column=4, sticky=SW)
dropBox_var.set('Choose >>')
# dropbox_brands.

var = StringVar()
ttk.Radiobutton(register_tab, text='WP', variable=var, value=1).grid(row=0, column=5, sticky=SW, padx=20)  # WP
ttk.Radiobutton(register_tab, text='API', variable=var, value=2).grid(row=1, column=5, sticky=SW, padx=20)  # API
ttk.Radiobutton(register_tab, text='AWS', variable=var, value=3).grid(row=2, column=5, sticky=SW, padx=20)  # AWS
ttk.Radiobutton(register_tab, text='ALL', variable=var, value=4).grid(row=3, column=5, sticky=SW, padx=20)  # ALL
var.set(4)

ran_mail_var = IntVar()


def random_mail_func():
    if ran_mail_var.get() == 1:
        mail_var.set(vari.email_generator(7))
        mail_input.config(state=DISABLED)
    else:
        mail_input.config(state=NORMAL)
        mail_var.set('')


random_mail_check = ttk.Checkbutton(register_tab, text='Random Mail', onvalue=1, offvalue=0, variable=ran_mail_var,
                                    command=random_mail_func)
random_mail_check.grid(row=5, column=0, columnspan=3)
random_mail_check.state(['!alternate'])

all_brands_var = IntVar()


def all_brands_chk_func():
    if all_brands_var.get() == 1:
        dropbox_brands.config(state=DISABLED)
    elif all_brands_var.get() == 0:
        dropbox_brands.config(state=ACTIVE)


all_brands_check = ttk.Checkbutton(register_tab, text='All Brands', onvalue=1, offvalue=0, variable=all_brands_var,
                                   command=all_brands_chk_func)
all_brands_check.grid(row=5, column=2, columnspan=3)
all_brands_check.state(['!disabled', 'selected'])


def action():
    log_output.delete(1.0, END)
    output_login = 'LoginName: ' + username_input.get()
    output_pass = 'Password: ' + password_input.get()
    output_mail = 'Email: ' + mail_var.get() + '@mailinator.com'

    hyper = 'https://www.mailinator.com/v4/public/inboxes.jsp?to={}'.format(mail_var.get())
    link_to_mail.config(text=hyper)
    credentials_user_var.set(username_input.get())
    credentials_pass_var.set(password_input.get())
    credentials_mail_var.set(mail_input.get() + '@mailinator.com')

    log_output.insert(END, '*' * 20 + '\n')
    log_output.insert(END, output_login + '\n')
    log_output.insert(END, output_pass + '\n')
    log_output.insert(END, output_mail + '\n')
    log_output.insert(END, '*' * 20 + '\n\n')

    log_output.insert(END, "Register in progress\nPlease wait...\n\n")
    # payload_action_v()

    try:

        if all_brands_check == 1:
            for i in my_dict_brand.values():
                payload.registration(username_input.get(), password_input.get(), mail_input.get(), log_output, i[0])

        elif all_brands_check == 0:
            payload.registration(username_input.get(), password_input.get(), mail_input.get(), log_output,
                                 list(my_dict_brand[dropBox_var.get()])[0])  # list(my_dict_brand[dropBox_var.get()])[0])

    except Exception as e:
        messagebox.showerror("Error", e)


run_button = Button(register_tab, text='Run!', bg='lightgreen', height=2, width=15, command=action)
run_button.grid(row=5, column=4, rowspan=2, columnspan=2, sticky=NE)

label_space_two = Label(register_tab)  # Space Label ROW = 6
label_space_two.grid(row=6, columnspan=4, sticky=W)

change_var_pass = IntVar()
change_var_mail = IntVar()


def change_func():
    if change_var_pass.get() == 1:
        change_pass_entry.config(state=NORMAL)
    if change_var_mail.get() == 1:
        change_mail_entry.config(state=NORMAL)
    if change_var_pass.get() == 0:
        change_pass_entry.config(state=DISABLED)
    if change_var_mail.get() == 0:
        change_mail_entry.config(state=DISABLED)


change_pass_check = ttk.Checkbutton(qa_tab, text='Change Password: ', onvalue=1, offvalue=0, variable=change_var_pass,
                                    command=change_func)
change_pass_check.grid(row=7, column=0, sticky=W)
change_pass_check.state(['!alternate'])

change_pass_entry = Entry(qa_tab, state=DISABLED)
change_pass_entry.grid(row=7, column=1, sticky=W)

change_mail_check = ttk.Checkbutton(qa_tab, text='Change Mail: ', onvalue=1, offvalue=0, variable=change_var_mail,
                                    command=change_func)
change_mail_check.grid(row=8, column=0, sticky=W)
change_mail_check.state(['!alternate'])

change_mail_entry = Entry(qa_tab, state=DISABLED)
change_mail_entry.grid(row=8, column=1, sticky=W)

label_space_three = Label(qa_tab)  # Space Label ROW = 6
label_space_three.grid(row=7, column=2, sticky=W)

label_space_three = Label(qa_tab)  # Space Label ROW = 6
label_space_three.grid(row=8, column=2, sticky=W)

game_check_label = ttk.Checkbutton(qa_tab, text='Check game')
game_check_label.grid(row=7, column=3, sticky=W)
game_check_label.state(['!alternate'])

login_check = ttk.Checkbutton(qa_tab, text='Check Login')
login_check.grid(row=7, column=4, sticky=W)
login_check.state(['!alternate'])

psp_check = ttk.Checkbutton(qa_tab, text='Check PSP')
psp_check.grid(row=8, column=3, sticky=W)
psp_check.state(['!alternate'])

checked_test_acc = IntVar()


def test_account():
    if checked_test_acc.get() == 1:
        entryText_name.set(vari.login_name_generator(5))
        username_input.config(state=DISABLED)
        password_input.config(state=DISABLED)
    else:
        username_input.config(state=NORMAL)
        entryText_name.set('')
        password_input.config(state=NORMAL)


test_account_check = ttk.Checkbutton(register_tab, text='Test Account', onvalue=1, offvalue=0,
                                     variable=checked_test_acc,
                                     command=test_account)
test_account_check.grid(row=8, column=4, sticky=W)
test_account_check.state(['!alternate'])

label_space_four = Label(register_tab)  # Sapce Label ROW = 12
label_space_four.grid(row=10, columnspan=4, sticky=W)

separator = ttk.Separator(register_tab, orient='horizontal')  # Separator
separator.place(x=0, y=200, relwidth=5, anchor=N)

credentials_user = Label(register_tab, text='UserName:', fg='red')
credentials_user.grid(row=11, column=0, sticky=W)

credentials_user_var = StringVar()
credentials_user_output = Label(register_tab, text='UserName:', fg='green', textvariable=credentials_user_var)
credentials_user_output.grid(row=11, column=1, sticky=W, columnspan=2)

credentials_pass = Label(register_tab, text='Password:', fg='red')
credentials_pass.grid(row=11, column=2, sticky=W)

credentials_pass_var = StringVar()
credentials_pass_output = Label(register_tab, text='pass:', fg='green', textvariable=credentials_pass_var)
credentials_pass_output.grid(row=11, column=3, sticky=W, columnspan=2)

credentials_mail = Label(register_tab, text='Mail:', fg='red')
credentials_mail.grid(row=11, column=4, sticky=W)

credentials_mail_var = StringVar()
credentials_mail_output = Label(register_tab, text='Mail:', fg='green', textvariable=credentials_mail_var)
credentials_mail_output.grid(row=11, column=4, sticky=E, padx=55, columnspan=2)

link_to_mail = Label(register_tab, text='< LINK >', fg='blue')
link_to_mail.grid(row=12, columnspan=5)


def open_mail_btn():
    link = 'https://www.mailinator.com/v4/public/inboxes.jsp?to={}'.format(mail_var.get())
    webbrowser.open_new_tab(link)


mail_open = Button(register_tab, text='Go to Mail', command=open_mail_btn, bg='blue', fg='white')
mail_open.grid(row=12, column=3, columnspan=2, sticky=E)

log_output = Text(register_tab)
log_output.grid(row=13, columnspan=8, sticky=N)

scrollbar = Scrollbar(register_tab, orient='vertical', command=log_output.yview())
scroll_frame = Frame(log_output)

########################## Threading #####################################

# t1 = threading.Thread(target=payload.registration,
#                       args=(username_input.get(), password_input.get(), mail_input.get(), log_output.insert))

##########################################################################

root.mainloop()
