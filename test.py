import tkinter as tk

root = tk.Tk()

# sidebar
sidebar = tk.Frame(root, width=200, bg='white', height=500, relief='sunken', borderwidth=2)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

# main content area
mainarea = tk.Frame(root, bg='#CCC', width=500, height=500)
mainarea.pack(expand=True, fill='both', side='right')

root.mainloop()