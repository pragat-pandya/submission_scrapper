from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def login(username, password, url):
    # Initialize the WebDriver
    driver = webdriver.Chrome()  
    # url = url
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # Open the URL
    driver.get(url)

    # Find the username and password fields and enter your credentials
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "inputPassword")

    username = username
    password = password

    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the login form
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Wait for a bit to ensure the page loads
    time.sleep(2)  
    return driver
    # Now you should be logged in and can proceed with further automation steps as needed

    # Example: You can get the page source after login
    # print(driver.page_source)


if __name__ == '__main__':
    a = login('admin', '@dmin$1234', 'http://172.24.16.139/domjudge/login')

    # Go to teams 
    teams = a.find_element(By.XPATH, "//a[contains(text(), 'Teams')]")
    teams.click()

    # We're at Teams page now-------------------------------------------------------
    
    # CLICK CATEGORIES TO SORT CP MAKEUP ON TOP
    # category_header = a.find_element(By.XPATH, "//th[contains(text(), 'category')]")
    # category_header.click()


    # get all the table rows
    all_table_rows = a.find_elements(By.CSS_SELECTOR,"tbody tr")

    # GET ONLY MAKEUP TABLE ROWS 
    # table_rows = all_table_rows[:142]
    
    # Find all anchor tags within table data elements
    for row in all_table_rows:
        # Find the first anchor tag inside the first table data tag in the row
        first_td_anchor = row.find_element(By.CSS_SELECTOR,"td:first-child a")
        
        # Get the URL of the anchor tag
        link_url = first_td_anchor.get_attribute("href")
        
        # Open the URL in a new tab
        a.execute_script("window.open(arguments[0], '_blank');", link_url)
        a.switch_to.window(a.window_handles[1])

        # ON a student's submission page------------------------------------------

        # Find the first table row
        first_row = a.find_element(By.CSS_SELECTOR,"table.data-table tbody tr:first-child")
        
        
        # Find the first table data element within the table row
        first_table_data = first_row.find_element(By.XPATH, "./td[1]")

        # Find the anchor tag within the first table data element
        anchor_tag = first_table_data.find_element(By.XPATH, "./a")

        # Find the link within the first row
        link = first_row.find_element(By.TAG_NAME,"td").find_element(By.TAG_NAME, "a")
        # Click on the link
        link.click()

       # Find the last span element containing the anchor tag
        last_span = a.find_element(By.CSS_SELECTOR, "div.submission-summary.mb-2 span:last-child")

        
        # DOWNLOAD submission via clicking the last span of parent div
        anchor_tag = last_span.find_element(By.XPATH, "/html/body/div/div/div/div[2]/span[8]/a")
        anchor_tag.click()

        # ON source code page----------------------------------------------------------------------------
        # Perform Download
        anchor_tag = a.find_element(By.LINK_TEXT, "Download")
        anchor_tag.click()
        a.execute_script("window.close();")

        # Switch back to the original tab
        a.switch_to.window(a.window_handles[0])
