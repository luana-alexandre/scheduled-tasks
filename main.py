import smtplib
import pandas
import datetime
import random
import OS

with open("birthdays.csv", "r") as file:
    birthdays = pandas.read_csv(file)

birthdays_dict = {
    (row.month, row.day): row
    for index, row in birthdays.iterrows()
}


today = datetime.date.today()
today_tuple = (today.month, today.day)

birthday_people = birthdays[
    (birthdays["month"] == today.month) &
    (birthdays["day"] == today.day)
]

for index, birthday_person in birthday_people.iterrows():
    birthday_person = birthdays_dict[today_tuple]

    random_number = random.randint(1, 3)

    with open(f"letter_templates/letter_{random_number}.txt") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        print(contents)
        
        MY_EMAIL = os.environ.get("MY_EMAIL")
        MY_PASSWORD = os.environ.get("MY_PASSWORD")

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(MY_EMAIL, MY_PASSWORD)
            email_message =  f"Subject:Happy Birthday!\n\n{contents}"
            smtp.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=email_message)




