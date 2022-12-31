from tkinter import *

def showAnimal():
    showAnimalSelected.config(text=BoxContainer.get(ANCHOR))

def reset():
    showAnimalSelected.config(text="")

root = Tk()
root.geometry("260x300")
root.title("OpenBootcamp")
root.iconbitmap("OpenBootcamp.ico")
root.config(bg="#2c2c2c")
root.resizable(0,0)

question = Label(root,text="Elegir un animal de la lista")
question.pack(padx=4,pady=10)
question.config(bg="#2c2c2c", fg="White")


AnimalLista = ["Perro", "Gato", "Caballo", "Elefante", "Loro", "Tortuga", "Escorpion","Jirafa","Mono"]

BoxContainer = Listbox(root)

indice = 0
for animal in AnimalLista:
    BoxContainer.insert(indice, animal)
    indice += 1

BoxContainer.pack()
BoxContainer.config(bg="#2c2c2c",fg="white")

showAnimalSelected = Label(root)
showAnimalSelected.pack(pady=8)
showAnimalSelected.config(bg="#2c2c2c", fg="yellow",font=("Arial & bold", 12))

Button(root, text="Selected", command=showAnimal).pack(padx=20,pady=8, side="left")
Button(root, text="Reset", command=reset).pack(padx=20,pady=8, side="right")



#EventLoop
root.mainloop()