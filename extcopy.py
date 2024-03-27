import requests
from bs4 import BeautifulSoup
import psycopg2

def extract_data(data):
    data_list = []
    title_data = data.select_one('h5')
    if title_data:
        data_list.append(title_data.text.strip())
    else:
        data_list.append("N/A")  # Or any placeholder value if title is not found

    author_data = data.select_one('div.col-8.loempia_panel_author')
    if author_data:
        data_list.append(author_data.text.strip())
    else:
        data_list.append(None)  # Or any placeholder value if author is not found

    price_data = data.select_one('div.col-4.loempia_panel_price.text-end')
    if price_data:
        price_text = price_data.text.strip()
        try:
            if price_text.startswith('$'):
                amount = float(price_text[1:])
            else:
                amount = float(price_text)
            data_list.append(amount)
        except ValueError:
            data_list.append(0)
    else:
        data_list.append(0)  # Or any placeholder value if price is not found

    rating_element = data.find('span', class_='loempia_rating_stars')
    if rating_element:
        votes_text = rating_element.find('small').text.strip()
        data_list.append(votes_text)
    else:
        data_list.append(None)  # Or any placeholder value if ratings is not found
    # print(data_list)
    return data_list


def store_in_sql(allData):
    try:
        conn = psycopg2.connect(host='127.0.0.1', dbname='extraction', user='postgres', password='postgres', port=5432)
        cursor = conn.cursor()

        sql = """CREATE TABLE IF NOT EXISTS APPS(
            APP_NAME VARCHAR(255) PRIMARY KEY,
            AUTHOR VARCHAR(255),
            PRICE REAL,
            RATINGS INT
        )"""

        cursor.execute(sql)
        print("Table created successfully........")

        for row in allData:
            # if row[3] == 'N/A':
            #     row[3] = None
            sqld = """
                INSERT INTO APPS (APP_NAME, AUTHOR, PRICE, RATINGS)
                VALUES (%s, %s, %s, %s) 
            """
            cursor.execute(sqld,row)
        print("Data inserted successfully into APPs TABLES")

        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

def main():
    url = 'https://apps.odoo.com/apps'

    r = requests.get(url)
    html_content = r.content
    soup = BeautifulSoup(html_content, "html.parser")

    datas = soup.find_all('div', class_='loempia_app_entry_bottom')
    all_data = []
    for data in datas:
        d = extract_data(data)
        all_data.append(d)
    print(all_data)
    store_in_sql(all_data)

if __name__ == "__main__":
    main()
