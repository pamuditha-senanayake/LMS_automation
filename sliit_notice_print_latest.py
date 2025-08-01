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

    # Handle login redirect if necessary
    if "login/index.php" in driver.current_url:
        login_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "SLIIT Login")))
        login_btn.click()
        time.sleep(5)
        driver.get("https://courseweb.sliit.lk/course/view.php?id=25")
        time.sleep(3)

    print("Waiting for main content to load...")
    wait.until(EC.presence_of_element_located((By.ID, "section-1")))

    latest_section = driver.find_element(By.ID, "section-1")
    title_element = latest_section.find_element(By.CLASS_NAME, "sectionname")
    content_element = latest_section.find_element(By.CLASS_NAME, "content")

    title = title_element.text.strip()
    content = content_element.text.strip()

    print("\n📢 Latest Update:")
    print("Title:", title)
    print("Content Preview:", content[:200], "...")  # Only show 1st 200 characters

except Exception as e:
    print("❌ An error occurred:", e)

finally:
    input("\nPress ENTER to close browser...")
    driver.quit()
