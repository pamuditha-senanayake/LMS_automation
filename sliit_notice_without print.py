
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = "/Users/pamudithasenanayake/Downloads/chromedriver-mac-arm64/chromedriver"
service = Service(driver_path)

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/Users/pamudithasenanayake/Library/Application Support/Google/Chrome/SeleniumProfile")
options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

try:
    print("Opening notice page...")
    driver.get("https://courseweb.sliit.lk/course/view.php?id=25")
    time.sleep(3)

    current_url = driver.current_url
    print(f"Current URL after loading: {current_url}")

    if "login/index.php" in current_url:
        print("Detected redirect to login page.")
        try:
            login_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "SLIIT Login")))
            print("Clicking 'SLIIT Login' button...")
            login_btn.click()
            time.sleep(5)
        except Exception as e:
            print("SLIIT Login button not clickable or not found:", e)

        # May be redirected again to login page with "already logged in" notice
        print("Navigating back to notice page...")
        driver.get("https://courseweb.sliit.lk/course/view.php?id=25")
        time.sleep(3)
    else:
        print("No login redirect — probably already logged in.")

    print("Fetching course sections...")
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "sectionname")))
    sections = driver.find_elements(By.CLASS_NAME, "sectionname")

    print("\n📢 Latest course sections:\n")
    for sec in sections:
        text = sec.text.strip()
        if text:
            print("-", text)

except Exception as e:
    print("❌ An error occurred:", e)

finally:
    input("\nPress ENTER to close browser...")
    driver.quit()
