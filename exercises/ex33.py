def while_loop(times, increment):
    i = 0
    numbers  = []

    while i < times:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

print(f"""Here is the result of the while loop: \n
{while_loop(6, 2)}
""")
