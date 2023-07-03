import random

year_numbers = map(str, range(2020, 2030))
month_numbers = map(lambda x: ("%02d" % x), range(13))
day_numbers = map(lambda x: ("%02d" % x), range(29))

for _ in range(100):
    print (random.choice(day_numbers) + "/" + random.choice(month_numbers) + "/" + random.choice(year_numbers))
for _ in range(100):
    print (random.choice(month_numbers) + "/" + random.choice(day_numbers) + "/" + random.choice(year_numbers))
for _ in range(100):
    print (random.choice(year_numbers) + "/" + random.choice(month_numbers) + "/" + random.choice(day_numbers))