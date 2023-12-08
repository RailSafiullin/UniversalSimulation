import tkinter as tk
from tkinter import messagebox


class InitWindow:
    def __init__(self, help='', version=''):
        self.__init_window = tk.Tk()
        self.__init_window.title("Начальное окно")
        self.__init_window.geometry("320x380")

        self.__version_text = version
        self.__help_text = help

        self.variables = {

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

        self.__init_window.destroy()

        
    def __show_help(self):
        messagebox.showinfo("Справка", self.__help_text)

    def run(self):
        self.__init_window.mainloop()