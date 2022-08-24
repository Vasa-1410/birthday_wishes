import smtplib
import datetime as dt
import random
import pandas

def send_mail(thought):
    password = "efcizpsocbrpmmfl"
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user="vasanthmuni14@gmail.com", password=password)
        connection.sendmail(from_addr="vasanthmuni14@gmail.com",
                            to_addrs="munivasanth10@gmail.com",
                            msg=f"Subject:Thought of the Day\n\n{thought}")

def send_bd(add,message):
    password = "efcizpsocbrpmmfl"
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user="vasanthmuni14@gmail.com", password=password)
        connection.sendmail(from_addr="vasanthmuni14@gmail.com",
                            to_addrs=add,
                            msg=f"Subject:Birthday Wishes\n\n{message}")
#
#
now = dt.datetime.now()
day = now.weekday()
if day==0:
    with open("vasa1410/birthday_wishes/quotes.txt",mode="r") as quotes:
        quote = quotes.readlines()
        quote_list =[line.strip() for line in quote]
        thought = random.choice(quote_list)
        send_mail(thought)

day = now.day
month_now = now.month

data = pandas.read_csv("vasa-1410/birthday_wishes/wishes.csv")
for index,row in data.iterrows():
    if row["date"]==day and row["month"] == month_now:
        name_ = row["name"]
        address = row["mail"]
        with open("vasa-1410/birthday_wishes/letter_1.txt","r") as letter:
            content = letter.read()
            new_letter=content.replace("[name]",name_)
        send_bd(address,new_letter)

