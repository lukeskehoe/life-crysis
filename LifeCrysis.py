import datetime


def get_age_in_hours(birthday: object) -> object:

#    datetime_now = datetime.date.today()
    day, month, year = list(map(int, birthday.split("/")))
    birth_date = datetime.date(year, month, day)
    print(f"Birthday is on {birth_date.strftime('%d/%m/%Y')}")

    # returns a timedelta object
    diff = datetime_now - birth_date
#    print('Difference: ', diff)
    #     hours = age*365*24
    hours = diff.total_seconds() / 60 / 60
    print('Age in hours: ', hours)
    return hours


def get_wake_hours(age):

    average_waking_hours = 16/24
    wake_hours = age*average_waking_hours
    return wake_hours


def hours_played_percentage(hours, age_in_hours):

    percentage_of_life = (hours / age_in_hours) * 100
    return percentage_of_life


def waking_hours_played_percentage(hours, age_in_hours):

    wake_hours = get_wake_hours(age_in_hours)
    percentage_of_life = (hours/wake_hours)*100
    return percentage_of_life

def get_hours_since_start(activity_start_date):


    day, month, year = list(map(int, activity_start_date.split("/")))
    start_date = datetime.date(year,month,day)
    diff = datetime_now - start_date
    hours = diff.total_seconds() / 60 / 60
    print('hours since  date: ', hours)

    return hours


datetime_now = datetime.date.today()


#activity_start_date = input('Enter when you started doing the activity dd/mm/yyyy format: ')
activity_start_date = "09/01/2021"
hours_since_start = get_hours_since_start(activity_start_date)
#activity_hours_played = float(input("Enter activity hours: "))
activity_hours_played = 1


percent_since_start = hours_played_percentage(activity_hours_played, hours_since_start)
wake_hours = waking_hours_played_percentage(activity_hours_played, hours_since_start)

print("You have done this activity for :", percent_since_start, "% of since the start date")
print("You have done this activity for :", wake_hours, "% of your waking hours since start date")

dob = input('Enter your birthday in dd/mm/yyyy format: ')
age_hours = get_age_in_hours(dob)


total_life_result = hours_played_percentage(activity_hours_played, age_hours)
wake_hours = waking_hours_played_percentage(activity_hours_played, age_hours)

print("You have done this activity for :", total_life_result, "% of your life")
print("You have done this activity for :", wake_hours, "% of your waking life")


