import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

days = ['sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city=input("\nSelect one of the following cities:\nChicago \nNew York City \nWashington \nType your selection here: ").lower()
    while city not in cities:
        print("\nNo data available for this city. \nDouble check your selection and try again!\n")
        city=input("\nYou must select one of these cities:\nChicago \nNew York City \nWashington \nType your selection here: ").lower()
        
    month=input("\nSelect one of the following months or all, to see all months together: \nJanuary \nFebruary \nMarch \nApril \nMay \nJune \nAll\nType your selection here: ").lower()
    while month not in months:
        print("\nNo data available for this month(s). \nDouble check your selection and try again!\n")
        month=input("\nYou must select one of the following months or all, to see all months together: \nJanuary \nFebruary \nMarch \nApril \nMay \nJune \nAll\nType your selection here: ").lower()
    
    day=input("\nSelect one of the following days or all, to see all days together: \nMonday \nTuesday \nWednesday \nThursday \nFriday \nSaturday \nSunday \nAll\nType your selection here: ").lower()
    while day not in days:
        print("\nNo data available for this day(s). \nDouble check your selection and try again!\n")
        day=input("\nYou must select one of the following days or all, to see all days together: \nMonday \nTuesday \nWednesday \nThursday \nFriday \nSaturday \nSunday \nAll\nType your selection here: ").lower()
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    mc_month = df['month'].mode()[0] 
    print("The most common month is:")
    print(mc_month, "\n")
   
    df['day'] = df['Start Time'].dt.weekday_name
    mc_day = df['day'].mode()[0]
    print("The most common day is:")
    print(mc_day, "\n")
    
    
    df['hour'] =df['Start Time'].dt.hour    
    mc_start_hour = df['hour'].mode()[0] 
    print("The most common start hour is:")
    print(mc_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   
       

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

   
    mc_start_station = df['Start Station'].mode()[0] 
    print("The most commonly used start station:")
    print(mc_start_station, "\n")
    
    mc_end_station = df['End Station'].mode()[0] 
    print("The most commonly used end station:")
    print(mc_end_station, "\n")
    
    mc_combination_station = ('From: '+df['Start Station'] + ' To: ' +df['End Station']).mode()[0]
    print("The most common start to end station trip:")
    print(mc_combination_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)      


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time in seconds:")
    print(total_travel_time, "\n")

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("The average travel time in seconds:")
    print(average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:")
    print(user_types, "\n")

    # TO DO: Display counts of gender
    if 'Gender' in list(df):
        gender_types = df['Gender'].value_counts()
        print("Counts of gender types:")
        print(gender_types,"\n")
     
    else:
        print("Counts of gender types:")
        print("Gender information is not tracked for this city.\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in list(df):
        e_birth = df['Birth Year'].min()
        e_birth = int(e_birth)
        print("Earliest year of birth: ")
        print(e_birth,"\n")
        mr_birth = df['Birth Year'].max()
        mr_birth = int(mr_birth)
        print("Most recent year of birth: ")
        print(mr_birth, "\n")
        mc_birth = df['Birth Year'].mode()[0]
        mc_birth = int(mc_birth)
        print("Most common year of birth: ")
        print(mc_birth)
        
    else:
        print("Birth informtaion:")
        print("Date of birth is not tracked for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    rd = input("Would you like to look at the raw data? Enter yes or no.\nType your selection here: ").lower()
    while rd == 'yes':
        print(df.head())
        df = df.tail(-5)
        rd = input("Would you like more raw data? Enter yes or no:\nType your selection here: ")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\nType your selection here: ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
# References
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.title.html
# https://www.geeksforgeeks.org/title-in-python/
# https://www.geeksforgeeks.org/python-list-index/
# https://www.geeksforgeeks.org/python-pandas-series-str-lower-upper-and-title/
# https://www.geeksforgeeks.org/python-pandas-series-str-lower-upper-and-title/
# https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
# https://www.geeksforgeeks.org/title-in-python/ 
