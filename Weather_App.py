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
window.config(bg='#4070E0')
window.resizable(height=False, width=False)
title_bar_icon = PhotoImage(file='./Images/Icon.png')
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
            weather_in_lable = Label(window, text=weather_in,font=('Arial',26,'bold'), background='#4070E0', foreground='White')
            text_box.delete(0, 'end')
            weather_in_lable.place(x=200, y=120)

        except:
            messagebox.showerror("Weather App","City Not Found")
    
    else:
        messagebox.showerror("Weather App","Please Check Your Internet Connection")

# Search Bar Settings

search_bar_image = PhotoImage(file='./Images/Search_Bar.png')
sb_image = Label(image=search_bar_image, background='#4070E0')
sb_image.place(x=230, y=10)

# Text Box Settings

text_box = tk.Entry(window, justify='center', width=23, border=0,  font=('Arial', 14, 'bold'), background='#202020', foreground='White')
text_box.place(x=270, y=25)
text_box.focus()

# Weather In Settings

weather_in_text = Label(window, font=('Arial', 16, 'bold'), background='#4070E0', foreground='#FFFF00')
weather_in_text.config(text='WEATHER IN')
weather_in_text.place(x=200, y=85)

# App Logo Settings

app_logo = PhotoImage(file='./Images/App_Logo.png')
logo = Label(image=app_logo, background='#4070E0')
logo.place(x=35, y=105)

# Bottom Bar Settings

bottom_bar_image = PhotoImage(file='./Images/Bottom_Bar.png')
bb_image = Label(image=bottom_bar_image,background='#202020')
bb_image.pack(side='bottom')

# Time & Zone Settings

current_time_text = Label(window, font=('Arial', 14, 'bold'), background='#4070E0', foreground='#FFFF00')
current_time_text.config(text='CURRENT TIME')
current_time_text.place(x=593, y=80)

time = Label(window, font=('Arial', 12, 'bold'), background='#4070E0', foreground='White')
time.place(x=625, y=110)

time_zone_text = Label(window, font=('Arial', 14, 'bold'), background='#4070E0', foreground='#FFFF00')
time_zone_text.config(text='TIMEZONE')
time_zone_text.place(x=615, y=10)

show_time_zone = Label(window, font=('Arial', 12, 'bold'), background='#4070E0', foreground='White')
show_time_zone.place(x=615, y=45)

# Temprature Settings

temprature = Label(font=('Arial', 50, 'bold'), background='#4070E0', foreground="#FF9A00")
temprature.place(x=200, y=180)

feeles_like_temp = Label(font=('Arial', 12, 'bold'), background='#4070E0', foreground='White')
feeles_like_temp.place(x=405, y=200)

# Forecast Lable Settings

wind_lable = Label(window, text='WIND SPEED', font=('Arial', 12, 'bold'), background='#202020', foreground='#5cb435')
wind_lable.place(x=20, y=315)

humidity_lable = Label(window, text='HUMIDITY', font=('Arial', 12, 'bold'), background='#202020', foreground='#5cb435')
humidity_lable.place(x=175, y=315)

weather_condition_lable = Label(window, text='WEATHER INFO', font=('Arial', 12, 'bold'), background='#202020', foreground='#5cb435')
weather_condition_lable.place(x=320, y=315)

pressure_lable = Label(window, text='PRESSURE', font=('Arial', 12, 'bold'), background='#202020', foreground='#5cb435')
pressure_lable.place(x=525, y=315)

visibility_lable = Label(window, text='VISIBILITY', font=('Arial', 12, 'bold'), background='#202020', foreground='#5cb435')
visibility_lable.place(x=700, y=315)

# Blank Lable Settings

wl_blank = Label(text="...............", font=('Arial', 12, 'bold'), background='#202020',foreground='White')
wl_blank.place(x=40, y=350)

hl_blank = Label(text=".........", font=('Arial', 12, 'bold'), background='#202020',foreground='White')
hl_blank.place(x=195, y=350)

wcl_blank = Label(text="..............................", font=('Arial', 12, 'bold'), background='#202020',foreground='White')
wcl_blank.place(x=320, y=350)

pl_blank = Label(text="..................", font=('Arial', 12, 'bold'), background='#202020',foreground='White')
pl_blank.place(x=535, y=350)

vl_blank = Label(text="...............", font=('Arial', 12, 'bold'), background='#202020',foreground='White')
vl_blank.place(x=710, y=350)

# Version Info

version = Label(text="Version : 1.0.1", font=('Arial', 8,'bold'), background='#202020',foreground='White')
version.place(x=350, y=415)

# Search Icon Settings

search_icon_image = PhotoImage(file='./Images/Search_Icon.png')
si_button = Button(image=search_icon_image, border=0, background='#202020', activebackground='#202020', cursor='hand2', command=getweather)
si_button.place(x=535, y=18)

# When You Hit Enter Or Click Button Result Is Same

window.bind('<Return>', getweather)

window.mainloop()

