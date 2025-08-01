# 🧠 SeleniumProfile – LMS Automation Tools (SLIIT & University of Peradeniya)

Automate repetitive LMS tasks using Python and Selenium.
This tool handles persistent login sessions and speeds up LMS interactions for both SLIIT and University of Peradeniya.

---

## 🔧 Features

### ✅ SLIIT LMS Automation

* Logs in using a **custom Chrome profile** (bypasses forced logouts)
* Navigates directly to **Notices** page
* Extracts the **4 most recent notices** without manual clicks

### ✅ Peradeniya LMS Automation

* Skips repeated logins by reusing authenticated session
* Quickly switches between multiple course pages
* Optimized for speed and low interaction delay

---

## 📆 Tech Stack

* **Python 3.x**
* **Selenium WebDriver**
* **Google Chrome & ChromeDriver**

---

## 🛠️ Setup Instructions

### 1️⃣ Create a Persistent Chrome Profile

This avoids repeated logins.

```bash
# Windows
start chrome --user-data-dir="C:\SeleniumProfile" --profile-directory="Profile1"

# macOS/Linux
google-chrome --user-data-dir="/home/youruser/SeleniumProfile" --profile-directory="Profile1"
```

1. Login to your LMS inside this new Chrome window
2. Close the window (session will be saved)

---

### 2️⃣ Install Python Dependencies

```bash
pip install selenium
```

---

### 3️⃣ Download & Place ChromeDriver

* Download from: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
* Match it with your Chrome version
* Add it to the same folder or PATH

---

## 📚 Usage Examples

### 📘 SLIIT LMS – Extract Latest Notices

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-data-dir=C:\\SeleniumProfile")
options.add_argument("profile-directory=Profile1")

driver = webdriver.Chrome(options=options)
driver.get("https://lms.sliit.lk/mod/forum/view.php?id=XYZ")  # Replace with correct forum ID

notices = driver.find_elements("css selector", ".discussion .topic a")[:4]
for notice in notices:
    print(notice.text)
```

---

### 🏫 Peradeniya LMS – Fast Subject Switching

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("user-data-dir=C:\\SeleniumProfile")
options.add_argument("profile-directory=Profile1")

driver = webdriver.Chrome(options=options)
driver.get("https://lms.pdn.ac.lk")

courses = [
    "https://lms.pdn.ac.lk/course/view.php?id=123",
    "https://lms.pdn.ac.lk/course/view.php?id=456",
    "https://lms.pdn.ac.lk/course/view.php?id=789"
]

for course in courses:
    driver.get(course)
    time.sleep(2)
```

---

## 🔐 Permissions & Best Practices

* Avoid using your **default Chrome profile**
* Keep `ChromeDriver` and `Chrome` updated
* This project **does not store credentials**, only uses Chrome sessions

---

## 📊 Project Impact

* Saved **2–4 hours per week** for \~10–20 students
* Reduced friction and missed LMS notifications
* Increased LMS usage efficiency during busy periods

---

## 📁 Folder Structure

```
SeleniumProfile/
├── sliit_notices.py
├── pera_switcher.py
├── README.md
└── requirements.txt
```

---

## 👨‍💻 Author

**Pamuditha Senanayake**
[LinkedIn](https://www.linkedin.com/in/pamuditha-senanayake-87794357/) • [GitHub](https://github.com/pamuditha-senanayake)

---

## 📜 License

MIT
