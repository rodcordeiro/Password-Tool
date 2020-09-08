# Import Stuff
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import sys

"""This is where the Code for the Frontend will be"""
class Frontend(QMainWindow):
    def __init__(self, *args, **kwargs): # Collect all the Init from QMainWidnow
        """This is where the UI Logic Is"""
        super(Frontend, self).__init__(*args, **kwargs)
        # Make a Global Password
        self.password_info = ""
        self.password_output = ""
        self.password_input = ""
        self.setWindowTitle("Password Tool")

        # Create a ToolBar
        toolbar = QToolBar("Menu")
        self.addToolBar(toolbar)

        # Generate the Make Password Button
        make_password_action = QAction("Make A Password", self)
        make_password_action.setStatusTip("Generate A Password")

        # Connect the Button Press to the Make Password Page
        make_password_action.triggered.connect(self.make_passwd_Page)
        toolbar.addAction(make_password_action)

        # Generate the Check Password Button
        check_password_action = QAction("Check A Password", self)
        check_password_action.setStatusTip("Check A Password")

        # Connect the Button Press to the Check Password Page
        check_password_action.triggered.connect(self.check_password_Page)
        toolbar.addAction(check_password_action)

        # Generate the make Passphrase Page
        make_passphrase_action = QAction("Make A Passphrase", self)
        make_passphrase_action.setStatusTip("Generate a Passphrase")

        # Generate the Button Press to connect to the Check Password Page
        make_passphrase_action.triggered.connect(self.make_passphrase_Page)
        toolbar.addAction(make_passphrase_action)


    def make_passwd_Page(self, s):
        """This handles the UI to make the password"""

        # Set default stuff
        self.password_output = ""
        self.password_info = ""

        # Create the Content of the page
        widget = QWidget()
        layout = QVBoxLayout()
        title = QLabel("Password Maker")
        button = QPushButton("Generate A Password")
        button.clicked.connect(self.make_password)
        self.password_output = QLabel(f"Password: {self.password_info}")
        self.password_output.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # Start adding widgets to the Layout Engine
        layout.addWidget(title)
        layout.addWidget(button)
        layout.addWidget(self.password_output)

        # Add the Layout to the widget
        widget.setLayout(layout)

        # Initialize the Page
        page = lambda: self.setCentralWidget(widget)

        # Return the output
        return page()

    def check_password_Page(self, s):
        """This handles the UI to check the password"""
        # Creating the Content of the Page
        self.password_output = ""
        self.password_info = ""
        widget = QWidget()
        layout = QVBoxLayout()
        title = QLabel("Password Checker")
        self.password_input = QLineEdit()
        self.password_input.setMaxLength(100) # The Maximum number of characters pressed is 100
        self.password_input.setPlaceholderText("Enter Your Password") # Prompt
        self.password_input.returnPressed.connect(self.check_password_if_return)
        button = QPushButton("Check Password")
        button.clicked.connect(self.check_password_if_button)
        self.password_output = QLabel(f"Password Strength {self.password_info}")
        self.password_output.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # Start Adding widgets to the Layout
        layout.addWidget(title)
        layout.addWidget(self.password_input)
        layout.addWidget(button)
        layout.addWidget(self.password_output)

        # Start Adding the Layout to the Main Widget
        widget.setLayout(layout)

        # Initialize the Page
        page = lambda: self.setCentralWidget(widget)

        # Return the page
        return page()
    
    def make_passphrase_Page(self, s):
        """This handles the UI to Generate the Passphrase"""
        # Creating the Content of the Page
        self.password_output = ""
        self.password_info = ""

        # Set Up the Widgets
        widget = QWidget()
        layout = QVBoxLayout()
        title = QLabel("Generate a Passpharse (recommended)")
        self.password_input = QLineEdit()
        self.password_input.setMaxLength(100) # The Maximum number of characters pressed is 100
        self.password_input.setPlaceholderText("Eneter a Phrase") # Prompt
        self.password_input.returnPressed.connect(self.make_passphrase_if_return)
        button = QPushButton("Generate Passphrase")
        button.clicked.connect(self.make_passphrase_if_button)
        self.password_output = QLabel(f"Passphrase: {self.password_info}")
        self.password_output.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # Start Adding widgets to the Layout
        layout.addWidget(title)
        layout.addWidget(self.password_input)
        layout.addWidget(button)
        layout.addWidget(self.password_output)

        # Start Adding the Layout to the Main Widget
        widget.setLayout(layout)

        # Initialize the Page
        page = lambda: self.setCentralWidget(widget)

        # Return the page
        return page()




    """This is where the Code for the backend will Live"""
    def make_password(self, s):
        pass

    def check_password_if_button(self, s):
        pass

    def check_password_if_return(self):
        pass

    def make_passphrase_if_button(self, s):
        print("Passphrase Generated, button pressed")
    
    def make_passphrase_if_return(self):
        print("Passphrase Generated, enter Pressed")
