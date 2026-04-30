import time
import os


def get_time():
    user_input = input("Enter time (seconds or mm:ss): ").strip()

    try:
        if ":" in user_input:
            minutes, seconds = user_input.split(":")
            total_seconds = int(minutes) * 60 + int(seconds)

            if int(seconds) >= 60:
                print("Seconds must be less than 60.")
                return None

            return total_seconds

        if user_input.isdigit():
            return int(user_input)

        print("Please enter a valid time.")
        return None

    except ValueError:
        print("Please enter a valid time.")
        return None


def play_sound():
    os.system('say "Time is up"')


def countdown(total_seconds):
    while total_seconds:
        minutes, seconds = divmod(total_seconds, 60)
        timer = f"{minutes:02d}:{seconds:02d}"

        print(f"\r⏳ {timer}", end="")
        time.sleep(1)

        total_seconds -= 1

    print("\nTime's up!")
    play_sound()


def main():
    total_seconds = get_time()

    if total_seconds is None or total_seconds <= 0:
        print("Countdown cancelled.")
        return

    try:
        countdown(total_seconds)
    except KeyboardInterrupt:
        print("\nCountdown stopped.")


if __name__ == "__main__":
    main()
