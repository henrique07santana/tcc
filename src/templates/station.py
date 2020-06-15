import npyscreen

class StationForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Estações e Trechos", editable = False)
        self.add(npyscreen.ButtonPress, name = "Inserir Estação", when_pressed_function = lambda: self.parentApp.switchForm("InsertStationForm"))
        self.add(npyscreen.ButtonPress, name = "Editar/Remover Estação", when_pressed_function = lambda: self.parentApp.switchForm("EditRemoveStationForm"))
        self.add(npyscreen.ButtonPress, name = "Listar Estações", when_pressed_function = lambda: self.parentApp.switchForm("DisplayStationForm"))
        self.add(npyscreen.ButtonPress, name = "Inserir Trecho", when_pressed_function = lambda: self.parentApp.switchForm("InsertSpanForm"))
        self.add(npyscreen.ButtonPress, name = "Editar/Remover Trecho", when_pressed_function = lambda: self.parentApp.switchForm("EditRemoveSpanForm"))
        self.add(npyscreen.ButtonPress, name = "Listar Trechos", when_pressed_function = lambda: self.parentApp.switchForm("DisplaySpanForm"))
        self.add(npyscreen.ButtonPress, name = "Pesquisar Trechos", when_pressed_function = lambda: self.parentApp.switchForm("SearchSpanForm"))
        self.add(npyscreen.ButtonPress, name = "Retornar", when_pressed_function = lambda: self.parentApp.switchFormPrevious())

class InsertStationForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Inserir Estação", editable = False)
        self.name_field = self.add(npyscreen.TitleText, name = "Nome da Estação", use_two_lines=True, begin_entry_at=2)
        self.add_button = self.add(npyscreen.ButtonPress, name = "Adicionar", hidden=True, when_pressed_function = lambda: self.insert_vehicle())
        self.add(npyscreen.ButtonPress, name = "Retornar", when_pressed_function = lambda: self.parentApp.switchFormPrevious())
        self.status = self.add(npyscreen.TitleText,   name = "Status:", editable = False)
    # def while_editing(self, *args, **keywords):
    #     if(self.name_field.value == ""):
    #         self.status.value="Por favor, preencha o nome da estação"
    #         self.add_button.hidden=True
    #     else:
    #         self.status.value=""
    #         self.add_button.hidden=False
    #     self.add_button.display()
    #     self.status.display()
    def insert_vehicle(self):
        pass
        # dbms.execute_query(query='INSERT INTO STATIONS(name) VALUES ("{}")'.format(self.name_field.value))
        # self.status.value="Estação {} adicionada com sucesso".format(self.name_field.value)
        # self.name_field.value=""
        # self.name_field.display()
        # self.status.display()


### TODO: Confirmação da edição/deleção no campo status
class EditRemoveStationForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Editar/Remover Estação", editable = False)
        self.id_field = self.add(npyscreen.TitleText, name = "ID da Estação", use_two_lines=True, begin_entry_at=2 )
        self.name_field = self.add(npyscreen.TitleText, name = "Nome", use_two_lines=True, begin_entry_at=2)
        # self.edit_button = self.add(npyscreen.ButtonPress, name = "Editar", hidden=True, when_pressed_function = lambda: dbms.update_by_id(table = "stations", update="name='{}'".format(self.name_field.value), update_id = self.id_field.value))
        # self.remove_button = self.add(npyscreen.ButtonPress, name = "Remover", hidden=True, when_pressed_function = lambda: dbms.delete_by_id(table = "stations", delete_id = self.id_field.value))
        self.add(npyscreen.ButtonPress, name = "Retornar",  when_pressed_function = lambda: self.parentApp.switchFormPrevious())
        self.status = self.add(npyscreen.TitleText,   name = "Status:", editable = False)
        self.queried_id=0
    # def while_editing(self, *args, **keywords):
    #     if(not self.id_field.value.isdigit()):
    #         self.status.value="O ID da estação deve ser um número inteiro."
    #         self.edit_button.hidden=True
    #         self.remove_button.hidden=True
    #     elif(self.id_field.value != self.queried_id):
    #         self.status.value=""
    #         self.result = dbms.execute_query_one(query='SELECT name FROM STATIONS WHERE id="{}"'.format(self.id_field.value))
    #         #print(self.result)
    #         if(self.result is None):
    #             self.status.value = "Estação ID {} não existe na base de dados".format(self.id_field.value)
    #         else: 
    #             self.edit_button.hidden = False
    #             self.remove_button.hidden = False
    #             self.name_field.value = str(self.result)
    #         self.queried_id = self.id_field.value
    #     self.edit_button.display()
    #     self.remove_button.display()
    #     self.status.display()

class DisplayStationForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Listagem das Estações", editable = False)
        self.add(npyscreen.ButtonPress, name = "Retornar",  when_pressed_function = lambda: self.parentApp.switchFormPrevious())
        self.grid = self.add(npyscreen.GridColTitles, width = 60, column_width = 20, select_whole_line = True, always_show_cursor = False, col_titles = ['Id da Estação','Nome'])
        # self.grid.values = dbms.select_all(table="stations")
