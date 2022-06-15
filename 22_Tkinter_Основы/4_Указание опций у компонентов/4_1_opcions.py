"""
Для задания параметров компонентов библиотеки Tkinter применяются опции, которые задаются способами:
♦ непосредственно в конструкторе класса компонента — через именованные параметры,
чьи названия совпадают с названиями опций:
self.btnHello = tkinter.ttk.Button(self, text="Пpивeтcтвoвaть\nпoльзoвaтeля")
♦ в стиле словаря — присвоив значения опций элементам с одноименными ключами:
self,btnShow["text"] = "Выход"
self.btnShow["command"] = root.destroy
Аналогичным способом можно и получить значения той или иной опции:
txt = self.btnShow["text"]
♦ configure(<Название опции 1>=<3начение опции 1>, сНазвание опции 2>=<3начение
опции 2> . . .) — задает значения сразу для нескольких опций текущего компонента:
self.btnShow.configure(ЬехГ="Выход", command=root.destroy)
♦ config () — TO же самое, ЧТО configure ();
♦ cget (<Название опции>) — возвращает значение опции с указанным названием в виде
строки:
txt = self.btnShow.cget("text")
♦ keys () — возвращает список названий опций текущего компонента, представленных
в виде строк.
"""