#KIVY LIBARY
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

#OTHER LIBARIES
import subprocess

#PARDIES IMPORTS
from pardies_pvpl_workspace import *
from pardies_run_edit_shop_base import *




#RUN
class Run(RunEditShopBase):
    def __init__(self, **kwargs):    
        super(Run, self).__init__(**kwargs)
        #workspace background
        boring_box = BoxLayout(orientation = "vertical")
        boring_box.spacing = 1
        boring_box.add_widget(Widget(size_hint = (1, None), size = (69, 119)))
        boring_box.add_widget(AdjWhiteBox())
        boring_box.add_widget(AdjWhiteBox())
        boring_box.add_widget(Widget())
        self.add_widget(boring_box)
        #prd connection and pvpl script scrolls
        boring_box = BoxLayout(orientation = "vertical")
        boring_box.add_widget(Widget(size_hint = (1, None), size = (69, 120)))
        boring_minibox = BoxLayout(orientation = "vertical")
            #prd scroll
        prd_scroll = ScrollView(do_scroll_x = True, do_scroll_y = False)
        self.prd_scroll_layout = BoxLayout(orientation = "horizontal", size_hint = (None, 1))
        self.prd_scroll_layout.bind(minimum_width = self.prd_scroll_layout.setter('width'))
        prd_scroll.add_widget(self.prd_scroll_layout)
        boring_rel = RelativeLayout()
        boring_rel.add_widget(Widget(size_hint = (1, None), size = (69, 30)))
        boring_rel.add_widget(prd_scroll)
        boring_minibox.add_widget(boring_rel)
            #pvpl script scroll
        pvpl_scroll = ScrollView(do_scroll_x = True, do_scroll_y = False)
        self.pvpl_scroll_layout = BoxLayout(orientation = "horizontal", size_hint = (None, 1))
        self.pvpl_scroll_layout.bind(minimum_width = self.pvpl_scroll_layout.setter('width'))
        pvpl_scroll.add_widget(self.pvpl_scroll_layout)
        boring_rel = RelativeLayout()
        boring_rel.add_widget(Widget(size_hint = (1, None), size = (69, 30)))
        boring_rel.add_widget(pvpl_scroll)
        boring_minibox.add_widget(boring_rel)
            #buffer
        boring_minibox.add_widget(Widget())
            #added
        boring_box.add_widget(boring_minibox)
        self.add_widget(boring_box)
        #textbox searches
            #setup
        boring_box = BoxLayout(orientation = "vertical")
        boring_box.add_widget(Widget(size_hint = (1, None), size = (69, 120)))
        boring_minibox = BoxLayout(orientation = "vertical")
            #prd_search
        self.prd_search = TextInput(hint_text = 'Search robot connections ... ', size_hint = (1, None), size = (69, 30))
        prd_search_anchor = AnchorLayout(anchor_x = "left", anchor_y = "top")
        prd_search_anchor.add_widget(self.prd_search)
        boring_rel = RelativeLayout()
        boring_rel.add_widget(prd_search_anchor)
        boring_minibox.add_widget(boring_rel)
            #pvpl_search
        self.pvpl_search = TextInput(hint_text = 'Search PVPL scripts ... ', size_hint = (1, None), size = (69, 30))
        pvpl_search_anchor = AnchorLayout(anchor_x = "left", anchor_y = "top")
        pvpl_search_anchor.add_widget(self.pvpl_search)
        boring_rel = RelativeLayout()
        boring_rel.add_widget(pvpl_search_anchor)
        boring_minibox.add_widget(boring_rel)
            #buffer
        boring_minibox.add_widget(Widget())
            #added
        boring_box.add_widget(boring_minibox)
        self.add_widget(boring_box)
        #colour theme added
        self.add_widget(self.colour_theme_rel)
        #profile, settings, logout added
        self.add_widget(self.psl_box)
        #main buttons background added
        self.add_widget(self.main_buttons_background)
        #main buttons added
        self.main_buttons_layout.add_widget(self.run_button_selected)
        self.main_buttons_layout.add_widget(self.edit_button)
        self.main_buttons_layout.add_widget(self.shop_button)
        boring_box = BoxLayout(orientation = "vertical")
        boring_box.add_widget(Widget(size_hint = (1, None), size = (69, 60)))
        boring_box.add_widget(self.main_buttons_layout)
        boring_box.add_widget(Widget())
        self.add_widget(boring_box)
        #refresh button
        boring_box = BoxLayout(orientation = "horizontal", pos_hint = {"top" : 1}, size_hint = (1, None), size = (69, 60))
        boring_box.add_widget(Widget())
        boring_button = Button(size_hint = (None, None), size = (45, 45), background_normal = pardies_configuration.path + "\\Icons\\Refresh_Icon.png")
        boring_button.bind(on_press = self.refresh)
        boring_anchor = AnchorLayout(anchor_x = "center", anchor_y = "center", size_hint = (None, 1), size = (45, 69))
        boring_anchor.add_widget(boring_button)
        boring_box.add_widget(boring_anchor)
        boring_box.add_widget(Widget(size_hint = (None, 1), size = (167, 69)))
        self.add_widget(boring_box)
        #assignPVPL attributes
        self.connection_choice = None
        self.script_choice = None
        self.pvpl_assignments = {}
        #list of discovered prd connections and pvpl scripts
        self.connections_list = []
        self.scripts_list = []
        #bind prd connection and pvpl script get to transition state, bind textbox filters to text state changes
        self.bind(transition_state = self.getPRDPVPL)
        self.prd_search.bind(text = self.filterPRDSearch)
        self.pvpl_search.bind(text = self.filterPVPLSearch)
        #refresh on initialisation (cannot use if self.manager.current is runSM because it doesn't exist during initialisation)
        self.refresh()
        #placeholder prompt
        self.bt_or_wf = BoxLayout()
        bt_choice = Button(text = "BlueTooth")
        bt_choice.bind(on_press = partial(self.runScript, "BT"))
        wf_choice = Button(text = "WiFi")
        wf_choice.bind(on_press = partial(self.runScript, "WF"))
        self.bt_or_wf.add_widget(bt_choice)
        self.bt_or_wf.add_widget(wf_choice)
    #bluetooth connection search NOTE: do not hard code directory for powershell, this will need changing depending on os
    def refresh(self, *args):
        bt_pairs_list = subprocess.check_output(["powershell", "Get-PnpDevice", "-Class", "Bluetooth"], shell = True).decode().split("\n")
        for i in bt_pairs_list:
            bt_pairs_spaces = i.split(" ")
            bt_pairs = []
            for x in bt_pairs_spaces:
                if x != "":
                    bt_pairs.append(x)
            print(bt_pairs)
    #assign and run pvpl scripts
    def assignPVPL(self, *args, **kwargs):
        if args[0] == 0:
            if self.connection_choice == args[1]:
                self.connection_choice = None
                print(args[1] + " deselected.")
            else:
                if args[1] in self.pvpl_assignments:
                    if self.pvpl_assignments[args[1]] != None:
                        try:
                            os.remove(pardies_configuration.path + "\\Connections\\" + args[1] + "\\" + self.pvpl_assignments[args[1]] + ".py")
                        except:
                            pass
                        print("No longer running " + self.pvpl_assignments[args[1]] + " on " + args[1])
                        self.pvpl_assignments[args[1]] = None
                        self.connection_choice = None
                        self.script_choice = None
                    else:
                        self.connection_choice = args[1]
                        print(args[1] + " selected.")
                else:
                    self.connection_choice = args[1]
                    print(args[1] + " selected.")
        elif args[0] == 1:
            if self.script_choice == args[1]:
                self.script_choice = None
                print(args[1] + " deselected.")
            else:
                self.script_choice = args[1]
                print(args[1] + " selected.")
        if self.connection_choice != None and self.script_choice != None:
            self.add_widget(self.bt_or_wf)
    #search \Connections for prd connections and Scripts for scripts
    def getPRDPVPL(self, *args):
        if self.manager.current == "runSM":
            #get prd connections
            folder_name_list = os.listdir(pardies_configuration.path + "\\Connections")
            folder_name_list.sort()
            self.connections_list = folder_name_list
            #get pvpl scripts
            folder_name_list = os.listdir(pardies_configuration.path + "\\Scripts")
            folder_name_list.sort()
            self.scripts_list = folder_name_list
            #filter based on textboxes before adding
            self.filterPRDSearch()
            self.filterPVPLSearch()
    #filter based on 'prd_search' text and add to scroll_layout
    def filterPRDSearch(self, *args):
        #part 1
        filtered_connections_list = []
        for connection in self.connections_list:
            proceed = True
            for letter_no in range(len(self.prd_search.text)):
                try:
                    connection[letter_no]
                except:
                    proceed = False
                else:
                    if self.prd_search.text[letter_no] != connection[letter_no]:
                        proceed = False
            if proceed == True:
                filtered_connections_list.append(connection)
        #part 2
        if len(filtered_connections_list) != len(self.prd_scroll_layout.children):
            self.prd_scroll_layout.clear_widgets()
            for connection in filtered_connections_list:
                x = PRD()
                x.prd_name.text = connection
                x.text_size = (None, self.height)
                x.prd_name.halign = "left"
                x.prd_name.color = (0, 0, 0)
                x.robot_icon.bind(on_press = partial(self.assignPVPL, 0, connection))
                self.prd_scroll_layout.add_widget(x)
    #filter based on 'pvpl_search' text and add to scroll_layout
    def filterPVPLSearch(self, *args):
        #part 1
        filtered_scripts_list = []
        for script in self.scripts_list:
            proceed = True
            for letter_no in range(len(self.pvpl_search.text)):
                try:
                    script[letter_no]
                except:
                    proceed = False
                else:
                    if self.pvpl_search.text[letter_no] != script[letter_no]:
                        proceed = False
            if proceed == True:
                filtered_scripts_list.append(script)
        #part 2
        if len(filtered_scripts_list) != len(self.pvpl_scroll_layout.children):
            self.pvpl_scroll_layout.clear_widgets()
            for script in filtered_scripts_list:
                x = PVPL()
                x.pvpl_name.text = script
                x.text_size = (None, self.height)
                x.pvpl_name.halign = "left"
                x.pvpl_name.color = (0, 0, 0)
                x.script_icon.bind(on_press = partial(self.assignPVPL, 1, script))
                self.pvpl_scroll_layout.add_widget(x)
    #run script
    def runScript(self, *args, **kwargs):
        if args[0] == "BT": 
            try:
                shutil.copy(pardies_configuration.path + "\\Scripts\\" + self.script_choice + "\\Cython_BT\\" + self.script_choice + ".py", pardies_configuration.path + "\\Connections\\" + self.connection_choice)
            except:
                print("PRD connection or PVPL script no longer exists, resetting.")
            else:
                if os.path.exists(pardies_configuration.path + "\\Connections\\" + self.connection_choice + "\\RecImg"): #checks if path exists logic returns true or false
                    shutil.rmtree(pardies_configuration.path + "\\Connections\\" + self.connection_choice + "\\RecImg")
                shutil.copytree(pardies_configuration.path + "\\Scripts\\" + self.script_choice + "\\RecImg", pardies_configuration.path + "\\Connections\\" + self.connection_choice + "\\RecImg")
                print("Running " + self.script_choice + " on " + self.connection_choice)
                os.startfile(pardies_configuration.path + "\\Connections\\" + self.connection_choice + "\\" + self.script_choice + ".py")
                self.pvpl_assignments[self.connection_choice] = self.script_choice
        elif args[0] == "WF":
            try:
                shutil.copy(pardies_configuration.path + "\\Scripts\\" + self.script_choice + "\\Cython_WF\\" + self.script_choice + ".py", pardies_configuration.path + "\\Connections\\" + self.connection_choice)
            except:
                print("PRD connection or PVPL script no longer exists, resetting.")
            else:
                if os.path.exists(pardies_configuration.path + "\\Connections\\" + self.connection_choice + "\\RecImg"): #checks if path exists logic returns true or false
                    shutil.rmtree(pardies_configuration.path + "\\Connections\\" + self.connection_choice + "\\RecImg")
                shutil.copytree(pardies_configuration.path + "\\Scripts\\" + self.script_choice + "\\RecImg", pardies_configuration.path + "\\Connections\\" + self.connection_choice + "\\RecImg")
                print("Running " + self.script_choice + " on " + self.connection_choice)
                os.startfile(pardies_configuration.path + "\\Connections\\" + self.connection_choice + "\\" + self.script_choice + ".py")
                self.pvpl_assignments[self.connection_choice] = self.script_choice
        self.connection_choice = None
        self.script_choice = None
        self.remove_widget(self.bt_or_wf)




