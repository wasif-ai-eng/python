def student(name, age=18, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

student(
    "Wasif",
    20,
    "C++",
    "Python",
    branch="CSE",
    college="IIIT"
)