def main():

    current_time = input("What time is it? ")
    time_in_hours = convert(current_time)
    if 7.0 <= time_in_hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_in_hours <= 13.0:
        print("lunch time")
    elif 18.0 <= time_in_hours <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    h = int(hours)
    m = int(minutes)
    return h + (m / 60)

if __name__ == "__main__":
    main()
