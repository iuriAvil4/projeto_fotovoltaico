from dataclasses import replace
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import oracledb


username = 'SYSTEM'  # usuário
password = '123456'  # senha
# string de conexão do Oracle, configurado no cliente Oracle, arquivo tnsnames.ora
dsn = 'localhost/xe'
port = 1521
encoding = 'UTF-8'


class Placas:


    def __init__(self):
        self.placa = Tk()
        self.placa.geometry("800x500+565+270")
        self.placa.title("Adicionar placa")

        
        # COMBOBOX PLACAS
        self.placa_selecionada = tkinter.StringVar()
        self.cb_placa = ttk.Combobox(self.placa, textvariable=self.placa_selecionada, width=35)
        self.cb_placa.place(x=290, y=30)

        self.cb_placa.bind("<<ComboboxSelected>>", self.preenche_campos)

        self.texto_placa = Label(self.placa, text="DIGITE OS DADOS DA PLACA",
                            font=("Arial Black", 17), fg="#3b3b3b")
        self.texto_placa.place(x=220, y=75)

        # TEXTO LADO ESQUERDO
        self.texto_marca = Label(self.placa, text="Marca:", font=("Arial", 12), fg="#3b3b3b")
        self.texto_marca.place(x=125, y=130)

        self.texto_modelo = Label(self.placa, text="Modelo:",
                            font=("Arial", 12), fg="#3b3b3b")
        self.texto_modelo.place(x=125, y=170)

        self.texto_potmax = Label(self.placa, text="Pot. Max.:",
                            font=("Arial", 12), fg="#3b3b3b")
        self.texto_potmax.place(x=125, y=210)

        self.texto_vmax = Label(self.placa, text="V. Max.:",
                        font=("Arial", 12), fg="#3b3b3b")
        self.texto_vmax.place(x=125, y=250)

        self.texto_imax = Label(self.placa, text="I. Max.:",
                        font=("Arial", 12), fg="#3b3b3b")
        self.texto_imax.place(x=125, y=290)

        self.texto_vcaberto = Label(self.placa, text="V. C. Aberto:",
                            font=("Arial", 12), fg="#3b3b3b")
        self.texto_vcaberto.place(x=125, y=330)

        self.texto_icurc = Label(self.placa, text="I. Cur. C.:",
                            font=("Arial", 12), fg="#3b3b3b")
        self.texto_icurc.place(x=125, y=370)

        # TEXTO LADO DIREITO
        self.texto_eficiencia = Label(self.placa, text="Eficiencia:",
                                font=("Arial", 12), fg="#3b3b3b")
        self.texto_eficiencia.place(x=430, y=130)

        self.texto_dlarg = Label(self.placa, text="D. Larg:",
                            font=("Arial", 12), fg="#3b3b3b")
        self.texto_dlarg.place(x=430, y=170)

        self.texto_dalt = Label(self.placa, text="D. Alt:", font=("Arial", 12), fg="#3b3b3b")
        self.texto_dalt.place(x=430, y=210)

        self.texto_desp = Label(self.placa, text="D. Esp:", font=("Arial", 12), fg="#3b3b3b")
        self.texto_desp.place(x=430, y=250)

        self.texto_peso = Label(self.placa, text="Peso:", font=("Arial", 12), fg="#3b3b3b")
        self.texto_peso.place(x=430, y=290)

        self.texto_tpcel = Label(self.placa, text="Tp. Cel:",
                            font=("Arial", 12), fg="#3b3b3b")
        self.texto_tpcel.place(x=430, y=330)

        self.texto_descricao = Label(self.placa, text="Descricao:",
                                font=("Arial", 12), fg="#3b3b3b")
        self.texto_descricao.place(x=430, y=370)

        # CAMPOS LADO ESQUERDO
        self.campo_marca = Entry(self.placa, text="Marca", font=(10), width=15)
        self.campo_marca.place(x=220, y=130)

        self.campo_modelo = Entry(self.placa, text="Modelo", font=(10), width=15)
        self.campo_modelo.place(x=220, y=170)

        self.campo_potmax = Entry(self.placa, text="Potencia Maxima", font=(10), width=15)
        self.campo_potmax.place(x=220, y=210)

        self.campo_vmax = Entry(self.placa, text="Tensao Maxima", font=(10), width=15)
        self.campo_vmax.place(x=220, y=250)

        self.campo_imax = Entry(self.placa, text="Corrente Maxima", font=(10), width=15)
        self.campo_imax.place(x=220, y=290)

        self.campo_vcaberto = Entry(self.placa, text="Tensao em circuito aberto", font=(10), width=15)
        self.campo_vcaberto.place(x=220, y=330)

        self.campo_icurc = Entry(self.placa, text="Corrente em circuito",
                            font=(10), width=15)
        self.campo_icurc.place(x=220, y=370)

        # CAMPOS LADO DIREITO
        self.campo_eficiencia = Entry(self.placa, text="Eficiencia", font=(10), width=15)
        self.campo_eficiencia.place(x=530, y=130)

        self.campo_dlarg = Entry(self.placa, text="Largura", font=(10), width=15)
        self.campo_dlarg.place(x=530, y=170)

        self.campo_dalt = Entry(self.placa, text="Altura", font=(10), width=15)
        self.campo_dalt.place(x=530, y=210)

        self.campo_desp = Entry(self.placa, text="Espessura", font=(10), width=15)
        self.campo_desp.place(x=530, y=250)

        self.campo_peso = Entry(self.placa, text="Peso", font=(10), width=15)
        self.campo_peso.place(x=530, y=290)

        self.campo_tpcel = Entry(self.placa, text="Tipo celula", font=(10), width=15)
        self.campo_tpcel.place(x=530, y=330)

        self.campo_descricao = Entry(self.placa, text="Descricao", font=(10), width=15)
        self.campo_descricao.place(x=530, y=370)

        # BOTOES
        self.botao_salvar = Button(self.placa, text="Salvar placa", bg="#3b3b3b",
                            fg="white", font=("Arial Black", 11), command=self.add_placa)

        self.botao_salvar.place(x=330, y=430)

        self.botao_deletar = Button(self.placa, text="Deletar placa", bg="#3b3b3b",
                            fg="white", font=("Arial Black", 8), command=self.delete_placas)

        self.botao_deletar.place(x=565, y=440)

        self.botao_limpar = Button(self.placa, text="Limpar campos", bg="#3b3b3b",
                            fg="white", font=("Arial Black", 8), command=self.limpar_campos)

        self.botao_limpar.place(x=565, y=410)

        self.placa.mainloop()
        
        


    def add_placa(self):

        # Data for binding
        pcampo_marca = self.campo_marca.get().replace(" ", "")
        pcampo_modelo = self.campo_modelo.get().strip()
        pcampo_potmax = float(self.campo_potmax.get().strip())
        pcampo_vmax = float(self.campo_vmax.get().strip())
        pcampo_imax = float(self.campo_imax.get().strip())
        pcampo_vcaberto = float(self.campo_vcaberto.get().strip())
        pcampo_icurc = float(self.campo_icurc.get().strip())
        pcampo_eficiencia = float(self.campo_eficiencia.get().strip())
        pcampo_dlarg = float(self.campo_dlarg.get().strip())
        pcampo_dalt = float(self.campo_dalt.get().strip())
        pcampo_desp = float(self.campo_desp.get().strip())
        pcampo_peso = float(self.campo_peso.get().strip())
        pcampo_tpcel = self.campo_tpcel.get().strip()
        pcampo_descricao = self.campo_descricao.get().strip()

        try:
            # establish a new connection
            connection = oracledb.connect(user="SYSTEM", password=password, dsn="localhost/xe")
            # create a cursor
            cursor = connection.cursor()
            pmsg = cursor.var(str)
            cursor.callproc('PKG_PLACAS.add_placas', [pcampo_marca.strip(), pcampo_modelo, pcampo_potmax,
                                                      pcampo_vmax, pcampo_imax, pcampo_vcaberto,
                                                      pcampo_icurc, pcampo_eficiencia, pcampo_dlarg,
                                                      pcampo_dalt, pcampo_desp, pcampo_peso,
                                                      pcampo_tpcel, pcampo_descricao, pmsg])

            tkinter.messagebox.showinfo(
                title='Result',
                message=f'{pmsg.getvalue()}!'
            )

            self.pesquisar_placa()
            print(pmsg)

        except oracledb.Error as error:
            print('Error occurred on add_placa:')
            print(error)
            return error


    def pesquisar_placa(self):

        sql = """select id, marca ||' - ' || modelo
                from PLACA_SOLAR"""

        try:
            # establish a new connection
            connection = oracledb.connect(user="SYSTEM", password=password, dsn="localhost/xe")
            # create a cursor
            cursor = connection.cursor()
            pmsg = cursor.var(str)
            cursor.execute(sql)

            self.cb_placa.delete(0, END)
            self.cb_placa['values'] = [i[1] for i in cursor]

        except oracledb.Error as error:
            print('Error occurred on pesquisar_placa:')
            print(error)
            return error

    

    def limpar_campos(self):
       
        self.campo_marca.delete(0, END)
        self.campo_modelo.delete(0, END)
        self.campo_potmax.delete(0, END)
        self.campo_vmax.delete(0, END)
        self.campo_imax.delete(0, END)
        self.campo_vcaberto.delete(0, END)
        self.campo_icurc.delete(0, END)
        self.campo_eficiencia.delete(0, END)
        self.campo_dlarg.delete(0, END)
        self.campo_dalt.delete(0, END)
        self.campo_desp.delete(0, END)
        self.campo_peso.delete(0, END)
        self.campo_tpcel.delete(0, END)
        self.campo_descricao.delete(0, END)
        ####self.pesquisar_placa()

    def preenche_campos(self, event):

        sql = """select marca, modelo, pot_max, v_max, i_max, v_c_aberto, i_cur_c, eficiencia, d_larg, d_alt, d_esp, peso, tp_cel, nvl(descricao, ' ') descricao 
                    from placa_solar
                    where modelo = :pmodelo """
        # where modelo = :pmodelo"""

        self.cb_placa = event.widget.get()
       # print(cb_placa[0:12])
        aux = self.cb_placa[self.cb_placa.find(" - "):]
        pmodel = aux[3:]
        print(pmodel)

        try:
            # establish a new connection
            connection = oracledb.connect(user="SYSTEM", password=password, dsn="localhost/xe")
            # create a cursor
            cursor = connection.cursor()
            cursor.execute(sql, pmodelo=pmodel)

            self.limpar_campos()

            for row in cursor:

                self.campo_marca.insert(0, row[0])
                self.campo_modelo.insert(0, row[1])
                self.campo_potmax.insert(0, row[2])
                self.campo_vmax.insert(0, row[3])
                self.campo_imax.insert(0, row[4])
                self.campo_vcaberto.insert(0, row[5])
                self.campo_icurc.insert(0, row[6])
                self.campo_eficiencia.insert(0, row[7])
                self.campo_dlarg.insert(0, row[8])
                self.campo_dalt.insert(0, row[9])
                self.campo_desp.insert(0, row[10])
                self.campo_peso.insert(0, row[11])
                self.campo_tpcel.insert(0, row[12])
                self.campo_descricao.insert(0, row[13])

        except oracledb.Error as error:
            print('Error occurred on preencher_campos:')
            print(error)
            return error
        ####self.pesquisar_placa()

    def delete_placas(self):

        # Data for binding
        asker = tkinter.messagebox.askyesno(
            'Aviso', 'Tem certeza que quer remover o registro?')
        pcampo_modelo = self.campo_modelo.get()

        if asker == True:

            try:
                # establish a new connection
                connection = oracledb.connect(user="SYSTEM", password=password, dsn="localhost/xe")
                # create a cursor
                cursor = connection.cursor()
                pmsg = cursor.var(str)
                cursor.callproc('PKG_PLACAS.delete_placas',
                                [pcampo_modelo, pmsg])

                tkinter.messagebox.showinfo(
                    title='Atencao',
                    message=f'Registros apagados {pmsg.getvalue()}!'
                )

                print(pmsg)
                self.pesquisar_placa()
                self.limpar_campos()

            except oracledb.Error as error:
                print('Error occurred on delete_placa:')
                print(error)
                return error


        
        #self.pesquisar_placa()
Placas()
