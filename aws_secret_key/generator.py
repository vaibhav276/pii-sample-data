import random
import string

domain = (string.ascii_letters * 2) + "0123456789" + ("/+" * 5)
for _ in range(200):
    print "".join(random.sample(domain, 40))