# Bikeshare project

#import ipywidgets as widgets
from IPython import display

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the US city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    print()

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city do you want to explore? (Chicago, New york city, Washington or all)\n').lower()
    # print(indata)

    print()
    while city not in ['chicago','new york city','washington']:
        city = input('Lets try again - Which city do you want to explore? (Chicago, New york city, Washington)\n').lower()
        # print(indata)

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month would you like to explore? (January, February, March etc. or all)\n').lower()
    # print(indata)

    print()
    while month not in ['january','february','march','april','may','june','july','august','october','november','december','all']:
        month = input('Lets try again - Which month would you like to explore? (January, February, March etc. or all)\n').lower()        # print(indata)

    # print()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which weekday would you like to explore? (Monday, Tuesday, Wednesday etc. or all)\n').lower()
    # print(indata)

    print()
    while day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
        day = input('Lets try again - Which weekday would you like to explore? (Monday, Tuesday, Wednesday etc. or all)\n').lower()        # print(indata)


    print('-'*40)
    return city, month, day

def load_data(city):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # print('df looks like: ', df.head())

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # print('Start Time looks like: ', df['Start Time'].head())

    df['End Time'] = pd.to_datetime(df['End Time'])
    # print('End Time looks like: ', df['End Time'].head())

    # extract month and day of week from Start Time to create new columns
    # month name column
    df['Month'] = df['Start Time'].dt.month_name().str.lower() # convert month to month name
    # print('month name column looks like: ', df['Month'].head())
    #List unique values in the df['name'] column
    # print('unique months: ', df.Month.unique())

    # week day column
    df['Weekday'] = df['Start Time'].dt.weekday_name.str.lower() # convert starttime to weekday
    # print('weekday column looks like: ', df['Weekday'].head())

    return df

def filter_funct(df, month, day):

    # filter by month if applicable
    # filter by month to create the new dataframe
    # print('I am in filter_funct')

    if month != 'all':
        # print('month name in month filter: ', month)
        df_filt = df[df['Month'] == month]

    # filter by day of week if applicable
    # filter by day to create the new dataframe

    if day != 'all':
        # print('day name in day filter: ', day)
        df_filt = df_filt[df_filt['Weekday'] == day]

    if df_filt.empty == True:
        print('Looks like there were no trips during this period.')
    else:
        print('The city table for {} during {}s looks like: \n'.format(month, day))

    return df_filt

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # pop_start_time = df['Start Time'].mode()[0]
    # print('Most popular start time: ', pop_start_time)
    # popular_hour = df['hour'].mode()[0] - ta bort sen

    # TO DO: display the most common month
    # to print to pop month
    mnth_freq = df['Month'].value_counts().to_dict()
    # print(mnth_freq)
    most_freq_month = list(mnth_freq.keys())[0] # give most pop month
    highest_freq_month = mnth_freq[list(mnth_freq.keys())[0]] # give frequency of the most popular month
    print('The most frequent month is {} with {} bikers.'.format(most_freq_month,highest_freq_month))

    # TO DO: display the most common day of week
    day_freq = df['Weekday'].value_counts().to_dict()
    # print(day_freq)
    most_freq_day = list(day_freq.keys())[0] # give most pop day
    highest_freq_day = day_freq[list(day_freq.keys())[0]] # give frequency of the most popular day
    print('The most frequent weekday is {}s with {} bikers.'.format(most_freq_day,highest_freq_day))

    # TO DO: display the most common start hour
    hour_freq = df['Start Time'].dt.hour.value_counts().to_dict()
    # print(hour_freq)
    most_freq_hour = list(hour_freq.keys())[0] # give most pop day
    highest_freq_hour = hour_freq[list(hour_freq.keys())[0]] # give frequency of the most popular day
    print('The most frequent hour is {} with {} bikers.'.format(most_freq_hour,highest_freq_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_stst_dict = df['Start Station'].value_counts().to_dict()
    # print(pop_stst_dict)
    pop_stst = list(pop_stst_dict.keys())[0] # give most populat start station
    freq_pop_stst = pop_stst_dict[list(pop_stst_dict.keys())[0]] # give frequency of the most popular start station
    print('The most frequent start station is {} with {} bikers.'.format(pop_stst,freq_pop_stst))

    # TO DO: display most commonly used end station
    pop_endst_dict = df['End Station'].value_counts().to_dict()
    # print(pop_endst_dict)
    pop_endst = list(pop_endst_dict.keys())[0] # give most populat start station
    freq_pop_endst = pop_endst_dict[list(pop_endst_dict.keys())[0]] # give frequency of the most popular start station
    print('The most frequent end station is {} with {} bikers.'.format(pop_endst,freq_pop_endst))

    # TO DO: display most frequent combination of start station and end station trip
    df_comb = df['Start Station'] +' to '+ df['End Station']
    # print(comb[0])

    pop_comb_dict = df_comb.value_counts().to_dict()
    # print(pop_comb_dict)
    pop_comb = list(pop_comb_dict.keys())[0] # give most populat start station
    freq_pop_comb = pop_comb_dict[list(pop_comb_dict.keys())[0]] # give frequency of the most popular start station
    print('The most frequent station combination is from {} with {} bikers.'.format(pop_comb,freq_pop_comb))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    summa = df['Trip Duration'].sum()/60/60/24/365 # years
    print('Total travel time is {} years.'.format(round(summa,1)))

    # TO DO: display mean travel time
    medel = df['Trip Duration'].mean()/60 # min
    print('Mean travel time is {} min.'.format(int(round(medel,1))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertype_data = df['User Type'].value_counts()
    print('User types: \n', usertype_data)

    if city in ['chicago', 'new york city']:
    # TO DO: Display counts of gender
        print()
        gender_data = df['Gender'].value_counts()
        print('Gender data: \n', gender_data)

    # TO DO: Display earliest, most recent, and most common year of birth
    # chicago and new york city contains gender and birth date
    # TO DO: Display earliest, most recent, and most common year of birth
        birth_min = df['Birth Year'].min()
        print('Min birth year in the database: ', int(birth_min))
        birth_mode = df['Birth Year'].mode()
        print('Most common birth year in the database: ', int(birth_mode))
        birth_max = df['Birth Year'].max()
        print('Max birth year in the database: ', int(birth_max))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters() # user input
        #city, month, day = 'washington', 'june', 'tuesday'
        df = load_data(city) # loading data & compute month and day column
        #display.display(df.head())
        df_filt = filter_funct(df, month, day) # filter citydata
        display.display(df_filt.head())


        time_stats(df) # pop_time_stats
        station_stats(df) # station_stats
        trip_duration_stats(df) # trip_duration_stats
        user_stats(df, city) #user_stats

        #restart = 'no'
        startover = input('\nWould you like to restart? Enter yes or no.\n')
        if startover.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
