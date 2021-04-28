#the import programs for the GUI
import tkinter as tk
from tkinter import scrolledtext as sct



"""defining variables to use as input and code.
this tells the lists that the code will use.
we are converting our code into hexadecimal.
the first list is a list of letters, while the second
list tells their corresponding hexadecimal codes."""
#a to z list of letters:
ab_letter_list = ["a","b", "c",
"d","e","f","g",
"h","i","j","k",
"l","m","n","o",
"p","q","r","s",
"t","u","v","w",
"x","y","z","hello World!"]
abc = ab_letter_list

#hexacode corresponding list of letters:
hexa_letter_list = ["0" + str(hex(10)),"0" + str(hex(11)),
"0" + str(hex(12)),"0" + str(hex(13)),"0" + str(hex(14)),
"0" + str(hex(15)),str(hex(16)),str(hex(17)),
str(hex(18)),str(hex(19)),str(hex(20)),str(hex(21)),
str(hex(22)),str(hex(23)),str(hex(24)),str(hex(25)),
str(hex(26)),str(hex(27)),str(hex(28)),str(hex(29)),
str(hex(30)),str(hex(31)),str(hex(32)),str(hex(33)),
str(hex(34)),str(hex(35)), "Hello World!"]
hexa = hexa_letter_list

#this encodes and decodes the tool
def coding_tool(start_list, end_list):
    #string input
    if (start_list == abc):
        input_string = encrypt.get()
    if (start_list == hexa):
        input_string = decrypt.get()
    new_string = input_string
    temp_string = input_string
    
    #actual encoder
    for i in range (27):
        replace_letter = start_list[i]
        replace_with = end_list[i]
        temp_string = input_string
        for j in range(0,len(input_string)):
            if (start_list == abc):
                if (replace_letter == input_string[j]):
                    temp_string = temp_string[:j*4] + replace_with  +temp_string[j*4+4:]
                    new_string = new_string[:j*4] + replace_with  +new_string[j*4+4:]
            if (start_list == hexa):
                if (j == input_string.find(replace_letter)):
                    temp_string = temp_string[:j] + replace_with + temp_string[j*4+20:]
                    new_string = new_string[:j] + replace_with + new_string[j*4+20:]
    
    #output
    result = sct.ScrolledText(frame, height = 25, width = 100)
    result.grid(row = 5, column = 0)
    if (start_list == abc):
        result.insert("1.0","   Copy this into the decrypt box to return to English!")
    result.insert("1.0","")
    result.insert("1.0",new_string)
    result.insert("1.0","   New String: ")
    result.insert("1.0","")
    result.insert("1.0",input_string)
    result.insert("1.0","Original String: ")
    result.insert("1.0","")
    result.update()

#this creates the actual GUI
root = tk.Tk()
frame = tk.Frame(root, bg="light pink")
root.title("Encryption Tool")

#this is for the encryption half of the code
#this is the text entry box
encrypt = tk.Entry(frame, text = "Enter Text Here", fg = "grey", 
bg = "white")
encrypt.grid(row = 1, column = 1)

#these are the labels for the encryption half
e_label_a = tk.Label(frame, 
text = "Enter any 5 lowercase letters in ascending order to encrypt",
fg = "black", bg = "pink", font = ("comic sans ms", 16, "bold") )
e_label_a.grid(row = 0, column = 0)
e_label_b = tk.Label(frame, text = "try words like adopt",
bg = "light pink", fg = "dark grey", font = ("comic sans ms", 12, "italic"))
e_label_b.grid(row = 1, column = 0)


"""These are the actual workers. they are the 
encryption and decryption buttons. They are to carry
out the entire purpose of the program"""
#encrypt button
e_button = tk.Button(frame, text = "Encrypt- Into Gibberish",
command = lambda:coding_tool(abc, hexa), fg = "black",
bg = "orange", font = ("Comic sans ms",14, "bold" ))
e_button.grid(row = 4, column = 0)

#the text entry for the decrypt half
decrypt = tk.Entry(frame, text = "Enter Text Here", fg = "grey", 
bg = "white")
decrypt.grid(row = 3, column = 1)

#these are the labels for the decryption half
d_label_a = tk.Label(frame, 
text = "Copy the code into here!",
fg = "black", bg = "pink", font = ("comic sans ms", 16, "bold") )
d_label_a.grid(row = 2, column = 0)
d_label_b = tk.Label(frame, text = "try 00xa00xd0x180x190x1d",
bg = "light pink", fg = "dark grey", font = ("comic sans ms", 12, "italic"))
d_label_b.grid(row = 3, column = 0)

#decrypt button
d_button = tk.Button(frame, text = "Decrypt- Into English",
command = lambda:coding_tool(hexa, abc), fg = "black",
bg = "orange", font = ("Comic sans ms",14, "bold" ))
d_button.grid(row = 4, column = 1)

frame.pack()
root.mainloop()
