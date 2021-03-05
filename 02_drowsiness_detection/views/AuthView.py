from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controllers.AuthController import AuthController

class AuthView:

    next  = None
    def load(self):
        self.window = Tk()
        self.window.title("Drowsiness  Detection Application")
        tab_control = ttk.Notebook(self.window)


        self.login_tab = Frame(tab_control,bg="white",padx=20,pady=20)
        self.register_tab = Frame(tab_control,bg="white",padx=20,pady=20)

        tab_control.add(self.login_tab, text="Login")
        tab_control.add(self.register_tab, text = "Register")

        self.login()
        self.register()

        tab_control.grid()

        self.window.mainloop()

    def register(self):
        window = self.register_tab

        # Name label and entry
        nl = Label(window, text="Name")
        nl.grid(row=0, column=0)

        ne = Entry(window, width=10)
        ne.grid(row=0, column=1)

        # username label and entry
        ul = Label(window, text="Username")
        ul.grid(row=1, column=0)

        ue = Entry(window, width=10)
        ue.grid(row=1, column=1)

        #  password name and entry
        pl = Label(window, text="Password")
        pl.grid(row=2, column=0)

        pe = Entry(window, show="*", width=10)
        pe.grid(row=2, column=1)

        # email label and entry
        el = Label(window, text="Email")
        el.grid(row=3, column=0)

        ee = Entry(window, width=10)
        ee.grid(row=3, column=1)

        # Phone label and entry
        phl = Label(window, text="Phone")
        phl.grid(row=4, column=0)

        phe = Entry(window, width=10)
        phe.grid(row=4, column=1)

        b1 = Button(window, text="Register",command = lambda: self.registerControl(ne.get(),
                                                                              phe.get(),ee.get(),
                                                                              ue.get(),pe.get()
                                                                              ), padx=5,pady=5)
        b1.grid(row=5, column=1,pady=5)

    def login(self):
        window = self.login_tab

        ul = Label(window,text="Username")
        ul.grid(row=0,column=0)

        ue = Entry(window,width=10)
        ue.grid(row=0,column=1)

        pl = Label(window, text="Password")
        pl.grid(row=1, column=0)

        pe = Entry(window, show="*", width=10)
        pe.grid(row=1, column=1)

        b1 = Button(window,text="Login",command=lambda: self.loginControl( ue.get() ,pe.get()),  padx=5,pady=5)
        b1.grid(row=2,column=1,pady=5)

    def loginControl(self,username,password):
        ac = AuthController()
        message = ac.login(username,password)
        if message == 1:
            self.window.destroy()
            # print("window destroyed")
            self.transfer_control()
        else:
            messagebox.showinfo('Message',message)

    def registerControl(self,name,phone,email,username,password):

        ac = AuthController()
        message = ac.register(name,phone,email,username,password)
        messagebox.showinfo('Message', message)

if __name__ == '__main__':
    av = AuthView()