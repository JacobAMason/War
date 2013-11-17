#war_gui.py

import tkinter
import tkinter.messagebox
import time

class gui:
    
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.withdraw()
        """
        self.textBody = tkinter.Frame(self.main_window)
        self.buttons = tkinter.Frame(self.main_window)
        
        self.label1 = tkinter.Label(self.textBody, text="Hello World")
        self.label2 = tkinter.Label(self.textBody, text="This is my GUI program.")
        
        self.label1.pack(side="left")
        self.label2.pack(side="right")
        
        self.textBody.pack()
        
        self.button1 = tkinter.Button(self.buttons, text="Click here", command=self.do_something)
        
        self.exitButton = tkinter.Button(self.buttons, text="Exit", command=self.main_window.destroy)
        
        self.button1.pack(side="left")
        self.exitButton.pack(side="right")
        
        self.buttons.pack(side="bottom")
        """
        #tkinter.mainloop() #this is like a spin  
              
    def message(self, message):
        tkinter.messagebox.showinfo("War", message)
        
    def exit(self):
        self.main_window.destroy()
        
    def welcome(self):
        time.sleep(2)
        print("\n"*25)
        print("                             By")
        print("                                   Jacob Mason")
        print("\n"*10)
        time.sleep(4)
        print("\n"*25)
        time.sleep(5)
        print("                             An")
        print("                                    MSU")
        print("                                            Production")
        print("\n"*10)
        time.sleep(4)
        print("\n"*25)
        time.sleep(6)
        print(" WWWWWWWW                           WWWWWWWW                                  ")
        print(" W::::::W                           W::::::W                                  ")
        print(" W::::::W                           W::::::W                                  ")
        print(" W::::::W                           W::::::W                                  ")
        print("  W:::::W           WWWWW           W:::::Waaaaaaaaaaaaa  rrrrr   rrrrrrrrr   ")
        print("   W:::::W         W:::::W         W:::::W a::::::::::::a r::::rrr:::::::::r  ")
        print("    W:::::W       W:::::::W       W:::::W  aaaaaaaaa:::::ar:::::::::::::::::r ")
        print("     W:::::W     W:::::::::W     W:::::W            a::::arr::::::rrrrr::::::r")
        print("      W:::::W   W:::::W:::::W   W:::::W      aaaaaaa:::::a r:::::r     r:::::r")
        print("       W:::::W W:::::W W:::::W W:::::W     aa::::::::::::a r:::::r     rrrrrrr")
        print("        W:::::W:::::W   W:::::W:::::W     a::::aaaa::::::a r:::::r            ")
        print("         W:::::::::W     W:::::::::W     a::::a    a:::::a r:::::r            ")
        print("          W:::::::W       W:::::::W      a::::a    a:::::a r:::::r            ")
        print("           W:::::W         W:::::W       a:::::aaaa::::::a r:::::r            ")
        print("            W:::W           W:::W         a::::::::::aa:::ar:::::r            ")
        print("             WWW             WWW           aaaaaaaaaa  aaaarrrrrrr            ")
        print("\n"*4)
        time.sleep(5)
        print()
        return