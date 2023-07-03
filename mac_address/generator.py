with open("./prefixes.txt") as prefixes:
    lines = [p.rstrip() for p in prefixes]

mac_addr = ["{}:{}".format(x, y) for x in lines for y in lines]

for a in mac_addr:
    print a