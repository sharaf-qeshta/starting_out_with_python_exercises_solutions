def main():
    try:
        file = open("golf.txt")
        i = 0
        for line in file:
            if i == 0:
                print(f"Player Name: {line}")
                i = 1
            else:
                print(f"Player Score: {line}")
                i = 0
    except Exception as error:
        print(error)


main()
