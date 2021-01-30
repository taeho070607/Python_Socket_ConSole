import TaeMe
import tkinter as tk
from _thread import *
TaeMe2 = TaeMe.TaeMe
@TaeMe2
def index(admin,content,color):
    if len(content.split(" ")) > 1:
        if content.split(" ")[1] == "next":
            fun = TaeMe2.search(self=TaeMe2,Taeget="next")
            return fun(Post=[admin["ConSoleAddr"][0]],content=content,color=color,admin=admin)
        else:
            return "Hellow,Word (if you want next page input 'index next')"
    else:
        return "Hellow,Word (if you want next page input 'index next')"
@TaeMe2
def next(Post: list,content,color,admin):
    return "We Are Targeting You (You : "+Post[0]+")"
@TaeMe2
def ban_users(content,color):
    if len(content.split(" ")) > 1:
        TaeMe2.ban_users.append(content.split(" ")[1])
        return "banned " + content.split(" ")[1]
    return None
@TaeMe2
def max_users(content,color):
    if len(content.split(" ")) > 1:
        TaeMe2.max_users = content.split(" ")
        return "max_users" + content.split(" ")[1]
    return None
TaeMe2.display_run(self=TaeMe2)
