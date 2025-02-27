import tkinter as tk
import random

x_multiplier = 0.8
y_multiplier = 0.8

class BallApp:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root, width=400, height=400)
        self.frame.pack()
        self.canvas = tk.Canvas(self.frame, width=400, height=400, bg="red")
        self.canvas.pack()
        self.ball = self.canvas.create_oval(190, 190, 210, 210, fill='blue')
        self.dx = 10
        self.dy = 10
        self.canvas.bind('<Button-1>', self.move_ball)
        self.update_ball()

    def move_ball(self, event):
        self.dx = random.choice([-10, 10])
        self.dy = random.choice([-10, 10])

    def update_ball(self):
        self.canvas.move(self.ball, self.dx, self.dy)
        pos = self.canvas.coords(self.ball)
        if pos[0] <= 0 or pos[2] >= 400:
            self.dx = -self.dx * x_multiplier
        if pos[1] <= 0 or pos[3] >= 400:
            self.dy = -self.dy * y_multiplier
        self.root.after(50, self.update_ball)

root = tk.Tk()
app = BallApp(root)
root.mainloop()