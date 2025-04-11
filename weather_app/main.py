import sys
from PySide6.QtWidgets import QApplication
#from ui import MainWindow  # Assuming your UI code is in a file named ui.py
#from ui.window_ui import Ui_WeatherChercker  # Assuming your API code is in a file named weather_api.py
#from ui.window_ui import Ui_WeatherChercker  # Use absolute import
from ui.gui_weather import MainWindow
#from ui.window_ui import Ui_WeatherChercker

def main():
    app = QApplication(sys.argv)  # Create the application
    window = MainWindow()  # Create an instance of your main window
    window.show()  # Show the main window
    sys.exit(app.exec())  # Start the application event loop

if __name__ == "__main__":
    main()