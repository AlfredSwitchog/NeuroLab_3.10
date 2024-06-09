
# Initialize WebDriver
driver = webdriver.Chrome()  # Assuming you are using Chrome. You may need to download chromedriver.

# Define the URL of the webpage
url = 'https://example.com'

# Open the webpage
driver.get(url)

# Loop through each postcode
for postcode in postcodes_df['Postcode']:
    # Find the search box and enter the postcode
    search_box = driver.find_element_by_id('search-box')  # Replace 'search-box' with the actual ID of the search box
    search_box.clear()
    search_box.send_keys(postcode)
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load (you may need to adjust the wait time)
    time.sleep(5)

    # Get the search results
    search_results = driver.find_elements_by_class_name(
        'search-result')  # Replace 'search-result' with the actual class name of the search results

    # Write the search results to a CSV file
    with open('search_results.csv', 'a') as file:
        file.write(f'Postcode: {postcode}\n')
        for result in search_results:
            file.write(result.text + '\n')
        file.write('\n')

# Close the browser
driver.quit()
