import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def retrieve_input():
    global URL
    URL = url_entry.get()
    print(URL)
    return URL

def do_command(command):
    global command_textbox
    URL = retrieve_input()
    if URL == "":
        URL = "::1"

    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    p = subprocess.Popen(command + " " +URL, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # v2

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

def msave():
    filename = asksaveasfilename(defaultextension='.txt', filetypes=(
    ('Text files', '*.txt'), ('Python files', '*.py *.pyw'), ('All files', '*.*')))
    if filename is None:
        return
    file = open(filename, mode='w')
    text_to_save = command_textbox.get("1.0", tk.END)

    file.write(text_to_save)
    file.close()

root = tk.Tk()
root.title("Use a Command Line GUI")
frame_a = tk.Frame(root, bg="light pink")
frame_a.pack()

#ping button
ping_btn = tk.Button(frame_a, text="Ping - Check if URL is Up and Active", command=lambda:do_command("ping"),
    font=("comic sans ms", 12),
    fg="navy blue", activeforeground = "light blue", 
    height = 5, width = 20, wraplength = 180, padx = 7,
    bg="light blue", activebackground = "navy blue")
ping_btn.grid(row = 0, column =0) 

#tracert button
tracert_btn = tk.Button(frame_a, text="Tracert - See Packet Routes",
    command=lambda:do_command("tracert"),
    font=("comic sans ms", 12),
    fg="navy blue", activeforeground = "light blue", 
    height = 5, width = 20, wraplength = 180, padx = 7,
    bg="light blue", activebackground = "navy blue")
tracert_btn.grid(row = 0, column = 1)

#nslookup button
nslookup_btn = tk.Button(frame_a, text="Nslookup - Find DNS Server Info", command=lambda:do_command("nslookup"),
    font=("comic sans ms", 12),
    fg="navy blue", activeforeground = "light blue", 
    height = 5, width = 20, wraplength = 180, padx = 7,
    bg="light blue", activebackground = "navy blue")
nslookup_btn.grid(row = 0, column = 2)

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="bisque") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    font=("comic sans ms", 14),
    fg="navy blue",
    bg="light blue")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans ms", 14)) # change font
url_entry.pack(side=tk.RIGHT)

frame_b = tk.Frame(root,  bg="light pink") # change frame color
frame_b.pack()

command_textbox = tksc.ScrolledText(frame_b, height=30, width=130)
command_textbox.pack()

#save button
save_btn = tk.Button(frame_b, text="Save - ", command=lambda:msave,
    font=("comic sans ms", 12),
    fg="navy blue", activeforeground = "light blue",
    height = 5, width = 24, padx = 7,
    bg="light blue", activebackground = "navy blue")
save_btn.pack()

frame_b.pack()
root.mainloop() 
