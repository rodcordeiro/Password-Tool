# Import Stuff
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import backend as back
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
        self.backend = back.AppTools()

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

        # Generate the Check Action Page
        stored_password_action = QAction("My Passwords", self)
        stored_password_action.setStatusTip("Look At My Passwords")

        # Generate the Settings Action 
        settings_action = QAction("Settings", self)
        settings_action.setStatusTip("App Settings")
         
        # Generate the store password page
        stored_password_action.triggered.connect(self.stored_password_Page)
        toolbar.addAction(stored_password_action)

        # Connect the Click to the Page
        settings_action.triggered.connect(self.settings_Page)
        toolbar.addAction(settings_action)
        
        # Set the Default Page (when the user opens the app)
        widget = QWidget()
        layout = QVBoxLayout()
        title = QLabel("<h1>Welcome to the</h1><h1>Password-Tool</h1>")
        title.setAlignment(Qt.AlignCenter)
        password_open = QPushButton("Get Started")
        password_open.clicked.connect(self.make_passwd_Page)
        layout.addWidget(password_open)
        layout.addWidget(title)
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def make_passwd_Page(self, s):
        """This handles the UI to make the password"""

        # Set default stuff
        self.password_output = ""
        self.password_info = ""

        # Create the Content of the page
        widget = QWidget()
        bottom = QHBoxLayout()
        layout = QVBoxLayout()
        title = QLabel("Password Maker")
        button = QPushButton("Generate A Password")
        button.clicked.connect(self.make_password)
        self.password_output = QLabel(f"Password: {self.password_info}")
        self.password_output.setTextInteractionFlags(Qt.TextSelectableByMouse)
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_password)

        # Start adding widgets to the Layout Engine
        layout.addWidget(title)
        layout.addWidget(button)
        bottom.addWidget(self.password_output)
        bottom.addWidget(save_button)
        layout.addLayout(bottom)

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
        bottom = QHBoxLayout()
        title = QLabel("Generate a Passphrase (recommended)")
        self.password_input = QLineEdit()
        self.password_input.setMaxLength(100) # The Maximum number of characters pressed is 100
        self.password_input.setPlaceholderText("Enter a Phrase") # Prompt
        self.password_input.returnPressed.connect(self.make_passphrase_if_return)
        button = QPushButton("Generate Passphrase")
        button.clicked.connect(self.make_passphrase_if_button)
        self.password_output = QLabel(f"Passphrase: {self.password_info}")
        self.password_output.setTextInteractionFlags(Qt.TextSelectableByMouse)
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_password)

        # Start Adding widgets to the Layout
        layout.addWidget(title)
        layout.addWidget(self.password_input)
        layout.addWidget(button)
        bottom.addWidget(self.password_output)
        bottom.addWidget(save_button)
        layout.addLayout(bottom)

        # Start Adding the Layout to the Main Widget
        widget.setLayout(layout)

        # Initialize the Page
        page = lambda: self.setCentralWidget(widget)

        # Return the page
        return page()
    
    def stored_password_Page(self, s):
        """This is where the stored Passwords Are Shown"""
        scroll = QScrollArea()
        widget = QWidget()
        layout = QVBoxLayout()
        display = []
        title = QLabel("Stored Passwords").setAlignment(Qt.AlignCenter)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.setWidgetResizable(True)
        if self.backend.get_file_content("passwords.passwd") == False:
            layout.addWidget(QLabel("No Stored Passwords :("))
        else:
            for passkey in self.backend.get_file_content("passwords.passwd"):
                if passkey == "":
                    pass
                else:
                    object = QLabel(passkey)
                    object.setTextInteractionFlags(Qt.TextSelectableByMouse)
                    object.setAlignment(Qt.AlignCenter)
                    object.setAutoFillBackground(True)
                    object.setStyleSheet("QLabel {background-color: gray; color: white}")
                    display.append(object)

            for label in display:
                layout.addWidget(label)
            
        layout.addWidget(title)
        widget.setLayout(layout)
        scroll.setWidget(widget)
        page = lambda: self.setCentralWidget(scroll)
        return page()
    
    def settings_Page(self, s):
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.setWidgetResizable(True)
        widget = QWidget()
        layout = QVBoxLayout()
        title = QLabel("Settings")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        widget.setLayout(layout)
        scroll.setWidget(widget)
        page = lambda: self.setCentralWidget(scroll)
        return page()

    """This is where the Holders for the backend will Live"""
    def make_password(self, s):
        pass

    def check_password_if_button(self, s):
        pass

    def check_password_if_return(self):
        pass

    def make_passphrase_if_button(self, s):
        pass
    
    def make_passphrase_if_return(self):
        pass

    def save_password(self, s):
        print("Password Saved")
