# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 17:04:20 2023

@author: Ankan Datta
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:25:00 2023

@author: Ankan Datta
"""

from tkinter import * 
import random

root = Tk()

root.title("Random Word Generator")
root.geometry("600x600")
root.configure(background='yellow')

alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
show_result = Label(root)
print(alpha_list)
 
def random_alpha():
    random_no = random.randint(0,26)
    print(random_no)
    random_no_alpha = alpha_list[random_no]
    print("Random Number : " + random_no_alpha)
    show_result["text"] = random_no_alpha

    
btn = Button(root)
btn = Button(root, text="Show random number", command=random_alpha)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)



show_result.pack()
root.mainloop()