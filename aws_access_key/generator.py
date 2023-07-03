import random
import string

domain = (string.ascii_uppercase * 3) + "0123456789"
for _ in range(200):
    print "".join(random.sample(domain, 20))