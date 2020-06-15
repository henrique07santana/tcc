import npyscreen

class MainForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Menu principal",  editable = False)
        self.add(npyscreen.ButtonPress, name = "Passageiros", when_pressed_function = lambda: self.parentApp.switchForm("PassengerForm"))
        self.add(npyscreen.ButtonPress, name = "Agendamentos", when_pressed_function = lambda: self.parentApp.switchForm("BookingForm"))
        self.add(npyscreen.ButtonPress, name = "Veículos", when_pressed_function = lambda: self.parentApp.switchForm("VehicleForm"))
        self.add(npyscreen.ButtonPress, name = "Estações e Trechos", when_pressed_function = lambda: self.parentApp.switchForm("StationForm"))
        
        self.add(npyscreen.ButtonPress, name = "Quit (Q)",   when_pressed_function = lambda: self.parentApp.switchForm(None))
        self.add_handlers({"q": lambda x: self.parentApp.switchForm(None),
                           "Q": lambda x: self.parentApp.switchForm(None)})
