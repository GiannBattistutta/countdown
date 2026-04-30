# ⏳ Python Countdown Timer

A simple and interactive countdown timer built with Python.
It allows users to input time in seconds or `mm:ss` format and displays a live countdown in the terminal.

---

## 🚀 Features

* Accepts time in seconds or `mm:ss`
* Real-time countdown display
* Clean `MM:SS` formatting
* Handles invalid input
* Safe interruption with `Ctrl + C`
* Voice alert when finished (macOS)

---

## 📸 Preview

```text
Enter time (seconds or mm:ss): 1:10

⏳ 01:10
⏳ 01:09
⏳ 01:08
...
Time's up!
```

---

## ▶️ How to Run

Make sure you have Python 3 installed.

```bash
python countdown.py
```

or:

```bash
python3 countdown.py
```

---

## 📂 Project Structure

```text
countdown/
├── countdown.py
└── README.md
```

---

## 🧠 Concepts Used

* Functions
* Loops (`while`)
* Conditionals (`if/else`)
* Input validation
* Time manipulation (`time.sleep`)
* String formatting (`f-strings`)
* Error handling

---

## 🛠️ Technologies

* Python 3

---

## ⚠️ Notes

* The voice alert uses `os.system('say')`, which works only on macOS
* On Windows/Linux, this feature can be replaced with other libraries

---

## 📈 Future Improvements

* Add pause/resume feature
* Add custom sound alerts
* Create GUI version (Tkinter)
* Add CLI arguments (`python countdown.py 60`)
* Build web version with Flask

---

## 👨‍💻 Author

Giann Battistutta
GitHub: https://github.com/GiannBattistutta
