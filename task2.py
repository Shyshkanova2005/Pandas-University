import pandas as pd
import matplotlib.pyplot as plt

emp = pd.DataFrame(
    {
        'Name':['Peter Parker', 'Steeve Rogers', 'Ryan Reynolds', 'Sam Smith', 'Kate Johanson', 'Mary Jane', 'Ann Rossman', 'Chris Pratt', 'Scarlett Johanson', 'Sandra Bulok'],
        'Date of Birth': ['1995-08-10', '1987-07-04', '1976-10-23', '1990-03-11', '1985-06-22', '1998-02-14', '1992-11-30', '1989-05-15', '1984-12-01', '1991-01-09'],
        'Salary': [ 1000, 1899, 3000, 2000, 2800,  3200, 2900,  2100, 3120, 2500],
        'Experiance (Year)': [2, 4, 16, 8, 10, 1, 3, 7, 19, 5],
        'Days worked': [21, 12, 20, 19, 17, 5, 21, 21, 14, 18]
    }
)
print(emp)

#нарахована з/п
emp['Accrued salary'] = (emp['Salary']/31*emp['Days worked']).round(2)
print(emp)

#доплата за стаж
emp['Supplement for seniority'] = (emp['Salary']* (0.1/100 * emp['Experiance (Year)'])).round(2)
print(emp)

#Всього нараховано=нарахована з/п + доплата за стаж
emp['Total calculated'] = (emp['Salary'] + emp['Supplement for seniority']).round(2)
print(emp)

#Податок = всього нараховано -19,5%
emp['Tax'] = (emp['Total calculated'] - 0.195).round(2)
print(emp)

#До видачі = всього нараховано-податок
emp['To issued'] = (emp['Total calculated'] - emp['Tax']).round(2)
print(emp)

emp.to_csv('зарплата_розрахунок.csv', index=False)


working_days_in_month = 21
full_month_workers = emp[emp['Days worked'] == working_days_in_month]
avarege_sal = full_month_workers['Salary'].mean()
print("Середня зарплата співробітників, які пропрацювали повний місяць:", avarege_sal)

employee = emp[emp['Experiance (Year)'] > 10]
count_experianced = employee.shape[0]
print("Кількість співробітників зі стажем більше 10 років:", count_experianced)

plt.plot(emp['Salary'])
plt.ylabel('Зарплата')
plt.title('Зарплата співробітників')
plt.show()
