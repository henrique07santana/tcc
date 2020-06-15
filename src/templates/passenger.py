import npyscreen

class PassengerForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Passageiros", editable = False)
        self.add(npyscreen.ButtonPress, name = "Retornar", when_pressed_function = lambda: self.parentApp.switchForm("MAIN"))
        self.add(npyscreen.ButtonPress, name = "Sair",       when_pressed_function = lambda: self.parentApp.switchFormPrevious())
        self.add_handlers({"q": lambda x: self.parentApp.switchFormPrevious(),
                           "Q": lambda x: self.parentApp.switchFormPrevious()})