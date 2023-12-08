import tkinter as tk
from tkinter import messagebox
from UniversalSimulation import Universal_simulation

class InitWindow:
    def __init__(self, help='', version=''):
        self.__init_window = tk.Tk()
        self.__init_window.title("Начальное окно")
        self.__init_window.geometry("320x380")

        self.__version_text = version
        self.__help_text = help

        self.variables = {
            "star_count": {"value": 200, "label": "Количество звезд"},
            "x_min": {"value": -800, "label": "Минимальное значение x"},
            "x_max": {"value": 800, "label": "Максимальное значение x"},
            "y_min": {"value": -500, "label": "Минимальное значение y"},
            "y_max": {"value": 500, "label": "Максимальное значение y"},
            "z_min": {"value": -500, "label": "Минимальное значение z"},
            "z_max": {"value": 500, "label": "Максимальное значение z"},
            "size_min": {"value": 0.1, "label": "Минимальный размер"},
            "size_max": {"value": 2.0, "label": "Максимальный размер"}
        }

        self.__create_widgets()

    def __create_widgets(self):
        row = 0
        for var_name, var_info in self.variables.items():
            label_text = var_info["label"]
            default_value = var_info["value"]

            label = tk.Label(self.__init_window, text=label_text)
            label.grid(row=row, column=0, padx=4, pady=4)

            entry = tk.Entry(self.__init_window)
            entry.insert(0, str(default_value))
            entry.grid(row=row, column=1, columnspan=2,  padx=4, pady=4)
            self.variables[var_name]["entry"] = entry

            row += 1

        button_start = tk.Button(self.__init_window, text="Старт", command=self.__start_simulation)
        button_start.grid(row=row, column=0, ipadx=6, ipady=6, padx=4, pady=4)

        button_help = tk.Button(self.__init_window, text="Справка", command=self.__show_help)
        button_help.grid(row=row, column=1, ipadx=6, ipady=6, padx=4, pady=4)

        label_version = tk.Label(self.__init_window, text=self.__version_text)
        label_version.grid(row=row, column=2, ipadx=6, ipady=6, padx=4, pady=4)

    def __start_simulation(self):

        star_count = int(self.variables["star_count"]["entry"].get())
        size_min = float(self.variables["size_min"]["entry"].get())
        size_max = float(self.variables["size_max"]["entry"].get())
        x_min = int(self.variables["x_min"]["entry"].get())
        x_max = int(self.variables["x_max"]["entry"].get())
        y_min = int(self.variables["y_min"]["entry"].get())
        y_max = int(self.variables["y_max"]["entry"].get())
        z_min = int(self.variables["z_min"]["entry"].get())
        z_max = int(self.variables["z_max"]["entry"].get())

        simulation = Universal_simulation(star_count, 
                            (x_min, x_max), 
                            (y_min, y_max), 
                            (z_min, z_max),
                            (size_min, size_max))
        simulation.run()

        #self.__init_window.destroy()

        
    def __show_help(self):
        messagebox.showinfo("Справка", self.__help_text)

    def run(self):
        self.__init_window.mainloop()