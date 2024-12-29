from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
options = UiAutomator2Options().load_capabilities({
    # Specify device and os_version for testing
    "platformName" : "android",
    "platformVersion" : "9.0",
    "deviceName" : "Google Pixel 3"

    # Add your caps here
})

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

# Test case for the BrowserStack sample Android app.
# If you have uploaded your app, update the test case here.
'''
search_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
)
search_element.click()
search_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
)
search_input.send_keys("BrowserStack")
time.sleep(5)
search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
assert (len(search_results) > 0)

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
'''

try:
    
    # Find and click the 'Load URL' button
    getStartedbutton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.elkroom.gamelauncher:id/fragment_container"]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.widget.Button'))
    )
    getStartedbutton.click()
    time.sleep(3)

    '''
    #%% Get attributes
    print(f'Location:{getStartedbutton.location}')
    print(f'Size:{getStartedbutton.size}')

    time.sleep(5)

    #%% System actions
    driver.lock()                       # Lock device
    driver.unlock()                     # Unlock device                    # Shake device
    driver.get_screenshot_as_file("startingPage.png")  # Take screenshot

    # Keyboard
    # driver.hide_keyboard()              # Hide keyboard
    print("Keyboard is shown:",driver.is_keyboard_shown())          # Check if keyboard visible

    # Orientation
    driver.orientation                  # Get orientation
    driver.orientation = "LANDSCAPE"    # Set orientation
    time.sleep(2)
    driver.orientation = "PORTRAIT"    # Set orientation
    time.sleep(2)

    getStartedbutton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.elkroom.gamelauncher:id/fragment_container"]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.widget.Button'))
    )
    getStartedbutton.click()
    time.sleep(5)
    '''

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the driver
    driver.quit()