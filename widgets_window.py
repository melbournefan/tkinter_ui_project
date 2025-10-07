import tkinter as tk
import tkinter.messagebox

class Application(tk.Frame):
    def __init__(self, window_width, window_height, master=None):
        super().__init__(master)
        self.master = master
        

# here we create the frame

        frame = tk.Frame(self.master, width=window_width,
        height=window_height)
        frame.pack()

        self.canvas = tk.Canvas(frame, bg='red')
        self.canvas.place(x=100, y=20, width=500, height=240)

        self.rectangle = self.canvas.create_rectangle(100, 0, 400, 200,
                                                      fill='blue')
        button = tk.Button(frame, text="Change Colour",
                           command=self.change_color)
        button.place(x=300, y=40)

    def change_color(self):
        self.canvas.itemconfig(self.rectangle, fill='yellow')
        tk.messagebox.showinfo(title="Message box", message="Change Colour")

if __name__ == '__main__':
    master = tk.Tk()
    window_width = 700
    window_height = 300
    master.geometry(str(window_width) + 'x' + str(window_height) )
    master.resizable(0, 0)
    app = Application(window_width, window_height, master=master)
    app.mainloop()
