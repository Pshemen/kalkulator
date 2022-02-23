import tkinter as tk

def inicjalizacjaOkienek ():
    root = tk.Tk()
    root.geometry('480x480')
    root.title('Kalkulator')

    return root
def inicjalizacjaekranu (root):
    ekran = [tk.Label(root, bg='#c0cbcb', text='test', width=70, anchor='w', borderwidth=2 ) for i in range (3)]

    for i in range(len(ekran)):
        ekran[i].grid(row =i , column =0, ipady =15, ipadx= 1 )
    return ekran

if __name__ == '__main__':


    root = inicjalizacjaOkienek()

    ekran = inicjalizacjaekranu (root)

    root.mainloop()


