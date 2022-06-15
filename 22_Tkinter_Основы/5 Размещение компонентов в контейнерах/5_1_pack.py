"""
Размещение по сторонам контейнера pack
"""
import tkinter
import tkinter.ttk

class Application(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # В вызове метода pack() самого контейнера, помещающего его в
        # окно, мы также можем указать необходимые нам параметры
        self.pack(fill="both", padx=4, pady=4)
        self.create_widgets()
        self.master.title("Pack")
        # Указываем у окна возможность изменения только ширины
        self.master.resizable(True, False)

    def create_widgets(self):
        entValue = tkinter.ttk.Entry(self)
        entValue.pack(fill="x", padx=4)

        btnShow = tkinter.ttk.Button(self, text="Вывести значение")
        btnShow.pack(fill="x", padx=4, pady=(0, 10))

        btnExit = tkinter.ttk.Button(self, text="Выход")
        btnExit.pack(side="bottom", anchor="ne")

root = tkinter.Tk()
app = Application(master=root)
root.mainloop()