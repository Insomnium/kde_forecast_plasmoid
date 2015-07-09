import urllib2
import xml.etree.ElementTree as et
import datetime

from DailyForecast import DailyForecast


class Forecast:
    __nsmap = {'n': 'http://weather.yandex.ru/forecast'}
    __source = None
    __forecast = None
    __today = None
    __tomorrow = None

    TODAY = 0

    def __init__(self):
        self.__update_forecast()

    def __update_forecast(self):
        self.__source = urllib2.urlopen('http://export.yandex.ru/weather-ng/forecasts/28411.xml').read()
        self.__forecast = et.fromstring(self.__source)

    @staticmethod
    def __day_from_today(offset=1):
        return (datetime.date.today() + datetime.timedelta(days=offset)).strftime("%Y-%m-%d")

    def forecast(self, offset):
        criteria = 'n:fact' if offset == self.TODAY else "n:day[@date='%s']" % self.__day_from_today(offset)
        tag = self.__forecast.find(criteria, namespaces=self.__nsmap)
        return DailyForecast(tag, self.__nsmap, offset == self.TODAY)

if __name__ == '__main__':
    forecast = Forecast()
    print forecast.forecast(Forecast.TODAY)
    print forecast.forecast(1)
    print forecast.forecast(2)
