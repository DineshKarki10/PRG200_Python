def build_profile(name, **details):
    print("Name:", name)
    for key, value in details.items():
        print(key, ":", value)


build_profile("John", age=25, city="London", job="Teacher")