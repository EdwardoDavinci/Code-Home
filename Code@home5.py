from guizero import App, TextBox, PushButton, Text, info, TitleBox, CheckBox, Box
from datetime import date,datetime
import time
today=date.today()
d1 = today.strftime("%d/%m/%Y")
print(time.time())
epoch_time = datetime(2021, 6, 9, 2, 0).timestamp()

print("Today's date:", d1)
app=App(title="Age Calculator")
box=Box(app,width="fill", border=False)
box.bg=(250,249,246)
name_label=Text(box, text="Name: ", align="left")
name=TextBox(box, width="fill", align="top")

day_label=Text(box, text="Day: ", align="left")
day=TextBox(box, width="fill", align="top")
day=int(day.value)
month_label=Text(box, text="Month: ", align="left")
month=TextBox(box, width="fill", align="top")
month=int(month.value)
year_label=Text(box, text="Year: ", align="left")
year=TextBox(box, width="fill", align="top")
year=int(year.value)


app.display()