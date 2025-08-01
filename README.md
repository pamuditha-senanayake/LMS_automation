# 🧠 SeleniumProfile – LMS Automation Tools (SLIIT & University of Peradeniya)

Automate repetitive LMS tasks using Python and Selenium.  
This tool handles persistent login sessions and speeds up LMS interactions for both SLIIT and University of Peradeniya.

---

## 🔧 Features

### ✅ SLIIT LMS Automation
- Logs in using a **custom Chrome profile** (bypasses forced logouts)
- Navigates directly to **Notices** page
- Extracts the **4 most recent notices** without manual clicks

### ✅ Peradeniya LMS Automation
- Skips repeated logins by reusing authenticated session
- Quickly switches between multiple course pages
- Optimized for speed and low interaction delay

---

## 🧪 Tech Stack
- **Python 3.x**
- **Selenium WebDriver**
- **Google Chrome & ChromeDriver**

---

## 🛠️ Initial Setup

### 1️⃣ Create a Persistent Chrome Profile

This avoids repeated logins.

```bash
# Windows
start chrome --user-data-dir="C:\SeleniumProfile" --profile-directory="Profile1"

# macOS/Linux
google-chrome --user-data-dir="/home/youruser/SeleniumProfile" --profile-directory="Profile1"
