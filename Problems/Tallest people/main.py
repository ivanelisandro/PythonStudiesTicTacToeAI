def tallest_people(**kwargs):
    max_height = max(kwargs.values())
    tall_people = {key: value for key, value in kwargs.items()
                   if value == max_height}
    sorted_people = sorted(tall_people.items())
    for name, height in sorted_people:
        print(f"{name} : {height}")
