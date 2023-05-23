
import tkinter as tk

# Diccionario con las conversiones
conversion_rates = {
    "Longitud": {
        "Metros": 1,
        "Kilometros": 0.001,
        "Millas": 0.000621371,
        "Pulgadas": 39.3701,
        "Pies": 3.28084
    },
    "Peso": {
        "Gramos": 1000,
        "Kilogramos": 1,
        "Libras": 2.20462,
        "Onzas": 35.274
    },
    # Añade más categorías y unidades aquí...
}

# Creando la ventana
window = tk.Tk()
window.title("Conversor de unidades")

# Creando los widgets
input_label = tk.Label(master=window, text="Introduzca el valor a convertir:")
input_entry = tk.Entry(master=window)

categoria_var = tk.StringVar(master=window)
categoria_var.set("Longitud")  # Valor inicial

from_unit_var = tk.StringVar(master=window)
from_unit_menu = tk.OptionMenu(window, from_unit_var, *conversion_rates[categoria_var.get()].keys())

to_unit_var = tk.StringVar(master=window)
to_unit_menu = tk.OptionMenu(window, to_unit_var, *conversion_rates[categoria_var.get()].keys())

convert_button = tk.Button(master=window, text="Convertir")
result_label = tk.Label(master=window, text="Resultado:")

def convert():
    """Convierte el valor de una unidad a otra"""
    try:
        input_value = float(input_entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        from_value = conversion_rates[categoria_var.get()][from_unit]
        to_value = conversion_rates[categoria_var.get()][to_unit]
        result = input_value * to_value / from_value # Convierte a la unidad base y luego a la unidad final
        result_label.config(text=str(result))
    except ValueError:
        result_label.config(text="Por favor, introduce un número.")

def update_options(*args):
    """Actualiza las opciones de los menus cuando cambia la categoría"""
    from_unit_var.set('')  # Borra el valor actual
    to_unit_var.set('')  # Borra el valor actual

    from_unit_menu['menu'].delete(0, 'end')  # Borra las opciones actuales
    to_unit_menu['menu'].delete(0, 'end')  # Borra las opciones actuales

    # Obtiene las nuevas opciones
    new_choices = conversion_rates[categoria_var.get()].keys()

    # Actualiza las opciones
    for choice in new_choices:
        from_unit_menu['menu'].add_command(label=choice, command=tk._setit(from_unit_var, choice))
        to_unit_menu['menu'].add_command(label=choice, command=tk._setit(to_unit_var, choice))

    # Establece un valor por defecto
    from_unit_var.set(next(iter(new_choices)))
    to_unit_var.set(next(iter(new_choices)))

categoria_var.trace('w', update_options)  # Llama a update_options cuando cambia categoria_var
categoria_option = tk.OptionMenu(window, categoria_var, *conversion_rates.keys())

convert_button.config(command=convert)

# Ubicando los widgets
input_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1)
categoria_option.grid(row=1, column=0)
from_unit_menu.grid(row=2, column=0)
to_unit_menu.grid(row=2, column=1)
convert_button.grid(row=3, column=0)
result_label.grid(row=4, column=0)

# Establecer los valores iniciales de los menús de selección de unidades
from_unit_var.set(next(iter(conversion_rates[categoria_var.get()].keys())))
to_unit_var.set(next(iter(conversion_rates[categoria_var.get()].keys())))

# Iniciar la aplicación
window.mainloop()