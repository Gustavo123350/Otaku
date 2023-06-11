import tkinter as tk
from PIL import ImageTk, Image
import time
from datetime import date
import getpass

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

root = tk.Tk()
root.geometry('400x200')
root.maxsize(400,200)
root.minsize(400,200)
root.title('Otaku')

# Definindo a cor de fundo transparente
root.attributes("-transparentcolor", "black")

# Carregando a imagem de fundo
image = Image.open("F://relogio_otaku//relogio.jpg")
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Obtendo o nome do usuário atual
username = getpass.getuser()
name_label = tk.Label(root, text=username, font=('Monterrat', 24), bg='dark red')
name_label.pack(pady=30)

# Obtendo a hora
clock_label = tk.Label(root, font=('Montserrrat', 18), bg='dark red')
clock_label.pack(pady=10)

# Obtendo a data e o ano
today = date.today()
date_label = tk.Label(root, text=today.strftime("%d/%m/%Y"), font=('Montserrat', 14), bg='dark red')
date_label.pack(pady=10)

# Atualizando o relógio a cada segundo
update_clock()

root.mainloop()



