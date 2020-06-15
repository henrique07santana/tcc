import npyscreen

class VehicleForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Veículos", editable = False)
        self.add(npyscreen.ButtonPress, name = "Inserir Veículo", when_pressed_function = lambda: self.parentApp.switchForm("InsertVehicleForm"))
        self.add(npyscreen.ButtonPress, name = "Editar/Remover Veículo", when_pressed_function = lambda: self.parentApp.switchForm("EditRemoveVehicleForm"))
        self.add(npyscreen.ButtonPress, name = "Listar Veículos", when_pressed_function = lambda: self.parentApp.switchForm("DisplayVehicleForm"))
        self.add(npyscreen.ButtonPress, name = "Retornar", when_pressed_function = lambda: self.parentApp.switchForm("MAIN"))
        self.add(npyscreen.ButtonPress, name = "Sair",       when_pressed_function = lambda: self.parentApp.switchFormPrevious())
        self.add_handlers({"q": lambda x: self.parentApp.switchFormPrevious(),
                           "Q": lambda x: self.parentApp.switchFormPrevious()})

class InsertVehicleForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Inserir Veículo", editable = False)
        self.seats_field = self.add(npyscreen.TitleText, name = "Número de assentos", use_two_lines=True, begin_entry_at=2)
        self.add_button = self.add(npyscreen.ButtonPress, name = "Adicionar", hidden=True, when_pressed_function = lambda: self.insert_vehicle())
        self.add(npyscreen.ButtonPress, name = "Retornar", when_pressed_function = lambda: self.parentApp.switchFormPrevious())
        self.status = self.add(npyscreen.TitleText,   name = "Status:", editable = False)
    # def while_editing(self, *args, **keywords):
    #     if(not self.seats_field.value.isdigit()):
    #         self.status.value="O número de assentos do veículo deve ser um número inteiro."
    #         self.add_button.hidden=True
    #     else:
    #         self.status.value=""
    #         self.add_button.hidden=False
    #     self.add_button.display()
    #     self.status.display()
    def insert_vehicle(self):
        pass
    #     dbms.execute_query(query='INSERT INTO VEHICLES(capacity) VALUES ({})'.format(self.seats_field.value))
    #     self.status.value="Veículo com {} lugares adicionado com sucesso".format(self.seats_field.value)
    #     self.seats_field.value=""
    #     self.seats_field.display()
    #     self.status.display()

### TODO: Confirmação da edição/deleção no campo status
class EditRemoveVehicleForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Editar/Remover Veículo", editable = False)
        self.id_field = self.add(npyscreen.TitleText, name = "ID do Veículo", use_two_lines=True, begin_entry_at=2 )
        self.seats_field = self.add(npyscreen.TitleText, name = "Número de assentos", use_two_lines=True, begin_entry_at=2)
    #     self.edit_button = self.add(npyscreen.ButtonPress, name = "Editar", hidden=True, when_pressed_function = lambda: dbms.update_by_id(table = "vehicles", update="capacity={}".format(self.seats_field.value), update_id = self.id_field.value))
    #     self.remove_button = self.add(npyscreen.ButtonPress, name = "Remover", hidden=True, when_pressed_function = lambda: dbms.delete_by_id(table = "vehicles", delete_id = self.id_field.value))
        self.add(npyscreen.ButtonPress, name = "Retornar",  when_pressed_function = lambda: self.parentApp.switchFormPrevious())
        self.status = self.add(npyscreen.TitleText,   name = "Status:", editable = False)
    #     self.queried_id=0
    # def while_editing(self, *args, **keywords):
    #     if(not self.id_field.value.isdigit()):
    #         self.status.value="O ID do veículo deve ser um número inteiro."
    #         self.edit_button.hidden=True
    #         self.remove_button.hidden=True
    #     elif(self.id_field.value != self.queried_id):
    #         self.status.value=""
    #         self.result = dbms.execute_query_one(query='SELECT capacity FROM VEHICLES WHERE id="{}"'.format(self.id_field.value))
    #         #print(self.result)
    #         if(self.result is None):
    #             self.status.value = "Veículo ID {} não existe na base de dados".format(self.id_field.value)
    #         else: 
    #             self.edit_button.hidden = False
    #             self.remove_button.hidden = False
    #             self.seats_field.value = str(self.result)
    #         self.queried_id = self.id_field.value
    #     self.edit_button.display()
    #     self.remove_button.display()
    #     self.status.display()

class DisplayVehicleForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Listagem dos Veículos", editable = False)
        self.add(npyscreen.ButtonPress, name = "Retornar",  when_pressed_function = lambda: self.parentApp.switchFormPrevious())
        self.grid = self.add(npyscreen.GridColTitles, width = 60, column_width = 20, select_whole_line = True, always_show_cursor = False, col_titles = ['Id do Veículo','Número de assentos'])
        #self.grid.values = dbms.select_all(table="vehicles")
