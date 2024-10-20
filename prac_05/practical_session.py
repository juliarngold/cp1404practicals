name_to_age = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}
# for name, age in name_to_age.items():
#     print(f"{name:12}: {age:3}")

from operator import itemgetter

names_width = max((len(name) for name in name_to_age.keys()))
age_width = max((len(str(age)) for age in name_to_age.values()))
for name, age in sorted(name_to_age.items(), key= itemgetter(1), reverse= True):
    print(f"{name:{names_width}}: {age:{age_width}}")


name_to_length = {}
names = ['Anna', 'Max', 'Steve', 'Maddy']
length = [80, 10, 2, 4]
def main():
    name_to_length=




main()