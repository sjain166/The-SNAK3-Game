import neopixel # To control LEDs
import random   # To generate food at random Locations
from machine import Pin #To control the GPIO pins
import time     # To add delay
import usocket as socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))
s.listen(5)

n = 300     # Number of LEDs
p = 5       # Pin D1 on ESP8266

## LEDs arrangement in a 2D Matrix
arr=[[  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12, 13,  14],
    [ 34,  33,  32,  31,  30,  29,  28,  27,  26,  25,  24,  23,  22, 21,  20],
    [ 40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52, 53,  54],
    [ 74,  73,  72,  71,  70,  69,  68,  67,  66,  65,  64,  63,  62, 61,  60],
    [ 80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,  92, 93,  94],
    [114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100],
    [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134],
    [154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 143, 142, 141, 140],
    [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174],
    [194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180],
    [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214],
    [234, 233, 232, 231, 230, 229, 228, 227, 226, 225, 224, 223, 222, 221, 220],
    [240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254],
    [274, 273, 272, 271, 270, 269, 268, 267, 266, 265, 264, 263, 262, 261, 260],
    [280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294]]


np = neopixel.NeoPixel(Pin(p), n)

def led(r,c,s=1):  ## To On and Off the leds to red
    if s==0:
        np[arr[r][c]]=(0,0,0)
        np.write()
    else:
        np[arr[r][c]]=(225,0,0)
        np.write()

def randmake():     ## To generate food at random places random module doesn't support randint in ESP8266
    temp=random.getrandbits(8)
    if temp>225:
        temp=temp-31
    fst=int(temp/15)
    snd=temp%15
    return (fst,snd)

def web_page():   ## Web page to take inputs for the game (the content value changes the speed of the snake movement in the refresh line)
    html = """
    <html>
    <head>
    <title>Snake Game</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="refresh" content="0.8">
    <style>
    html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #4286f4; border: none; 
      border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    </style>
    
    </head>
    <body>
    <h1 style="text-align: center;">Let's Play Snake Game</h1>
    <p style="text-align: center;"><a href="/?led=up"><button class="button">^</button></a></p>
    <p style="text-align: center;"><a href="/?led=left"><button class="button">&lt;</button></a>
    &emsp; &emsp; &emsp; &emsp;
    <a href="/?led=right"><button class="button">&gt;</button></a></p>
    <p style="text-align: center;"><a href="/?led=down"><button class="button">v</button></a></p>
    </body>
    </html>
    """
    return html

# Initializations
flag=0
rf,cf=randmake()
np[arr[rf][cf]]=(0,255,0)
np.write()
print(rf,cf)
r=c=0
lrc=[[r,c]]

# Main Loop
while True:
    try:
        conn,addr=s.accept()
#         print(str(addr))
        request = conn.recv(1024)
        request = str(request)
        if "GET /?led=up" in request:
            print("up")
            r=r+1
        elif "GET /?led=left" in request:
            print("left")
            c=c-1
        elif "GET /?led=right" in request:
            print("right")
            c=c+1
        elif "GET /?led=down" in request:
            print("down")
            r=r-1
        else:
            continue
        
        cr,cc=lrc[-1]        
        if ((len(lrc)>1) and ([r,c] in lrc)):
            flag=1

        if flag==1:
            print("Game Over!")
            for i in range (15):
                for j in range (15):
                    np[arr[i][j]]=(0,0,255)
                    np[arr[j][i]]=(0,0,255)
                    np[arr[14-j][i]]=(0,0,255)
                    np[arr[j][14-i]]=(0,0,255)
                np.write()
            for i in range (15):
                for j in range (15):
                    np[arr[i][j]]=(0,0,0)
                    np[arr[j][i]]=(0,0,0)
                    np[arr[14-j][i]]=(0,0,0)
                    np[arr[j][14-i]]=(0,0,0)
                np.write()
            flag=0
            rf,cf=randmake()
            np[arr[rf][cf]]=(0,255,0)
            np.write()
            print(rf,cf)
            r=c=0
            lrc=[[r,c]]
            
        if c<0:
            c=c+15
        if r<0:
            r=r+15
        if c>14:
            c=c-15
        if r>14:
            r=r-15

        lrc.insert(0,[r,c])
        led(lrc[0][0],lrc[0][1])
        led(cr,cc,0)
        lrc.pop()
                
        if (lrc[0]==[rf,cf]):
            rf,cf=randmake()
            print("food is {},{}".format(rf,cf))
            np[arr[rf][cf]]=(0,255,0)
            np.write()
            lrc.append([cr,cc])
            led(cr,cc)
            
        response=web_page()
        conn.send("HTTP/1.1 200 OK\n")
        conn.send("Content-type: text/html\n")
        conn.send("Connection: close\n\n")
        conn.sendall(response)
        conn.close()
    except:
        continue
