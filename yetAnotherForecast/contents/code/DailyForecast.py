class DailyForecast:
    __ns = None
    tmp = None
    tmp_from = None
    tmp_to = None
    weather_type = None
    weather_type_shrt = None
    wind_spd = None
    wind_direction = None
    humidity = None

    def __init__(self, forecastElement, namespace={'n': 'http://weather.yandex.ru/forecast'}, fact=False):
        self.__tag = forecastElement
        self.__ns = namespace
        if not fact:
            data = forecastElement.find("n:day_part[@type='day']", namespaces=namespace)
            temperature = data.find('n:temperature-data', namespaces=namespace)
            self.tmp = self.__extract_val(temperature, 'avg')
            self.tmp_from = self.__extract_val(temperature, 'from')
            self.tmp_to = self.__extract_val(temperature, 'to')
            self.__common_init(data)
        else:
            self.tmp = self.__extract_val(forecastElement, 'temperature')
            self.__common_init(forecastElement)

    def __common_init(self, data):
        self.weather_type = self.__extract_val(data, 'weather_type')
        self.weather_type_shrt = self.__extract_val(data, 'weather_type_short')
        self.wind_spd = self.__extract_val(data, 'wind_speed')
        self.wind_direction = self.__extract_val(data, 'wind_direction')
        self.humidity = self.__extract_val(data, 'humidity')

    def __extract_val(self, element, tag_name):
        return element.find('n:' + tag_name, namespaces=self.__ns).text