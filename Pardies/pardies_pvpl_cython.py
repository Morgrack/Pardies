#IMPORTS
import math
import os
import re

#PARDIES IMPORTS
import pardies_configuration




#COMPILE FUNCTION
def cythonCompile(script):
    #1. PREPARE CYTHON FILES
    cython_bt = open(pardies_configuration.path + "\\Scripts\\" + script + "\\Cython_BT\\" + script + ".py", "w")
    cython_bt.write("#IMPORTS\n")
    cython_bt.write("import bluetooth\n")
    cython_bt.write("import threading\n")
    cython_bt.write("import time\n")
    cython_bt.write("import info\n")
    cython_bt.write("\n\n\n\n")
    cython_bt.write("#BLUETOOTH SOCKETS\n")
    cython_bt.write("port = 10\n")
    cython_bt.write("bluetoothsocket = bluetooth.BluetoothSocket()\n")
    cython_bt.write("bluetoothsocket.connect((info.bt_hex_addr, port))\n")
    cython_bt.write("\n\n\n\n")
    cython_bt.write("#BLUETOOTH GLOBALS\n")
    cython_bt.write("global PRD0_I_Forward\n")
    cython_bt.write("PRD0_I_Forward = 0.0\n")
    cython_bt.write("global PRD0_I_Rotate\n")
    cython_bt.write("PRD0_I_Rotate = 0.0\n")
    cython_bt.write("global PRD0_I_RecImg\n")
    cython_bt.write("PRD0_I_RecImg = {}\n")
    cython_bt.write("global PRD0_I_RecImgParas\n")
    cython_bt.write("PRD0_I_RecImgParas = {}\n")
    cython_bt.write("global PRD0_O_RecImg\n")
    cython_bt.write("PRD0_O_RecImg = []\n")
    cython_bt.write("global PRD0_O_Ultrasonic\n")
    cython_bt.write("PRD0_O_Ultrasonic = 0.0\n")
    cython_bt.write("global outgoing\n")
    cython_bt.write("outgoing = b''\n")
    cython_bt.write("global incoming\n")
    cython_bt.write("incoming = b''\n")
    cython_bt.write("\n\n\n\n")
    cython_bt.write("#EVERY CHECKER\n")
    cython_bt.write("global every\n")
    cython_bt.write("every = {}\n")
    cython_bt.write("\n\n\n\n")
    cython_wf = open(pardies_configuration.path + "\\Scripts\\" + script + "\\Cython_WF\\" + script + ".py", "w")
    cython_wf.write("#IMPORTS\n")
    cython_wf.write("import socket\n")
    cython_wf.write("import time\n")
    cython_wf.write("import threading\n")
    cython_wf.write("import info\n")
    cython_wf.write("\n\n\n\n")
    cython_wf.write("#WIFI SOCKETS\n")
    cython_wf.write("port = 1500\n")
    cython_wf.write("socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n") #AF_INET is the internet address family for IPv4. SOCK_STREAM is the socket type for TCP
    cython_wf.write("socket.connect((info.wifi_server_ip, port))\n")
    cython_wf.write("\n\n\n\n")
    cython_wf.write("#WIFI GLOBALS\n")
    cython_wf.write("global PRD0_I_Forward\n")
    cython_wf.write("PRD0_I_Forward = 0.0\n")
    cython_wf.write("global PRD0_I_Rotate\n")
    cython_wf.write("PRD0_I_Rotate = 0.0\n")
    cython_wf.write("global PRD0_I_RecImg\n")
    cython_wf.write("PRD0_I_RecImg = {}\n")
    cython_wf.write("global PRD0_I_RecImgParas\n")
    cython_wf.write("PRD0_I_RecImgParas = {}\n")
    cython_wf.write("global PRD0_O_RecImg\n")
    cython_wf.write("PRD0_O_RecImg = []\n")
    cython_wf.write("global PRD0_O_Ultrasonic\n")
    cython_wf.write("PRD0_O_Ultrasonic = 0.0\n")
    cython_wf.write("global outgoing\n")
    cython_wf.write("outgoing = b''\n")
    cython_wf.write("global incoming\n")
    cython_wf.write("incoming = b''\n")
    cython_wf.write("\n\n\n\n")
    cython_wf.write("#EVERY CHECKER\n")
    cython_wf.write("global every\n")
    cython_wf.write("every = {}\n")
    cython_wf.write("\n\n\n\n")
    #2. PREPARE WRITING FROM PVPL
    #prepare lines for reading
    lines = open(pardies_configuration.path + "\\Scripts\\" + script + "\\PVPL\\" + script + ".txt", "r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
    #variables setup
    var_list_dict = ["#BLOCKS: VARIABLES, LISTS, DICTIONARIES\n"]
    var_list_dict_funcs = []
    user_functions = ["#BLOCKS: USER FUNCTIONS\n"]
    user_functions_funcs = []
    other = ["#BLOCKS: OTHER\n"]
    other_funcs = []
    every_while = ["#BLOCKS: EVERY, WHILE\n"]
    every_while_funcs = []
    threads = ["#RUN\n", "if __name__ == '__main__':\n", "    time.sleep(1)\n"]
    thread_starts = []
    count = 0
    func_count = 0
    every_count = 0
    whevery_indent = (None, 0)
    read_position = False
    read_pvpl = 0
    category = ""
    for i in lines:
        #block start
        if i == "BLOCK START":
            found_block = False
            for x in range(count, len(lines)):
                if found_block == False and lines[x] == "BLOCK END":
                    type_list = lines[x - 1].split(", ")
                    found_block = True
            type_count = 0
            text_to_add = ["def func" + str(func_count) + "():\n"]
            indentation = "    "
            global_vars = []
            reading_func = False
            read_position = True        
        #position of block
        elif read_position == True:
            read_position = False
            read_pvpl = 1
        #establish category
        elif read_pvpl == 1:
            if (type_list[type_count] == "FirstBlock"
            or type_list[type_count] == "SecondBlock"
            or type_list[type_count] == "ThirdBlock"
            or type_list[type_count] == "PRD0IForward"
            or type_list[type_count] == "PRD0IRotate"
            or type_list[type_count] == "PRD0OUltrasonic"
            or type_list[type_count] == "PRD0IRecImg"
            or type_list[type_count] == "PRD0IRecImgParas"
            or type_list[type_count] == "PRD0ORecImg"):
                category = "var_list_dict"
                var_list_dict_funcs.append("func" + str(func_count))
            elif type_list[type_count] == "FourthBlock":
                category = "user_functions"
                user_functions_funcs.append("func" + str(func_count))
            elif type_list[type_count] == "SixteenthBlock" or type_list[type_count] == "SeventeenthBlock":
                category = "every_while"
                every_while_funcs.append("func" + str(func_count))
            else:
                category = "other"
                other_funcs.append("func" + str(func_count))
            func_count = func_count + 1
            read_pvpl = 2
        #prepare writing
        if read_pvpl == 2 and type_count != len(type_list) and i != "BLOCK END":
            #check for list: / dict: / dictionary:
            while "list:" in i or "dict:" in i or "dictionary:" in i:
                if "dictionary:" in i:
                    i = i.replace("dictionary:", "dict:")
                if "list:" in i:
                    i = i.replace("list:", "[", 1)
                    bracket_open = "["
                    bracket_close = "]"
                elif "dict:" in i:
                    i = i.replace("dict:", "{", 1)
                    bracket_open = "{"
                    bracket_close = "}"
                start_listing = False
                new = i
                for chara_no in range(len(i)):
                    if i[chara_no] == bracket_open:
                        start_listing = True
                    elif start_listing == True:
                        #3 ahead
                        if chara_no < len(i)-2:
                            if i[chara_no] + i[chara_no + 1] + i[chara_no + 2] == " in":
                                new = new.replace(" in", bracket_close + " in")
                                start_listing = False   
                            elif i[chara_no] + i[chara_no + 1] + i[chara_no + 2] == " !=":
                                new = new.replace(" !=", bracket_close + " !=")
                                start_listing = False
                            elif i[chara_no] + i[chara_no + 1] + i[chara_no + 2] == " ==":
                                new = new.replace(" ==", bracket_close + " ==")
                                start_listing = False
                        #2 ahead    
                        if chara_no < len(i)-1:
                            if i[chara_no] + i[chara_no + 1] == "!=":
                                new = new.replace("!=", bracket_close + "!=")
                                start_listing = False   
                            elif i[chara_no] + i[chara_no + 1] == "==":
                                new = new.replace("==", bracket_close + "==")
                                start_listing = False 
                            elif i[chara_no] + i[chara_no + 1] == " +":
                                new = new.replace(" +", bracket_close + " +")
                                start_listing = False
                            elif i[chara_no] + i[chara_no + 1] == " -":
                                new = new.replace(" -", bracket_close + " -")
                                start_listing = False
                            elif i[chara_no] + i[chara_no + 1] == " =":
                                new = new.replace(" =", bracket_close + " =")
                                start_listing = False
                            elif i[chara_no] + i[chara_no + 1] == " :":
                                new == new.replace(" :", bracket_close + " :")
                                start_listing = False
                        #1 ahead
                        if i[chara_no] == "+":
                            new = new.replace("+", bracket_close + "+")
                            start_listing = False
                        elif i[chara_no] == "-":
                            new = new.replace("-", bracket_close + "-")
                            start_listing = False
                        elif i[chara_no] == "=":
                            new = new.replace("=", bracket_close + "=")
                            start_listing = False
                        elif i[chara_no] == ":":
                            new == new.replace(":", bracket_close + ":")
                            start_listing = False
                        elif chara_no == len(i) - 1:
                            new = i + bracket_close
                            start_listing = False
                i = new
                if bracket_open + " " in i:
                    i = new.replace(bracket_open + " ", bracket_open)
                if bracket_close == "}":
                    x = re.findall("{.*}", i)
                    for contents in x:
                        old_contents = contents
                        contents = contents.replace(",", ":")
                        contents = contents.replace(";", ",")
                        i = i.replace(old_contents, contents, 1)
                    if ",}" in i:
                        i = i.replace(",}", "}")
            #check for length / ran
            #_
            while " length(" in i:
                i = i.replace(" length(", " len(")
            while " ran(" in i:
                i = i.replace(" ran(", " range(")
            #(
            while "(length(" in i:
                i = i.replace("(length(", "(len(")
            while "(ran(" in i:
                i = i.replace("(ran(", "(range(")
            #[
            while "[length(" in i:
                i = i.replace("[length(", "[len(")
            while "[ran(" in i:
                i = i.replace("[ran(", "[range(")
            #{
            while "{length(" in i:
                i = i.replace("{length(", "{len(")
            while "{ran(" in i:
                i = i.replace("{ran(", "{range(")
            #check for self-change methods
            words = ["(append)", "(extend)", "(remove)", "(pop)", "(update)"]
            for word in words:
                while word in i:
                    i = i.split(" = ")
                    new_word = word.replace("(", ".")
                    new_word = new_word.replace(")", "(")
                    i = i[0].replace(word, new_word + i[1] + ")")
            #check for return methods with parameters
            words = ["(count(", "(index(", "(fromkeys(", "(get(", "(setdefault("]
            for word in words:
                while word in i:
                    i = i.split(word, 1)
                    i[1] = i[1].replace("))", ")", 1)
                    i = i[0] + word.replace("(", ".", 1) + i[1]
            #check for return methods without parameters
            words = ["(reverse)", "(sort)", "(clear)", "(copy)", "(items)", "(keys)", "(popitem)", "(values)"]
            for word in words:
                while word in i:
                    rplacement = word.replace("(", ".")
                    rplacement = rplacement.replace(")", "()")
                    i = i.replace(word, rplacement)
            #check for float inserts, function calls, list references and dict references
            if "(" in i and ")" in i:
                seperators = [" ", ".", "=", "+", "-", ":", ")"]
                words = ["placeholders", "len", "range", "type",
                         "append", "extend", "remove", "pop","update",
                         "count", "index", "fromkeys", "get", "setdefault",
                         "reverse", "sort", "clear", "copy", "items", "keys", "popitems", "values"]
                if " placeholders " in i:
                    i = i.replace(" placeholders ", " placeholders")
                read_cont = False
                word_before = ""
                contents = ""
                new = i
                for chara_no in range(len(i)):
                    if read_cont == False:
                        if i[chara_no] in seperators:
                            word_before = ""
                        elif i[chara_no] == "(":
                            if word_before not in words: #maybe check letter before for full stop with certain ones too to allow words like sort to be used as variables
                                read_cont = True
                            else:
                                 word_before = ""
                        else:
                            word_before = word_before + i[chara_no]   
                    elif read_cont == True:
                        if i[chara_no] == ")":
                            try:
                                contents = int(contents)
                            except:
                                try:
                                    contents = float(contents)
                                #if not float and not integer
                                except:
                                    new = new.split("(" + contents + ")")
                                    if contents.strip() == "":
                                        new = new[0].replace(word_before, "info.bracketHandler(" + word_before + ")", 1) + new[1]
                                    else:   
                                        new = new[0].replace(word_before, "info.bracketHandler(" + word_before + ", " + contents + ")", 1) + new[1]
                                #if float
                                else:
                                    new = new.split(" = ")
                                    new = new[0].replace("(" + str(contents) + ")", ".insert(") + str(math.ceil(contents)) + ", " + new[1] + ")"
                            #if integer
                            else:
                                new = new.split("(" + str(contents) + ")")  
                                new = new[0].replace(word_before, "info.bracketHandler(" + word_before + ", " + str(contents) + ")", 1) + new[1]
                        else:
                            contents = contents + i[chara_no]
                i = new
            #FirstBlock, SecondBlock, ThirdBlock
            if type_list[type_count] == "FirstBlock" or type_list[type_count] == "SecondBlock" or type_list[type_count] == "ThirdBlock":
                if " = " in i:
                    glob_word = i.split(" = ")[0]
                    if glob_word not in global_vars and reading_func == False:
                        global_vars.append(glob_word)
                    text_to_add.append(indentation + i + "\n")
                else:
                    text_to_add.append(indentation + i + "\n")
            #FourthBlock
            elif type_list[type_count] == "FourthBlock":
                glob_word = i.split()[1]
                i = "def" + i[6:]
                i = i.replace(" placeholders( ", "(")
                i = i[:len(i) - 3] + "):"
                if glob_word not in global_vars:
                    global_vars.append(glob_word)
                text_to_add.append(indentation + i + "\n")
                reading_func = len(indentation)
                indentation = indentation + "    "
            #FifthBlock
            elif type_list[type_count] == "FifthBlock":
                text_to_add.append(indentation + i + "\n")
            #SixthBlock
            elif type_list[type_count] == "SixthBlock":
                seconds = i.split()[1]
                i = "time.sleep(" + seconds + ")"
                text_to_add.append(indentation + i + "\n")
            #SeventhBlock (needs improving)
            elif type_list[type_count] == "SeventhBlock":
                i = i.split(" as ")
                var = i[1].replace(":", "")
                i[0] = i[0].split(" through " )
                hop = i[0][0].replace("+ ", "")
                array = i[0][1]
                if hop == "1" or hop == "":
                    text_to_add.append(indentation + "for " + var + " in " + array + ":")
                indentation = indentation + "    "
            #EighthBlock
            elif type_list[type_count] == "EighthBlock":
                i = i.replace("swap ", "", 1)
                i = i.split(" and ")
                i = i[0] + ", " + i[1] + " = " + i[1] + ", " + i[0]
                text_to_add.append(indentation + i + "\n")
            #Ninthlock
            elif type_list[type_count] == "NinthBlock":
                i = i.replace("delete ", "del ", 1)
                text_to_add.append(indentation + i + "\n")
            #TenthBlock
            elif type_list[type_count] == "TenthBlock":
                text_to_add.append(indentation + i + "\n")
                indentation = indentation + "    "
            #EleventhBlock
            elif type_list[type_count] == "EleventhBlock":
                indentation = indentation.replace("    ", "", 1)
                text_to_add.append(indentation + "except:\n")
                indentation = indentation + "    "
            #TwelfthBlock
            elif type_list[type_count] == "TwelfthBlock":
                indentation = indentation.replace("    ", "", 1)
                text_to_add.append(indentation + "else:\n")
                indentation = indentation + "    "
            #ThirteenthBlock
            elif type_list[type_count] == "ThirteenthBlock":
                text_to_add.append(indentation + i + "\n")
                indentation = indentation + "    "
            #FourteenthBlock
            elif type_list[type_count] == "FourteenthBlock":
                indentation = indentation.replace("    ", "", 1)
                text_to_add.append(indentation + i + "\n")
                indentation = indentation + "    "
            #FifteenthBlock
            elif type_list[type_count] == "FifteenthBlock":
                indentation = indentation.replace("    ", "", 1)
                text_to_add.append(indentation + i + "\n")
                indentation = indentation + "    "
            #SixteenthBlock
            elif type_list[type_count] == "SixteenthBlock":
                text_to_add.append(indentation + "try:\n")
                text_to_add.append(indentation + "    every[" + str(every_count) + "]\n")
                text_to_add.append(indentation + "except:\n")
                text_to_add.append(indentation + "    every[" + str(every_count) + "] = False\n")
                text_to_add.append(indentation + "while True:\n")
                indentation = indentation + "    "
                i = i.replace("every ", "if ", 1)
                text_to_add.append(indentation + i + "\n")
                indentation = indentation + "    "
                text_to_add.append(indentation + "if every[" + str(every_count) + "] == False:\n")
                every_statement = i
                whevery_indent = ("every", len(indentation))  
                indentation = indentation + "    "
                text_to_add.append(indentation + "every[" + str(every_count) + "] = True\n")                  
            #SeventeenthBlock
            elif type_list[type_count] == "SeventeenthBlock":
                text_to_add.append(indentation + "while True:\n")
                indentation = indentation + "    "
                i = i.replace("while ", "if ")
                text_to_add.append(indentation + i + "\n")
                whevery_indent = ("while", len(indentation))
                indentation = indentation + "    "
            #EighteenthBlock
            elif type_list[type_count] == "EighteenthBlock":
                indentation = indentation.replace("    ", "", 1)
                if len(indentation) <= reading_func:
                    reading_func = False
            #NineteenthBlock
            elif type_list[type_count] == "NineteenthBlock":
                text_to_add.append(indentation + "break\n")
            #TwentiethBlock
            elif type_list[type_count] == "TwentiethBlock":
                text_to_add.append(indentation + "continue\n")
            #TwentyfirstBlock
            elif type_list[type_count] == "TwentyfirstBlock":
                text_to_add.append(indentation + "pass\n")
            #PRD0IForward
            elif type_list[type_count] == "PRD0IForward":
                glob_word = i.split(" = ")[0]
                if glob_word not in global_vars:
                    global_vars.append(glob_word)
                text_to_add.append(indentation + i + "\n")
            #PRD0IRotate
            elif type_list[type_count] == "PRD0IRotate":
                glob_word = i.split(" = ")[0]
                if glob_word not in global_vars:
                    global_vars.append(glob_word)
                text_to_add.append(indentation + i + "\n")
            #PRD0OUltrasonic
            elif type_list[type_count] == "PRD0OUltrasonic":
                text_to_add.append(indentation + i + "\n")
            #PRD0IRecImg
            elif type_list[type_count] == "PRD0IRecImg":
                glob_word = "PRD0_I_RecImg"
                if glob_word not in global_vars:
                    global_vars.append(glob_word)
                i = i.replace("PRD0_I_RecImg = ", "")
                text_to_add.append(indentation + "PRD0_I_RecImg['" + i + "'] = " + str(os.listdir(pardies_configuration.path + "\\Scripts\\" + script + "\\RecImg\\" + i)) + "\n")
            #PRD0IRecImgParas
            elif type_list[type_count] == "PRD0IRecImgParas":
                glob_word = "PRD0_I_RecImgParas"
                if glob_word not in global_vars:
                    global_vars.append(glob_word)
                text_to_add.append(indentation + i + "\n")
            #PRD0ORecImg
            elif type_list[type_count] == "PRD0ORecImg":
                text_to_add.append(indentation + i + "\n")
            #every else statement
            if len(indentation) == whevery_indent[1] and type_list[type_count] != "FourteenthBlock" and type_list[type_count] != "FifteenthBlock":
                if whevery_indent[0] == "every":
                    indentation = indentation.replace("    ", "", 1)
                    text_to_add.append(indentation + every_statement + "\n")
                    text_to_add.append(indentation + "    if every[" + str(every_count) + "] == True:\n")
                    text_to_add.append(indentation + "        pass\n")
                    text_to_add.append(indentation + "else:\n")
                    text_to_add.append(indentation + "    every[" + str(every_count) + "] = False\n")
                    every_count = every_count + 1
                    every_statement = ""
                elif whevery_indent[0] == "while":
                    indentation = indentation.replace("    ", "", 1)
                whevery_indent = (None, 0)
            elif type_count == len(type_list) - 1 and whevery_indent[1] != 0:
                if whevery_indent[0] == "every":
                    to_indent = ""
                    for x in range(whevery_indent[1] - 4):
                        to_indent = to_indent + " "
                    text_to_add.append(to_indent + every_statement + "\n")
                    text_to_add.append(to_indent + "    if every[" + str(every_count) + "] == True:\n")
                    text_to_add.append(to_indent + "        pass\n")
                    text_to_add.append(to_indent + "else:\n")
                    text_to_add.append(to_indent + "    every[" + str(every_count) + "] = False\n")
                    every_count = every_count + 1
                    every_statement = ""
                whevery_indent = (None, 0)
            #type_count + 1
            type_count = type_count + 1
        #add to category and reset
        elif i == "BLOCK END":
            for glob_word in global_vars:
                text_to_add.insert(1, "    global " + glob_word + "\n")
            if category == "var_list_dict":
                var_list_dict = var_list_dict + text_to_add + ["\n"]
            elif category == "user_functions":
                user_functions = user_functions + text_to_add + ["\n"]
            elif category == "other":
                other = other + text_to_add + ["\n"]
            elif category == "every_while":
                every_while = every_while + text_to_add + ["\n"]
            read_pvpl = 0
        #count
        count = count + 1
    #3. ORGANISE THREADS
    for i in var_list_dict_funcs:
        threads.append("    thr" + i + " = threading.Thread(target = " + i + ")\n")
        thread_starts.append("    thr" + i + ".start()\n") 
    for i in user_functions_funcs:
        threads.append("    thr" + i + " = threading.Thread(target = " + i + ")\n")
        thread_starts.append("    thr" + i + ".start()\n")
    for i in other_funcs:
        threads.append("    thr" + i + " = threading.Thread(target = " + i + ")\n")
        thread_starts.append("    thr" + i + ".start()\n")
    for i in every_while_funcs:
        threads.append("    thr" + i + " = threading.Thread(target = " + i + ")\n")
        thread_starts.append("    thr" + i + ".start()\n")
    #4. ADD WRITING TO CYTHON_BT
    #var_list_dict
    for i in var_list_dict:
        cython_bt.write(i)
    cython_bt.write("\n\n\n")    
    #user_functions
    for i in user_functions:
        cython_bt.write(i)
    cython_bt.write("\n\n\n")
    #other
    for i in other:
        cython_bt.write(i)
    cython_bt.write("\n\n\n")
    #every_while
    for i in every_while:
        cython_bt.write(i)
    cython_bt.write("\n\n\n")
    #bluetooth stuff
    cython_bt.write(open(pardies_configuration.path + "\pardies_pvpl_cython_bt.py", "r").read())
    #threads
    for i in threads:
        cython_bt.write(i)
    cython_bt.write("    s_loop_thr = threading.Thread(target = sendLoop)\n")
    cython_bt.write("    r_loop_thr = threading.Thread(target = receiveLoop)\n")
    #thread_starts
    for i in thread_starts:
        cython_bt.write(i)
    cython_bt.write("    s_loop_thr.start()\n")
    cython_bt.write("    r_loop_thr.start()\n")
    #5. ADD WRITING TO CYTHON_WF
    #var_list_dict
    for i in var_list_dict:
        cython_wf.write(i)
    cython_wf.write("\n\n\n")    
    #user_functions
    for i in user_functions:
        cython_wf.write(i)
    cython_wf.write("\n\n\n")
    #other
    for i in other:
        cython_wf.write(i)
    cython_wf.write("\n\n\n")
    #every_while
    for i in every_while:
        cython_wf.write(i)
    cython_wf.write("\n\n\n")
    #bluetooth stuff
    cython_wf.write(open(pardies_configuration.path + "\pardies_pvpl_cython_wf.py", "r").read())
    #threads
    for i in threads:
        cython_wf.write(i)
    cython_wf.write("    s_loop_thr = threading.Thread(target = sendLoop)\n")
    cython_wf.write("    r_loop_thr = threading.Thread(target = receiveLoop)\n")
    #thread_starts
    for i in thread_starts:
        cython_wf.write(i)
    cython_wf.write("    s_loop_thr.start()\n")
    cython_wf.write("    r_loop_thr.start()\n")
    #close all
    cython_bt.close()
    cython_wf.close()
