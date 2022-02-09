import tkinter as tk
window = tk.Tk()

turned = 0
buttonstat = "Off"

# schijf hier tussen je code

def switch():
    global turned
    global button
    if turned == 0:
        turned += 1
    elif turned == 1:
        turned -= 1
    
    if turned == 1:
        mywindow = window.config(bg="yellow")
        button.config(text = "Lightswitch: On")
        print("The light is on")
    if turned == 0:
        mywindow = window.config(bg="white")
        button.config(text='Lightswitch: Off')
        print("The light is off")
    return buttonstat


button = tk.Button(text='Lightswitch: Off', bg="white", fg="black",command = switch)
button.pack(pady = 240, padx = 426)
# schijf hier tussen je code

window.mainloop()