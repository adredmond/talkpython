import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'condition, location, tempValue, tempUnit')

def main():
    print_header()

    zipcode = input('What zipcode do you want the weather for (97021)? ')

    # grab html
    html = get_html_from_web(zipcode)

    # parse html
    report = get_weather_from_html(html)

    # display forecast
    print('The temp in {} is {} {} and {}'.format(
        report.location, report.tempValue, report.tempUnit, report.condition
    ))

def print_header():
    print('--------------------------')
    print('    WEATHER APP')
    print('--------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    # CSS classifiers:
    #   Location: #location h1
    #   Condition: #curCond .wx-value
    #   Temperature: #curTemp .wx-value
    #   Temperature Units: #curTemp .wx-unit
    soup = bs4.BeautifulSoup(html, 'html.parser')
    location = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    tempValue = soup.find(id='curTemp').find(class_='wx-value').get_text()
    tempUnit = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    location = cleanup_text(location)
    location = find_city_and_state_from_location(location)
    condition = cleanup_text(condition)
    tempValue = cleanup_text(tempValue)
    tempUnit = cleanup_text(tempUnit)

    return WeatherReport(location=location, condition=condition,
                         tempValue=tempValue, tempUnit=tempUnit)


def cleanup_text(text: str):
    if not text:
        return text
    text = text.strip()
    return text


def find_city_and_state_from_location(location: str):
    parts = location.split('\n')
    return parts[0].strip()


if __name__ == '__main__':
    main()
