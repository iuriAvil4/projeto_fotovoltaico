from dataclasses import replace
import datetime
from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
import tkinter.messagebox
import oracledb


username = 'SYSTEM'  # usuário
password = '123456'  # senha
# string de conexão do Oracle, configurado no cliente Oracle, arquivo tnsnames.ora
dsn = 'localhost/xe'
port = 1521
encoding = 'UTF-8'

consumos = Tk()
consumos.geometry("1000x700+565+270")
consumos.title("Consumos")

global cal_ativo
cal_ativo = False


def calendario(campo, ycal):
    global cal_ativo

    if cal_ativo == False:
        cal_ativo = True

        cal = Calendar(consumos, selectmode='day',
                       font=("Times", '9', 'bold'), locale='pt_br')
        cal.place(x=350, y=ycal)

        def pegar_data():
            global cal_ativo

            data_selec = cal.get_date()
            cal.destroy()
            campo.delete(0, END)
            campo.insert(END, data_selec)
            botao_inserir.destroy()
            cal_ativo = False

        botao_inserir = Button(consumos, text="Inserir data",
                               command=pegar_data)
        botao_inserir.place(x=502, y=ycal+190)


def teste():
    print("teste")


def add_consumo():

    # Data for binding
    pCONTA01 = campo_1.get().strip()
    pCONTA02 = campo_2.get().strip()
    pCONTA03 = campo_3.get().strip()
    pCONTA04 = campo_4.get().strip()
    pCONTA05 = campo_5.get().strip()
    pCONTA06 = campo_6.get().strip()
    pCONTA07 = campo_7.get().strip()
    pCONTA08 = campo_8.get().strip()
    pCONTA09 = campo_9.get().strip()
    pCONTA10 = campo_10.get().strip()
    pCONTA11 = campo_11.get().strip()
    pCONTA12 = campo_12.get().strip()

    pKWH_1 = float(campok_1.get().strip())
    pKWH_2 = float(campok_2.get().strip())
    pKWH_3 = float(campok_3.get().strip())
    pKWH_4 = float(campok_4.get().strip())
    pKWH_5 = float(campok_5.get().strip())
    pKWH_6 = float(campok_6.get().strip())
    pKWH_7 = float(campok_7.get().strip())
    pKWH_8 = float(campok_8.get().strip())
    pKWH_9 = float(campok_9.get().strip())
    pKWH_10 = float(campok_10.get().strip())
    pKWH_11 = float(campok_11.get().strip())
    pKWH_12 = float(campok_12.get().strip())
    pID_PRJ = float(campo_id.get().strip())

    try:
        # establish a new connection
        connection = oracledb.connect(user="SYSTEM", password=password, dsn="localhost/xe")
        # create a cursor
        cursor = connection.cursor()
        pmsg = cursor.var(str)
        cursor.callproc('ProjetoPS.add_consumo', [pCONTA01,   pCONTA02,   pCONTA03,   pCONTA04,
                                           pCONTA05,   pCONTA06,   pCONTA07,   pCONTA08,
                                           pCONTA09,   pCONTA10,   pCONTA11,   pCONTA12,
                                           pKWH_1,     pKWH_2,     pKWH_3,     pKWH_4,
                                           pKWH_5,     pKWH_6,     pKWH_7,     pKWH_8,
                                           pKWH_9,     pKWH_10,    pKWH_11,    pKWH_12,    pID_PRJ,    pmsg])

        tkinter.messagebox.showinfo(
            title='Result',
            message=f'{pmsg.getvalue()}!'
        )
        print(pmsg)

    except oracledb.Error as error:
        print('Error occurred on add_consumo:')
        print(error)
        return error


def calc_potencia_min():

    # Data for binding
    pID_projetos = campo_id.get().strip()

    try:
        # establish a new connection
        connection = oracledb.connect(user="SYSTEM", password=password, dsn="localhost/xe")
        # create a cursor
        cursor = connection.cursor()
        pmsg = cursor.var(str)
        cursor.callproc('HR.calc_potencia_min', [pID_projetos,    pmsg])

        tkinter.messagebox.showinfo(
            title='Result',
            message=f'{pmsg.getvalue()}!'
        )
        print(pmsg)

    except oracledb.Error as error:
        print('Error occurred on calc_potencia_min:')
        print(error)
        return error


#######################################  ESQUERDA  ##############################################


campo_id = Entry(consumos, text="Id Projeto", font=(
    10), width=10, justify='center', fg='green')
campo_id.place(x=140, y=100)

