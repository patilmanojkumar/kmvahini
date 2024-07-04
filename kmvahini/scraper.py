import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from io import StringIO
from tqdm import tqdm

def scrape_website(months, years, commodities, markets):
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode

    # Create a new browser session with headless Chrome
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://krama.karnataka.gov.in/reports/DateWiseReport.aspx")

        # Initialize an empty list to store DataFrames
        data_frames = []

        # Calculate the total number of iterations for the progress bar
        total_iterations = len(months) * len(years) * len(commodities) * len(markets)

        # Initialize the progress bar
        with tqdm(total=total_iterations, desc="Scraping Data", ncols=100) as pbar:
            # Iterate through the combinations
            for year in years:
                for month in months:
                    for commodity in commodities:
                        for market in markets:
                            # Select values in the dropdown menus
                            month_dropdown = Select(driver.find_element(By.ID, "_ctl0_content5_ddlmonth"))
                            month_dropdown.select_by_visible_text(month)

                            year_dropdown = Select(driver.find_element(By.ID, "_ctl0_content5_ddlyear"))
                            year_dropdown.select_by_visible_text(year)

                            commodity_dropdown = Select(driver.find_element(By.ID, "_ctl0_content5_ddlcommodity"))
                            commodity_dropdown.select_by_visible_text(commodity)

                            market_dropdown = Select(driver.find_element(By.ID, "_ctl0_content5_ddlmarket"))
                            market_dropdown.select_by_visible_text(market)

                            # Click the "View Report" button
                            view_button = driver.find_element(By.ID, "_ctl0_content5_viewreport")
                            view_button.click()
                            time.sleep(2)  # Wait for the page to load

                            # Find the table element by its ID
                            table = driver.find_element(By.ID, "_ctl0_content5_gv")

                            # Get the HTML content of the table
                            table_html = table.get_attribute("outerHTML")

                            # Convert the HTML table to a Pandas DataFrame
                            html_buffer = StringIO(table_html)
                            df = pd.read_html(html_buffer)[0]  # Assuming it's the first (and only) table on the page

                            # Add Commodity as a Column to the fetch dataframe
                            df['Commodity'] = commodity

                            # Append the DataFrame to the list
                            data_frames.append(df)

                            # Update the progress bar
                            pbar.update(1)

                            # Go back to the main page to select the next combination
                            driver.back()

        # Concatenate all DataFrames into a single DataFrame
        final_dataframe = pd.concat(data_frames, ignore_index=True)

        # Additional preprocessing
        # Filter out rows containing 'Total' in any column
        final_dataframe = final_dataframe[~final_dataframe.apply(lambda row: row.astype(str).str.contains('Total').any(), axis=1)].copy()

        # Fill missing values in 'Market' column with the last non-null value
        final_dataframe.loc[:, 'Market'] = final_dataframe['Market'].ffill()

        # Convert the 'Date' column to a datetime object with day-first format
        final_dataframe.loc[:, 'Date'] = pd.to_datetime(final_dataframe['Date'], dayfirst=True)

        # Explicitly convert objects to avoid FutureWarning
        final_dataframe = final_dataframe.infer_objects()

        # Set the 'Date' column as the index
        final_dataframe.set_index('Date', inplace=True)
        return final_dataframe        
    finally:
        driver.quit()

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Run the kmvahini scraper")
    parser.add_argument('--months', nargs='+', default=["JANUARY", "FEBRUARY"], help='List of months to scrape')
    parser.add_argument('--years', nargs='+', default=[str(year) for year in range(2010, 2023)], help='List of years to scrape')
    parser.add_argument('--commodities', nargs='+', default=["BENGALGRAM"], help='List of commodities to scrape')
    parser.add_argument('--markets', nargs='+', default=["AllMarkets"], help='List of markets to scrape')
    args = parser.parse_args()

    scrape_website(args.months, args.years, args.commodities, args.markets)

if __name__ == "__main__":
    main()