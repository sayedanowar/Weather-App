from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from tkinter import messagebox
from datetime import datetime
import urllib.request
from tkinter import *
import tkinter as tk
import requests
import pytz

# Check Internet Connection

def is_connected():
  try:
    urllib.request.urlopen("https://www.google.com", timeout=5)
    return True
  except urllib.request.URLError:
    return False

# Window Settings

window = Tk()
window.title("Weather App")
window.geometry('815x450')
window.config(bg='#0370F7')
window.resizable(height=False, width=False)
title_bar_icon = PhotoImage(file='./Images/Ico.png')
window.iconphoto(True, title_bar_icon)

# Fetche weather Info

def getweather(*args):
    
    if is_connected():
        try:
            # City Data

            city = text_box.get()
            geo_locator = Nominatim(user_agent='WeatherApp')
            location = geo_locator.geocode(city)
            timezone = TimezoneFinder()
            result = timezone.timezone_at(lng=location.longitude, lat=location.latitude)
            lon.config(text=("Lon",":", location.longitude))
            lat.config(text=("Lat",":", location.latitude))

            # TimeZone Settings

            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime('%I : %M %p')
            time.config(text=current_time)
            show_time_zone.config(text=result)

            # Collect Weather Data

            api = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=6ab9537c94001a93096b2c7e83aa9df0'
            json_data = requests.get(api).json()
            condition = json_data['weather'][0]['main']
            temp = int(json_data['main']['temp']-273.15)
            wind = json_data['wind']['speed']
            humidity = json_data['main']['humidity']
            weather_condition = str(json_data['weather'][0]['description']).capitalize()
            pressure = json_data['main']['pressure']
            visibility = float(format(json_data['visibility']/1000, '.1f'))

            # Show Temprature Data

            temprature.config(text=(temp,'°C'))
            feeles_like_temp.config(text=(condition, "|", "FEELS", "LIKE", temp,"°C"))

            # Show Weather Data

            wl_blank.config(text=(wind,"m/s"))
            hl_blank.config(text=(humidity,"%"))
            wcl_blank.config(text=weather_condition)
            pl_blank.config(text=(pressure,"hPa"))
            vl_blank.config(text=(visibility,"KM"))

            # Weather In Settings

            weather_in = str(text_box.get()).upper()
            weather_in_lable = Label(window, text=weather_in,font=('Calibri',30,'bold'), background='#0370F7', foreground='White')
            text_box.delete(0, 'end')
            weather_in_lable.place(x=200, y=125)

        except:
            messagebox.showerror("Weather App","City Not Found")
    
    else:
        messagebox.showerror("Weather App","Please Check Your Internet Connection")

# Search Bar Settings

search_bar_image = PhotoImage(file='./Images/SearchBar.png')
sb_image = Label(image=search_bar_image, background='#0370F7')
sb_image.place(x=230, y=10)

# Text Box Settings

text_box = tk.Entry(window, justify='center', width=23, border=0,  font=('Calibri', 14, 'bold'), background='#0D1117', foreground='White')
text_box.place(x=270, y=25)
text_box.focus()

# Weather In Settings

weather_in_text = Label(window, font=('Calibri', 18, 'bold'), background='#0370F7', foreground='#FFFF00')
weather_in_text.config(text='WEATHER IN')
weather_in_text.place(x=200, y=85)

# App Logo Settings

app_logo = PhotoImage(file='./Images/App_Logo.png')
logo = Label(image=app_logo, background='#0370F7')
logo.place(x=35, y=105)

# Bottom Bar Settings

bottom_bar_image = PhotoImage(file='./Images/BottomBar.png')
bb_image = Label(image=bottom_bar_image,background='#0D1117')
bb_image.pack(side='bottom')

# Time & Zone Settings

current_time_text = Label(window, font=('Calibri', 14, 'bold'), background='#0370F7', foreground='#FFFF00')
current_time_text.config(text='CURRENT TIME')
current_time_text.place(x=670, y=10)

time = Label(window, font=('Calibri', 14, 'bold'), background='#0370F7', foreground='White')
time.place(x=670, y=40)

time_zone_text = Label(window, font=('Calibri', 12, 'bold'), background='#0370F7', foreground='#FFFF00')
time_zone_text.config(text='TIMEZONE')
time_zone_text.place(x=10, y=8)

show_time_zone = Label(window, font=('Calibri', 10, 'bold'), background='#0370F7', foreground='White')
show_time_zone.place(x=10, y=35)

gps_coordinates = Label(window, font=('Calibri', 14, 'bold'), background='#0370F7', foreground='#FFFF00')
gps_coordinates.config(text='Coordinates')
gps_coordinates.place(x=670, y=125)

lon = Label(window, font=('Calibri', 10), background='#0370F7', foreground='White')
lon.place(x=670, y=155)

lat = Label(window, font=('Calibri', 10), background='#0370F7', foreground='White')
lat.place(x=670, y=177)

# Temprature Settings

temprature = Label(font=('Calibri', 50, 'bold'), background='#0370F7', foreground="#FF9A00")
temprature.place(x=200, y=180)

feeles_like_temp = Label(font=('Calibri', 14, 'bold'), background='#0370F7', foreground='White')
feeles_like_temp.place(x=405, y=200)

# Forecast Lable Settings

wind_lable = Label(window, text='WIND SPEED', font=('Calibri', 12, 'bold'), background='#0D1117', foreground='#22c55e')
wind_lable.place(x=25, y=315)

humidity_lable = Label(window, text='HUMIDITY', font=('Calibri', 12, 'bold'), background='#0D1117', foreground='#22c55e')
humidity_lable.place(x=175, y=315)

weather_condition_lable = Label(window, text='WEATHER INFO', font=('Calibri', 12, 'bold'), background='#0D1117', foreground='#22c55e')
weather_condition_lable.place(x=320, y=315)

pressure_lable = Label(window, text='PRESSURE', font=('Calibri', 12, 'bold'), background='#0D1117', foreground='#22c55e')
pressure_lable.place(x=525, y=315)

visibility_lable = Label(window, text='VISIBILITY', font=('Calibri', 12, 'bold'), background='#0D1117', foreground='#22c55e')
visibility_lable.place(x=700, y=315)

# Blank Lable Settings

wl_blank = Label(text="...................", font=('Calibri', 12, 'bold'), background='#0D1117',foreground='White')
wl_blank.place(x=28, y=350)

hl_blank = Label(text="...............", font=('Calibri', 12, 'bold'), background='#0D1117',foreground='White')
hl_blank.place(x=178, y=350)

wcl_blank = Label(text="..........................", font=('Calibri', 12, 'bold'), background='#0D1117',foreground='White')
wcl_blank.place(x=320, y=350)

pl_blank = Label(text="................", font=('Calibri', 12, 'bold'), background='#0D1117',foreground='White')
pl_blank.place(x=528, y=350)

vl_blank = Label(text="...............", font=('Calibri', 12, 'bold'), background='#0D1117',foreground='White')
vl_blank.place(x=703, y=350)

# Version Info

version = Label(text="Version : 1.0.5", font=('Calibri', 10), background='#0D1117',foreground='White')
version.place(x=350, y=415)

# Search Icon Settings

search_icon_image = PhotoImage(file='./Images/Search_Icon.png')
si_button = Button(image=search_icon_image, border=0, background='#0D1117', activebackground='#0D1117', cursor='hand2', command=getweather)
si_button.place(x=535, y=18)

# When You Hit Enter Or Click Button Result Is Same

window.bind('<Return>', getweather)

window.mainloop()

