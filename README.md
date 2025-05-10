# AMAZON-SCRAPER-PROJECT

AMAZON-SCRAPER-PROJECT is a Python-based tool designed to extract product information from Amazon. It gathers details such as product titles, prices, ratings, and reviews, facilitating market analysis, price tracking, and competitive research.

## 📌 Features
- Scrapes product details including title, price, rating, and number of reviews.
- Handles pagination to retrieve data from multiple pages.
- Stores extracted data in CSV format for easy analysis.
- Implements request headers to mimic browser behavior and reduce the risk of blocking.

## 🛠️ Technologies Used
- Python 3.x
- Requests
- BeautifulSoup (bs4)
- Pandas

## 🚀 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AMAZON-SCRAPER-PROJECT.git
   cd AMAZON-SCRAPER-PROJECT
   ```
2. Create Virtual Environment(optional but recommended):
   ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required packages:
   ```bash
     pip install -r requirements.txt
   ```
   
## 🧪 Data Analysis & Visualization
- Once the data has been scraped and cleaned, you can generate insightful visualizations to better understand trends like pricing, ratings, and review volumes.
- Perform analysis and generate plot.
  ```bash
     python analysis.py
   ```
- This script will clean and preprocess the scraped data.
- Generate multiple visualizations such as:
    - Price vs Rating scatter plot and
    - (Other plots you have, e.g. Top Reviewed, Rating Distribution, etc.)
- These generated images will be stored in the project directory.

## 📊 Sample Visualization
 ![image](https://github.com/user-attachments/assets/99a7fc8b-fc2d-4e58-a6e6-03768b4a85f0)

  
   
