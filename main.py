from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select 
import time
from datetime import datetime

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5500/src/')

# Test case 
def test_parking(lot_type, start_date, start_time, leave_date, leave_time, result_cost, numTest): 
  # Select 'Valet Parking'
  select = Select(driver.find_element(By.ID, 'park'))
  select.select_by_visible_text(lot_type)

  # Input for entry and leave time and date 
  driver.find_element(By.XPATH, "(//input[@type='date'])[1]").send_keys(start_date)
  driver.find_element(By.XPATH, "(//input[@type='time'])[1]").send_keys(start_time)

  driver.find_element(By.XPATH, "(//input[@type='date'])[2]").send_keys(leave_date)
  driver.find_element(By.XPATH, "(//input[@type='time'])[2]").send_keys(leave_time)
  
  # Click Calculate Button
  driver.find_element(By.CLASS_NAME, 'calculate-button').click()

  time.sleep(0.5)

  # Cost result 
  result = driver.find_element(By.CLASS_NAME, 'TotalCost').text
  assert result == result_cost, f"Test failed! Expected {result_cost} but got {result}"
  print(f"Test case {numTest}: PASS - Result: {result}, {lot_type} - from {start_date} {start_time} to {leave_date} {leave_time} ")


print("")
#  Run Valet Parking Test Cases
print("Valet Parking Test")
test_parking("Valet Parking", "29/08/2024", "9:00", "29/08/2024", "13:00", "$12.00", "1")
test_parking("Valet Parking", "29/08/2024", "12:00", "29/08/2024", "12:00", "$0", "2")
test_parking("Valet Parking", "29/08/2024", "12:00", "31/08/2024", "12:00", "$36.00", "3")
test_parking("Valet Parking", "29/08/2024", "12:00", "29/08/2024", "9:00", "Leaving date and time cannot be before Entry Date and Time", "4")
test_parking("Valet Parking", "29/08/2024", "12:00", "29/08/2024", "12:01", "$12.00", "5")

print("")
print("")

#  Run Hourly Parking Test Cases
print("Hourly Parking Test")
test_parking("Hourly Parking", "29/08/2024", "9:00", "29/08/2024", "12:00", "$6.00", "1")
test_parking("Hourly Parking", "29/08/2024", "12:00", "29/08/2024", "12:00", "$0", "2")
test_parking("Hourly Parking", "29/08/2024", "12:00", "31/08/2024", "12:00", "$24.00", "3")
test_parking("Hourly Parking", "29/08/2024", "12:00", "29/08/2024", "9:00", "Leaving date and time cannot be before Entry Date and Time", "4")
test_parking("Hourly Parking", "29/08/2024", "12:00", "29/08/2024", "12:01", "$2.00", "5")

print("")
print("")

#  Run Garage Parking Test Cases
print("Garage Parking Test")
test_parking("Garage Parking", "29/08/2024", "9:00", "29/08/2024", "12:00", "$6.00", "1")
test_parking("Garage Parking", "29/08/2024", "12:00", "29/08/2024", "12:00", "$0", "2")
test_parking("Garage Parking", "29/08/2024", "12:00", "31/08/2024", "12:00", "$72.00", "3")
test_parking("Garage Parking", "29/08/2024", "12:00", "29/08/2024", "9:00", "Leaving date and time cannot be before Entry Date and Time", "4")
test_parking("Garage Parking", "29/08/2024", "12:00", "29/08/2024", "12:01", "$2.00", "5")

print("")
print("")

#  Run Surface Parking Test Cases
print("Surface Parking Test")
test_parking("Surface Parking", "29/08/2024", "9:00", "29/08/2024", "12:00", "$6.00", "1")
test_parking("Surface Parking", "29/08/2024", "12:00", "29/08/2024", "12:00", "$0", "2")
test_parking("Surface Parking", "29/08/2024", "12:00", "31/08/2024", "12:00", "$60.00", "3")
test_parking("Surface Parking", "29/08/2024", "12:00", "29/08/2024", "9:00", "Leaving date and time cannot be before Entry Date and Time", "4")
test_parking("Surface Parking", "29/08/2024", "12:00", "29/08/2024", "12:01", "$2.00", "5")

print("")
print("")

#  Run Lot Parking Test Cases
print("Lot Parking Test")
test_parking("Lot Parking", "29/08/2024", "9:00", "29/08/2024", "12:00", "$6.00", "1")
test_parking("Lot Parking", "29/08/2024", "12:00", "29/08/2024", "12:00", "$0", "2")
test_parking("Lot Parking", "29/08/2024", "12:00", "31/08/2024", "12:00", "$54.00", "3")
test_parking("Lot Parking", "29/08/2024", "12:00", "29/08/2024", "9:00", "Leaving date and time cannot be before Entry Date and Time", "4")
test_parking("Lot Parking", "29/08/2024", "12:00", "29/08/2024", "12:01", "$2.00", "5")

print("")


# Close 
driver.quit()