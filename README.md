# ⏳ Python Countdown Timer

Simple countdown timer built in Python.
The user inputs a number of seconds, and the program counts down to zero.

## 🚀 Features

* Input validation (only accepts numbers)
* Displays time in **MM:SS format**
* Real-time countdown in terminal
* Clean and simple logic (great for beginners)

## 📂 Project Structure

```
countdown.py
file-organizer.py
database.py
```

## 🧠 How it works

* Takes user input in seconds
* Converts to integer
* Uses a `while` loop to decrement time
* Formats using `divmod()` into minutes and seconds
* Updates output every second with `time.sleep(1)`

## ▶️ How to run

Make sure you have Python installed.

```bash
python countdown.py
```

## 📌 Example

```
Enter the number of seconds for the countdown: 10
00:10
00:09
...
00:00
Time's up!
```

## 🛠️ Technologies

* Python 3

## 🎯 Purpose

This project was built for learning basic Python concepts:

* Loops
* Conditionals
* User input
* Time handling

## 📈 Next Improvements

* Add sound alert when finished
* GUI version (Tkinter)
* Pause/Resume feature

---

Made by Giann 🚀
