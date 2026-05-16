import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def cut_text(event=None):
    event.widget.event_generate("<<Cut>>")
    return "break"

def copy_text(event=None):
    event.widget.event_generate("<<Copy>>")
    return "break"

def paste_text(event=None):
    event.widget.event_generate("<<Paste>>")
    return "break"


def open_button_functionallity(window,text,current_path):
    filepath = askopenfilename(filetypes=[("All Files","*.*")])

    if not filepath:
        return

    text.delete(1.0,tk.END)
    with open(filepath, 'r') as f:
        content = f.read()
        text.insert(tk.END,content)
    current_path["path"] = filepath

    window.title(f"open file:{filepath}")
    

def save_button_functionallity(window,text,current_path):
    filepath = current_path["path"]
    
    if not filepath:
        filepath = asksaveasfilename(filetypes=[("All Files", "*.*")])
        if not filepath:
            return
    
    current_path["path"] = filepath 

    
    with open(filepath,"w") as f:
        content = text.get(1.0,tk.END)
        f.write(content)
    window.title(f"open file:{filepath}")
    


def main():  
    window = tk.Tk()
    current_path = {"path":None}
    

    
    

    window.title("Text editor")
    window.geometry("400x400")

    window.config(bg="black")


    text = tk.Text(window,
                   font=("Arial",12,"bold"),
                   fg="#00FF00",
                   bg="black",
                   height=30,
                   width=90,
                   insertbackground="#32CD32")

    
    frame = tk.Frame(window,relief=tk.RAISED,bg="black")

    save_button = tk.Button(frame,text="save",
                            background="#1F1F1F",
                         font=("ariel",13,'bold'),
                         border=3,
                         foreground="#FFC107",
                         activebackground="#141414",
                         activeforeground="#B0B0B0",
                         relief="raised",
                          command=lambda: save_button_functionallity(window,text,current_path) )
   
   
    open_button = tk.Button(frame,text="open",
                            background="#1F1F1F",
                         font=("ariel",13,'bold'),
                         border=3,
                         foreground="#FFC107",
                         activebackground="#141414",
                         activeforeground="#B0B0B0",
                         relief="raised",
                         command= lambda: open_button_functionallity(window,text,current_path))


    save_button.grid(row=0,column=0,padx=5,pady=5)
    open_button.grid(row=0,column=1,padx=5)


    frame.grid(row=0,column=0, sticky="ne")

    text.grid(row=1,column=0,sticky="nsew")
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0,weight=1)

    text.focus_set()

    window.bind("<Control-s>",lambda x: save_button_functionallity(window,text,current_path))
    window.bind("<Control-o>",lambda x: open_button_functionallity(window,text,current_path))
    window.bind("<Control-x>",cut_text)
    window.bind("<Control-c>",copy_text)
    window.bind("<Control-v>",paste_text)
    window.mainloop()






if __name__ == "__main__":
    main()