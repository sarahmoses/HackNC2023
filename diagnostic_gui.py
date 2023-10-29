import tkinter as tk

root = tk.Tk()

root.title("Diagnostic")

root.geometry("360x800")

label = tk.Label(root, text="Select all symptoms that apply below:", font=(18))

label.pack(padx=20, pady=20)

frame = tk.Frame(root, padx=10)
frame.pack(pady=40)

listbox = tk.Listbox(frame, selectmode="multiple", width=100, height=10, font=18)
symptoms = ["Nausea", "Headache", "Fatigue", "Sore Throat", "Shortness of Breath", "Wheezing"]


def listbox_used(event):
    curselection = listbox.curselection()
    for index in curselection:
        print(listbox.get(index))

for item in symptoms:
    listbox.insert(symptoms.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)  # bind function allows any selection to call listbox_used function.
listbox.pack(padx=10, pady=10)

root.mainloop()