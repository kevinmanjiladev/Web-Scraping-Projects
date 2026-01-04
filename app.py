import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

def scrape_alibaba(search):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = f'https://www.alibaba.com/trade/search?SearchText={search}'
    driver.get(url)

    input("Browser open. Press Enter to exit...")

    # Product containers
    products = driver.find_elements(By.CSS_SELECTOR, '.search-card-info__wrapper')

    titles = []
    prices = []
    moqs = []
    countries = []
    suppliers = []
    response_rates = []

    for p in products:

        # TITLE
        try:
            title = p.find_element(By.CSS_SELECTOR, 'h2.search-card-e-title').text
        except:
            title = "N/A"

        # PRICE
        try:
            price = p.find_element(By.CSS_SELECTOR, '.search-card-e-price-main').text
        except:
            price = "N/A"

        # MINIMUM ORDER
        try:
            moq = p.find_element(By.CSS_SELECTOR, '.search-card-m-sale-features__item').text
        except:
            moq = "N/A"

        # SUPPLIER COUNTRY (last <span> inside supplier__year)
        try:
            country = p.find_element(By.CSS_SELECTOR, '.search-card-e-supplier__year span span:last-child').text
        except:
            country = "N/A"

        # SUPPLIER NAME
        try:
            supplier = p.find_element(By.CSS_SELECTOR, '.search-card-e-company').text
        except:
            supplier = "N/A"

        # RESPONSE RATE (this appears only sometimes)
        # try:
        #     response_rate = p.find_element(By.CSS_SELECTOR, '.seb-supplier__response-rate').text
        # except:
        #     response_rate = "N/A"

        # Store all values
        titles.append(title)
        prices.append(price)
        moqs.append(moq)
        countries.append(country)
        suppliers.append(supplier)
        # response_rates.append(response_rate)

    driver.quit()

    df = pd.DataFrame({
        "Title": titles,
        "Price": prices,
        "Min Order": moqs,
        "Supplier Country": countries,
        "Supplier Name": suppliers,
        # "Response Rate": response_rates
    })

    return df






# STREAMLIT UI PART
st.title("Alibaba Scraper")

search = st.text_input("Enter product to search (example: laptop):")

if st.button("Search"):
    st.write("Scraping... Please wait 😀")
    df = scrape_alibaba(search)
    st.dataframe(df)