#EDIT
class Edit(RunEditShopBase):
    def __init__(self, **kwargs):
        super(Edit, self).__init__(**kwargs)
        #workspace background        
        boring_box = BoxLayout(orientation = "vertical")
        boring_box.add_widget(Widget(size_hint = (1, None), size = (69, 120)))        
        boring_box.add_widget(AdjWhiteBox())
        boring_box.add_widget(EditColourTheme())
        self.add_widget(boring_box)
        #workspace screen manager
        self.WSSM = ScreenManager(transition = NoTransition())
        self.add_widget(self.WSSM)
        #colour theme added
        self.add_widget(self.colour_theme_rel)
        #profile, settings, logout added
        self.add_widget(self.psl_box)
        #main buttons background added
        self.add_widget(self.main_buttons_background)
        #main buttons added
        self.main_buttons_layout.add_widget(self.run_button)
        self.main_buttons_layout.add_widget(self.edit_button_selected)
        self.main_buttons_layout.add_widget(self.shop_button)
        boring_box = BoxLayout(orientation = "vertical")
        boring_box.add_widget(Widget(size_hint = (1, None), size = (69, 60)))
        boring_box.add_widget(self.main_buttons_layout)
        boring_box.add_widget(Widget())
        self.add_widget(boring_box)
        #workspace selection
        ws_selection_scroll = ScrollView(do_scroll_x = True, do_scroll_y = False, size_hint = (1, None), size = (69, 30))
        self.ws_selection_layout = BoxLayout(orientation = "horizontal", size_hint = (None, 1))
        self.ws_selection_layout.bind(minimum_width = self.ws_selection_layout.setter('width'))
        ws_selection_scroll.add_widget(self.ws_selection_layout)
            #add popup button
        popup_button = Button(size_hint = (None, None), size = (25, 25), background_normal = pardies_configuration.path + "\\Icons\\Plus_Icon.png")
        popup_button.bind(on_press = self.summonPopup)
        self.pb_anchor = AnchorLayout(size_hint = (None, 1), size = (50, 69), anchor_x = "center", anchor_y = "center")
        self.pb_anchor.add_widget(popup_button)
        self.ws_selection_layout.add_widget(self.pb_anchor)
            #added in correct position
        boring_box = BoxLayout(orientation = "vertical")
        boring_anchor = AnchorLayout(anchor_x = "left", anchor_y = "top")
        boring_anchor.add_widget(ws_selection_scroll)
        boring_box.add_widget(Widget(size_hint = (1, None), size = (69, 120)))
        boring_box.add_widget(boring_anchor)
        boring_box.add_widget(Widget())
        self.add_widget(boring_box)
        #WSSM handling
        self.ws_button_list = []
        self.pvpl_type = None
        self.screen_pvpl_list = []
        self.highlighted_button = None
        self.change_ws_number = None
    #popup
    def summonPopup(self, *args):
        #initialisation
        self.pvpl_popup = Popup(title = "PVPL Script Management")
        top_division = BoxLayout(orientation = "vertical", size_hint = (1, 0.5))
        bottom_division = BoxLayout(orientation = "vertical", size_hint = (1, 0.5))
        #top_division
            #"Create PVPL" / close_popup
        boring_rel = RelativeLayout(size_hint = (1, None), size = (69, 50))
        boring_rel.add_widget(PopupLabel(text = "Create PVPL"))
        boring_box = BoxLayout(orientation = "horizontal")
        boring_box.add_widget(Widget())
        close_popup_anchor = AnchorLayout(anchor_x = "center", anchor_y = "center", size_hint = (None, 1), size = (50, 69))
        close_popup = Button(size_hint = (None, None), size = (50, 50), background_normal = pardies_configuration.path + "\\Icons\\Minimise_Icon.png")
        close_popup.bind(on_press = self.dismissPopup)
        close_popup_anchor.add_widget(close_popup)
        boring_box.add_widget(close_popup_anchor)
        boring_rel.add_widget(boring_box)
        top_division.add_widget(boring_rel)
            #pvpl_name / pvpl_type, create_pvpl
        boring_box = BoxLayout(orientation = "horizontal")
                #pvpl_name 
        self.pvpl_name = TextInput()
        boring_box.add_widget(self.pvpl_name)
                #pvpl_type, create_pvpl
        boring_minibox = BoxLayout(orientation = "vertical")
        pvpl_type_scroll = ScrollView(do_scroll_x = True, do_scroll_y = False, size_hint = (1, None), size = (69, 35))
        self.pvpl_type_scroll_layout = BoxLayout(orientation = "horizontal", size_hint = (None, 1))
        self.pvpl_type_scroll_layout.bind(minimum_width = self.pvpl_type_scroll_layout.setter('width'))
        for i in range(21):
            pvpl_type_button = (Button(size_hint = (None, 1), size = (60, 69), text = "PRD-" + str(i)))
            pvpl_type_button.bind(on_press = partial(self.changeTypePVPL, "PRD-" + str(i))) #learn list
            self.pvpl_type_scroll_layout.add_widget(pvpl_type_button)
        pvpl_type_scroll.add_widget(self.pvpl_type_scroll_layout)
        boring_minibox.add_widget(pvpl_type_scroll)
        create_pvpl = MainButton(text = "Create PVPL")
        create_pvpl.bind(on_press = self.createPVPL)
        boring_minibox.add_widget(create_pvpl)
        boring_box.add_widget(boring_minibox)
                #added
        top_division.add_widget(boring_box)
        #bottom_division
            #"Load/Delete PVPL"
        boring_rel = RelativeLayout(size_hint = (1, None), size = (69, 50))
        boring_rel.add_widget(PopupLabel(text = "Load/Delete PVPL"))
        bottom_division.add_widget(boring_rel)
            #pvpl scroll search / load_pvpl, delete_pvpl
        boring_box = BoxLayout(orientation = "horizontal")
                #pvpl scroll search
        pvpl_scroll = ScrollView(do_scroll_x = False, do_scroll_y = True)
        self.pvpl_scroll_layout = BoxLayout(orientation = "vertical", size_hint = (1, None))
        self.pvpl_scroll_layout.bind(minimum_height = self.pvpl_scroll_layout.setter('height'))
        pvpl_scroll_list = []
        for folder_name in os.listdir(pardies_configuration.path + "\\Scripts"):
            pvpl_scroll_list.append(folder_name)
        for ws_screen in self.WSSM.screen_names:
            if ws_screen in pvpl_scroll_list:
                pvpl_scroll_list.remove(ws_screen)
        pvpl_scroll_list.sort()
        for foldername in pvpl_scroll_list:
            pvpl_scroll_button = Button(text = foldername, size_hint = (1, None), size = (1, 48))
            pvpl_scroll_button.bind(on_press = partial(self.changeHighlight, foldername)) #learn list
            self.pvpl_scroll_layout.add_widget(pvpl_scroll_button)
        pvpl_scroll.add_widget(self.pvpl_scroll_layout)
        boring_box.add_widget(pvpl_scroll)
                #load_pvpl, delete_pvpl
        boring_minibox = BoxLayout(orientation = "vertical")
        load_pvpl = MainButton(text = "Load PVPL")
        load_pvpl.bind(on_press = self.loadPVPL)
        boring_minibox.add_widget(load_pvpl)
        delete_pvpl = MainButton(text = "Delete PVPL", color = (1, 0, 0))
        delete_pvpl.bind(on_press = self.deletePVPL)
        boring_minibox.add_widget(delete_pvpl)
        boring_box.add_widget(boring_minibox)
                #added
        bottom_division.add_widget(boring_box)
        #finalise
        boring_box = BoxLayout(orientation = "vertical")
        boring_box.add_widget(top_division)
        boring_box.add_widget(bottom_division)
        self.pvpl_popup.add_widget(boring_box)
        self.pvpl_popup.open()
    #dismissPopup
    def dismissPopup(self, *args):
        self.pvpl_type = None
        self.highlighted_button = None
        self.pvpl_popup.dismiss()
    #change PVPL type prepared for create
    def changeTypePVPL(self, *args, **kwargs):
        self.pvpl_type = args[0]
        print(self.pvpl_type)
        for i in self.pvpl_type_scroll_layout.children:
            if i.text == args[0]:
                i.background_normal = ""
                i.background_color = (pardies_configuration.rd, pardies_configuration.gd, pardies_configuration.bd, 1) #remember, background_color acts as a multiplier to base image which is defined with other attributes
            else:
                i.background_normal = "atlas://data/images/defaulttheme/button" #default button image path
                i.background_color = (1, 1, 1, 1)
    #change button prepared for load or delete
    def changeHighlight(self, *args, **kwargs):
        self.highlighted_button = args[0]
        print(self.highlighted_button)
        for i in self.pvpl_scroll_layout.children:
            if i.text == args[0]:
                i.background_normal = ""
                i.background_color = (pardies_configuration.rd, pardies_configuration.gd, pardies_configuration.bd, 1) #remember, background_color acts as a multiplier to base image which is defined with other attributes
            else:
                i.background_normal = "atlas://data/images/defaulttheme/button" #default button image path
                i.background_color = (1, 1, 1, 1)
    #createPVPL
    def createPVPL(self, *args):
        #check for selected pvpl script type and valid name
        proceed = True
        if self.pvpl_type == None:
            print("Please select a PVPL script type.")
            proceed = False
        elif self.pvpl_name.text == "" or self.pvpl_name.text == "info": #temp
            print("This name is invalid, please try another.")
            proceed = False
        elif self.pvpl_name.text in os.listdir(pardies_configuration.path + "\Scripts"):
            print("This name is already in use, please try another.")
            proceed = False
        if proceed == True:
            for ws_screen in self.WSSM.screen_names:
                if self.pvpl_name.text == ws_screen:
                    print("This name is already in use, please try another.")
                    proceed = False
        #proceed
        if proceed == True:
            #new screen, imported from pvpl_workspace
            ScreenPVPLAdded = ScreenPVPL(name = self.pvpl_name.text)
            ScreenPVPLAdded.panelExtras(self.pvpl_type)
            #add new screen to self.WSSM and transition to it
            self.WSSM.add_widget(ScreenPVPLAdded)
            self.WSSM.current = self.pvpl_name.text
            #create new button bound with unique on_press function and add to pvpl_button list and subsequently ws_selection_layout
            ws_selection_button = Button()
            ws_selection_button.size_hint = (None, 1)
            ws_selection_button.size = (100, 1)
            ws_selection_button.text = self.pvpl_name.text
            ws_selection_button.background_normal = ""
            ws_selection_button.background_color = (pardies_configuration.rd, pardies_configuration.gd, pardies_configuration.bd, 1)
            for i in self.ws_button_list: #no condition needed here because ws_selection_button has not yet been added to list
                i.background_normal = "atlas://data/images/defaulttheme/button" #default button image path
                i.background_color = (0.5, 0.5, 0.5)
            position = len(self.ws_button_list)
            ws_selection_button.bind(on_press = lambda x: self.changeWorkspaceN(position))
            self.ws_button_list.append(ws_selection_button)
            self.ws_selection_layout.add_widget(self.ws_button_list[position])
            self.ws_selection_layout.remove_widget(self.pb_anchor)
            self.ws_selection_layout.add_widget(self.pb_anchor)
            #dismiss self.pvpl_popup
            self.dismissPopup()
    #loadPVPL
    def loadPVPL(self, *args):
        if self.highlighted_button != None:
            #prepare workspace
            ScreenPVPLAdded = ScreenPVPL(name = self.highlighted_button)           
            #readlines
            lines = open(pardies_configuration.path + "\\Scripts\\" + self.highlighted_button + "\\PVPL\\" + self.highlighted_button + ".txt", "r").readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].replace("\n", "")
            #setup
            count = 0
            type_count = 0
            read_pvpl = 0
            read_position = False
            #check pvpl type
            self.pvpl_type = lines[0]
            ScreenPVPLAdded.panelExtras(self.pvpl_type)
            #start reading
            for i in lines:
                #block start
                if i == "BLOCK START":
                    found_block = False
                    for x in range(count, len(lines)):
                        if found_block == False and lines[x] == "BLOCK END":
                            type_list = lines[x - 1].split(", ")
                            found_block = True
                    read_position = True
                #position of block
                elif read_position == True:
                    i = i.replace("[", "")
                    i = i.replace("]", "")
                    top_position = i.split(", ")
                    read_position = False
                    read_pvpl = 1
                #first block
                elif read_pvpl == 1:
                    BlockAdded = pvpl_collection[type_list[type_count]]()
                    BlockAdded.block_number = len(ScreenPVPLAdded.blocks_list)
                    BlockAdded.block_button.bind(on_press = partial(ScreenPVPLAdded.doubleTapStart, BlockAdded.block_number))
                    ScreenPVPLAdded.block_structure[BlockAdded.block_number] = [BlockAdded.block_number]
                    current_block_structure = BlockAdded.block_number
                    read_pvpl = 2
                #other blocks
                elif read_pvpl == 2 and type_count != len(type_list) and i != "BLOCK END":
                    BlockAdded = pvpl_collection[type_list[type_count]]()
                    BlockAdded.block_number = len(ScreenPVPLAdded.blocks_list)
                    BlockAdded.block_button.bind(on_press = partial(ScreenPVPLAdded.doubleTapStart, BlockAdded.block_number))
                    ScreenPVPLAdded.block_structure[BlockAdded.block_number] = []
                    ScreenPVPLAdded.block_structure[current_block_structure].append(BlockAdded.block_number)
                #add words to block
                if read_pvpl == 2 and type_count != len(type_list) and i != "BLOCK END":
                    if type_list[type_count] == "FirstBlock":
                        i = i.split(" = ")
                        BlockAdded.block_first_text.text = i[0]
                        BlockAdded.block_second_text.text = i[1]
                    elif type_list[type_count] == "SecondBlock":
                        i = i.split(" = list: ")
                        BlockAdded.block_first_text.text = i[0]
                        BlockAdded.block_second_text.text = i[1]
                    elif type_list[type_count] == "ThirdBlock":
                        i = i.split(" = dictionary: ")
                        BlockAdded.block_first_text.text = i[0]
                        BlockAdded.block_second_text.text = i[1]
                    elif type_list[type_count] == "FourthBlock":
                        i = i.replace("define ", "")
                        i = i.split(" placeholders ( ")
                        BlockAdded.block_first_text.text = i[0]
                        i = i[1]
                        i = i.replace(" ):", "")
                        BlockAdded.block_second_text.text = i
                    elif type_list[type_count] == "FifthBlock":
                        i = i.replace("return ", "")
                        BlockAdded.block_first_text.text = i
                    elif type_list[type_count] == "SixthBlock":
                        i = i.replace("wait ", "")
                        i = i.replace(" seconds", "")
                        BlockAdded.block_first_text.text = i
                    elif type_list[type_count] == "SeventhBlock":
                        i = i.split(" through ")
                        i[0] = i[0].replace("+ ", "")
                        BlockAdded.block_first_text.text = i[0]
                        i = i[1]
                        i = i.split(" as ")
                        BlockAdded.block_second_text.text = i[0]
                        BlockAdded.block_third_text.text = i[1].replace(":", "")
                    elif type_list[type_count] == "EighthBlock":
                        i = i.replace("swap ", "")
                        i = i.split(" and ")
                        BlockAdded.block_first_text.text = i[0]
                        BlockAdded.block_second_text.text = i[1]
                    elif type_list[type_count] == "NinthBlock":
                        i = i.replace("delete ", "")
                        BlockAdded.block_first_text.text = i
                    elif type_list[type_count] == "ThirteenthBlock":
                        i = i.replace("if ", "")
                        i = i.replace(i[-1], "")
                        BlockAdded.block_first_text.text = i
                    elif type_list[type_count] == "FourteenthBlock":
                        i = i.replace("elif ", "")
                        i = i.replace(i[-1], "")
                        BlockAdded.block_first_text.text = i
                    elif type_list[type_count] == "SixteenthBlock":
                        i = i.replace("every ", "")
                        i = i.replace(i[-1], "")
                        BlockAdded.block_first_text.text = i
                    elif type_list[type_count] == "SeventeenthBlock":
                        i = i.replace("while ", "")
                        i = i.replace(i[-1], "")
                        BlockAdded.block_first_text.text = i
                    elif type_list[type_count] == "PRD0IForward":
                        i = i.replace("PRD0_I_Forward = ", "")
                        BlockAdded.block_first_text.text = i
                    elif type_list[type_count] == "PRD0IRotate":
                        i = i.replace("PRD0_I_Rotate = ", "")
                        BlockAdded.block_first_text.text = i
                    elif type_list[type_count] == "PRD0OUltrasonic":
                        i = i.replace("PRD0_O_Ultrasonic = ", "")
                        BlockAdded.block_first_text.text = i
                    elif type_list[type_count] == "PRD0IRecImg":
                        i = i.replace("PRD0_I_RecImg = ", "")
                        BlockAdded.block_first_text.text = i
                    elif type_list[type_count] == "PRD0IRecImgParas":
                        i = i.replace("PRD0_I_RecImgParas = dict: ", "")
                        BlockAdded.block_first_text.text = i
                    elif type_list[type_count] == "PRD0ORecImg":
                        i = i.replace("PRD0_O_RecImg = ", "")
                        BlockAdded.block_first_text.text = i
                    type_count = type_count + 1
                    ScreenPVPLAdded.blocks_list.append(BlockAdded)
                #add to parent and reset
                elif i == "BLOCK END":
                    for a in ScreenPVPLAdded.block_structure[current_block_structure]:
                        for x in ScreenPVPLAdded.blocks_list:
                            if x.block_number == a:
                                multiplier = ScreenPVPLAdded.block_structure[current_block_structure].index(a)
                                ScreenPVPLAdded.add_widget(x)
                                x.created = True
                                x.pos[0] = float(top_position[0])
                                x.pos[1] = float(top_position[1]) - 35 * multiplier
                    type_list = []
                    type_count = 0
                    read_pvpl = 0
                #count
                count = count + 1
            #chameleon indentation
            colour_factor = 0
            for i in ScreenPVPLAdded.block_structure:
                if len(ScreenPVPLAdded.block_structure[i]) != 1:
                    for x in ScreenPVPLAdded.block_structure[i]:
                        for a in ScreenPVPLAdded.blocks_list:
                            if a.block_number == x:
                                result = chameleonIndentation(a, pardies_configuration.r, pardies_configuration.g, pardies_configuration.b, colour_factor)
                                a = result[0]
                                colour_factor = result[1] 
            #add new screen to self.WSSM and transition to it
            self.WSSM.add_widget(ScreenPVPLAdded)
            self.WSSM.current = self.highlighted_button
            #create new button bound with unique on_press function and add to pvpl_button list and subsequently ws_selection_layout
            ws_selection_button = Button()
            ws_selection_button.size_hint = (None, 1)
            ws_selection_button.size = (100, 1)
            ws_selection_button.text = self.highlighted_button
            ws_selection_button.background_normal = ""
            ws_selection_button.background_color = (pardies_configuration.rd, pardies_configuration.gd, pardies_configuration.bd, 1)
            for i in self.ws_button_list: #no condition needed here because ws_selection_button has not yet been added to list
                i.background_normal = "atlas://data/images/defaulttheme/button" #default button image path
                i.background_color = (0.5, 0.5, 0.5)
            position = len(self.ws_button_list)
            ws_selection_button.bind(on_press = lambda x: self.changeWorkspaceN(position))
            self.ws_button_list.append(ws_selection_button)
            self.ws_selection_layout.add_widget(self.ws_button_list[len(self.ws_button_list) - 1])
            self.ws_selection_layout.remove_widget(self.pb_anchor)
            self.ws_selection_layout.add_widget(self.pb_anchor)
            #dismiss
            self.dismissPopup()
            #reset movers list
            ScreenPVPLAdded.movers.clear()
        else:
            print("Please select a PVPL script to load.")
    #deletePVPL
    def deletePVPL(self, *args):
        if self.highlighted_button != None:
            for i in self.pvpl_scroll_layout.children:
                if i.text == self.highlighted_button:
                    target = i
            self.pvpl_scroll_layout.remove_widget(target)
            shutil.rmtree(pardies_configuration.path + "\\Scripts\\" + self.highlighted_button)
            self.highlighted_button = None
        else:
            print("Please select a PVPL script to delete.")
    #change or delete WSSM screen pt1
    def changeWorkspaceN(self, value):
        self.change_ws_number = value
        #eventually add if condition here for value variable check to determine if it calls changeWorkspace or deleteWorkspace
        self.changeWorkspace()
    #change or delete WSSM screen pt2
    def changeWorkspace(self, *args):
        self.WSSM.current = self.ws_button_list[self.change_ws_number].text
        for i in self.ws_button_list:
            if i.text == self.WSSM.current:
                i.background_normal = ""
                i.background_color = (pardies_configuration.rd, pardies_configuration.gd, pardies_configuration.bd, 1) #remember, background_color acts as a multiplier to base image which is defined with other attributes
            else:
                i.background_normal = "atlas://data/images/defaulttheme/button" #default button image path
                i.background_color = (0.5, 0.5, 0.5, 1)
        self.change_ws_number = None




#SHOP
class Shop(RunEditShopBase):
    def __init__(self, **kwargs):
        super(Shop, self).__init__(**kwargs)
        #colour theme added
        self.add_widget(self.colour_theme_rel)
        #profile, settings, logout added
        self.add_widget(self.psl_box)
        #main buttons background added
        self.add_widget(self.main_buttons_background)
        #main buttons added
        self.main_buttons_layout.add_widget(self.run_button)
        self.main_buttons_layout.add_widget(self.edit_button)
        self.main_buttons_layout.add_widget(self.shop_button_selected)
        boring_box = BoxLayout(orientation = "vertical")
        boring_box.add_widget(Widget(size_hint = (1, None), size = (69, 60)))
        boring_box.add_widget(self.main_buttons_layout)
        boring_box.add_widget(Widget())
        self.add_widget(boring_box)
