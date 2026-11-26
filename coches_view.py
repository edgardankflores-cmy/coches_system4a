import conexionBD
from tkinter import Label,Entry,Button,Tk,messagebox,StringVar,Menu,Frame,ttk


def insertar_view(self):
    self.borrarPantalla()
    self.barraMenu()

    Label(self.frame1,text="...Ingresar los datos del Coche...").pack(pady=10)

    Label(self.frame1,text="Marca: ").pack(pady=5,padx=5,sticky="e")
    self.marca=Entry(self.frame1)
    self.marca.focus()
    self.marca.pack(pady=5)
    self.marca.grid(row=0,column=1,pady=5,padx=5,sticky="w")

    Label(self.frame1,text="Color: ").pack(pady=5,padx=5,sticky="e")
    self.color=Entry(self.frame1)
    self.color.pack(pady=5)
    self.color.grid(row=1,column=1,pady=5,padx=5,sticky="w")

    Label(self.frame1,text="Modelo: ").pack(pady=5,padx=5,sticky="e")
    self.modelo=Entry(self.frame1)
    self.modelo.pack(pady=5)
    self.modelo.grid(row=2,column=1,pady=5,padx=5,sticky="w")

    Label(self.frame1,text="Velocidad: ").pack(pady=5,padx=5,sticky="e")
    self.velocidad=Entry(self.frame1)
    self.velocidad.pack(pady=5)
    self.velocidad.grid(row=3,column=1,pady=5,padx=5,sticky="w")

    Label(self.frame1,text="Potencia: ").pack(pady=5,padx=5,sticky="e")
    self.potencia=Entry(self.frame1)
    self.potencia.pack(pady=5)
    self.potencia.grid(row=4,column=1,pady=5,padx=5,sticky="w")

    Label(self.frame1,text="# de Asientos: ").pack(pady=5,padx=5,sticky="e")
    self.asientos=Entry(self.frame1)
    self.asientos.pack(pady=5)
    self.asientos.grid(row=5,column=1,pady=5,padx=5,sticky="w")

    Button(self.frame1,text="Guardar",command=lambda:{self.insertar_controller(),self.insertar_view()}).pack(pady=10)

    Button(self.frame1,text="Regresar",command=self.menu_acciones).pack(pady=5)


    
    def eliminar_view(self):
        self.borrarPantalla()
        self.barraMenu()

        self.frame1=Frame(self.ventana)
        self.frame1.pack(pady=20)

        Label(self.frame1,text="...Ingresar el ID del Coche a Eliminar...").grid(row=0,column=0,columnspan=2,pady=10)

        Label(self.frame1,text="ID: ").grid(row=1,column=0,pady=5,padx=5,sticky="e")
        self.id=Entry(self.frame1)
        self.id.focus()
        self.id.grid(row=1,column=1,pady=5,padx=5,sticky="w")

        self.btn_buscar=Button(self.frame1,text="Buscar",command=lambda:self.buscar_controller("eliminar"))
        self.btn_buscar.grid(row=2,column=0,pady=10,padx=5)

        self.btn_eliminar=Button(self.frame1,text="Eliminar",state="disabled",command=lambda:{self.eliminar_controller(),self.eliminar_view()})
        self.btn_eliminar.grid(row=2,column=1,pady=10,padx=5)

        Button(self.frame1,text="Regresar",command=self.menu_acciones).grid(row=3,column=0,columnspan=2,pady=10)
 

    def modificar_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text="...Ingresar el ID del Coche a modificar...").pack(pady=10)

        self.frame1=Frame(self.ventana)
        self.frame1.pack(pady=10)

        Label(self.frame1,text="ID: ").grid(row=0,column=0,pady=5,padx=5,sticky="e")
        self.id=Entry(self.frame1)
        self.id.focus()
        self.id.grid(row=0,column=1,pady=5,padx=5,sticky="w")

        Button(self.frame1,text="Buscar",command=lambda:self.buscar_controller("modificar")).grid(row=1,column=0,columnspan=2,pady=5)

        self.var_marca=StringVar()
        self.var_color=StringVar()
        self.var_modelo=StringVar()
        self.var_velocidad=StringVar()
        self.var_potencia=StringVar()
        self.var_asientos=StringVar()

        Label(self.ventana,text="Nueva Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana,textvariable=self.var_marca)
        self.marca.pack(pady=5)

        Label(self.ventana,text="Nuevo Color: ").pack(pady=5)
        self.color=Entry(self.ventana,textvariable=self.var_color)
        self.color.pack(pady=5)

        Label(self.ventana,text="Nuevo Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana,textvariable=self.var_modelo)
        self.modelo.pack(pady=5)

        Label(self.ventana,text="Nueva Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana,textvariable=self.var_velocidad)
        self.velocidad.pack(pady=5)

        Label(self.ventana,text="Nueva Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana,textvariable=self.var_potencia)
        self.potencia.pack(pady=5)

        Label(self.ventana,text="Nuevo # de Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana,textvariable=self.var_asientos)
        self.asientos.pack(pady=5)

        self.btn_modificar=Button(self.ventana,text="Guardar",state="disabled",command=self.modificar_controller)
        self.btn_modificar.pack(pady=10)

        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)

    def consultar_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text=" ::: Consultar los Coches :::").pack(pady=10)
    # Tabla
        self.tree =ttk.Treeview(self.ventana, columns=("ID", "Marca", "Color", "Modelo","Velocidad","Potencia","Asientos"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Marca", text="Marca")
        self.tree.heading("Color", text="Color")
        self.tree.heading("Modelo", text="Modelo")
        self.tree.heading("Velocidad", text="Velocidad")
        self.tree.heading("Potencia", text="Potencia")
        self.tree.heading("Asientos", text="Asientos")
        self.tree.pack(fill="both", expand=False)

        self.mostrar_coches()
        
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)

    def cambiar_estado_btn(self,estado,tipo_accion):
        if estado and tipo_accion=="eliminar":
            self.btn_modificar.config(state="normal")
        elif estado and tipo_accion=="modificar":
            self.btn_eliminar.config(state="normal")
        elif not estado and tipo_accion=="eliminar":
            self.btn_modificar.config(state="disabled")
        elif not estado and tipo_accion=="modificar":
            self.btn_eliminar.config(state="disabled")

    def confirmacion_eliminar(self,tipo):
        resp=messagebox.askquestion(title="...¡Atencion!...",message=f"...¿Desea {tipo} este registro?...")

        if resp=="yes":
            return True
        else:
            return False

    # ... Contralador de Coches ...

    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(title="... Exitoso ...",message="...¡Accion Realizada con Exito!...")
        else:
            messagebox.showerror(title="...¡ Verifica por favor !...",message="...¡Esta Accion no pudo realizarse en este momento!...")
