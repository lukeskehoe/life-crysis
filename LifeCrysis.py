import datetime


def get_age_in_hours(birthday: object) -> object:

#    datetime_now = datetime.date.today()
    day, month, year = list(map(int, birthday.split("/")))
    birth_date = datetime.date(year, month, day)
#    print(f"Birthday is on {birth_date.strftime('%d/%m/%Y')}")

    # returns a timedelta object
    diff = datetime_now - birth_date
#    print('Difference: ', diff)
    #     hours = age*365*24
    hours = diff.total_seconds() / 60 / 60
    print('Age in hours: ', hours)
    return hours


def get_wake_hours(age):

    sleep = 8 # TODO will change to average sleep per age demographic
    average_waking_hours = (24-sleep)/24
    hours_waking = age*average_waking_hours
    return hours_waking


def life_hours_percentage(hours, age_in_hours):

    percentage_of_life = (hours / age_in_hours) * 100
    return percentage_of_life


def life_waking_hours_percentage(hours, age_in_hours):

    hours_awake = get_wake_hours(age_in_hours)
    percentage_of_life = (hours/hours_awake)*100
    return percentage_of_life

def get_hours_since_start(activity_start_date):

    day, month, year = list(map(int, activity_start_date.split("/")))
    start_date = datetime.date(year,month,day)
    diff = datetime_now - start_date
    hours = diff.total_seconds() / 60 / 60
#    print('Hours since date: ', hours)

    return hours


datetime_now = datetime.date.today()


activity_start_date = input('Enter when you started doing the activity dd/mm/yyyy format: ')
#activity_start_date = "09/01/2021"
hours_since_start = get_hours_since_start(activity_start_date)
activity_hours_played = float(input("Enter activity hours: "))
#activity_hours_played = 1


percent_since_start = life_hours_percentage(activity_hours_played, hours_since_start)
wake_hours = life_waking_hours_percentage(activity_hours_played, hours_since_start)

print("You have done this activity for :", percent_since_start, "% of since the start date")
print("You have done this activity for :", wake_hours, "% of your waking hours since start date")

dob = input('Enter your birthday in dd/mm/yyyy format: ')
age_hours = get_age_in_hours(dob)


total_life_result = life_hours_percentage(activity_hours_played, age_hours)
wake_hours = life_waking_hours_percentage(activity_hours_played, age_hours)

print("You have done this activity for :", total_life_result, "% of your life")
print("You have done this activity for :", wake_hours, "% of your waking life")


