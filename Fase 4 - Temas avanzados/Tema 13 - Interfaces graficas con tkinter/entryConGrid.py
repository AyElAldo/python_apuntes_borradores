from tkinter import *

root = Tk()

label = Label(root, text='Label muy largo: ',fg='red')
label.grid(row=0, column=0, sticky='w', padx=5,pady=5)

entry = Entry(root, justify='center')
entry.grid(row=0, column=1,padx=5,pady=5)


label2 = Label(root, text='Apellido: ')
label2.grid(row=1, column=0, sticky='w',padx=5,pady=5)

entry2 = Entry(root, justify='right')
entry2.grid(row=1, column=1,padx=5,pady=5)


label3 = Label(root, text='No ESCRIRIBR: ')
label3.grid(row=2, column=0, sticky='w',padx=3,pady=3)

entry3 = Entry(root, state='disabled')
entry3.grid(row=2, column=1,padx=5,pady=5)


label4 = Label(root, text='Constraseña: ')
label4.grid(row=3, column=0, sticky='w',padx=3,pady=3)

entry4 = Entry(root, show='-', fg='blue', font='Bold')
entry4.grid(row=3, column=1,padx=5,pady=5)


root.mainloop()
