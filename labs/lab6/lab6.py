"""
Name: Joshua Uys
lab6.py

Vigenere

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Text, Entry, Point, Rectangle

width = 800
height = 400

win = GraphWin("Vigenere", width, height)

message_instruction = Text(Point(265, 100), "Message: ")
message_instruction.draw(win)
message_entry = Entry(Point(400, 100), 30)
message_entry.draw(win)

key_instruction = Text(Point(265, 150), "Key: ")
key_instruction.draw(win)
key_entry = Entry(Point(400, 150), 30)
key_entry.draw(win)

button = Rectangle(Point(300, 350), Point(500, 300))
button_text = Text(Point(400, 325), "Encode")
button_text.draw(win)
button.draw(win)

win.getMouse()

message = message_entry.getText()
message = message.upper()
message = message.replace(" ", "")

key = key_entry.getText()
key = key.upper()
key = key.replace(" ", "")

message_length = len(message)
key_length = len(key)
key_tracker = 0
key_list = []

encoded_message = ""
for x in range(message_length // key_length + message_length % key_length):
    for i in range(key_length):
        key_list.append(ord(key[i]) - 65)

for i in range(message_length):
    unicode_message = ord(message[i]) - 65
    unicode_key = key_list[key_tracker]
    unicode_shifted_message = (unicode_message + unicode_key) % 26
    shifted_message = chr(unicode_shifted_message + 65)

    key_tracker += 1

    encoded_message += shifted_message

print(encoded_message)

button.undraw()
button_text.setText(f"Encoded Message: \n {format(encoded_message)}")
close_text = Text(Point(400, 375), "Click to close")
close_text.draw(win)

win.getMouse()
win.close()


