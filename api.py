from selenium import webdriver


def get_lenovo():
    with webdriver.Firefox() as browser:
        browser.get(
            'https://webscraper.io/test-sites/e-commerce/allinone/computers/'
            'laptops')
        company_data = browser.find_elements_by_class_name('caption')
        notebooks_lenovo = []
        for data in company_data:
            if 'Lenovo' in data.get_attribute('innerHTML'):
                notebooks_lenovo_list = data.text.split('\n')
                notebooks_lenovo.append({
                    'price': notebooks_lenovo_list[0],
                    'name': notebooks_lenovo_list[1],
                    'description': notebooks_lenovo_list[2]
                })
    return notebooks_lenovo
