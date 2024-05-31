import pandas as pd


def calculate_demographic_data(print_data=True):
    # Reading data with pandas
    df = pd.read_csv('adult.data.csv')
    
    results = {}
    
    # Task 1: How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()
    results['race_count'] = race_count
    
    # Task 2: What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    results['average_age_men'] = round(average_age_men, 1)
    
    # Task 3: What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100
    results['percentage_bachelors'] = round(percentage_bachelors, 1)
    
    # Task 4: What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = (df[advanced_education]['salary'] == '>50K').mean() * 100
    results['higher_education_rich'] = round(higher_education_rich, 1)
    
    # Task 5: What percentage of people without advanced education make more than 50K?
    non_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education_rich = (df[non_advanced_education]['salary'] == '>50K').mean() * 100
    results['lower_education_rich'] = round(lower_education_rich, 1)
    
    # Task 6: What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()
    results['min_work_hours'] = min_work_hours
    
    # Task 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100
    results['rich_percentage'] = round(rich_percentage, 1)
    
    # Task 8: What country has the highest percentage of people that earn >50K and what is that percentage?
    countries_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    countries_all = df['native-country'].value_counts()
    highest_earning_country = (countries_salary / countries_all * 100).idxmax()
    highest_earning_country_percentage = (countries_salary / countries_all * 100).max()
    results['highest_earning_country'] = highest_earning_country
    results['highest_earning_country_percentage'] = round(highest_earning_country_percentage, 1)
    
    # Task 9: Identify the most popular occupation for those who earn >50K in India.
    india_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
    results['top_IN_occupation'] = india_occupation
    
    return results
