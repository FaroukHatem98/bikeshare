import time
import pandas as pd
import numpy as np
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def city_det():
    """ Asks user to specify a city.
    Takes no arg 
    Returns :
        (str) city - name of the city to analyze
    """
    while True:

        city = input(
            'please choose a city from(chicago, new york city, washington) \n')
        city = city.lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('='*40)
            print('the city could be just one of(chicago, new york city, washington) \n ')

    return city


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Takes no arg 
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    def day_det():
        """Asks user to specify a day.
           Takes no arg
           Returns:
            (str) day - name of the day of week to filter by
        """
        while True:
            print(f'you choosed {filter_type} as your filter')
            days = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
            day = input(
                'please choose day from Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday\n')
            day = day.title()
            if day in days:
                print(f'you choosed {day}')
                break
            else:
                print('='*40)
                print('Make sure to choose one of the next days \n')
        return day

    def month_det():
        """Asks user to specify a month.
           Takes no arg
           Returns:
            (str) month - name of the month to filter by
        """
        while True:
            print(f'you choosed {filter_type} as your filter')
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            month = input(
                'please choose monthe from January, February, March, April, May, or June\n')
            month = month.title()
            if month in months:
                print(f'you choosed {month}')
                break
            else:
                print('='*40)
                print('Make sure to choose one of the next six months\n ')
        return month
    print('Hello! Let\'s explore some US bikeshare data!')

    city = city_det()

    while True:
        day = 'All'
        month = 'All'
        filter_type = input(
            'Would you like to filter the data by month, day,both, or not at all? for no time filter type \'none\'\n')
        filter_type = filter_type.lower()
        if filter_type == 'month':

            month = month_det()
            break
        elif filter_type == 'day':

            day = day_det()
            break
        elif filter_type == 'both':
            month = month_det()
            day = day_det()
            break
        elif filter_type == 'none':
            print(f'you choosed {filter_type} as your filter')
            break
        else:
            print('='*40)
            print('Make sure choose one of the next four filters \n')
    print('-'*40)
    print('calculating your statistics please wait')
    return city, month, day, filter_type


def load_data(city, month, day):
    """load a new data frame after applying the filter
        Takes city, month, day as args 
        Returns
        new data frame 
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['start_hour'] = df['Start Time'].dt.hour
    df['start_to_end'] = df['Start Station'] + ' to ' + df['End Station']
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'All':
        days = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = day.title()
        day = days.index(day)
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df, filter_type):
    """Displays statistics on the most frequent times of travel."""
    def common_month():
        popular_month = df['month'].mode()[0]
        print('Most Frequent month:', popular_month)
        return

    def common_day():
        popular_dayn = df['day_of_week'].mode()[0]
        days = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
        popular_day = days[popular_dayn]
        print('Most Frequent day:', popular_day)
        return

    def common_hour():
        popular_start_hour = df['start_hour'].mode()[0]
        print('Most Frequent Start Hour:', popular_start_hour)
        return
    if filter_type == 'month':
        common_day()
        common_hour()
    elif filter_type == 'day':
        common_hour()
        common_month()
    elif filter_type == 'both':
        common_hour()
    else:
        common_hour()
        common_month()
        common_day()
    print('-'*40)
    return


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    most_commonly_used_sart_station = df['Start Station'].mode()[0]
    print('the most commonly used start station: ',
          most_commonly_used_sart_station)
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('the most commonly used end station :',
          most_commonly_used_end_station)
    most_frequent_combination_trip = df['start_to_end'].mode()[0]
    print('the most commonly trip:\n', most_frequent_combination_trip)
    print('-'*40)
    return


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    sum_value = df['Trip Duration'].sum()
    print('the total travel time:', sum_value)
    av_value = df['Trip Duration'].mean()
    print('the mean travel time:', av_value)
    print('-'*40)
    return


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')

    user_types = df['User Type'].value_counts()
    print('the number of subscriber users :', user_types['Subscriber'])
    print('the number of customer users :', user_types['Customer'])
    Gender_Birth_Year_cities = ['chicago', 'new york city']
    if city in Gender_Birth_Year_cities:
        user_Gender = df['Gender'].value_counts()
        print('the number of male users :', user_Gender['Male'])
        print('the number of female users :', user_Gender['Female'])
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('the most common year of birth:', int(most_common_birth_year))
        most_earliest_birth_year = df['Birth Year'].min()
        print('the earliest year of birth:', int(most_earliest_birth_year))
        most_recent_birth_year = df['Birth Year'].max()
        print('the recent year of birth:', int(most_recent_birth_year))
    print('-'*40)
    return


def raw_data(city):
    """printing raw data to the user five rows at a time """
    df1 = pd.read_csv(CITY_DATA[city])
    decision = input(
        'do you want to sea 5 lines of raw data ? type yes or no\n')
    s = 0
    e = 6
    while True:
        decision = decision.lower()
        if decision == 'yes':
            while decision == 'yes':
                a = df1[s:e]
                print(a)
                print('-'*40)
                s = e
                e += 5
                decision = input(
                    'do you want to sea more 5 lines of raw data ? type yes or no \n')
                decision = decision.lower()
        elif decision == 'no':
            break
        else:
            decision = input(
                'it seams you enterd wrong word please type yes or no \n')


def main():
    while True:

        city, month, day, filter_type = get_filters()
        df = load_data(city, month, day)
        time_stats(df, filter_type)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
