import npyscreen
import os
import sys
sys.path.append(os.path.realpath('.'))
from templates.passenger import PassengerForm
from templates.booking import BookingForm, InsertBookingForm
from templates.vehicle import VehicleForm, InsertVehicleForm, EditRemoveVehicleForm, DisplayVehicleForm
from templates.station import StationForm, InsertStationForm, EditRemoveStationForm, DisplayStationForm
from templates.span import InsertSpanForm, EditRemoveSpanForm, DisplaySpanForm, SearchSpanForm

class AppTheme(npyscreen.ThemeManager):
    pass

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(AppTheme)
        self.addForm("MAIN", MainForm, name = "Sistema de Reservas de passagens")
        self.addForm("PassengerForm", PassengerForm, name = "Sistema de Reservas de passagens")
        self.addForm("BookingForm", BookingForm, name = "Sistema de Reservas de passagens")
        self.addForm("InsertBookingForm", InsertBookingForm, name = "Sistema de Reservas de passagens")
        self.addForm("VehicleForm", VehicleForm, name = "Sistema de Reservas de passagens")
        self.addForm("InsertVehicleForm", InsertVehicleForm, name = "Sistema de Reservas de passagens")
        self.addForm("EditRemoveVehicleForm", EditRemoveVehicleForm, name = "Sistema de Reservas de passagens")
        self.addForm("DisplayVehicleForm", DisplayVehicleForm, name = "Sistema de Reservas de passagens")
        self.addForm("StationForm", StationForm, name = "Sistema de Reservas de passagens")
        self.addForm("InsertStationForm", InsertStationForm, name = "Sistema de Reservas de passagens")
        self.addForm("EditRemoveStationForm", EditRemoveStationForm, name = "Sistema de Reservas de passagens")
        self.addForm("DisplayStationForm", DisplayStationForm, name = "Sistema de Reservas de passagens")
        self.addForm("InsertSpanForm", InsertSpanForm, name = "Sistema de Reservas de passagens")
        self.addForm("EditRemoveSpanForm", EditRemoveSpanForm, name = "Sistema de Reservas de passagens")
        self.addForm("DisplaySpanForm", DisplaySpanForm, name = "Sistema de Reservas de passagens")
        self.addForm("SearchSpanForm", SearchSpanForm, name = "Sistema de Reservas de passagens")

class MainForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText, name = "Menu principal", editable = False)
        self.add(npyscreen.ButtonPress, name = "Passageiros", when_pressed_function = lambda: self.parentApp.switchForm("PassengerForm"))
        self.add(npyscreen.ButtonPress, name = "Agendamentos", when_pressed_function = lambda: self.parentApp.switchForm("BookingForm"))
        self.add(npyscreen.ButtonPress, name = "Veículos", when_pressed_function = lambda: self.parentApp.switchForm("VehicleForm"))
        self.add(npyscreen.ButtonPress, name = "Estações e Trechos", when_pressed_function = lambda: self.parentApp.switchForm("StationForm"))
        self.add(npyscreen.ButtonPress, name = "Quit (Q)",   when_pressed_function = lambda: self.parentApp.switchForm(None))
        self.add_handlers({"q": lambda x: self.parentApp.switchForm(None),
                           "Q": lambda x: self.parentApp.switchForm(None)})

if __name__ == '__main__':
    app = App()
    app.run() 
