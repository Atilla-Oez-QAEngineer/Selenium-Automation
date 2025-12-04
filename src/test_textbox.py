from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    time.sleep(1)

    driver.find_element(By.ID, "userName").send_keys("Atilla Automation")
    driver.find_element(By.ID, "userEmail").send_keys("test@mail.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Automation Test Adresse")
    driver.find_element(By.ID, "permanentAddress").send_keys("Automation Test Adresse for Permanent")

    # Scrollen bevor wir klicken – verhindert Werbe-Overlays
    submit_btn = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    time.sleep(1)
    submit_btn.click()

    time.sleep(1)

    output = driver.find_element(By.ID, "name").text
    assert "Atilla Automation" in output

    driver.save_screenshot("result.png")
    print("Test erfolgreich – Screenshot erstellt: result.png")

except Exception as e:
    print("Test fehlgeschlagen:", e)

finally:
    time.sleep(2)
    driver.quit()
