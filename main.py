import random

def get_random_number(length):
    number = ''
    for i in range(length):
        number += str(random.randint(0, 9))
    return number

def feedback(random_number, user_number):
    numbers_in = 0
    numbers_in_places = 0

    if user_number == str(random_number):
        return True
    for i in str(random_number):
        if i in user_number:
            numbers_in += 1
        if i == user_number[str(random_number).index(i)]:
            numbers_in_places += 1
    print(f"Numbers in: {numbers_in}, numbers in places: {numbers_in_places}, random_number: {random_number}")
    return False

while True:
    length = int(input("Գրեք թե քանի նիշանոց թիվ պետքա լինի։ "))
    if length >= 4:
        break
    print("Թիվը առնվազն պետքա 4 նիշ լինի")

random_number = get_random_number(length)
min_attempts = 0
max_attempts = 10

while min_attempts < max_attempts:
    user_input1 = input(f"Գրեք {length} նիշանոց թիվ մնացելա {max_attempts} փորձ։ ")
    if len(user_input1) != length:
        print("Ձեր գրած թիվը չի համապատասխանում գրած նիշանոց թվին")
        continue
    if not user_input1.isdigit():
        print("Միայն թիվ պետք է լինի")
        continue

    max_attempts -= 1

    if feedback(random_number, user_input1):
        print("Շնորհավորում եմ դուք հախտեցիք")
        break
    continue
else:
    print("Ցավում եմ դուք պարտվեցիք")