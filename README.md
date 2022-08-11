# THE-Snake Game

## Setting up ESP8266
The whole program is written in Micropython for ESP8266 so before getting started you have to flash the ESP8266 to run micropython.

![Esp8266](https://user-images.githubusercontent.com/89619544/179682320-f9fc702a-c628-4a6b-b145-ec742bab3af4.jpg)

Here is the documentation to do that https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html

This video online could help you if you still have any doubts about how to do this https://www.youtube.com/watch?v=dY0QyILX8NA

if you cannot find the com port in your device when plugged in device manager download this software from silicon labs https://www.silabs.com/documents/public/software/CP210x_Universal_Windows_Driver.zip

if you have a issue to run the esptool.py command lines just use "python-m esptool" instead of the "esptool.py"

Install Thonny to make modifications or to push the code to the microcontroller 

## Program

The boot.py is to connect to the wifi change the Username and Password to your Network

![Code](https://user-images.githubusercontent.com/89619544/179682375-a869208f-8d3e-45f5-a309-49cf82ab991e.png)

Here is the circuit diagram. The Power suppy is 5v since I am using a ws2812B led strip

![Schematic](https://user-images.githubusercontent.com/89619544/179682356-a1fda991-a5c9-4e7a-aa6b-fbd7c128fe25.png)

This program is to run snake game in a 15x15 Matrix made with WS2812B (5M 300led) Led Strip.

I also added background.py for generation of the square matrix if you are doing for a matrix of different size without cutting the strip by just folding.

![My Matrix](https://user-images.githubusercontent.com/89619544/179683082-6f3e3fb3-ad79-45c8-a88a-20853798fed1.jpg)


## Here is the Code in Action


