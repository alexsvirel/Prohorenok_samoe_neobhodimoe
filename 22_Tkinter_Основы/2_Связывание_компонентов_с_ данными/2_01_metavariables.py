"""
Связывание компонентов с данными. Метапеременные
"""
import tkinter
import tkinter.ttk

class Application(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.master.title("Использование метапеременных")
        # self.master.resizable(False, False)

    def create_widgets(self):
        # Метапеременные Tkinter: StringVar, IntVar, DoubleVar, BooleanVar
        # set() - заносит значение в метапеременную
        # get() - возвращает значение из метапеременной
        self.varValue = tkinter.StringVar()
        self.varValue.set("Значение")

        # Опция textvariable класса Entry указывает метепеременную,
        # с которой будет связан компонент
        self.entValue = tkinter.ttk.Entry(self,
                                          textvariable=self.varValue)
        self.entValue.pack()
        self.btnShow = tkinter.ttk.Button(self, text="Вывести значение",
                                          command=self.show_value)
        self.btnShow.pack(side="bottom")

    def show_value(self):
        print(self.varValue.get())

if __name__ == '__main__':
    root = tkinter.Tk()
    app = Application(master=root)
    root.mainloop()
