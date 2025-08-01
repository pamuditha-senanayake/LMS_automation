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
    time.sleep(2)

    # Handle login redirect if necessary
    if "login/index.php" in driver.current_url:
        login_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "SLIIT Login")))
        login_btn.click()
        time.sleep(3)
        driver.get("https://courseweb.sliit.lk/course/view.php?id=25")
        time.sleep(2)

    print("Waiting for notice sections to load...")
    for i in range(1, 5):  # sections 1 to 4 (skip section-0)
        section_id = f"section-{i}"
        wait.until(EC.presence_of_element_located((By.ID, section_id)))
        section = driver.find_element(By.ID, section_id)

        title = section.find_element(By.CLASS_NAME, "sectionname").text.strip()
        content = section.find_element(By.CLASS_NAME, "content").text.strip()

        print(f"\n📢 Notice {i}:")
        print("Title:", title)
        print("Content Preview:", content[:250], "...")  # Limit to 250 chars for preview

except Exception as e:
    print("❌ An error occurred:", e)

finally:
    input("\nPress ENTER to close browser...")
    driver.quit()

