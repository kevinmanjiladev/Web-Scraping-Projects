🛒 Alibaba Product Scraper (Streamlit + Selenium)
--------------------------------------------------
This project is a web scraping application built with Streamlit and Selenium to extract product details from Alibaba.com.
Users can enter a product name (e.g., laptop, smartwatch, camera), and the app automatically opens a browser, scrapes product information, and displays it in a structured table.


🚀 Features
--------------
🔍 Search any product on Alibaba

🖥️ Automated browser scraping using Selenium

📦 Extracts:
    >Product Title
    >Price
    >Minimum Order (MOQ)
    >Supplier Country
    >Supplier Name

📊 Displays results in an interactive Streamlit table

🧹 Handles missing fields gracefully

💾 Data exported as a Pandas DataFrame



🧰 Tech Stack
---------------

| Component       | Technology                           |
| --------------- | ------------------------------------ |
| Web UI          | Streamlit                            |
| Web Scraping    | Selenium                             |
| Browser Driver  | ChromeDriver (via webdriver-manager) |
| Data Handling   | Pandas                               |
| Website Scraped | Alibaba.com                          |


📦 Installation
------------------

1️⃣ Create and activate a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate    # Windows


2️⃣ Install dependencies
pip install -r requirements.txt

(If you don’t have a requirements file, generate it with:
pip freeze > requirements.txt*)

▶️ How to Run
---------------
Run the Streamlit app using:
streamlit run app.py
