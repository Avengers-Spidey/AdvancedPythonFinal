import tkinter as tk
import random as rn

class Magic8Ball:
    answers = ["Yes, Most Definetely!",
           "The Chances Are High!",
           "Not Likely!",
           "The Odds Look Good!",
           "Is That Your Question?",
           "You Have To Wait And See!",
           "99.9% Success Rate!",
           "It looks good!",
           "The computer Says NO!",
           "Unable to Decide!"
           "Ask Again Later!",
           "Better Not Tell You Now!",
           "Cannot Predict Result!",
           "Concentrate and Ask Again!",
           "Don't Count On It!",
           "No Chance!",]
    
    error_msg = "ERROR: Your question must be TEXT"
    
    def get_respose(self,userentry):
        y = userentry.isdigit()
        l = len(userentry)
        if y or l == 0:
            return self.error_msg
        else:
            return rn.choice(self.answers)

class View(tk.Frame):
    def __init__(self,master,*args,**kwargs):
        tk.Frame.__init__(self,master,*args,**kwargs)
        
        self.data = Magic8Ball()
        
        self.configure(bg='Black')
        
        self.user_question = tk.StringVar()
        self.reply = tk.StringVar()

        lbl1 = tk.Label(self, text='Enter Your Question', bg='Black', fg='Red', font='freesansbold')
        lbl2 = tk.Label(self, text='Answer', bg='Black', fg='Red', font='freesansbold')
        lbl3 = tk.Label(self, text='0\n-\n0', bg='Black', font='Black')
        self.lbl_reply = tk.Label(self,font='freesansbold',textvariable=self.reply)

        btn1 = tk.Button(self, text='Get Answer', bg='darkBlue', fg='Red', font='freesansbold', command=self.get_answer)
        btn2 = tk.Button(self, text='Exit', bg='Red', fg='Black', font='freesansbold', command=self.quit)
        btn3 = tk.Button(self, text='Clear', bg='Green', fg='Black', font='freesansbold', command=self.clear)

        self.user_entry = tk.Entry(self, bg='Black', fg='Red', font='freesansbold, 12',textvariable = self.user_question)
        
        lbl1.pack()
        self.user_entry.pack()
        btn1.pack()
        lbl3.pack()
        lbl2.pack()
        self.lbl_reply.pack()
        btn3.pack()
        btn2.pack(side=tk.BOTTOM)
        
    def get_answer(self):
        self.reply.set(self.data.get_respose(self.user_question.get()))
        
    def clear(self):
        self.user_question.set("")
        self.reply.set("")
        
   
class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.minsize(300,300)
        self.title('Magic 8 Ball - Ben Woodfield')
        View(self).pack()

MainWindow().mainloop()