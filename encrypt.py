import random

f = open("message.txt", "r")    
pt = list(f.read())     # Opens message.txt to store message in pt variable
f.close()
sd = list(input("Enter Seed:"))        # Asks for user input for encrpytion key and stores in sd variable
ct = ""
sct = ""
msg = ""        # Blank vairables to be used for storing messages later

# Below shows 2 lists key1 and key2 which are used later for converting characters found in key1 to characters in key2
# Table for below can be found in numbers.xlsx

key1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "`", "¬", "¦", "!", "\"", "£", "$", "€", "%", "^", "&", "*", "(", ")", "_", "+",
        "-", "=", "[", "]", "{", "}", ";", ":", "'", "@", "~", "#", ",", "<", ">", ".", "/", "?", "\\", "|", " ", "\n"]

key2 = ["9135", "7535", "9568", "6141", "1522", "7707", "3454", "4029", "9506", "9146", "2673", "1575", "1804",
        "3705", "1734", "6763", "4176", "6260", "9268", "2834", "3277", "5662", "9150", "6384", "4910", "9943",
        "7284", "4880", "1024", "2535", "6668", "6484", "7882", "4163", "6673", "9485", "4518", "1018", "8630",
        "4371", "8396", "1961", "9102", "9887", "8670", "6715", "5773", "6895", "3382", "8517", "5165", "1982",
        "4514", "1157", "9888", "1871", "4150", "2897", "1141", "5312", "7054", "9223", "3295", "7880", "7350",
        "4280", "7236", "3066", "4799", "9698", "1681", "2676", "6948", "8901", "2977", "9491", "7791", "1970",
        "8579", "1859", "3103", "7828", "9320", "4932", "5567", "2906", "8210", "9283", "6904", "2527", "2303",
        "2946", "7189", "9473", "2474", "2650", "1767", "5493", "8872", "6701"]

# Below shows how the hex number generated later will be converted
# Table for below can be found in numbers.xlsx

hxlst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

hxlst1 = ["I", "T", "4", "@", " ", "2", "^", "Z", "\\", "¬", "w", "%", "<", ".", "n", "Q"]

hxlst2 = ["B", "v", "A", "S", "|", "0", "3", "X", "&", "'", "d", "h", "?", "k", "£", "["]

hxlst3 = ["*", "E", "$", "#", "L", "1", "6", ";", ":", "¦", "f", ",", ">", "p", "\n", "7"]

def conv1(x, y):        # Function used to convert each character in pt and sd into its 4 digit counterpart
    global ct
    global sct
    z = key1.index(x)
    if y == pt:
        ct = ct + key2[z]
    elif y == sd:
        sct = sct + key2[z]

def conv2(x):   # Function used to generate a random digit (1,2 or 3) and convert the hex character into one of three characters accordingly
    global msg
    y = random.randint(1, 3)
    z = hxlst.index(x)
    if y == 1:
        msg = msg + hxlst1[z]
    elif y == 2:
        msg = msg + hxlst2[z]
    elif y == 3:
        msg = msg + hxlst3[z]

for count in pt:        # For loop for cycling through each letter of plain text and converting using conv1 function
    conv1(count, pt)
    
for count in sd:        # For loop for cycling through each letter of encryption key and converting using conv1 function
    conv1(count, sd)

ct = hex(int(ct)* int(sct))     # Multplying the enciphered seed and plaintext integers together and then converting to hexadecimal format
slc = slice(2, len(ct), 1)      
ct = ct[slc]                    # Removing the 0x at the start of the hex number

for count in ct:        # For loop for cycling through each letter of the Hex number and converting using conv2 function 
    conv2(count)

f = open("message.txt", "w")
f.write(msg)                    # Writing the finished message back to message.txt
f.close()