id_projeto = Label(consumos, text="ID Projeto ", font=(10), width=15)
id_projeto.place(x=10, y=100)


# 1

campo_1 = Entry(consumos, text="Campo 1", font=(
    10), width=13, justify='center', fg='blue')
campo_1.place(x=140, y=200)

conta_1 = Label(consumos, text="Conta 1", font=(10), width=15)
conta_1.place(x=0, y=200)

botao_1 = Button(consumos, text=" . . . ",
                 command=lambda: [calendario(campo_1, 200)])
botao_1.place(x=300, y=200)


# 2

campo_2 = Entry(consumos, text="Campo 2", font=(
    10), width=13, justify='center', fg='blue')
campo_2.place(x=140, y=240)

conta_2 = Label(consumos, text="Conta 2", font=(10), width=15)
conta_2.place(x=0, y=240)

botao_2 = Button(consumos, text=" . . . ",
                 command=lambda: [calendario(campo_2, 240)])
botao_2.place(x=300, y=240)

# 3

campo_3 = Entry(consumos, text="Campo 3", font=(
    10), width=13, justify='center', fg='blue')
campo_3.place(x=140, y=280)

conta_3 = Label(consumos, text="Conta 3", font=(10), width=15)
conta_3.place(x=0, y=280)

botao_3 = Button(consumos, text=" . . . ",
                 command=lambda: [calendario(campo_3, 280)])
botao_3.place(x=300, y=280)

# 4

campo_4 = Entry(consumos, text="Campo 4", font=(
    10), width=13, justify='center', fg='blue')
campo_4.place(x=140, y=320)

conta_4 = Label(consumos, text="Conta 4", font=(10), width=15)
conta_4.place(x=0, y=320)

botao_4 = Button(consumos, text=" . . . ",
                 command=lambda: [calendario(campo_4, 320)])
botao_4.place(x=300, y=320)

# 5

campo_5 = Entry(consumos, text="Campo 5", font=(
    10), width=13, justify='center', fg='blue')
campo_5.place(x=140, y=360)

conta_5 = Label(consumos, text="Conta 5", font=(10), width=15)
conta_5.place(x=0, y=360)

botao_5 = Button(consumos, text=" . . . ",
                 command=lambda: [calendario(campo_5, 360)])
botao_5.place(x=300, y=360)

# 6

campo_6 = Entry(consumos, justify='center', text="Campo 6",
                font=(10), width=13, fg='blue')
campo_6.place(x=140, y=400)

conta_6 = Label(consumos, text="Conta 6", font=(10), width=15)
conta_6.place(x=0, y=400)

botao_6 = Button(consumos, text=" . . . ",
                 command=lambda: [calendario(campo_6, 400)])
botao_6.place(x=300, y=400)

# 7

campo_7 = Entry(consumos, text="Campo 7", font=(
    10), width=13, justify='center', fg='blue')
campo_7.place(x=140, y=440)

conta_7 = Label(consumos, text="Conta 7", font=(10), width=15)
conta_7.place(x=0, y=440)

botao_7 = Button(consumos, text=" . . . ",
                 command=lambda: [calendario(campo_7, 440)])
botao_7.place(x=300, y=440)

# 8

campo_8 = Entry(consumos, text="Campo 8", font=(
    10), width=13, justify='center', fg='blue')
campo_8.place(x=140, y=480)

conta_8 = Label(consumos, text="Conta 8", font=(10), width=15)
conta_8.place(x=0, y=480)

botao_8 = Button(consumos, text=" . . . ",
                 command=lambda: [calendario(campo_8, 480)])
botao_8.place(x=300, y=480)

# 9

campo_9 = Entry(consumos, text="Campo 9", font=(
    10), width=13, justify='center', fg='blue')
campo_9.place(x=140, y=520)

conta_9 = Label(consumos, text="Conta 9", font=(10), width=15)
conta_9.place(x=0, y=520)

botao_9 = Button(consumos, text=" . . . ",
                 command=lambda: [calendario(campo_9, 360)])
botao_9.place(x=300, y=520)

# 10

campo_10 = Entry(consumos, text="Campo 10", font=(10),
                 width=13, justify='center', fg='blue')
campo_10.place(x=140, y=560)

conta_10 = Label(consumos, text="Conta 10", font=(10), width=15)
conta_10.place(x=0, y=560)

botao_10 = Button(consumos, text=" . . . ",
                  command=lambda: [calendario(campo_10, 400)])
botao_10.place(x=300, y=560)

# 11

campo_11 = Entry(consumos, text="Campo 11", font=(10),
                 width=13, justify='center', fg='blue')
