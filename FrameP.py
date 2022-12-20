from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from optimization.Optimizador import Optimizador
from grammar import grammar
from grammar.optimizator import optimizator
from sym.Environment import *
from sym.Generator import *

import sys

class Interfaz():

    def __init__(self, *args, **kwargs):
        self.raiz = Tk()
        self.menubar = Menu(self.raiz)

        self.Modo = True
        self.ReporteErrores = ''
        self.ReporteSimbolos = ''
        self.TextoErrores([])
        self.menubar.add_command(label="Modo Claro", command=self.CambiarModo)
        self.menubar.add_command(label="Ejecutar", command=self.Ejecutar)
        self.menuReportes = Menu(self.menubar)
        self.menuReportes.add_command(label="Tabla de símbolos", command=self.GenerarReporteSimbolos)
        self.menuReportes.add_command(label="Tabla de errores", command=self.GenerarReporteErrores)
        self.menuReportes.add_command(label="Tabla de bases de datos existentes", command=self.donothing)
        self.menuReportes.add_command(label="Tabla de base de datos", command=self.donothing)
        self.menubar.add_cascade(label="Reportes", menu=self.menuReportes)
        self.menuLimpiar = Menu(self.menubar)
        self.menuLimpiar.add_command(label="Entrada", command=self.LimpiarEntrada)
        self.menuLimpiar.add_command(label="Consola", command=self.LimpiarConsola)
        self.menuLimpiar.add_command(label="Todo", command=self.LimpiarTodo)
        self.menubar.add_cascade(label="Limpiar", menu=self.menuLimpiar)
        self.menubar.add_command(label="Acerca De", command=self.donothing)

        self.raiz.config(menu=self.menubar)
        self.raiz.title("PyToPy")
        self.raiz.iconbitmap("Python.ico")

        self.frameP = Frame(self.raiz)
        self.frameP.pack()
        self.frameP.grid(row=0,column=0,sticky="NSEW")

        self.style = ttk.Style()
        self.style.theme_use('winnative')

        Grid.rowconfigure(self.raiz,0,weight=1) 
        Grid.columnconfigure(self.raiz,0,weight=1)
        Grid.rowconfigure(self.frameP,0,weight=0)
        Grid.rowconfigure(self.frameP,1,weight=1)
        Grid.columnconfigure(self.frameP,0,weight=0)
        Grid.columnconfigure(self.frameP,1,weight=1)
        Grid.columnconfigure(self.frameP,2,weight=0)
        Grid.columnconfigure(self.frameP,3,weight=0)
        Grid.columnconfigure(self.frameP,4,weight=1)

        self.labelEntrada = Label(self.frameP, text = "Entrada")
        self.labelEntrada.grid(row=0, column=0, sticky = "w", padx=5)

        self.cuadroLineasEntrada = Text(self.frameP, width = 5, height = 40, wrap=NONE, bg="#E7E7E7", state=DISABLED)
        self.cuadroLineasEntrada.grid(row=1, column=0, padx=(5,0), pady=5,sticky="NSEW")

        self.cuadroEntrada = Text(self.frameP, width = 70, height = 40, wrap=NONE, selectforeground = 'white', selectbackground = 'black')
        self.cuadroEntrada.grid(row=1, column=1, padx=(0,0), pady=(5,0),sticky="NSEW")
        
        self.scrollBarVerticalE = ttk.Scrollbar(self.frameP, command=self.cuadroEntrada.yview, orient="vertical")
        self.scrollBarVerticalE.grid(row=1, column=2, sticky="nsew", padx=(0,5), pady=5)

        self.cuadroEntrada['yscrollcommand'] = self.scrollBarVerticalE.set

        self.scrollBarHorizontalE = ttk.Scrollbar(self.frameP, command=self.cuadroEntrada.xview, orient="horizontal")
        self.scrollBarHorizontalE.grid(row=2, column=1, sticky="nsew", padx=(0,0), pady=(0,10))

        self.cuadroEntrada['xscrollcommand'] = self.scrollBarHorizontalE.set
        self.cuadroEntrada.bind("<Key>", self.onPressDelayE)
        self.cuadroEntrada.bind("<Button-1>", self.redrawE)

        self.scrollBarVerticalE.bind("<Button-1>", self.onScrollPressE)

        self.cuadroEntrada.bind("<MouseWheel>", self.onPressDelayE)

        self.redrawE()

        self.labelConsola = Label(self.frameP, text = "Consola")
        self.labelConsola.grid(row=0, column=3, sticky = "w", padx=5)

        self.cuadroLineasConsola = Text(self.frameP, width = 5, height = 40, wrap=NONE, bg="#E7E7E7", state=DISABLED)
        self.cuadroLineasConsola.grid(row=1, column=3, padx=(5,0), pady=5,sticky="NSEW")

        self.cuadroConsola = Text(self.frameP, width = 70, height = 40, wrap=NONE, state=DISABLED, selectforeground = 'white', selectbackground = 'black')
        self.cuadroConsola.grid(row=1, column=4, padx=(0,0), pady=(5,0),sticky="NSEW")

        self.scrollBarVerticalC = ttk.Scrollbar(self.frameP, command=self.cuadroConsola.yview)
        self.scrollBarVerticalC.grid(row=1, column=5, sticky="nsew", padx=(0,5), pady=5)

        self.cuadroConsola['yscrollcommand'] = self.scrollBarVerticalC.set

        self.scrollBarHorizontalV = ttk.Scrollbar(self.frameP, command=self.cuadroConsola.xview, orient="horizontal")
        self.scrollBarHorizontalV.grid(row=2, column=4, sticky="nsew", padx=(0,0), pady=(0,10))

        self.cuadroConsola['xscrollcommand'] = self.scrollBarHorizontalV.set
        self.cuadroConsola.bind("<Key>", self.onPressDelayC)
        self.cuadroConsola.bind("<Button-1>", self.redrawC)

        self.scrollBarVerticalC.bind("<Button-1>", self.onScrollPressC)

        self.cuadroConsola.bind("<MouseWheel>", self.onPressDelayC)

        self.redrawC()

        self.raiz.mainloop()

    def CambiarModo(self):
        if self.Modo:
            self.menubar.entryconfigure(1, label="Modo Oscuro")
            self.menubar.configure(background='black', foreground='black', activebackground='white', activeforeground='white')
            self.frameP.configure(background="black")
            self.labelEntrada.configure(bg='black', fg='white')
            self.labelConsola.configure(bg='black', fg='white')
            self.cuadroLineasEntrada.configure(bg='#181818', fg='white')
            self.cuadroLineasConsola.configure(bg='#181818', fg='white')
            self.cuadroEntrada.configure(bg='black', fg='white', insertbackground = 'white', selectforeground = 'black', selectbackground = 'white')
            self.cuadroConsola.configure(bg='black', fg='white', insertbackground = 'white', selectforeground = 'black', selectbackground = 'white')
            #self.scrollBarVerticalE.configure(bg='black', fg='white', activebackground='black')
        else:
            self.menubar.entryconfigure(1, label="Modo Claro")
            self.menubar.configure(background='white', foreground='white', activebackground='black', activeforeground='black')
            self.frameP.configure(background="white")
            self.labelEntrada.configure(bg='white', fg='black')
            self.labelConsola.configure(bg='white', fg='black')
            self.cuadroLineasEntrada.configure(bg='#E7E7E7', fg='black', insertbackground='black')
            self.cuadroLineasConsola.configure(bg='#E7E7E7', fg='black')
            self.cuadroEntrada.configure(bg='white', fg='black', insertbackground = 'black', selectforeground = 'white', selectbackground = 'black')
            self.cuadroConsola.configure(bg='white', fg='black', insertbackground = 'black', selectforeground = 'white', selectbackground = 'black')
            #self.scrollBarVerticalE.configure(bg='white', fg='black', activebackground='white')
        self.Modo = not self.Modo

    def Ejecutar(self):
        self.Texto = self.cuadroEntrada.get(1.0, END)
        gen_aux = Generator()
        gen_aux.clean_all()
        generator = gen_aux.get_instance()
        new_env = Environment(None)
        ast = grammar.parse(self.Texto)
        try:
            for inst in ast:
                inst.compile(new_env)
            C3D = generator.get_code()
            generator.clean_all()
            self.cuadroConsola.configure(state='normal')
            self.cuadroConsola.delete('1.0','end')
            self.cuadroConsola.insert(END, C3D)
            self.cuadroConsola.configure(state='disabled')
            self.redrawC()
        except Exception as e:
            print("no se puede compilar", e)
            error = {}
            error['type'] = "no contemplado"
            error['text'] = "no se puede compilar"
            Environment.errores.append(error)
        #self.cuadroConsola.configure(state='normal')
        #self.cuadroConsola.insert(END, f"----------------------------\n")
        #self.cuadroConsola.configure(state='disabled')
        #self.Texto = self.cuadroEntrada.get(1.0, END)
        #self.cuadroConsola.delete('1.0','end')
        #[resultado, ListErrores] = Gramatica.parse(self.Texto)
        #Principal = TablaSimbolos('<General>',None,ListErrores)
        #Principal.Return.Tipo = '()'
        #Principal.Consola = self.cuadroConsola
        #if resultado != None:
        #    for i in resultado:
        #        if i.Tipo == "Funcion":
        #            if Principal.BuscarSimbolos(i.Nombre) == None:
        #                Principal.Insertar(Simbolo(i.Nombre, i, "Funcion", False, ListErrores))
        #            else:
        #                ListErrores.append(Errores('Ya existe ' + i.Nombre, 'Semantico'))
        #        elif i.Tipo == "Estructura":
        #            """"""
        #        elif i.Tipo == "Modulo":
        #            """"""
        #if not Principal.EjecutarMain():
        #    messagebox.showinfo(message="No se detecto metodo main", title="Sin main")
        #if len(ListErrores) != 0:
        #    messagebox.showinfo(message="se han encontrado error en la ejecucion", title="Errores")
        #    self.cuadroConsola.configure(state='normal')
        #    for x in ListErrores:
        #        self.cuadroConsola.insert(END, f"{x.PrintError()}")
        #    self.cuadroConsola.configure(state='disabled')
        #self.cuadroConsola.configure(state='normal')
        #self.cuadroConsola.insert(END, f"\n----------------------------\n")
        #self.cuadroConsola.configure(state='disabled')
        #self.redrawC()
        #self.TextoErrores(ListErrores)
        #self.TextoSimbolos(Principal)
        #Gramatica.ListErrores = []
        """"""

    def TextoSimbolos(self, Principal):
        self.ReporteSimbolos = """<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="viewport" content="initial-scale=1, maximum-scale=1">
    <title>Tabla de Errores</title>
    <style>
        h1 {
            font-size: 30px;
            color: #fff;
            text-transform: uppercase;
            font-weight: 300;
            text-align: center;
            margin-bottom: 15px;
        }

        table {
            width: 100%;
            table-layout: fixed;
        }

        .tbl-header {
            background-color: rgba(255, 255, 255, 0.3);
        }

        .tbl-content {
            height: 200px;
            overflow-x: auto;
            margin-top: 0px;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        th {
            padding: 20px 15px;
            text-align: left;
            font-weight: 500;
            font-size: 12px;
            color: #fff;
            text-transform: uppercase;
        }

        td {
            padding: 15px;
            text-align: left;
            vertical-align: middle;
            font-weight: 300;
            font-size: 12px;
            color: #fff;
            border-bottom: solid 1px rgba(255, 255, 255, 0.1);
        }

        /* demo styles */
        @import url(https://fonts.googleapis.com/css?family=Roboto:400,500,300,700);

        body {
            background: -webkit-linear-gradient(left, #25c481, #25b7c4);
            background: linear-gradient(to right, #25c481, #25b7c4);
            font-family: 'Roboto', sans-serif;
        }

        section {
            margin-top: 50px;
            margin-bottom: 50px;
            margin-left: 200px;
            margin-right: 200px;
        }

        /* follow me template */
        .made-with-love {
            margin-top: 40px;
            padding: 10px;
            clear: left;
            text-align: center;
            font-size: 10px;
            font-family: arial;
            color: #fff;
        }

        .made-with-love i {
            font-style: normal;
            color: #F50057;
            font-size: 14px;
            position: relative;
            top: 2px;
        }

        .made-with-love a {
            color: #fff;
            text-decoration: none;
        }

        .made-with-love a:hover {
            text-decoration: underline;
        }

        ::-webkit-scrollbar {
            width: 6px;
        }

        ::-webkit-scrollbar-track {
            -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
        }

        ::-webkit-scrollbar-thumb {
            -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
        }
    </style>
    <script type="text/javascript">
        $(window).on("load resize ", function () {
            var scrollWidth = $('.tbl-content').width() - $('.tbl-content table').width();
            $('.tbl-header').css({ 'padding-right': scrollWidth });
        }).resize();
    </script>
</head>

<body>
    <section>"""
        self.ReporteSimbolos += Principal.ReporteSimbolos()
        self.ReporteSimbolos += """</body>
    </section>
</html>
"""

    def LimpiarConsola(self):
        self.cuadroConsola.configure(state='normal')
        self.cuadroConsola.delete("1.0","end")
        self.cuadroConsola.configure(state='disabled')
        self.redrawC()

    def LimpiarEntrada(self):
        self.cuadroEntrada.delete("1.0","end")
        self.redrawE()

    def LimpiarTodo(self):
        self.LimpiarConsola()
        self.LimpiarEntrada()

    def TextoErrores(self, ListErrores):
        self.ReporteErrores = """<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="viewport" content="initial-scale=1, maximum-scale=1">
    <title>Tabla de Errores</title>
    <style>
        h1 {
            font-size: 30px;
            color: #fff;
            text-transform: uppercase;
            font-weight: 300;
            text-align: center;
            margin-bottom: 15px;
        }

        table {
            width: 100%;
            table-layout: fixed;
        }

        .tbl-header {
            background-color: rgba(255, 255, 255, 0.3);
        }

        .tbl-content {
            height: 500px;
            overflow-x: auto;
            margin-top: 0px;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        th {
            padding: 20px 15px;
            text-align: left;
            font-weight: 500;
            font-size: 12px;
            color: #fff;
            text-transform: uppercase;
        }

        td {
            padding: 15px;
            text-align: left;
            vertical-align: middle;
            font-weight: 300;
            font-size: 12px;
            color: #fff;
            border-bottom: solid 1px rgba(255, 255, 255, 0.1);
        }

        /* demo styles */
        @import url(https://fonts.googleapis.com/css?family=Roboto:400,500,300,700);

        body {
            background: -webkit-linear-gradient(left, #25c481, #25b7c4);
            background: linear-gradient(to right, #25c481, #25b7c4);
            font-family: 'Roboto', sans-serif;
        }

        section {
            margin-top: 50px;
            margin-bottom: 50px;
            margin-left: 200px;
            margin-right: 200px;
        }

        /* follow me template */
        .made-with-love {
            margin-top: 40px;
            padding: 10px;
            clear: left;
            text-align: center;
            font-size: 10px;
            font-family: arial;
            color: #fff;
        }

        .made-with-love i {
            font-style: normal;
            color: #F50057;
            font-size: 14px;
            position: relative;
            top: 2px;
        }

        .made-with-love a {
            color: #fff;
            text-decoration: none;
        }

        .made-with-love a:hover {
            text-decoration: underline;
        }

        ::-webkit-scrollbar {
            width: 6px;
        }

        ::-webkit-scrollbar-track {
            -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
        }

        ::-webkit-scrollbar-thumb {
            -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
        }
    </style>
    <script type="text/javascript">
        $(window).on("load resize ", function () {
            var scrollWidth = $('.tbl-content').width() - $('.tbl-content table').width();
            $('.tbl-header').css({ 'padding-right': scrollWidth });
        }).resize();
    </script>
</head>

<body>
    <section>
        <h1>Errores</h1>
        <div class="tbl-header">
            <table cellpadding="0" cellspacing="0" border="0">
                <thead>
                    <tr>
                        <th>Numero</th>
                        <th>Info</th>
                        <th>Tipo</th>
                    </tr>
                </thead>
            </table>
        </div>
        <div class="tbl-content">
            <table cellpadding="0" cellspacing="0" border="0">
                <tbody>"""
        for i in range(len(ListErrores)):
            self.ReporteErrores+="                    <tr>\n"
            self.ReporteErrores+="                        <td>" + str(i) + ".</td>\n"
            self.ReporteErrores+="                        <td>" + str(ListErrores[i].Valor) + ".</td>\n"
            self.ReporteErrores+="                        <td>" + str(ListErrores[i].Tipo) + ".</td>\n"
            self.ReporteErrores+="                    </tr>\n"
        self.ReporteErrores += """</tbody>
            </table>
        </div>
    </section>
</body>

</html>
"""

    def GenerarReporteErrores(self):
        Archivo = open("Reporte_Errores.html", 'w')
        Archivo.write(self.ReporteErrores)
        Archivo.close()

    def GenerarReporteSimbolos(self):
        Archivo = open("Reporte_Simbolos.html", 'w')
        Archivo.write(self.ReporteSimbolos)
        Archivo.close()

    def onScrollPressE(self, *args):
        self.scrollBarVerticalE.bind("<B1-Motion>", self.redrawE)

    def onPressDelayE(self, *args):
        self.raiz.after(2, self.redrawE)

    def redrawE(self, *args):
        self.cuadroLineasEntrada.configure(state='normal')
        self.cuadroLineasEntrada.delete("1.0","end")
        i = self.cuadroEntrada.index("@0,0")
        texto = ""
        while True :
            dline= self.cuadroEntrada.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            texto += linenum + "\n"
            #self.create_text(2, y, anchor="nw", text=linenum, fill="#606366")
            i = self.cuadroEntrada.index("%s+1line" % i)
        self.cuadroLineasEntrada.insert("end", texto)
        self.cuadroLineasEntrada.configure(state='disabled')

    def onScrollPressC(self, *args):
        self.scrollBarVerticalC.bind("<B1-Motion>", self.redrawC)

    def onPressDelayC(self, *args):
        self.raiz.after(2, self.redrawC)

    def redrawC(self, *args):
        self.cuadroLineasConsola.configure(state='normal')
        self.cuadroLineasConsola.delete("1.0","end")
        i = self.cuadroConsola.index("@0,0")
        texto = ""
        while True :
            dline= self.cuadroConsola.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            texto += linenum + "\n"
            #self.create_text(2, y, anchor="nw", text=linenum, fill="#606366")
            i = self.cuadroConsola.index("%s+1line" % i)
        self.cuadroLineasConsola.insert("end", texto)
        self.cuadroLineasConsola.configure(state='disabled')

    def donothing(self):
        print("hola")

if __name__ == "__main__":
    Interfaz()