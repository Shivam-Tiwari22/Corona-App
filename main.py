def Scrap():

    def notifyMe(title,message):
        plyer.notification.notify(
        title = title,
        message= message,
        app_icon = 'live1.ico',
        timeout = 20
            )


    url = 'https://www.worldometers.info/coronavirus/'

    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    tablebody = soup.find('tbody')

    ttt =  tablebody.find_all('tr')
    notifycountry = countrydata.get()
    if(notifycountry == ''):
        notifycountry = 'india'




    countries, total_cases, new_cases, total_deaths, new_deaths, total_recoverd, active_cases = [], [], [], [], [], [], []
    serious, totalcases_permillion, totaldeaths_permillion, totaltests, totaltest_permillion = [], [], [], [], []

    headers = ['countries', 'total_cases', 'new_cases', 'total_deaths', 'total_recoverd', 'active_cases',
    'serious', 'totalcases_permillion', 'totaldeaths_permillion', 'totaltests', 'totaltest_permillion']


    for i in ttt:
        id = i.find_all('td')
        if(id[1].text.strip().lower() == notifycountry):
            totalcases1 = int(id[2].text.strip().replace(',', ''))
            totaldeaths1 = id[4].text.strip()
            newcases1 = id[3].text.strip()
            newdeaths1 = id[4].text.strip()
            notifyMe('Corona Virus Details In {}'.format(notifycountry),
                     'Total Cases : {}\nTotal Deaths : {}\nNew Cases : {}\nNew Death : {}'.format(totalcases1, totaldeaths1,newcases1,newdeaths1))

        countries.append(id[1].text.strip()), total_cases.append(int(id[2].text.strip().replace(',', '')))
        new_cases.append(id[3].text.strip()), total_deaths.append(id[4].text.strip())
        new_deaths.append(id[5].text.strip()),
        total_recoverd.append(id[6].text.strip())
        active_cases.append(id[7].text.strip()), serious.append(id[8].text.strip())
        totalcases_permillion.append(id[9].text.strip()), totaldeaths_permillion.append(id[10].text.strip())
        totaltests.append(id[11].text.strip()), totaltest_permillion.append(id[12].text.strip())

    df = pd.DataFrame(list(zip(countries, total_cases, new_cases, total_deaths, new_deaths, total_recoverd, active_cases, serious,
                                totalcases_permillion, totaldeaths_permillion, totaltests, totaltest_permillion)), columns=headers)
    sor = df.sort_values('total_cases',ascending=False)
    for k in formatlist:
        if(k == 'html'):
            path2= '{}/alldata.html'.format(path)
            sor.to_html(r'{}'.format(path2))

        if(k=='json'):
             path2= '{}/alldata.json'.format(path)
             sor.to_json(r'{}'.format(path2))



        if(k=='csv'):
             path2= '{}/alldata.csv'.format(path)
             sor.to_csv(r'{}'.format(path2))

    if(len(formatlist) !=0):
        messagebox.showinfo("Notification",'Corona Record Is Saved{}'.format(path2),parent=root)

def Download():
    global path
    if(len(formatlist) != 0):
        path = filedialog.askdirectory()
        print(path)
    else:
        pass
    Scrap()
    formatlist.clear()
    InHtml.configure(state='normal')
    InJson.configure(state='normal')
    InCsv.configure(state='normal')


def InHtml():
    formatlist.append('html')
    InHtml.configure(state='disable')

def InJson():
    formatlist.append('json')
    InJson.configure(state='disable')

def InCsv():
    formatlist.append('csv')
    InCsv.configure(state='disable')



import plyer
import requests
from bs4 import BeautifulSoup
import pandas as pd

from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox,filedialog
root = Tk()
root.title('Corona Virus Information')
root.geometry('530x300+200+80')
load = Image.open('corona.jpg')
render = ImageTk.PhotoImage(load)

# frame2 = PhotoImage(file=giphy.gif, format="gif -index 2")


# root.configure(bg='plum2')
root.iconbitmap('covid.ico')
formatlist = []
path = []


################################################################# Lable

img = Label(root,image = render)
img.place(x=0, y=0)
IntroLabel = Label(root,text='Corona Virus Information',font=('new roman',30,'bold'),foreground='white',bg='black',width=22)
IntroLabel.place(x=0,y=0)
EntryLable = Label(root,text='Notify Country : ',font=('arial',20,'italic bold'),bg='salmon1',width=0)
EntryLable.place(x=10,y=70)

FormateLabble = Label(root,text='Download In : ',font=('arial',20,'italic bold'),bg='plum2',width=0)
FormateLabble.place(x=10,y=150)

###################################################### Entry
countrydata = StringVar()
ent1 = Entry(root,textvariable=countrydata,font=('arial',20,'italic bold'),relief=RIDGE,bd=2,width=20)
ent1.place(x=220 , y=70)

##############################################################Buttons
InHtml = Button ( root , text = 'Html' , bg = 'blue' , fg = 'white' , font = ('binary' , 15 , 'bold') , relief = RIDGE,
                  activebackground = 'green' , activeforeground = 'white' , bd = 5 , width = 5,command=InHtml)
InHtml.place ( x = 210 , y = 150 )

InJson = Button ( root , text = 'Json' , bg = 'blue' , fg = 'white' , font = ('binary' , 15 , 'bold') , relief = RIDGE,
                  activebackground = 'green' , activeforeground = 'white' , bd = 5 , width = 5,command=InJson )
InJson.place ( x = 320 , y = 150 )


InCsv = Button ( root , text = 'Csv' , bg = 'blue' , fg = 'white' , font = ('binary' , 15 , 'bold') , relief = RIDGE,
                  activebackground = 'green' , activeforeground = 'white' , bd = 5 , width = 5,command=InCsv )
InCsv.place ( x = 430 , y = 150 )

Submit = Button ( root , text = 'Submit' , bg = 'green' , fg = 'white' , font = ('binary' , 15 , 'bold') , relief = RIDGE,
                  activebackground = 'blue' , activeforeground = 'white' , bd = 5 , width = 25,command=Download )
Submit.place ( x = 110 , y = 250 )



root.mainloop()
