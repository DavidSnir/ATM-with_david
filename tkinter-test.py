import tkinter as tk
import styles
import ui
from models import Bank

bank = Bank()
app = ui.ATMApp(bank=bank)
app.mainloop()
