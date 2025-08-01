from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Real course links
course_links = {
    "2": ("BOT2092 - Food Chemistry and Technology", "https://scilms.pdn.ac.lk/course/view.php?id=626"),
    "3": ("CHE2282 - Techniques in Organic Chemistry I", "https://scilms.pdn.ac.lk/course/view.php?id=672"),
    "4": ("CSC2032 - Database Management Systems", "https://scilms.pdn.ac.lk/course/view.php?id=707"),
    "5": ("CSC2041 - Programming using DBMS", "https://scilms.pdn.ac.lk/course/view.php?id=708"),
    "6": ("CSC2112 - Introduction to Computer Networks", "https://scilms.pdn.ac.lk/course/view.php?id=709"),
    "7": ("MAT2102 - Computational Mathematics", "https://scilms.pdn.ac.lk/course/view.php?id=835"),
    "8": ("PHY2822 - Medical Physics", "https://scilms.pdn.ac.lk/course/view.php?id=919")
}

# === Step 1: Ask user before launching browser ===

while True:
    print("\nWhere do you want to go?")
    print("1. Just stay on My Courses page")
    for key, (name, _) in course_links.items():
        print(f"{key}. {name}")
    print("0. Exit")

    choice = input("Enter your option number: ").strip()

    if choice == "0":
        print("👋 Exiting...")
        sys.exit()
    elif choice not in ["1", *course_links.keys()]:
        print("❌ Invalid option. Try again.")
        continue
    else:
        break  # Valid choice, proceed to open browser

# === Step 2: Launch browser only now ===

driver_path = "/Users/pamudithasenanayake/Downloads/chromedriver-mac-arm64/chromedriver"
service = Service(driver_path)

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/Users/pamudithasenanayake/Library/Application Support/Google/Chrome/SeleniumProfile")
options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

try:
    print("Opening login page...")
    driver.get("https://scilms.pdn.ac.lk/login/index.php")
    time.sleep(2)

    print("Clicking Science Email login...")
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'login-identityprovider-btn') and contains(., 'Science Email')]")))
    login_btn.click()

    wait.until(EC.url_contains("https://scilms.pdn.ac.lk/"))
    print("✅ Logged in successfully.")

    print("Opening My Courses page...")
    driver.get("https://scilms.pdn.ac.lk/my/courses.php")
    time.sleep(2)
    print("✅ Reached My Courses page.")

    while True:
        if choice == "1":
            print("✅ Staying on My Courses page.")
        else:
            course_name, course_url = course_links[choice]
            print(f"➡️ Redirecting to {course_name} ...")
            driver.get(course_url)
            print("✅ Reached selected course page.")

        # Ask again
        print("\nWhere do you want to go next?")
        print("1. My Courses page")
        for key, (name, _) in course_links.items():
            print(f"{key}. {name}")
        print("0. Exit")

        choice = input("Enter your option number: ").strip()

        if choice == "0":
            print("👋 Exiting...")
            break
        elif choice not in ["1", *course_links.keys()]:
            print("❌ Invalid option. Try again.")
            choice = "1"  # Stay on course page if input is invalid

except Exception as e:
    print("❌ An error occurred:", e)

finally:
    input("\nPress ENTER to close browser...")
    driver.quit()
