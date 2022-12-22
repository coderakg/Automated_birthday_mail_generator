import pandas
import random
import smtplib
import datetime as dt

data = pandas.read_csv("birthdays.csv")
# print(data)
    
current_time = dt.datetime.now()
today = (current_time.month,current_time.day)
print(today)

bdays = {(data_row["month"],data_row["day"]) : data_row for (index,data_row) in data.iterrows()}
print(bdays)

my_email = "youremail@gmail.com"
passw = "userspassword"

if today in bdays:
    birthday_person = bdays[today]
    print("yes")
    file_path = f"letter_templates\letter_{random.randint(1,3)}.txt"
    with open(file_path) as text:
        content = text.read()
        mail_content = content.replace("[NAME]",birthday_person["name"])
        print(mail_content )
    with smtplib.SMTP("smtp.gmail.com",timeout=200) as connection:
        connection.starttls()
        connection.login(user=my_email ,
password = passw)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],msg=f"Subject: Wish!! \n\n {mail_content} " )
else:
    print("Nothing")


