#KIVY LIBARY
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

#OTHER LIBARIES
from functools import partial

#PARDIES IMPORTS
from pardies_chameleon_indentation import *
from pardies_pvpl_workspace_base import *
from pardies_pvpl_cython import *




#PVPL EDITING WORKSPACE
class ScreenPVPL(Screen):
    def __init__(self, **kwargs):
        super(ScreenPVPL, self).__init__(**kwargs)
        #save button ...
        save_button = Button(size_hint = (None, None), size = (50, 50), background_normal = pardies_configuration.path + "\Icons\Save_Icon.png")
        save_button.bind(on_press = self.save)
        boring_anchor = AnchorLayout(anchor_x = "left", anchor_y = "top")
        boring_anchor.add_widget(save_button)
        #... added in correct position
        boring_box = BoxLayout(orientation = "vertical")
        boring_box.add_widget(Widget(size_hint = (1, None), size = (69, 150)))
        boring_box.add_widget(boring_anchor)
        boring_box.add_widget(Widget())
        self.add_widget(boring_box)
        #pvpl panel buttons
        boring_box = BoxLayout(orientation = "vertical")
        boring_box.add_widget(Widget(size_hint = (1, None), size = (69, 120)))
        boring_box.add_widget(Widget())
        self.pvpl_panel_buttons = BoxLayout(orientation = "horizontal", size_hint = (1, None), size = (69, 30))
        boring_box.add_widget(self.pvpl_panel_buttons)
        boring_box.add_widget(Widget(size_hint = (1, None), size = (69, 144)))
        self.add_widget(boring_box)
        #pvpl type based on prd
        self.pvpl_type = None
        #block-handling attributes
        self.blocks_list = [] #works because Kivy can use list references to remove widgets so long as they were added with the same reference
        self.block_structure = {}
        self.deleted_list = []
        self.movers = []
        self.current = None
        self.last_cursor_pos = ()
        self.rearrange = False
        self.moving_chameleon = False
        self.target = None
        self.dubdelete = None
        #create core pvpl blocks
        self.core_blocks = ["FirstBlock",
                       "SecondBlock",
                       "ThirdBlock",
                       "FourthBlock",
                       "FifthBlock",
                       "SixthBlock",
                       "SeventhBlock",
                       "EighthBlock",
                       "NinthBlock",
                       "TenthBlock",
                       "EleventhBlock",
                       "TwelfthBlock",
                       "ThirteenthBlock",
                       "FourteenthBlock",
                       "FifteenthBlock",
                       "SixteenthBlock",
                       "SeventeenthBlock",
                       "EighteenthBlock",
                       "NineteenthBlock",
                       "TwentiethBlock",
                       "TwentyfirstBlock"]
        for i in self.core_blocks:
            self.createBlock(i)
        #core panel management
        core_button = Button(background_color = (0.5, 0.5, 0.5), text = "Core", size_hint = (None, 1), size = (75, 69))
        core_button.bind(on_press = partial(self.panelManage, "Core")) 
        self.pvpl_panel_buttons.add_widget(core_button)
    #PANEL EXTRAS DETERMINED BY PVPL TYPE
    def panelExtras(self, *args):
        self.pvpl_type = args[0]
        #PRD-0
        if self.pvpl_type == "PRD-0":
            #create prd0 pvpl blocks
            self.prd0_blocks = ["PRD0IForward",
                                "PRD0IRotate",
                                "PRD0OUltrasonic",
                                "PRD0IRecImg",
                                "PRD0IRecImgParas",
                                "PRD0ORecImg"]
            for i in self.prd0_blocks:
                self.createBlock(i)
            #prd0 panel management
            prd0_button = Button(background_color = (0.5, 0.5, 0.5), text = "PRD-0", size_hint = (None, 1), size = (75, 69))
            prd0_button.bind(on_press = partial(self.panelManage, "PRD-0"))
            self.pvpl_panel_buttons.add_widget(prd0_button)
        #first time
        self.panelManage("Core")
    #PANEL MANAGEMENT temporary fix until I can find a more elegant solution
    def panelManage(self, *args, **kwargs):
        if args[0] == "Core":
            for i in self.blocks_list:
                if i.created == False and i.block_type in self.core_blocks and i.block_number not in self.deleted_list: #last part lazy fix
                    i.pos = pvpl_collection[i.block_type]().pos
                elif i.created == False and i.block_type not in self.core_blocks and i.block_number not in self.deleted_list: #last part lazy fix
                    i.pos = (0, -36)
        elif args[0] == "PRD-0":
            for i in self.blocks_list:
                if i.created == False and i.block_type in self.prd0_blocks and i.block_number not in self.deleted_list: #last part lazy fix
                    i.pos = pvpl_collection[i.block_type]().pos 
                elif i.created == False and i.block_type not in self.prd0_blocks and i.block_number not in self.deleted_list: #last part lazy fix
                    i.pos = (0, -36)
        for i in self.pvpl_panel_buttons.children:
            if i.text == args[0]:
                i.background_normal = ""
                i.background_color = (pardies_configuration.rd, pardies_configuration.gd, pardies_configuration.bd, 1)
            else:
                i.background_normal = "atlas://data/images/defaulttheme/button" #default button image path
                i.background_color = (0.5, 0.5, 0.5, 1)
        self.movers.clear() #prevents blocks from being accidently created because they are in self.movers when on_touch_move is called
    #MOVING (on_touch_down causes too much lag)
    def on_touch_move(self, touch):
        #establish self.current OR drag all created blocks
        if self.current == None:
            if len(self.movers) != 0:
                for i in self.movers:
                    for x in self.blocks_list:
                        if x.block_number == i:
                            if self.current == None:
                                self.current = x
                            elif self.current.pos[1] < x.pos[1]: #failsafe code in case current is not the highest mover, it's logical but might not be necessary; nevertheless, it's harmless to keep in
                                self.current = x
            else:
                proceed = True
                for i in self.blocks_list:
                    if i.collide_point(*touch.pos):
                        proceed = False
                if proceed == True:
                    if self.last_cursor_pos == ():
                        self.last_cursor_pos = touch.pos
                    else:
                        x_change = touch.pos[0] - self.last_cursor_pos[0]
                        y_change = touch.pos[1] - self.last_cursor_pos[1]
                        for i in self.blocks_list:
                            if i.created == True:
                                i.pos[0] = i.pos[0] + x_change
                                i.pos[1] = i.pos[1] + y_change
                        self.last_cursor_pos = touch.pos
                    self.movers.clear()
        #once self.current found
        if self.current != None:
            #rearrange block structures
            if self.rearrange == False:
                list_transfer = []
                for i in self.block_structure:
                    if self.current.block_number in self.block_structure[i]:
                        old_list_key = i
                start_adding = False
                for i in self.block_structure[old_list_key]:
                    if i == self.current.block_number:
                        start_adding = True
                    if start_adding == True:
                        list_transfer.append(i)
                for i in list_transfer:
                    self.block_structure[old_list_key].remove(i)
                    self.block_structure[self.current.block_number].append(i)
                self.rearrange = True
            #drag others in same structure
            for i in self.block_structure[self.current.block_number]:
                if i != self.current.block_number:
                    for x in self.blocks_list:
                        if x.block_number == i:
                            multiplier = self.block_structure[self.current.block_number].index(i)
                            x.pos[0] = self.current.pos[0]
                            x.pos[1] = self.current.pos[1] - 35 * multiplier
            #chameleon indentation
            if self.moving_chameleon == False:
                colour_factor = 0
                for i in self.block_structure[self.current.block_number]:
                    for x in self.blocks_list:
                        if x.block_number == i:       
                            result = chameleonIndentation(x, pardies_configuration.r, pardies_configuration.g, pardies_configuration.b, colour_factor)
                            x = result[0]
                            colour_factor = result[1]
                self.moving_chameleon = True
            #search for connection targets
            for i in self.blocks_list:
                if i != self.current and i.created == True and i.block_number not in self.block_structure[self.current.block_number]:
                    for x in self.blocks_list:
                        if x.block_number == self.block_structure[self.current.block_number][-1]:
                            if (x.pos[0] >= i.pos[0] - 35 and x.pos[0] <= i.pos[0] + 35
                            and x.pos[1] > i.pos[1] + 17.5 and x.pos[1] <= i.pos[1] + 70):
                                self.target = i
            for i in self.blocks_list:
                if i != self.current and i.created == True and i.block_number not in self.block_structure[self.current.block_number]:
                    if (self.current.pos[0] >= i.pos[0] - 35 and self.current.pos[0] <= i.pos[0] + 35
                    and self.current.pos[1] >= i.pos[1] - 35 and self.current.pos[1] <= i.pos[1] + 17.5):
                        self.target = i
    #STOP MOVING
    def on_touch_up(self, touch):
        #confirm target
        build_type = 0
        if self.target != None:
            if (self.current.pos[0] >= self.target.pos[0] - 35 and self.current.pos[0] <= self.target.pos[0] + 35
            and self.current.pos[1] >= self.target.pos[1] - 35 and self.current.pos[1] <= self.target.pos[1] + 17.5):
                build_type = 1
        if self.target != None and build_type != 1:
            for x in self.blocks_list:
                if x.block_number == self.block_structure[self.current.block_number][-1]:
                    if (x.pos[0] >= self.target.pos[0] - 35 and x.pos[0] <= self.target.pos[0] + 35
                    and x.pos[1] > self.target.pos[1] + 17.5 and x.pos[1] <= self.target.pos[1] + 70):
                        build_type = 2
        #build type 1 (insert beneath target block)
        if build_type == 1:
            list_transfer = []  
            for i in self.block_structure:
                if self.target.block_number in self.block_structure[i]:
                    new_list_key = i
            for i in self.block_structure[self.current.block_number]:
                list_transfer.append(i)
            position = self.block_structure[new_list_key].index(self.target.block_number)
            count = 1
            for i in list_transfer:
                self.block_structure[new_list_key].insert(position + count, i)
                self.block_structure[self.current.block_number].remove(i)
                count = count + 1
            for i in self.blocks_list:
                if i.block_number == self.block_structure[new_list_key][0]:
                    top_x = i.pos[0]
                    top_y = i.pos[1]
            for i in self.blocks_list:
                if i.block_number in self.block_structure[new_list_key]:
                    multiplier = self.block_structure[new_list_key].index(i.block_number)
                    i.pos[0] = top_x
                    i.pos[1] = top_y - 35 * multiplier
        #build type 2 (attach above target block)    
        elif build_type == 2:
            proceed = False
            for i in self.block_structure:
                if self.target.block_number in self.block_structure[i]:
                    if self.target.block_number == self.block_structure[i][0]:
                        new_list_key = i
                        proceed = True
            if proceed == True:
                self.block_structure[self.current.block_number] = self.block_structure[self.current.block_number] + self.block_structure[new_list_key]
                self.block_structure[new_list_key].clear()
                position = self.block_structure[self.current.block_number].index(self.target.block_number)
                for i in self.blocks_list:
                    if i.block_number in self.block_structure[self.current.block_number]:
                        if self.block_structure[self.current.block_number].index(i.block_number) < position:
                            multiplier = position - self.block_structure[self.current.block_number].index(i.block_number)
                            i.pos[0] = self.target.pos[0]
                            i.pos[1] = self.target.pos[1] + 35 * multiplier
        #if self.current exists
        if self.current != None:
            #chameleon indentation
            for i in self.block_structure:
                if self.current.block_number in self.block_structure[i]:
                    colour_factor = 0
                    for x in self.block_structure[i]:
                        for a in self.blocks_list:
                            if a.block_number == x:
                                result = chameleonIndentation(a, pardies_configuration.r, pardies_configuration.g, pardies_configuration.b, colour_factor)
                                a = result[0]
                                colour_factor = result[1]
            #replace if necessary
            if self.current.created == False:
                self.create_block_type = self.current.block_type
                self.createBlock(self.current.block_type)
                self.current.created = True
            #reset
            self.current = None
            self.rearrange = False
            self.moving_chameleon = False
            self.target = None
            self.movers.clear()
        #reset last cursor pos if necessary
        if self.last_cursor_pos != ():
            self.last_cursor_pos = ()
    #CREATE BLOCK 
    def createBlock(self, *args): #adding to blocks list allows me to simply refer to the array position in order to edit their attributes because of how Kivy works
        BlockAdded = pvpl_collection[args[0]]()
        if self.deleted_list == []:
            BlockAdded.block_number = len(self.blocks_list)
            BlockAdded.block_button.bind(on_press = partial(self.doubleTapStart, BlockAdded.block_number))
            self.block_structure[BlockAdded.block_number] = [BlockAdded.block_number]
            self.blocks_list.append(BlockAdded)
            self.add_widget(self.blocks_list[len(self.blocks_list) - 1])
        else: #this system should conserve memory by minimising the size of blocks_list, but consumption still continues to increase with each block added, which makes me think this is a deeper issue with Kivy
            BlockAdded.block_number = self.deleted_list[0]
            BlockAdded.block_button.bind(on_press = partial(self.doubleTapStart, BlockAdded.block_number))
            self.block_structure[BlockAdded.block_number] = [BlockAdded.block_number]
            self.blocks_list[BlockAdded.block_number] = BlockAdded
            self.add_widget(self.blocks_list[BlockAdded.block_number])
            del self.deleted_list[0]
    #SAVE TO TEXT FILE AND COMPILE
    def save(self, *args):
        if not os.path.exists(pardies_configuration.path + "\\Scripts\\" + self.name): #checks if path exists logic returns false
            os.makedirs(pardies_configuration.path + "\\Scripts\\" + self.name + "\\PVPL")
            os.makedirs(pardies_configuration.path + "\\Scripts\\" + self.name + "\\Cython_BT")
            os.makedirs(pardies_configuration.path + "\\Scripts\\" + self.name + "\\Cython_WF")
            os.makedirs(pardies_configuration.path + "\\Scripts\\" + self.name + "\\RecImg")
        with open(pardies_configuration.path + "\\Scripts\\" + self.name + "\\PVPL\\" + self.name + ".txt", "w") as f:
            f.write(self.pvpl_type + "\n\n")
            for i in self.blocks_list:
                if i.created == True and len(self.block_structure[i.block_number]) != 0:
                    f.write("BLOCK START\n")
                    f.write(str(i.pos) + "\n")
                    type_list = []
                    for x in self.block_structure[i.block_number]:
                        for a in self.blocks_list:
                            if a.block_number == x:
                                if a.block_type == "FirstBlock":
                                    f.write(a.block_first_text.text + " = " + a.block_second_text.text + "\n")
                                    type_list.append("FirstBlock")
                                elif a.block_type == "SecondBlock":
                                    f.write(a.block_first_text.text + " = list: " + a.block_second_text.text + "\n")
                                    type_list.append("SecondBlock")
                                elif a.block_type == "ThirdBlock":
                                    f.write(a.block_first_text.text + " = dictionary: " + a.block_second_text.text + "\n")
                                    type_list.append("ThirdBlock")
                                elif a.block_type == "FourthBlock":
                                    f.write("define " + a.block_first_text.text + " placeholders ( " + a.block_second_text.text + " ):\n")
                                    type_list.append("FourthBlock")
                                elif a.block_type == "FifthBlock":
                                    f.write("return " + a.block_first_text.text + "\n")
                                    type_list.append("FifthBlock")
                                elif a.block_type == "SixthBlock":
                                    f.write("wait " + a.block_first_text.text + " seconds\n")
                                    type_list.append("SixthBlock")
                                elif a.block_type == "SeventhBlock":
                                    f.write("+ " + a.block_first_text.text + " through " + a.block_second_text.text + " as " + a.block_third_text.text + ":\n")
                                    type_list.append("SeventhBlock")
                                elif a.block_type == "EighthBlock":
                                    f.write("swap " + a.block_first_text.text + " and " + a.block_second_text.text + "\n")
                                    type_list.append("EighthBlock")
                                elif a.block_type == "NinthBlock":
                                    f.write("delete " + a.block_first_text.text + "\n")
                                    type_list.append("NinthBlock")
                                elif a.block_type == "TenthBlock":
                                    f.write("try:\n")
                                    type_list.append("TenthBlock")
                                elif a.block_type == "EleventhBlock":
                                    f.write("failure:\n")
                                    type_list.append("EleventhBlock")
                                elif a.block_type == "TwelfthBlock":
                                    f.write("succecss:\n")
                                    type_list.append("TwelfthBlock")
                                elif a.block_type == "ThirteenthBlock":
                                    f.write("if " + a.block_first_text.text + ":\n")
                                    type_list.append("ThirteenthBlock")
                                elif a.block_type == "FourteenthBlock":
                                    f.write("elif " + a.block_first_text.text + ":\n")
                                    type_list.append("FourteenthBlock")
                                elif a.block_type == "FifteenthBlock":
                                    f.write("else:\n")
                                    type_list.append("FifteenthBlock")
                                elif a.block_type == "SixteenthBlock":
                                    f.write("every " + a.block_first_text.text + ":\n")
                                    type_list.append("SixteenthBlock")
                                elif a.block_type == "SeventeenthBlock":
                                    f.write("while " + a.block_first_text.text + ":\n")
                                    type_list.append("SeventeenthBlock")
                                elif a.block_type == "EighteenthBlock":
                                    f.write("other condition ... \n")
                                    type_list.append("EighteenthBlock")
                                elif a.block_type == "NineteenthBlock":
                                    f.write("break loop\n")
                                    type_list.append("NineteenthBlock")
                                elif a.block_type == "TwentiethBlock":
                                    f.write("skip loop\n")
                                    type_list.append("TwentiethBlock")
                                elif a.block_type == "TwentyfirstBlock":
                                    f.write("do nothing\n")
                                    type_list.append("TwentyfirstBlock")
                                elif a.block_type == "PRD0IForward":
                                    f.write("PRD0_I_Forward = " + a.block_first_text.text + "\n")
                                    type_list.append("PRD0IForward")
                                elif a.block_type == "PRD0IRotate":
                                    f.write("PRD0_I_Rotate = " + a.block_first_text.text + "\n")
                                    type_list.append("PRD0IRotate")
                                elif a.block_type == "PRD0OUltrasonic":
                                    f.write("PRD0_O_Ultrasonic = " + a.block_first_text.text + "\n")
                                    type_list.append("PRD0OUltrasonic")
                                elif a.block_type == "PRD0IRecImg":
                                    if not os.path.exists(pardies_configuration.path + "\\Scripts\\" + self.name + "\\RecImg\\" + a.block_first_text.text):
                                        os.makedirs(pardies_configuration.path + "\\Scripts\\" + self.name + "\\RecImg\\" + a.block_first_text.text)
                                    if a.recimg != []:
                                        for img in os.listdir(pardies_configuration.path + "\\Scripts\\" + self.name + "\\RecImg\\" + a.block_first_text.text):
                                            os.remove(pardies_configuration.path + "\\Scripts\\" + self.name + "\\RecImg\\" + a.block_first_text.text + "\\" + img)
                                        for img in a.recimg:
                                            shutil.copy(img, pardies_configuration.path + "\\Scripts\\" + self.name + "\\RecImg\\" + a.block_first_text.text)
                                    f.write("PRD0_I_RecImg = " + a.block_first_text.text + "\n")
                                    type_list.append("PRD0IRecImg")
                                elif a.block_type == "PRD0IRecImgParas":
                                    f.write("PRD0_I_RecImgParas = dict: " + a.block_first_text.text + "\n")
                                    type_list.append("PRD0IRecImgParas")
                                elif a.block_type == "PRD0ORecImg":
                                    f.write("PRD0_O_RecImg = " + a.block_first_text.text + "\n")
                                    type_list.append("PRD0ORecImg")
                    f.write(", ".join(type_list) + "\n")
                    f.write("BLOCK END\n")
                    f.write("\n")
        cythonCompile(self.name)
        print("Saved!")
    #DOUBLE TAP DELETE PT 1
    def doubleTapStart(self, *args, **kwargs):
        if args[0] == self.dubdelete:
            count = 0
            for i in self.blocks_list:
                if i.block_number == self.dubdelete and i.created == True:
                    for x in self.block_structure:
                        if i.block_number in self.block_structure[x]:
                            self.block_structure[x].remove(i.block_number)
                            self.remove_widget(self.blocks_list[count])
                            i.created = False
                            self.deleted_list.append(self.dubdelete)
                            old_list_key = x
                count = count + 1
            try:
                self.block_structure[old_list_key][0]
            except:
                pass
            else:
                new_list_key = self.block_structure[old_list_key][0]
                list_transfer = []
                for i in self.block_structure[old_list_key]:
                    list_transfer.append(i)
                for i in list_transfer:
                    self.block_structure[new_list_key].append(i)
                    self.block_structure[old_list_key].remove(i)
                for i in self.blocks_list:
                    if i.block_number == self.block_structure[new_list_key][0]:
                        top_x = i.pos[0]
                        top_y = i.pos[1]
                for i in self.blocks_list:
                    if i.block_number in self.block_structure[new_list_key]:
                        multiplier = self.block_structure[new_list_key].index(i.block_number)
                        i.pos[0] = top_x
                        i.pos[1] = top_y - 35 * multiplier
                colour_factor = 0
                #chameleon indentation
                for i in self.block_structure[new_list_key]:
                    for x in self.blocks_list:
                        if x.block_number == i:
                            result = chameleonIndentation(x, pardies_configuration.r, pardies_configuration.g, pardies_configuration.b, colour_factor)
                            x = result[0]
                            colour_factor = result[1] 
            new_list_key = None
            self.dubdelete = None
            Clock.schedule_once(self.doubleTapEnd, 0)
        else:
            self.dubdelete = args[0]
            Clock.schedule_once(self.doubleTapEnd, 0.5)
    #DOUBLE TAP DELETE PT 2
    def doubleTapEnd(self, dt):
        self.dubdelete = None
        self.movers.clear()
