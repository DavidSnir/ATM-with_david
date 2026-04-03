from models import Bank
import tkinter as tk
import styles

class ATMApp(tk.Tk):
    def __init__(self, bank: Bank):
        super().__init__()
        self.geometry(f"{styles.window_width}x{styles.window_hight}")
        self.configure(bg=styles.color_dark_bg)
        
        # holds pages on top of each other
        container = tk.Frame(self, bg=styles.color_dark_bg)
        container.pack(fill="both", expand=True)
        
        self.frames = {}
        
        frame = LoginPage(parent=container, controller=self)
        self.frames[LoginPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(LoginPage)
        
        
    def show_frame(self, page_class: tk.Frame):
        frame = self.frames[page_class]
        frame.tkraise()
    

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=styles.color_dark_bg)
        self.controller = controller
        
        #---titles---
        
        self.page_title = tk.Label(
            self, 
            text="DevOps", 
            font=styles.font_page_title, 
            fg=styles.color_terminal_green,
            bg=styles.color_dark_bg
        )
        
        self.page_subtitle = tk.Label(
            self, 
            text="ATM_MACHINE", 
            font=styles.font_page_sub_title, 
            fg=styles.color_text_color,
            bg=styles.color_dark_bg
        )
        
        self.page_icon = tk.Label(
            self, 
            text="V1.0.3", 
            font=styles.font_page_title, 
            fg=styles.color_terminal_yellow,
            bg=styles.color_dark_bg

        )
        
        #---id---
        self.id_entry_frame_line = tk.Frame(
            self,
            bg=styles.color_terminal_green,
            height=2
        )
        self.id_entry_frame_line.pack(pady=12,padx=50, fill='x')
        
        self.id_entry_frame_background = tk.Frame(
            self.id_entry_frame_line,
            bg=styles.color_less_dark_bg
        )
        self.id_entry_frame_background.pack(side="top", fill="x", pady=(0,2))
        
        self.id_entry = tk.Entry(
            self.id_entry_frame_background,
            font=styles.font_field,
            bg=styles.color_less_dark_bg,
            fg=styles.color_text_color,
            borderwidth=0,
            highlightthickness=0
        )
        self.id_entry.pack(side="top", fill="x", ipady=12, padx=15)
        
        #---pin---
        self.pin_entry_frame_line = tk.Frame(
            self,
            bg=styles.color_terminal_green,
            height=2
        )
        self.pin_entry_frame_line.pack(pady=12,padx=50, fill='x')
        
        self.pin_entry_frame_background = tk.Frame(
            self.pin_entry_frame_line,
            bg=styles.color_less_dark_bg
        )
        self.pin_entry_frame_background.pack(side="top", fill="x", pady=(0,2))
        
        self.pin_entry = tk.Entry(
            self.pin_entry_frame_background,
            font=styles.font_field,
            bg=styles.color_less_dark_bg,
            fg=styles.color_text_color,
            borderwidth=0,
            highlightthickness=0
  
        )
        self.pin_entry.pack(side="top", fill="x", ipady=12, padx=15) 
        self.auth_button = tk.Button(
            
        )

        
        self.page_title.pack(pady=(20,0))
        self.page_subtitle.pack()
        self.page_icon.pack(pady=(20,0))
