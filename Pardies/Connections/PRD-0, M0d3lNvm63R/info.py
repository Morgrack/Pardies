#BRACKET HANDLER
def bracketHandler(var, *cont):
    if type(var) is list or type(var) is dict:
        return var[cont]
    else:
        return var(*cont)

#DIRECTORY
directory = "D:\Stuff\Programming and Robotics\Python and Robotics\Projects\Pardies\Pardies App\Pardies\Connections\PRD-0, M0d3lNvm63R"

#BLUETOOTH
bt_hex_addr = "censored"
bt_name = "raspberrypi"

#WIFI
wifi_server_ip = "censored"

