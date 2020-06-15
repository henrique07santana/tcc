import npyscreen

class BookingForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Agendamentos", editable = False)
        self.add(npyscreen.ButtonPress, name = "Inserir agendamento", when_pressed_function = lambda: self.parentApp.switchForm("InsertBookingForm"))
        self.add(npyscreen.ButtonPress, name = "Editar agendamento", when_pressed_function = lambda: self.parentApp.switchForm("MAIN"))
        self.add(npyscreen.ButtonPress, name = "Listar agendamentos", when_pressed_function = lambda: self.parentApp.switchForm("MAIN"))
        self.add(npyscreen.ButtonPress, name = "Retornar", when_pressed_function = lambda: self.parentApp.switchForm("MAIN"))
        self.add(npyscreen.ButtonPress, name = "Sair",       when_pressed_function = lambda: self.parentApp.switchFormPrevious())
        self.add_handlers({"q": lambda x: self.parentApp.switchFormPrevious(),
                           "Q": lambda x: self.parentApp.switchFormPrevious()})

class InsertBookingForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Inserir agendamento", editable = False)
        self.add(npyscreen.ButtonPress, name = "Sair",  when_pressed_function = lambda: self.parentApp.switchFormPrevious())
