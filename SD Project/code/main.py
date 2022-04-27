
#Сделал рандомайзер
from random import randint

#Импорт библиотеки tkinter 
from tkinter import *
# os - Операционная система 
import os
#PIL - Python Image Library - Библиотка картинок
from PIL import ImageTk, Image 
#Основной вид
master = Tk()
master.title('K P')

#Функциия Регистрации Temp - Временные данные  
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    family = temp_family.get()
    password = temp_password.get()
    all_accounts = os.listdir()
# Если поля пуста тогда выведи Вся поля 
    if name == '' or age == '' or family == '' or password == '':
        notif.config(
            fg='red',
            text='вся поля обязательны к заполнению*!',
        )
        return
#Проверка аккаунта
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg='red', text='Аккаунт уже существует')
            return
#Создания файла пользователья на компе
        else:
            new_file = open(name, 'w')
            new_file.write(name + '\n')
            new_file.write(password + '\n')
            new_file.write(family + '\n')
            new_file.write(age + '\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg='green', text='Ваш аккаунт  успешно создан')

#Функция регистрации
def register():
    #1 Variables - Переменные
    global temp_name
    global temp_age
    global temp_family
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_family = StringVar()
    temp_password = StringVar()

    #Окно Регистрации
    register_screen = Toplevel(master)
    register_screen.title('Register')

    #Метки Регистрации - Labels
    Label(register_screen,
          text='Пожалуйста ведите свои данные',fg="orange",bg='black',
          font=('Calibri', 12,)).grid(row=0, sticky=N, pady=10)
    Label(register_screen, text='Имя', font=('Calibri', 12)).grid(row=1,
                                                                  sticky=W)
    Label(register_screen, text='Возраст', font=('Calibri', 8)).grid(row=2,
                                                                      sticky=W)
    Label(register_screen, text='Фамилия', font=('Calibri', 8)).grid(row=3,
                                                                      sticky=W)
    Label(register_screen, text='Пароль',font=('Calibri',8)).grid(row=4,
                                                                     sticky=W)
    notif = Label(register_screen, font=('Calibri', 12))
    notif.grid(row=6, sticky=N, pady=10)

    #Entries - ВВОд
    Entry(register_screen, textvariable=temp_name).grid(row=1, column=0)
    Entry(register_screen, textvariable=temp_age).grid(row=2, column=0)
    Entry(register_screen, textvariable=temp_family).grid(row=3, column=0)
    Entry(register_screen, textvariable=temp_password).grid(row=4, column=0)

    #Register Buttons - Кнопки Регистрации
    Button(register_screen,
           text='Register',
           command=finish_reg,
           font=('Calibri', 12)).grid(row=5, sticky=N, pady=10)

#Функция сессия логин 
def login_session():
    global login_name
    all_accounts = os.listdir()
    login_name =temp_login_name.get()
    login_password =temp_login_password.get()
    file=open(login_name,'r')
    file_data=file.read()
    file_data=file_data.split("\n")
    password=file_data[1]
    if login_password == password:
        login_screen.destroy()
        account_dashboard = Toplevel(master)
           
        account_dashboard.title("управления учетной записью")
                #label
        Label(account_dashboard,
                      text='Панель управления учетной записью',
                      font=('Calibri',10)).grid(row=5, sticky=N, pady=10)
        Label(account_dashboard,
                      text='Добро пожаловать '+login_name,
                      fg='orange',bg='grey',font=('Calibri', 12)).grid(row=1, sticky=N, pady=5)
                #Кнопки Grid - раздел
        Button(account_dashboard,
                       text='Личные данные',fg='orange',bg='black', 
                       font=('Calibri', 12),
                       width=30,
                       command=personal_details).grid(row=2, sticky=N, padx=10)
        Button(account_dashboard,
                       text='Оплата',fg='black',bg='orange',
                       font=('Calibri', 12),
                       width=30,
                       command=pay).grid(row=3, sticky=N, padx=10)
        Button(account_dashboard,
                       text='Забронировать',fg='Orange',bg='black',
                       font=('Calibri', 12),
                       width=30,
                       command=book).grid(row=4, sticky=N, padx=10)
        Label(account_dashboard).grid(row=5, sticky=N, pady=10)
        
    else:
        login_notif.config(text="Не Правильный Пароль!!!",fg='red')




#Функция Бронирование 
def book():
  book_screen=Toplevel(master)
  book_screen.title=("Бук")
  N=1
  array=list()
  for i in range (N):
     array.append(randint(0,100))
     

  label=Label(book_screen,text='Ваше место  забронированно\nВаш ID : '+str(array),fg='yellow',bg='orange',font=        ('Calibri',9,))  
  label.place(x=0.5,y=0.5)


      

#Функция Депозит   
def deposit():
    #Vars
    global deposit_screen
    global amount
    global deposit_notif
   
    amount = StringVar()
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    #Pay Deposit
    deposit_screen = Toplevel(master)
    deposit_screen.title('Депозит')
    #Labels
    Label(deposit_screen, text='Депозит', font=('Calibri', 12)).grid(row=0,
                                                                     sticky=N,
                                                                     pady=10)
    current_balance_label = Label(deposit_screen,
                                  text='Баланс: $' + details_balance,
                                  font=('Calibri', 12)).grid(row=0,
                                                             sticky=N,
                                                             pady=10)
    current_balance_label.grid(row=1, sticky=W)
    Label(deposit_screen, text='Сумма :', font=('Calibri', 12)).grid(row=2,
                                                                     sticky=W)
    deposit_notif = Label(deposit_screen, font=('Calibri', 12))
    deposit_notif.grid(row=4, sticky=N, pady=5)
    #Entry
    Entry(deposit_screen, textvariables=amount).grid(row=2, column=1)
    #Button
    Button(deposit_screen,
           text='Оплатить',
           font=('Calibri', 12),
           command='finish_deposit').grid(row=3, sticky=W, pady=5)
#Функция конец Депозит 
    def finish_deposit():
        if amount.get() == "":
            deposit_notif.config(text='Cумма депозита', fg='red')
            return
        if float(amount.get()) <= 0:
            deposit_notif.config(text="Минусовая валюта не принимается",
                                 fg='red')
            return

        file = open(login_name, "r+")
        file_data = file.read()
        details = file_data.split('\n')
        current_balance = [4]
        updated_balance = current_balance
        updated_balance = float(updated_balance) - float(amount.get())
        file_data = file_data.replace(current_balance, str(updated_balance))
        file.seek()
        file.truncate(0)
        file.write(file_data)
        file.close()

        current_balance_label.config(
            text='Текуший Баланс: $' + str(updated_balance),
            fg='green',
        )

        deposit_notif.config(text='Баланс  Обновлён', fg='green')

#Функция Оплата 
def pay():
    #Vars - Переменные 
    
    global deposit_screen
    global pay_amount
    global pay_notif
    global current_balance_label
    pay_amount = StringVar()
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    #Pay Deposit
    pay_screen = Toplevel(master)
    pay_screen.title('Оплатить')
    #Labels
    Label(pay_screen,text='Ваше место забранированно',font=("Calibri",12))
    Label(pay_screen, text='Оплата', font=('Calibri', 12)).grid(row=0,
                                                                sticky=N,
                                                                pady=10)
    current_balance_label = Label(pay_screen,
                                  text='Баланс: $' + details_balance,
                                  font=('Calibri', 12))
    current_balance_label.grid(row=0,
                                                             sticky=N,
                                                             pady=10)
    Label(pay_screen, text='Сумма :', font=('Calibri', 12)).grid(row=2,
                                                                 sticky=W)
    pay_notif = Label(pay_screen, font=('Calibri', 12))
    pay_notif.grid(row=4, sticky=N, pady=5)
    #Entry
    Entry(pay_screen, textvariable=pay_amount).grid(row=2, column=1)
    #Button
    Button(pay_screen,
           text='Оплатить',
           font=('Calibri', 12),
           command=finish_pay).grid(row=3, sticky=W, pady=5)
    Button(pay_screen,
           text='депосит',
           font=('Calibri', 12),
           command=finish_deposit).grid(row=4, sticky=W, pady=5)
           
           
def finish_deposit():
    if pay_amount.get() == "":
        pay_notif.config(text='Cумма оплаты', fg='red')
        return
    if float(pay_amount.get()) <= 0:
        pay_notif.config(text="Минусовая валюта не принимается", fg='red')
        return
    file = open(login_name, "r+")
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]

    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(pay_amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text='Текуший Баланс: $' + str(updated_balance),
            fg='green',)
    pay_notif.config(text="Статус активирован", fg='green')
           


