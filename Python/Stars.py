def star(list):
    for x in list:
        print "*" * x


star([4,6,1,3,5,7,25])

def star2(list):
    for x in list:
        if type(x) is int:
            print "*" * x
        elif type(x) is str:
            print x[0].lower() * len(x);
star2([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
