import numpy as np
from tkinter import *
from PIL import Image
from PIL import ImageTk as itk
import scipy.io as sci
import time

res = 500  # Animation resolution
tk = Tk()
tk.geometry(str(int(res * 1.1)) + 'x' + str(int(res * 1.3)))
tk.configure(background='white')

canvas = Canvas(tk, bd=2)  # Generate animation window
tk.attributes('-topmost', 0)
canvas.place(x=res / 20, y=res / 20, height=res, width=res)
ccolor = ['#0008FF', '#DB0000', '#12F200']


# def restart():
#     global S
#     S = np.random.randn(l, l) > 0  # Random initialization, True: Alive, False: Dead


# def glider():
#     global S
#     S = sci.loadmat('glider.mat')['S'] == 1
#
#
# def glider_gun():
#     global S
#     S = sci.loadmat('glider_gun.mat')['S'] == 1


# rest = Button(tk, text='Restart', command=restart)
# rest.place(relx=0.05, rely=.85, relheight=0.12, relwidth=0.15)
#
# rest = Button(tk, text='Glider', command=glider)
# rest.place(relx=0.25, rely=.85, relheight=0.12, relwidth=0.15)
#
# rest = Button(tk, text='Glider Gun', command=glider_gun)
# rest.place(relx=0.45, rely=.85, relheight=0.12, relwidth=0.15)

# Decide on the parameters
l = 50  # Dimensions
S = np.random.randn(l, l) > 0  # Random initialization, True: Alive, False: Dead
gameoflife_image = np.zeros((l, l, 3))

t = 0

while True:
    s = S * 1
    C = s + np.roll(s, -1, axis=0) + np.roll(s, 1, axis=0) + \
        np.roll(s, -1, axis=1) + np.roll(s, 1, axis=1) + np.roll(np.roll(s, -1, axis=0), -1, axis=1) + \
        np.roll(np.roll(s, -1, axis=0), 1, axis=1) + np.roll(np.roll(s, 1, axis=0), -1, axis=1) + \
        np.roll(np.roll(s, 1, axis=0), 1, axis=1)

    for i in range(l):
        for j in range(l):
            if S[i, j]:  # Cell is alive
                if (C[i, j] - 1) < 2 or (C[i, j] - 1) > 3:  # If the number of alive cells around is not 2 or 3
                    S[i, j] = False
            else:  # Cell is dead
                S[i, j] = C[i, j] == 3  # Cell bocomes alive if there is exactly 3 live neighbors

    gameoflife_image[:, :, :] = 0
    gameoflife_image[:, :, 0] = S * 255
    gameoflife_image[:, :, 1] = S * 255
    gameoflife_image[:, :, 2] = np.logical_not(S) * 255
    t += 1

    img = itk.PhotoImage(Image.fromarray(np.uint8(gameoflife_image), 'RGB').resize((res, res), resample=Image.BOX))
    canvas.create_image(0, 0, anchor=NW, image=img)
    tk.title('time' + str(t))
    time.sleep(1 / 15)
    tk.update()

Tk.mainloop(canvas)