def finish_pay():
    if pay_amount.get() == "":
        pay_notif.config(text='Cумма оплаты', fg='red')
        return
    if float(pay_amount.get()) <= 0:
        pay_notif.config(text="Минусовая валюта не принимается", fg='red')
        return
    file = open(login_name, "r+")
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    if float(pay_amount.get()) > float(current_balance):
        pay_notif.config(text='Недостаточно средств', fg='red')
        return

    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(pay_amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text='Текуший Баланс: $' + str(updated_balance),
            fg='green',)
    pay_notif.config(text='Баланс Обновлён', fg='green')

#Персональные данные
def personal_details():
    #Vars
    file = open(login_name, 'r')
    file_data = file.read()
    User_details = file_data.split('\n')
    details_name = User_details[0]
    details_age = User_details[3]
    details_family = User_details[2]
    details_balance = User_details[4]
    details_password = User_details[1]

    #Личные данные
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Личные данные')
    #Labels
    Label(personal_details_screen, text='Личные данные',
          font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen,
          text='Name:' + details_name,
          font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(personal_details_screen,
          text='age:' + details_age,
          font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(personal_details_screen,
          text='family:' + details_family,
          font=('Calibri', 12)).grid(row=3, sticky=W)
    Label(personal_details_screen,
          text='password:' + details_password,
          font=('Calibri', 12)).grid(row=4, sticky=W)

#Функция Логин
def login():
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    #Страница логина
    login_screen = Toplevel(master)
    login_screen.title("Логин")
    #Метка Логина
    Label(login_screen, text="За логиньтесь для входа",bg='grey',fg='orange',
          font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(login_screen, text='Пользователь',bg='grey',
          font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(login_screen, text='Пароль',bg='grey', font=('Calibri', 12)).grid(row=2,
                                                                  sticky=W)
                                                                  
    login_notif = Label(login_screen, font=('Calibri', 12))
    login_notif.grid(row=4, sticky=N)
    #Vars:
    #Ввод-Entry
    Entry(login_screen, textvariable=temp_login_name).grid(row=1,
                                                           column=1,
                                                           padx=5)
    Entry(login_screen, textvariable=temp_login_password,
          show=("*")).grid(row=2, column=1, padx=5)
    #Button
    Button(login_screen,
           text='Логин',bg='orange',
           command=login_session,
           width=15,
           font=('Calibri', 12)).grid(row=3, sticky=W, pady=5, padx=5)


#Импорт фоток
img = Image.open('K.png')
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

#Label - Метка
Label(master, text='Komfort Parking',bg='orange', font=('Roboto', 15)).grid(row=0,
                                                                sticky=N,
                                                                pady=10)
Label(master, text='Добро пожаловать ',fg='orange',bg='black', font=('Calibri', 12)).grid(row=1,
                                                                   sticky=N,
                                                                   pady=10)
Label(master, image=img).grid(row=2, sticky=N, pady=16)
#Кнопки
Button(master,
       text='Регистрация',fg='orange',bg='black',
       font=('Calibri', 14),
       width=20,
       command=register).grid(row=3, sticky=N)
Button(master, text='Логин',fg='black',bg='orange',font=('Calibri', 14), width=20,
       command=login).grid(row=4, sticky=N, pady=5)

master.mainloop()
register_screen.mainloop()

