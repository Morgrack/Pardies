#BLUETOOTH SEND LOOP
def sendLoop():
    global outgoing
    global incoming
    history = {"PRD0_I_Forward" : 0.0, "PRD0_I_Rotate" : 0.0}
    to_pop = []
    while True:
        if PRD0_I_Forward != history["PRD0_I_Forward"]:
            outgoing = outgoing + b"PRD0_I_Forward,,," + str(PRD0_I_Forward).encode() + b",,,"
            history["PRD0_I_Forward"] = PRD0_I_Forward
        if PRD0_I_Rotate != history["PRD0_I_Rotate"]:
            outgoing = outgoing + b"PRD0_I_Rotate,,," + str(PRD0_I_Rotate).encode() + b",,,"
            history["PRD0_I_Rotate"] = PRD0_I_Rotate
        if PRD0_I_RecImgParas != {}:
            the_dict = PRD0_I_RecImgParas
            for key in the_dict:
                outgoing = outgoing + b"PRD0_I_RecImgParas,,," + str(key).encode() + b",,,"
                for val in the_dict[key]:
                    outgoing = outgoing + val + b",,,"
                to_pop.append(key)
        for key in to_pop:
            PRD0_I_RecImgParas.pop(key)
            if to_pop.index(key) == len(to_pop) - 1:
                to_pop.clear() 
        if PRD0_I_RecImg != {}:
            the_dict = PRD0_I_RecImg
            for key in the_dict:
                outgoing = outgoing + b"PRD0_I_RecImg,,," + str(key).encode() + b",,,"
                for val in the_dict[key]:
                    bytes_format = open(info.directory + "/RecImg/" + key + "/" + val, "rb")
                    bytes_format = bytes_format.read()
                    outgoing = outgoing + bytes_format + b",,,"
                to_pop.append(key)
        for key in to_pop:
            PRD0_I_RecImg.pop(key)
            if to_pop.index(key) == len(to_pop) - 1:
                to_pop.clear()           
        if outgoing != b"":
            consistent = outgoing + b"complete,,,"
            bluetoothsocket.sendall(consistent)
            outgoing = outgoing.replace(consistent[:-11], b"", 1)




#WIFI RECEIVE LOOP
def receiveLoop():
    global outgoing
    global incoming
    global PRD0_O_Ultrasonic
    while True:
        while b",,,complete,,," != incoming[-14:]:
            to_add = bluetoothsocket.recv(1024)
            incoming = incoming + to_add
        print(incoming)
        if incoming != b"":
            consistent = incoming
            consistent_split = consistent[:-11].split(b",,,")
            for i in range(len(consistent_split)):
                #PRD0_O_Ultrasonic
                if consistent_split[i] == b"PRD0_O_Ultrasonic":
                    val = float(consistent_split[i + 1])
                    PRD0_O_Ultrasonic = val
            incoming = incoming.replace(consistent, b"", 1)




