# import library
import tkinter as tk

# Initiate the root
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=700, bg="Black", highlightthickness=0)
canvas.pack()
root.resizable(False, False)


# Minimize Button (Where the problem is)
def MinimizeClick():
    root.update_idletasks()
    root.overrideredirect(False)
    root.state('iconic')


def OnIconClickReturnWindow(event):
    root.update_idletasks()
    root.overrideredirect(True)
    root.state('normal')


Minimize = tk.Button(text='−', command=MinimizeClick)
Minimize.bind("<Map>", OnIconClickReturnWindow)
canvas.create_window(425, 24, window=Minimize, width=50, height=49)
Minimize.config(bg="#242424", fg="white", activebackground="black", justify="center", border="0")


# Button is pressed background changer
def MinimizePressedBackground(event):
    Minimize["background"] = "#242424"


def MinimizeBackground(event):
    Minimize["background"] = "#242424"


def MinimizeChangeColorOnButtonHover(event):
    Minimize.config(cursor="hand2")
    Minimize['background'] = "#63B8FF"


Minimize.bind("<ButtonPress-1>", MinimizePressedBackground)
Minimize.bind("<ButtonRelease-1>", MinimizeBackground)
Minimize.bind("<Leave>", MinimizeBackground)
Minimize.bind("<Enter>", MinimizeChangeColorOnButtonHover)


# End of problem-code (probably)


# Quit Button
# Don't care about that, it's just for you to quit the program
def Quit():
    root.destroy()


Quit = tk.Button(text='×', command=Quit)
canvas.create_window(476, 24, window=Quit, width=50, height=49)
Quit.config(bg="#242424", fg="white", activebackground="black", justify="center", border="0")


# Button is pressed background changer
def QuitPressedBackground(event):
    Quit["background"] = "#242424"


def QuitBackground(event):
    Quit["background"] = "#242424"


def QuitChangeColorOnButtonHover(event):
    Quit.config(cursor="hand2")
    Quit['background'] = "#CF6679"


Quit.bind("<ButtonPress-1>", QuitPressedBackground)
Quit.bind("<ButtonRelease-1>", QuitBackground)
Quit.bind("<Leave>", QuitBackground)
Quit.bind("<Enter>", QuitChangeColorOnButtonHover)
# End of quit

# loop
root.mainloop()