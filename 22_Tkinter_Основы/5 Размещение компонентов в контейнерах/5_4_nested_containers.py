"""
Использование вложенных контейнеров

Для размещения компонентов можно использовать сразу несколько контейнеров, вложив
их друг в друга (вложенные контейнеры). Это может пригодиться, если требуется создать
окно со сложным интерфейсом. Контейнеры помещаются в другие контейнеры таким
же образом, как и обычные компоненты.

Есть два способа задать контейнер, в который должен быть помещен тот или иной компонент:
♦ указать нужный контейнер в первом параметре конструктора класса компонента;
♦ указать нужный контейнер в параметре in_ метода pack (), place () или grid ().
"""
import tkinter
import tkinter.ttk


class Application(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(padx=4, pady=4)
        self.create_widgets()
        self.master.title("Вложенные контейнеры")
        self.master.resizable(False, False)

    def create_widgets(self):
        # Создаем первый вложенный контейнер — для надписи и поля ввода
        cont1 = tkinter.ttk.Frame(self)
        # Создаем надпись (компонент Label). Опция text указывает текст
        # для надписи. Размещаем его первым способом — задав нужный
        # контейнер в первом параметре конструктора
        lblValue = tkinter.ttk.Label(cont1, text="Введите значение")
        lblValue.pack(padx=4, pady=4)
        # Создаем поле ввода и также размещаем ее на экране первым
        # способом
        entValue = tkinter.ttk.Entry(cont1)
        entValue.pack(padx=4, pady=4)
        # Выводим на экран первый вложенный контейнер
        cont1.pack(side="left")
        # Создаем второй вложенный контейнер — для кнопок
        cont2 = tkinter.ttk.Frame(self)
        # Создаем кнопки. выводим их на экран вторым способом — задав
        # нужный контейнер в параметре in_ метода pack()
        btnOK = tkinter.ttk.Button(self, text="ОК")
        btnOK.pack(in_=cont2, padx=4, pady=4)
        btnCancel = tkinter.ttk.Button(self, text="Отмена")
        btnCancel.pack(in_=cont2, padx=4, pady=4)
        # Выводим на экран второй вложенный контейнер
        cont2.pack(side="right")


if __name__ == '__main__':
    root = tkinter.Tk()
    app = Application(master=root)
    root.mainloop()
