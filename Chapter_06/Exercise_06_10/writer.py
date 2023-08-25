def main():
    try:
        file = open("golf.txt", "w")
        for i in range(10):
            player_name = input(f"enter player{i + 1} name: ")
            player_score = input(f"enter player{i + 1} scores: ")
            file.write(player_name + "\n")
            file.write(player_score + "\n")
    except Exception as error:
        print(error)


main()
