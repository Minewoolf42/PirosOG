import tkinter
import mouse,os,time,random
from tkinter import PhotoImage
x,y=64,64
target=[x,y]
delay=0.05
chance=25
speed=4
act=0
foget=16
gif=16
root=tkinter.Tk()
root.wm_attributes('-transparentcolor', '#000000')
root.wm_attributes('-topmost', 1)
root.overrideredirect(1)
a=tkinter.Canvas(root,bg='#000000',width=root.winfo_screenwidth(),height=root.winfo_screenheight())
a.pack()
pir = (PhotoImage(file="Пирожог (3D).png"),PhotoImage(file="Пирожог (3D)-.png"))
likeanim=[PhotoImage(file="Пирожог (3D) like.gif", format="gif -index "+str(i))for i in range(gif)]
sleepanim=[PhotoImage(file="Пирожог (3D) sleep.gif", format="gif -index "+str(i))for i in range(gif)]
def mefunc(event):
    if x-64<event.x<x+64 and y-64<event.y<y+64:
        acts=tkinter.Menu(root,tearoff=0)
        acts.add_command(label='Похвалить',command=like)
        acts.add_command(label='Спать',command=sleep)
        acts.add_command(label='Сохранить',command=saveme)
        acts.post(event.x,event.y)
def like():
    global favacts, favpos
    favacts.append(lastacts)
    favpos.append(lastpos)
    for i in range(gif):
        a.delete('all')
        a.create_image(x, y, image=likeanim[i])
        root.update()
        time.sleep(delay)
def sleep():
    global favacts, favpos
    favacts=random.choices(favacts,k=len(favacts)-foget)
    favpos=random.choices(favacts,k=len(favpos)-foget)
    for i in range(gif):
        a.delete('all')
        a.create_image(x, y, image=sleepanim[i])
        root.update()
        time.sleep(delay)
def openme():
    global favacts,favpos
    if not os.path.exists('favacts.txt'):
        f = open('favacts.txt', 'w')
        f.close()
        f = open('favpos.txt', 'w')
        f.close()
    try:
        favacts = [int(i) for i in open('favacts.txt').read().split(' ')]
        favpos = [[int(ii) for ii in i.split('.')] for i in open('favpos.txt').read().split(' ')]
    except:
        favacts = [0]
        favpos = [[x,y]]
def saveme():
    f = open('favacts.txt', 'w')
    f.write(' '.join([str(i) for i in favacts]))
    f.close()
    f = open('favpos.txt', 'w')
    f.write(' '.join(['.'.join([str(ii) for ii in i])for i in favpos]))
    f.close()
class acts:
    def null(self):
        a=0
    def click(self):
        a.delete('all')
        root.update()
        mposes=mouse.get_position()
        mouse.move(x-mposes[0],y-mposes[1], absolute=False, duration=0)
        mouse.click()
        mouse.move(mposes[0]-x,mposes[1]-y, absolute=False, duration=0)
        a.create_image(x, y, image=pir[0] if target[0] < x else pir[1])
        root.update()
    def douclick(self):
        a.delete('all')
        root.update()
        mposes=mouse.get_position()
        mouse.move(x-mposes[0],y-mposes[1], absolute=False, duration=0)
        mouse.double_click()
        mouse.move(mposes[0]-x,mposes[1]-y, absolute=False, duration=0)
        a.create_image(x, y, image=pir[0] if target[0] < x else pir[1])
        root.update()
    def rgclick(self):
        a.delete('all')
        root.update()
        mposes=mouse.get_position()
        mouse.move(x-mposes[0],y-mposes[1], absolute=False, duration=0)
        mouse.right_click()
        mouse.move(mposes[0]-x,mposes[1]-y, absolute=False, duration=0)
        a.create_image(x, y, image=pir[0] if target[0] < x else pir[1])
        root.update()
myacts=[acts.null,acts.click,acts.douclick,acts.rgclick]
openme()
root.bind('<Button-3>',mefunc)
while True:
    time.sleep(delay)
    if target==[x,y]:
        myacts[act](acts)
        lastacts=act
        lastpos=target
        if random.randint(0, 99) < chance:
            favacts.append(act)
        if random.randint(0, 99) < chance:
            favpos.append(target)
        if random.randint(0,99)<chance:
            act=random.choice(favacts)
            target=random.choice(favpos)
        else:
            act = random.randint(0,len(myacts)-1)
            target = [random.randint(0,root.winfo_screenwidth())//speed*speed,random.randint(0,root.winfo_screenheight())//speed*speed]
    if target[0]<x:
        x-=speed
    if target[0]>x:
        x+=speed
    if target[1]<y:
        y-=speed
    if target[1]>y:
        y+=speed
    root.update()
    a.delete('all')
    a.create_image(x, y, image=pir[0]if target[0]<x else pir[1])