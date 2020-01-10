import serial
from config import config_parser
import math


class GeigerCounter(object):

    def __init__(self):
        self._baud_rate = None
        self._port = None
        self._timeout = None
        self._write_timeout = None
        self.get_config()
        self._serial_device = None
        self.cpm = 0
        self.high_cpm = 0
        self.low_cpm = 0
        self.usv_dose = 0
        self.voltage = 0
        self.open_port()
        self.get_voltage()

    def __del__(self):
        self._serial_device.close()

    def get_config(self):
        cfg = config_parser.load_config()
        self._port = cfg['geiger']['dev_location']
        self._baud_rate = cfg['geiger']['baud_rate']
        self._timeout = cfg['geiger']['read_to']
        self._write_timeout = cfg['geiger']['write_to']

    def open_port(self):
        self._serial_device = serial.Serial(self._port, self._baud_rate, timeout = self._timeout,
                                            write_timeout = self._write_timeout)
        
    def send_message(self, message):
        message = "<{}>>".format(message)
        self._serial_device.write(message.encode())

    def correct_message(self, msg):
        msg = msg.replace('b', '')
        msg = msg.replace("'", '')
        return msg

    def cpm_bytes_to_num(self, msg):
        cpm_val = 0
        cpm_bytes = msg.split("\\x")
        try:
            for i in range(4):
                cpm_val = cpm_val << 8
                cpm_val = cpm_val | int(cpm_bytes[i+1], 16)
        except IndexError:
            cpm_val = -1
        except ValueError:
            cpm_val = -1
        return cpm_val
    
    def get_cpm(self):
        self.cpm = 0
        self.send_message("GETCPM")
        msg = str(self._serial_device.readline())
        msg = self.correct_message(msg)
        self.cpm = self.cpm_bytes_to_num(msg)

    def get_high_cpm(self):
        self.high_cpm = 0
        self.send_message("GETCPMH")
        msg = str(self._serial_device.readline())
        msg = self.correct_message(msg)
        self.high_cpm = self.cpm_bytes_to_num(msg)

    def get_low_cpm(self):
        self.low_cpm = 0
        self.send_message("GETCPML")
        msg = str(self._serial_device.readline())
        msg = self.correct_message(msg)
        self.low_cpm = self.cpm_bytes_to_num(msg)

    def get_voltage(self):
        self.send_message("GETVOLT")
        msg = str(self._serial_device.readline())
        msg = self.correct_message(msg)
        self.voltage = msg

    def cpm_to_usv(self):
        self.get_high_cpm()
        self.get_low_cpm()

        if self.low_cpm > 60000 or self.high_cpm > 2000:
            if (self.high_cpm*0.194) > (self.low_cpm*0.0065):
                self.usv_dose = (self.high_cpm*0.194)
            else:
                self.usv_dose = (self.low_cpm*0.0065)
        elif self.low_cpm < 30000:
            self.usv_dose = self.low_cpm*0.0065
        elif self.low_cpm < 60000:
            self.usv_dose = ((self.low_cpm*1 + self.high_cpm*30*math.sqrt(30))/(1+math.sqrt(30)))*0.0065

    def turn_off(self):
        self.send_message("POWEROFF")

    def turn_on(self):
        self.send_message("POWERON")

    def reboot(self):
        self.send_message("REBOOT")
