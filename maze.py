from tkinter import Tk, BOTH, Canvas


win = Tk()
        
win.title('Maze Solver')

win.geometry('1000x600')
win.minsize(600, 400)
win.maxsize(1000, 600)
C = Canvas(win, width="800", height="1000", bg='white')
C.pack(pady='20')

win.mainloop()