campo_11.place(x=140, y=600)

conta_11 = Label(consumos, text="Conta 11", font=(10), width=15)
conta_11.place(x=0, y=600)

botao_11 = Button(consumos, text=" . . . ",
                  command=lambda: [calendario(campo_11, 440)])
botao_11.place(x=300, y=600)

# 12

campo_12 = Entry(consumos, text="Campo 12", font=(10),
                 width=13, justify='center', fg='blue')
campo_12.place(x=140, y=640)

conta_12 = Label(consumos, text="Conta 12", font=(10), width=15)
conta_12.place(x=0, y=640)

botao_12 = Button(consumos, text=" . . . ",
                  command=lambda: [calendario(campo_12, 480)])
botao_12.place(x=300, y=640)

#######################################  DIREITA  ##############################################

# 1

campok_1 = Entry(consumos, text="Campok 1", font=(10), width=13)
campok_1.place(x=720, y=200)

kwh_1 = Label(consumos, text="KW/h 1", font=(10), width=15)
kwh_1.place(x=580, y=200)

# 2

campok_2 = Entry(consumos, text="Campok 2", font=(10), width=13)
campok_2.place(x=720, y=240)

kwh_2 = Label(consumos, text="KW/h 2", font=(10), width=15)
kwh_2.place(x=580, y=240)

# 3

campok_3 = Entry(consumos, text="Campok 3", font=(10), width=13)
campok_3.place(x=720, y=280)

kwh_3 = Label(consumos, text="KW/h 3", font=(10), width=15)
kwh_3.place(x=580, y=280)

# 4

campok_4 = Entry(consumos, text="Campok 4", font=(10), width=13)
campok_4.place(x=720, y=320)

kwh_4 = Label(consumos, text="KW/h 4", font=(10), width=15)
kwh_4.place(x=580, y=320)

# 5

campok_5 = Entry(consumos, text="Campok 5", font=(10), width=13)
campok_5.place(x=720, y=360)

kwh_5 = Label(consumos, text="KW/h 5", font=(10), width=15)
kwh_5.place(x=580, y=360)

# 6

campok_6 = Entry(consumos, text="Campok 6", font=(10), width=13)
campok_6.place(x=720, y=400)

kwh_6 = Label(consumos, text="KW/h 6", font=(10), width=15)
kwh_6.place(x=580, y=400)

# 7

campok_7 = Entry(consumos, text="Campok 7", font=(10), width=13)
campok_7.place(x=720, y=440)

kwh_7 = Label(consumos, text="KW/h 7", font=(10), width=15)
kwh_7.place(x=580, y=440)

# 8

campok_8 = Entry(consumos, text="Campok 8", font=(10), width=13)
campok_8.place(x=720, y=480)

kwh_8 = Label(consumos, text="KW/h 8", font=(10), width=15)
kwh_8.place(x=580, y=480)

# 9

campok_9 = Entry(consumos, text="Campok 9", font=(10), width=13)
campok_9.place(x=720, y=520)

kwh_9 = Label(consumos, text="KW/h 9", font=(10), width=15)
kwh_9.place(x=580, y=520)

# 10

campok_10 = Entry(consumos, text="Campok 10", font=(10), width=13)
campok_10.place(x=720, y=560)

kwh_10 = Label(consumos, text="KW/h 10", font=(10), width=15)
kwh_10.place(x=580, y=560)

# 11

campok_11 = Entry(consumos, text="Campok 11", font=(10), width=13)
campok_11.place(x=720, y=600)

kwh_11 = Label(consumos, text="KW/h 11", font=(10), width=15)
kwh_11.place(x=580, y=600)

# 12

campok_12 = Entry(consumos, text="Campok 12", font=(10), width=13)
campok_12.place(x=720, y=640)

kwh_12 = Label(consumos, text="KW/h 12", font=(10), width=15)
kwh_12.place(x=580, y=640)

#############
botao_salvar = Button(consumos, text="Salvar consumo", bg="#3b3b3b",
                      fg="white", font=("Arial Black", 9), command=add_consumo)

botao_salvar.place(x=260, y=100)

botao_calc_pot = Button(consumos, text="Calcular potencia minima", bg="#3b3b3b",
                        fg="white", font=("Arial Black", 9), command=calc_potencia_min)

botao_calc_pot.place(x=520, y=100)

campo_calc_pot = Entry(consumos, text="KW/h 12", font=(10), width=15)
campo_calc_pot.place(x=720, y=100)


consumos.mainloop()
