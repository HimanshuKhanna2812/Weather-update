from tkinter import *
import requests
from PIL import ImageTk,Image
import time

f1="constantia 30 bold"
f2="arial 16 bold"
root=Tk()
root.geometry("450x700")
root.title("Skarsh Weather App")
root.configure(bg="#0d633d")


def getweather(root):
    city=field.get()
    api="http://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=6fe008cb954f5f98358050bf4023dca4"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp']-273.15)
    mintemp=int(json_data['main']['temp_min']-273.15)
    maxtemp=int(json_data['main']['temp_max']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity'] 
    wind=json_data['wind']['speed']


    final_D_info=condition + "\n" +str(temp) +"°C"
    final_temp="\n"+ "Max temp: "+str(maxtemp)+"\n"+"Min temp: "+str(mintemp) +"\n"
    final_pressure="Pressure: "+str(pressure)+" "+"Humidity: "+str(humidity)+"\n"
    final_wind="Wind: "+str(wind)
    l1.config(text=final_D_info)
    l2.config(text=final_temp)
    l3.config(text=final_pressure)
    l5.config(text=final_wind)

img=Image.open(r"C:\Users\rahulkhanna01\Desktop\tkinterproj\w3.png")
img=img.resize((100,100))
img=ImageTk.PhotoImage(img)
Label(root,image=img,bg="#36736e").pack(pady=4)
field=Entry(root,font=f1,justify=CENTER)
field.pack(pady=20,side=TOP)
field.focus()
field.bind("<Return>",getweather)
Button(root,text="Search your city",textvariable=getweather,font="arial 18",relief=SUNKEN,bg="#216a70",fg="#7bc3c9").pack(side=TOP,pady=10)
l1=Label(root,font="arial 32 bold",bg="#0d633d",fg="#81dbd4")
l1.pack(pady=5)

l2=Label(root,font="arial 20 bold",bg="#36736e",height=3,fg="#81dbd4")
l2.pack(pady=5)
l3=Label(root,font="arial 20 bold",bg="#0d633d",fg="#81dbd4")
l3.pack(pady=5)

l5=Label(root,font="arial 22 bold",bg="#36736e",fg="#81dbd4")
l5.pack(pady=5)

root.mainloop()
