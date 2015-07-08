import urllib2
import xml.etree.ElementTree as et
import datetime

class Forecast:
    __namespace = 'http://weather.yandex.ru/forecast'
    __nsmap = {'n': __namespace}
    __source = None
    __forecast = None
    __today = None
    __tomorrow = None

    TODAY = 0
    TOMORROW = 1
    DAY_AFTER_TOMORROW = 2

    def __init__(self):
        self.__source = urllib2.urlopen('http://export.yandex.ru/weather-ng/forecasts/28411.xml').read()
        self.__forecast = et.fromstring(self.__source)
        self.__today = self.__forecast.find('n:fact', namespaces=self.__nsmap)
        self.__tomorrow = self.__forecast.find("n:day[@date='%s']" % self.__represent_date(self.TOMORROW), namespaces=self.__nsmap)
        self.__day_after_tomorrow = self.__forecast.find("n:day[@date='%s']" % self.__represent_date(self.DAY_AFTER_TOMORROW), namespaces=self.__nsmap)

    def __day_from_today(self, delta=1):
        return (datetime.date.today() + datetime.timedelta(days=delta)).strftime("%Y-%m-%d")

    def __represent_date(self, day=None):
        representation = None
        if day is None or day == self.TODAY:
            representation = ''
        elif day == self.TOMORROW:
            representation = self.__day_from_today(1)
        elif day == self.DAY_AFTER_TOMORROW:
            representation = self.__day_from_today(2)

        return representation

    def __get_future_date_tag(self, day=TOMORROW):
        tag = self.__tomorrow
        if day == self.DAY_AFTER_TOMORROW:
            tag = self.__day_after_tomorrow

        return tag

    def temperature(self, day):
        # print self.__tomorrow.find('n:sunrise', namespaces=self.__nsmap).text
        # print self.__day_after_tomorrow.find('n:sunrise', namespaces=self.__nsmap).text
        if day == self.TODAY:
            return self.__today.find('n:temperature', namespaces=self.__nsmap).text

        tag = self.__get_future_date_tag(day)
        # find = tag.find("n:hour[@at='7']/n:temperature", namespaces=self.__nsmap)
        return tag.find("n:day_part[@type='day_short']/n:temperature", namespaces=self.__nsmap).text

if __name__ == '__main__':
    forecast = Forecast()
    print forecast.temperature(Forecast.TODAY)
    print forecast.temperature(Forecast.TOMORROW)
    print forecast.temperature(Forecast.DAY_AFTER_TOMORROW)
