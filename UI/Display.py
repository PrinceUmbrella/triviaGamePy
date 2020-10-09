from tkinter import Tk, Label, Button, Radiobutton, IntVar
#    ^ Use capital T here if using Python 2.7


def Game(prompt, options):
    root = Tk()
    root.title("Game Window")
    root.wm_geometry("400x400")
    if prompt:
        Label(root, text=prompt).pack()
    v = IntVar()
    for i, option in enumerate(options):
        Radiobutton(root, text=option, variable=v, value=i).pack(anchor="w")
    Button(text="Submit", command=root.destroy).pack()
    root.mainloop()
    if v.get() == 0:
        return None
    return options[v.get()]


# result = Game(
#     "What is your favorite color?",
#     [
#         "Blue!",
#         "No -- Yellow!",
#         "Aaaaargh!"
#     ]
# )

# print("User's response was: {}".format(repr(result)))
