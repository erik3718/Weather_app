from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen, QColor
from ui.window_ui import Ui_WeatherChercker  # Make sure this is the generated UI file
import sys
from data_acess import weather_api  # Ensure weather_api.py exists and is properly implemented



class MainWindow(QMainWindow, Ui_WeatherChercker):  # Inherit from Ui_WeatherChercker
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Set up the UI
        self.submit_button.clicked.connect(self.handle_input)
        
    
    def handle_input(self):
        # Fetch text from the input field
        input_text = self.input_field.text()
        # Call the weather_api function with the input
        weather_api.geo_quest(input_text)
        self.longitude = weather_api.longitude
        self.latitude = weather_api.latitude
        self.temperature = weather_api.temp_in_c
        self.sky_clearance = weather_api.sky_clearance
        self.sunrise = weather_api.sunrise_time
        self.wind_speed = weather_api.wind_speed_km
        self.zone_of_time = weather_api.zone_of_time
        self.pressure = weather_api.pressure
        self.humidity = weather_api.humidity
        self.feels_like = weather_api.temp_in_c_feels
        self.sunset = weather_api.sunset_time

        # Display the temperature in the temperature_box (QLabel or similar)
        self.skyclearance_box.setText(str(self.sky_clearance))
        self.sunrisetime_box.setText(str(self.sunrise))
        self.sunsettime_box.setText(str(self.sunset))
        self.windspeed_box.setText(str(self.wind_speed))
        self.timezone_box.setText(str(self.zone_of_time))
        self.pressure_box.setText(str(self.pressure))
        self.humidity_box.setText(str(self.humidity))
        self.feelslike_box.setText(str(self.feels_like))
        self.temperature_box.setText(str(self.temperature))
        
        img_width = 6000   # Image width in pixels
        img_height = 3000  # Image height in pixels

        # Define real-world GPS boundaries of the map
        map_long_min, map_long_max = -10.0, 40.0   # Example: Longitude range
        map_lat_max, map_lat_min = 50.0, 30.0      # Example: Latitude range (inverted for pixels)

        # Scale longitude to X position (left to right)
        x = int(round((self.longitude - map_long_min) / (map_long_max - map_long_min) * img_width))

        # Scale latitude to Y position (top to bottom, inverted)
        y = int(round((map_lat_max - self.latitude) / (map_lat_max - map_lat_min) * img_height))
        #image redrawing 
        pixmap = self.WeatherChecker.pixmap()

        if pixmap is not None and not pixmap.isNull():
            # Make a copy to draw on
            pixmap_copy = pixmap.copy()
        
            # Draw marker
            painter = QPainter(pixmap_copy)
            pen = QPen(QColor("red"))
            pen.setWidth(5)  # Adjust thickness
            painter.setPen(pen)

            # Draw a cross marker (+)
            marker_size = 100  # Size of cross
            painter.drawLine(x - marker_size, y, x + marker_size, y)  # Horizontal
            painter.drawLine(x, y - marker_size, x, y + marker_size)  # Vertical
            painter.end()
            # Update QLabel with modified image
            self.WeatherChecker.setPixmap(pixmap_copy)
    


