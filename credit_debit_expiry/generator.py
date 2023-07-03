import random

month_numbers = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
month_lowercase = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
month_titlecase = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_uppercase = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
years_full = map(str, range(2020, 2030))
years_short = map(str, range(20, 30))

for _ in range(500):
    print (random.choice(month_numbers) + '/' + random.choice(years_short))

domain_months = month_lowercase + month_titlecase + month_uppercase
domain_years = years_short + years_full
for _ in range(50):
    print (random.choice(domain_months) + ' ' + random.choice(domain_years))