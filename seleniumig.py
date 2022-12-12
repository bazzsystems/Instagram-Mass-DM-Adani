from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

input1 = input("Type 1 to start the script: ")
if input1 == "1":
  print("Starting the script...")
  time.sleep(1)
  print("----------------------------------------------------------------------------------")
  print("Instagram Mass Direct Message Sender Created By @orelmizrahii @orelmizrahiadani") 
  print("----------------------------------------------------------------------------------")
  time.sleep(5)
  print("Opening the Instagram website...")
  driver = webdriver.Chrome('N:\chromedriver.exe')
  driver.get("https://www.instagram.com/")
  time.sleep(1)
  print("Logging in...")
  driver.find_element(By.NAME, 'username').send_keys("USERNAME")
  driver.find_element(By.NAME, 'password').send_keys("PASSWORD")
  time.sleep(1)
  driver.find_element(By.NAME, 'password').send_keys(Keys.ENTER)
  time.sleep(5)
  print("Opening the Instagram Direct Messages page...")
  driver.get("https://www.instagram.com/direct/inbox/")
  time.sleep(2)
  print("Clicking the 'Not Now' button...")
  driver.find_element(By.XPATH, '//button[contains(text(), "Not Now")]').click()
  time.sleep(2)
  print("Clicking the 'Send Message' button...")
  driver.find_element(By.XPATH, '//button[contains(text(), "Send Message")]').click()
  time.sleep(2)
  print("Entering the username...")
  driver.find_element(By.XPATH, '//input[contains(@placeholder, "Search")]').send_keys("USERNAME")
  time.sleep(2)
  print("Clicking the username...")
  driver.find_element(By.XPATH, '//div[contains(text(), "USERNAME")]').click()
  time.sleep(2)
  print("Clicking the 'Next' button...")
  driver.find_element(By.XPATH, '//div[contains(text(), "Next")]').click()
  time.sleep(4)
  print("Typing the message...")
  textarea = driver.find_element(By.XPATH, '//textarea[contains(@placeholder, "Message...")]')
  textarea.send_keys("רוצים לקנות עוקבים? @statbuy.co")
  time.sleep(2)
  print("Clicking the 'Send' button...")
  driver.find_element(By.XPATH, '//div[contains(text(), "Send")]').click()
  time.sleep(2)
  print("Closing the browser...")
  driver.close()
  print("Done!")
else:
  print("Closing the script...")
  time.sleep(1)
  print("Done!")



# Open the text file containing the list of username
with open("usernames.txt", "r") as file: # Read all of the lines in the file (each line contains a username)
  # Read each line in the file (each line contains a username)
  for line in file:
    # Remove leading and trailing whitespace from the username
    username = line.strip()

    YOUR_USERNAME = "USERNAME" # YOUR_USERNAME = "USERNAME"
    YOUR_PASSWORD = "PASSWORD" # YOUR_PASSWORD = "PASSWORD"
    YOUR_MESSAGE = "רוצים לקנות עוקבים? @statbuy.co" # YOUR_MESSAGE = "YOUR MESSAGE"
    # Open the text file containing the list of username
with open("usernames.txt", "r") as file:
  # Read all of the lines in the file (each line contains a username)
  usernames = file.readlines()

  YOUR_USERNAME = "USERNAME"
  YOUR_PASSWORD = "PASSWORD"
  YOUR_MESSAGE = "רוצים לקנות עוקבים? @statbuy.co"

  # Keep sending messages until there are no more usernames
  while usernames:
    # Get the next username from the list
    username = usernames.pop().strip()

    # Open the Instagram website and log in
    driver = webdriver.Chrome('N:\chromedriver.exe') # Change the path to the location of your chromedriver.exe file
    part1 = driver.get("https://www.instagram.com/") # Open the Instagram website
    time.sleep(1) # Wait for the page to load
    part2 = driver.find_element(By.NAME, 'username').send_keys(YOUR_USERNAME) # Enter your username
    part3 = driver.find_element(By.NAME, 'password').send_keys(YOUR_PASSWORD) # Enter your password
    time.sleep(1)
    part4 = driver.find_element(By.NAME, 'password').send_keys(Keys.ENTER) # Press the Enter key to log in
    time.sleep(5)
    part = driver.get("https://www.instagram.com/direct/inbox/") # Open the Instagram Direct Messages page
    time.sleep(2)
    part6 = driver.find_element(By.XPATH, '//button[contains(text(), "Not Now")]').click() # Click the "Not Now" button
    time.sleep(2)
    part7 = driver.find_element(By.XPATH, '//button[contains(text(), "Send Message")]').click() # Click the "Send Message" button
    time.sleep(2)
    part8 = driver.find_element(By.XPATH, '//input[contains(@placeholder, "Search")]').send_keys(username) # Enter the username
    time.sleep(2)
    part9 = driver.find_element(By.XPATH, '//div[contains(text(), "' + username + '")]').click() # Click the username
    time.sleep(2)
    part10 = driver.find_element(By.XPATH, '//div[contains(text(), "Next")]').click() # Click the "Next" button
    time.sleep(4)
    # Find the textarea element where the message is typed
    textarea = driver.find_element(By.XPATH, '//textarea[contains(@placeholder, "Message...")]') # Find the textarea element where the message is typed
    # Type the message into the textarea element
    part11 = textarea.send_keys(YOUR_MESSAGE) # Type the message into the textarea element
    # Send the message
    part12 = textarea.send_keys(Keys.ENTER) # Send the message
    time.sleep(1)
    driver.close() # Close the browser




while True:
  # Open the Instagram website
  driver = webdriver.Chrome('N:\chromedriver.exe')
  part1 = driver.get("https://www.instagram.com/")

  # Check if part1 was successful
  if part1:
    # Continue with the rest of the script
    ...
  else:
    # Restart the script
    continue
