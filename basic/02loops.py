
country_names = ["India","Singapore","Malaysia","Thailand","Sri lanka"]
for country in country_names:
    print("country names is {0}".format(country))

##break and continue
country_names = ["India","Singapore","Malaysia","Thailand","Sri lanka"]
for country in country_names:
    if country=="India":
        continue;
    print("country names with out india {0}".format(country))

# while loop
x=0
while x<3:
    print("while loop of 3")
    x+=1
