import npyscreen

class InsertSpanForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Inserir Trecho", editable = False)
        # self.station_choices = dbms.select_all(table="stations")
        self.Options = npyscreen.OptionList()
        self.options = self.Options.options
        # self.options.append(npyscreen.OptionSingleChoice('Estação de Origem', choices = [row[1] for row in self.station_choices]))
        # self.options.append(npyscreen.OptionSingleChoice('Estação de Destino', choices = [row[1] for row in self.station_choices]))
        self.add(npyscreen.OptionListDisplay, name="Lista de estações",
                values = self.options,
                scroll_exit=True,
                max_height=2)
        self.name_field = self.add(npyscreen.TitleText, name = "Nome do Trecho", use_two_lines=True, begin_entry_at=2, editable = False)
        self.add_button = self.add(npyscreen.ButtonPress, name = "Adicionar", hidden=True, when_pressed_function = lambda: self.insert_span())
        self.add(npyscreen.ButtonPress, name = "Retornar", when_pressed_function = lambda: self.parentApp.switchFormPrevious())
        self.status = self.add(npyscreen.TitleText,   name = "Status:", editable = False)
    # def while_editing(self, *args, **keywords):        
    #     if(self.options[0].get() == "" or self.options[1].get() == ""):
    #         self.status.value="Por favor, escolha as estações de Origem e Destino"
    #         self.add_button.hidden=True
    #     elif(self.options[0].get() ==  self.options[1].get()):
    #         self.status.value="As estações de Origem e Destino deve ser distintas"
    #         self.add_button.hidden=True        
    #     else:
    #         self.status.value=""
    #         self.name_field.value = self.options[0].get()[0]+" - "+self.options[1].get()[0]
    #         self.add_button.hidden=False
    #     self.add_button.display()
    #     self.status.display()
    #     self.name_field.display()
    def insert_span(self):
        pass
        # dbms.execute_query(query='INSERT INTO SPANS(name,origin_id,destination_id) VALUES ("{}","{}","{}")'.format(self.name_field.value,self.options[0].get()[0],self.options[1].get()[0]))
        # self.status.value="Trajeto {} adicionado com sucesso".format(self.name_field.value)
        # self.name_field.value=""
        # self.name_field.display()
        # self.status.display()


### TODO: Confirmação da edição/deleção no campo status
class EditRemoveSpanForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Editar/Remover Trecho", editable = False)
        # self.station_choices = dbms.select_all(table="stations")
        # self.span_choices = dbms.select_all(table="spans")
        self.station_options = npyscreen.OptionList()
        self.span_options = npyscreen.OptionList()
        self.st_options = self.station_options.options
        self.sp_options = self.span_options.options
        # self.sp_options.append(npyscreen.OptionSingleChoice('Trecho', choices = [row[1] for row in self.span_choices]))
        # self.span_ids = [row[0] for row in self.span_choices]
        # self.st_options.append(npyscreen.OptionSingleChoice('Estação de Origem', choices = [row[1] for row in self.station_choices]))
        # self.st_options.append(npyscreen.OptionSingleChoice('Estação de Destino', choices = [row[1] for row in self.station_choices]))

        self.add(npyscreen.OptionListDisplay, name="Lista de Trajetos",
                values = self.sp_options,
                scroll_exit=True,
                max_height=2)
        self.station_optionslist = self.add(npyscreen.OptionListDisplay, name="Lista de estações",
                                    values = self.st_options,
                                    scroll_exit=True,
                                    max_height=2,
                                    hidden = True)
        self.name_field = self.add(npyscreen.TitleText, name = "Nome do Trecho Atual", use_two_lines=True, begin_entry_at=2, editable = False, hidden = True)
        self.new_name_field = self.add(npyscreen.TitleText, name = "Nome do Novo Trecho", use_two_lines=True, begin_entry_at=2, editable = False, hidden = True)
        # self.edit_button = self.add(npyscreen.ButtonPress, name = "Editar", hidden=True, when_pressed_function = lambda: dbms.update_by_id(table = "spans", update="name='{}',origin_id='{}', destination_id='{}'".format(self.new_name_field.value,self.st_options[0].get()[0],self.st_options[1].get()[0]), update_id = self.span_ids[[row[1] for row in self.span_choices].index(self.name_field.value)]))
        # self.remove_button = self.add(npyscreen.ButtonPress, name = "Remover", hidden=True, when_pressed_function = lambda: dbms.delete_by_id(table = "spans", delete_id = self.span_ids[[row[1] for row in self.span_choices].index(self.name_field.value)]))
        self.add(npyscreen.ButtonPress, name = "Retornar",  when_pressed_function = lambda: self.parentApp.switchFormPrevious())
        self.status = self.add(npyscreen.TitleText,   name = "Status:", editable = False)
    # def while_editing(self, *args, **keywords):
    #     if(self.sp_options[0].get() != ""):
    #         self.station_optionslist.hidden = False
    #         self.name_field.value = self.sp_options[0].get()[0]
    #         self.name_field.hidden = False
    #         self.remove_button.hidden = False        
    #         if(self.st_options[0].get() == "" or self.st_options[1].get() == ""):
    #             self.status.value="Por favor, escolha as estações de Origem e Destino"
    #             self.edit_button.hidden=True
    #         elif(self.st_options[0].get() ==  self.st_options[1].get()):
    #             self.status.value="As estações de Origem e Destino deve ser distintas"
    #             self.edit_button.hidden=True        
    #         else:
    #             self.status.value=""
    #             self.new_name_field.value = self.st_options[0].get()[0]+" - "+self.st_options[1].get()[0]
    #             self.edit_button.hidden=False
    #             self.new_name_field.hidden = False
    #     self.edit_button.display()
    #     self.remove_button.display()
    #     self.name_field.display()
    #     self.status.display()

