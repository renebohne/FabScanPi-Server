__author__ = "Mario Lukas"
__copyright__ = "Copyright 2015"
__license__ = "AGPL"
__maintainer__ = "Mario Lukas"
__email__ = "info@mariolukas.de"

import time
import logging
import sys
from WebServer import WebServer

from fabscan.server.websockets import FSWebSocketServer
from fabscan.FSScanner import FSScanner
from fabscan.FSEvents import FSEventManager, FSEventManagerInterface
from fabscan.FSConfig import Config
from fabscan.FSSettings import Settings
from fabscan.controller import HardwareController
from fabscan.util.FSinject import injector
from fabscan.FSVersion import __version__


class FSServer():
    def __init__(self,config_file, settings_file):

        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        self.hardwareController = None
        self.config_file = config_file
        self.settings_file = settings_file



    def run(self):
        self._logger.info("FabScanPi-Server "+str(__version__))

        try:


            injector.provide_instance(FSEventManager, FSEventManager(), name="FSEventManager")

            # create Singleton instances
            _config = Config.instance(self.config_file)
            _settings = Settings.instance(self.settings_file)

            _hardwareController = HardwareController.instance()
            _eventManager = FSEventManager.instance()

            # Websocket Server
            self.fsWebSocketServer = FSWebSocketServer()
            self.fsWebSocketServer.start()

            _scanner = FSScanner()
            _scanner.start()

            # Web Server
            self.fsWebServer = WebServer()
            self.fsWebServer.start()

            while True:
                time.sleep(0.3)
            #self.fsWebServer.serve_forever()

        except (KeyboardInterrupt, SystemExit):

            time.sleep(0.5)
            _hardwareController.laser.off()
            _hardwareController.led.off()
            _hardwareController.turntable.stop_turning()

            sys.exit(0)






