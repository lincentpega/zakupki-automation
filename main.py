from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import csv

def main():
    driver = webdriver.Chrome('/home/imkrasnyukov/Documents/Development/Python/zakupki-automation/chromedriver')
    links = [
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00772177290520200000',
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00503103361520200006',
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00370254199020200020',
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00772166723420200002',
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00440115306520200000',
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00332840152020200000',
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00540542189520200009',
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00330800449020200000',
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00711614595320200033',
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00780734383420200015',
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00761005287720200000',
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00370211224720200000',
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00370203447920200000',
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00781059572920200000',
        'https://zakupki.gov.ru/epz/rkpo/card/general-information.html?reestr-number=00330579653720200000'

    ]
    

    # cards = driver.find_elements(By.CSS_SELECTOR, 'div.search-registry-entry-block')

    # for card in cards:
    #     a = ActionChains(driver)
    #     right_block = card.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(2)')
    #     a.move_to_element(right_block).perform()
    #     info = right_block.find_element(By.CSS_SELECTOR, '.d-flex.href > a')
    #     a.move_to_element(info).click().perform()
    for link in links:
        driver.get(link)
        block_sections = driver.find_elements(By.CSS_SELECTOR, '.blockInfo__section')

        data = []

        for section in block_sections:
            try:
                title_text = section.find_element(By.CSS_SELECTOR, '.section__title').text
                info_text = section.find_element(By.CSS_SELECTOR, '.section__info').text

                if title_text == 'Фамилия, имя и отчество':
                    data.append(info_text)
                if  title_text == 'Полное наименование':
                    data.append(info_text)
                if title_text == 'ИНН':
                    data.append(info_text)
                if title_text == 'Контактные телефоны':
                    data.append(info_text)
                if title_text == 'Адрес электронной почты':
                    data.append(info_text)
            except NoSuchElementException:
                pass

        print(data)
        with open('base.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)
            
            # driver.execute_script("window.history.go(-1)")
    

if __name__ == '__main__':
    main()
