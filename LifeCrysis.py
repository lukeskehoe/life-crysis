import datetime


def percentage(part, whole):
    return 100 * float(part)/float(whole)


def get_age_in_hours(birthday: object) -> object:

    # datetime_now = datetime.date.today()

    day, month, year = list(map(int, birthday.split("/")))
    birth_date = datetime.date(year, month, day)
#    print(f"Birthday is on {birth_date.strftime('%d/%m/%Y')}")

    # returns a timedelta object
    diff = datetime_now - birth_date
#    print('Difference: ', diff)
    #     hours = age*365*24
    hours = diff.total_seconds() / 60 / 60
#    print('Age in hours: ', hours)
    return hours


def get_hours_since_start(activity_start_date):

    day, month, year = list(map(int, activity_start_date.split("/")))
    start_date = datetime.date(year, month, day)
    diff = datetime_now - start_date
    hours = diff.total_seconds() / 60 / 60

    return hours

def get_wake_hours(age):

    sleep = 8 # TODO will change to average sleep per age demographic

    #  print('(getwakehours())Age in hours: ', age)
    average_waking_hours = (24-sleep)/24
    #  print('waking hours percent: ', average_waking_hours)
    hours_waking = age*average_waking_hours
    #  print('waking of person: ', hours_waking)
    return hours_waking


def life_hours_percentage(hours, age_in_hours):

    percentage_of_life = percentage(hours, age_in_hours)
    return percentage_of_life


def life_waking_hours_percentage(hours, age_in_hours):

    hours_awake = get_wake_hours(age_in_hours)
    percentage_of_life = percentage(hours, hours_awake)
    return percentage_of_life



def adult_life_hours_percentage(hours, age_in_hours):

    adult_hours = 157800.0
    if age_in_hours < adult_hours:
        print("Not an adult yet sweet summer child")
        percentage_of_life = 0.0
    else:
        age_in_hours=age_in_hours-adult_hours
        percentage_of_life = percentage(hours, age_in_hours)
    return percentage_of_life


datetime_now = datetime.date.today()


activity_start_date = input('Enter start date (dd/mm/yyyy): ')
    #   activity_start_date = "21/10/1992"
hours_since_start = get_hours_since_start(activity_start_date)
activity_hours_played = float(input("Enter activity hours: "))
    #   activity_hours_played = 82472.0



dob = input('Enter your birthday (dd/mm/yyyy): ')
    #   dob = "21/10/1992"
age_hours = get_age_in_hours(dob)

percent_since_start = life_hours_percentage(activity_hours_played, hours_since_start)
wake_hours_percentage_since_start = life_waking_hours_percentage(activity_hours_played, hours_since_start)
total_life_percentage = life_hours_percentage(activity_hours_played, age_hours)
wake_hours_percentage = life_waking_hours_percentage(activity_hours_played, age_hours)
adult_life_percentage = adult_life_hours_percentage(activity_hours_played, age_hours)



print("You have done this activity for:", percent_since_start, "% of your time since the start date")
print("                               :", wake_hours_percentage_since_start, "% of your waking hours since start date (assuming average 8hrs sleep)")
print("You have done this activity for:", total_life_percentage, "% of your life")
print("                               :", wake_hours_percentage, "% of your waking life (assuming average 8hrs sleep)")
print("                               :", adult_life_percentage, "% of your adult life")


