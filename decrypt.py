f = open("message.txt", "r")
msg = list(f.read())
f.close()
sd = list(input("Enter Seed:"))
ct = ""
sct = ""
pt = ""

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

hxlst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f",
         "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f",
         "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

hxlst1 = ["I", "T", "4", "@", " ", "2", "^", "Z", "\\", "¬", "w", "%", "<", ".", "n", "Q",
          "B", "v", "A", "S", "|", "0", "3", "X", "&", "'", "d", "h", "?", "k", "£", "[",
          "*", "E", "$", "#", "L", "1", "6", ";", ":", "¦", "f", ",", ">", "p", "\n", "7"]

def conv1(x):
    global sct
    z = key1.index(x)
    sct = sct + key2[z]

def deconv2(x):
    global ct
    z = hxlst1.index(x)
    ct = ct + hxlst[z]
    
def deconv1(x):
    global pt
    z = key2.index(x)
    pt = pt + key1[z]

for count in sd:
    conv1(count)

for count in msg:
    deconv2(count)


ct = "0x" + ct
ct = int(ct, 0)
ct = str(int(ct // int(sct))) #error here
n = 4
ct = [ct[i:i+n] for i in range(0, len(ct), n)]

for count in ct:
    deconv1(count)
    
f = open("message.txt", "w")
f.write(pt)
f.close()