import inflect
p = inflect.engine()

namelist = []

while True:
    try:

        name = input("Name: ")
        namelist.append(name)

    except(EOFError):
        joined_names = (p.join(namelist))
        print("Adieu, adieu, to " + joined_names)
        break

