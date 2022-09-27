player01 = int(input())
player02 = int(input())

command = input()



while command != "End":
    curPlayer = command

    if curPlayer == "one":
        player02 -= 1
        if player02 <1:
            print(f"Player two is out of eggs. Player one has {player01} eggs left.")
            break
    elif curPlayer == "two":
        player01 -= 1
        if player01 <1:
            print(f"Player one is out of eggs. Player two has {player02} eggs left.")
            break
    command=input()


if command == "End":
    print(f"Player one has {player01} eggs left.")
    print(f"Player two has {player02} eggs left.")

