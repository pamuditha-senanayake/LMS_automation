from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
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

    # Click the "Science Email" login button (Google OAuth)
    print("Clicking Science Email login...")
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'login-identityprovider-btn') and contains(., 'Science Email')]")))
    login_btn.click()

    # Wait for redirect to home page
    wait.until(EC.url_contains("https://scilms.pdn.ac.lk/"))
    print("Logged in successfully.")

    # Navigate to My Courses page
    print("Opening My Courses page...")
    driver.get("https://scilms.pdn.ac.lk/my/courses.php")
    time.sleep(2)

    print("✅ Reached My Courses page.")

except Exception as e:
    print("❌ An error occurred:", e)

finally:
    input("\nPress ENTER to close browser...")
    driver.quit()