class DisplaySpanForm(npyscreen.FormBaseNew):
    def create(self):
        ### TODO: Fix button name
        OK_BUTTON_TEXT = "Retornar"
        self.add(npyscreen.TitleText,   name = "Listagem dos Trechos", editable = False)
        self.add(npyscreen.ButtonPress, name = "Retornar",  when_pressed_function = lambda: self.parentApp.switchFormPrevious())
        self.grid = self.add(npyscreen.GridColTitles, width = 120, column_width = 20, select_whole_line = True, always_show_cursor = False, col_titles = ['Id do Trecho', 'Nome', 'Origem', 'Destino'])
        # self.grid.values = dbms.select_all(table="spans")

class SearchSpanForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleText,   name = "Pesquisa de Trechos", editable = False)
        self.add(npyscreen.ButtonPress, name = "Retornar",  when_pressed_function = lambda: self.parentApp.switchFormPrevious())
        self.search = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=6, value=0, name='Critério da busca', values=['Origem', 'Destino', 'Origem ou Destino'])
        # self.station_choices = dbms.select_all(table="stations")
        self.station_options = npyscreen.OptionList()
        self.st_options = self.station_options.options
        # self.st_options.append(npyscreen.OptionSingleChoice('Estação', choices = [row[1] for row in self.station_choices]))
        self.add(npyscreen.OptionListDisplay, name="Estações",
                values = self.st_options,
                scroll_exit=True,
                max_height=2)
        
        self.search_button = self.add(npyscreen.ButtonPress, name = "Procurar",  when_pressed_function = lambda: self.search_span())
        self.grid = self.add(npyscreen.GridColTitles, width = 120, column_width = 20, select_whole_line = True, always_show_cursor = False, col_titles = ['Id do Trecho', 'Nome', 'Origem', 'Destino'])
        #self.grid.values = dbms.select_all(table="spans")
    def search_span(self):
        pass
        # if(self.search.values[self.search.value[0]] == "Origem"):
        #     self.query = "SELECT * FROM spans where origin_id == '{}'".format(self.st_options[0].get()[0])
        # elif(self.search.values[self.search.value[0]] == "Destino"):
        #     self.query = "SELECT * FROM spans where destination_id == '{}'".format(self.st_options[0].get()[0])
        # elif(self.search.values[self.search.value[0]] == "Origem ou Destino"):
        #     self.query = "SELECT * FROM spans where origin_id == '{}' OR destination_id == '{}'".format(self.st_options[0].get()[0],self.st_options[0].get()[0])
        # else:
        #     self.query = "SELECT * FROM spans"
        # self.grid.values = dbms.execute_query(query = self.query)
        #self.result = dbms.execute_query(query = self.query)
        #print(self.result)
        #for row in result:
        #            print(row) # print(row[0], row[1], row[2])
        #self.grid.display()
        #print(self.query)
