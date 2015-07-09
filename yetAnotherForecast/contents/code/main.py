from PyQt4.QtCore import Qt
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from DailyForecast import DailyForecast
from forecast import Forecast


class YetAnotherForecast(plasmascript.Applet):
    __forecast = None

    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)

    def init(self):
        self.__forecast = Forecast().forecast(Forecast.TODAY)
        self.setHasConfigurationInterface(False)
        self.resize(125, 125)
        self.setAspectRatioMode(Plasma.Square)

    def paintInterface(self, painter, option, rect):
        painter.save()
        painter.setPen(Qt.white)
        painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, u"%s \u2103" % self.__forecast.tmp)
        painter.restore()


def CreateApplet(parent):
    return YetAnotherForecast(parent)