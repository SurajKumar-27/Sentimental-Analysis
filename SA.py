from tkinter import *
from textblob import TextBlob
from PIL import ImageTk,Image
main_window=Tk()
p1=PhotoImage(file="5645454.png")
main_window.iconphoto(False,p1)
main_window.title("Sentimental Analysis")
main_window.geometry('450x270')
main_window.configure(bg='#BFC9CA')
my_font=('Georgia',13,'bold')
my_font1=('Georgia',10)
Label(main_window,text="Enter the Text",font=my_font,bg='#BFC9CA').grid(row=0,column=0,pady=10)
text=Text(main_window,borderwidth=2,width=40,height=5)
text.grid(row=1,column=0,padx=55)
def sentiment():
    review=text.get(1.0,END)
    key=TextBlob(review)
    sentiment=key.sentiment.polarity
    if(sentiment<0):
        a=Toplevel(main_window)
        photo=Image.open("WhatsApp Image 2022-04-15 at 7.44.36 AM (1).jpg")
        img=ImageTk.PhotoImage(photo)
        Label(a,text="Negative",font=my_font).grid(row=0,column=0,padx=50,pady=20)
        label=Label(a,image=img)
        label.photo=img
        label.grid(row=1,column=0)
    elif(sentiment>0):
        b=Toplevel(main_window)
        photo1=Image.open("maxresdefault .jpg")
        img1=ImageTk.PhotoImage(photo1)
        Label(b,text='Positive',font=my_font).grid(row=0,column=0,pady=10,padx=50)
        label=Label(b,image=img1)
        label.photo1=img1
        label.grid(row=1,column=0)
    else:
        c=Toplevel(main_window)
        photo2=Image.open("WhatsApp Image 2022-04-15 at 8.33.01 AM.jpg")
        img2=ImageTk.PhotoImage(photo2)
        Label(c,text='Neutral',font=my_font).grid(row=0, column=0,pady=10,padx=50)
        label=Label(c,image=img2)
        label.photo2=img2
        label.grid(row=1,column=0)
Button(main_window,text="Check Sentiment",command=sentiment,font=my_font1,bg='#F85252').grid(row=2,column=0,pady=25)
main_window.mainloop()