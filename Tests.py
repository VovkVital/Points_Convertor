def main():
    des = convert(time=input("What time is it:"))
    if 7 <= des <= 8:
        print("breakfast time")
    elif 12 <= des <= 13:
        print("lunch time")
    elif 18 <= des <= 19:
        print("dinner time")
    else:
        pass


def convert(time):
    hours, minutes = time.split(":")
    converted_minutes = int(minutes)/60
    result = int(hours) + converted_minutes
    print(result)
    return result


if __name__ == "__main__":
    main()