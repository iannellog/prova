import sys
from PySide6.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow): 

    def __init__(self): 
        super().__init__() 


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create the instance of our Window and show it
    window = Window() 
    window.show()

    sys.exit(app.exec_())