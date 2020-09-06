import backend, frontend, sys
from PyQt5.QtWidgets import QApplication
import qdarkgraystyle as dgs

class MainWindow(frontend.Frontend):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

    def make_password(self, s):
        self.password_info = backend.make_password()
        self.password_output.setText(f"Password: {self.password_info}")
    
    def check_password_if_button(self, s):
        """This does the exact same thing as below, except it is for button press instead"""
        holder = ""
        self.password_info = backend.check_password_strength(self.password_input.text())
        if self.password_info[0] == False:
            if self.password_info[1] == 5:
                holder = "Dangerous"
            if self.password_info[1] == 4:
                holder = "Unsafe"
            if self.password_info[1] == 3:
                holder = "Risky"
            if self.password_info[1] == 2:
                holder = "Medium"
            if self.password_info[1] == 1:
                holder = "Strong"
        else:
            holder = "Very Strong"
        self.password_output.setText(f"Password Strength: {holder}")

    def check_password_if_return(self):

        """This does the exact same thing as above, except it is for return instead"""
        holder = ""
        self.password_info = backend.check_password_strength(self.password_input.text())
        if self.password_info[0] == False:
            if self.password_info[1] == 5:
                holder = "Dangerous"
            if self.password_info[1] == 4:
                holder = "Unsafe"
            if self.password_info[1] == 3:
                holder = "Risky"
            if self.password_info[1] == 2:
                holder = "Medium"
            if self.password_info[1] == 1:
                holder = "Strong"
        else:
            holder = "Very Strong"
        self.password_output.setText(f"Password Strength: {holder}")
    
    def make_passphrase_if_button(self, s):
        self.password_info = backend.make_passphrase(self.password_input.text())
        self.password_output.setText(f"Passphrase: {self.password_info}")
    
    def make_passphrase_if_return(self):
        self.password_info = backend.make_passphrase(self.password_input.text())
        self.password_output.setText(f"Passphrase: {self.password_info}")

app = QApplication(sys.argv)
window = MainWindow()
window.setStyleSheet(dgs.load_stylesheet())

window.show()
app.exec_()