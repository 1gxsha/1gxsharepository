# -*- coding: utf-8 -*-
import json
from tkinter import *
def request_repository():
  repo = 'github.com/openshift/origin'
  data = requests.get(repository).json()
  data = dict((key, data[key]) for key in ['company', 'created_at', 'email', 'id', 'name', 'url'] if key in data)
  with open('repository.json', 'w') as file:
    json.dump(data, file)
tk = Tk()
tk.minsize(600,600)
tk.title('Georgiy Shapkin')
Button(tk, text='Get repository', command=request_repository).pack()
tk.mainloop()
