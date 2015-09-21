#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 NXEZ.COM.
# http://www.nxez.com
#
# Licensed under the GNU General Public License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.gnu.org/licenses/gpl-2.0.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = 'Spoony'
__version__  = 'version 0.0.1'
__license__  = 'Copyright (c) 2015 NXEZ.COM'

from sakshat import SAKSHAT
import time
import commands

#Declare the SAKS Board
SAKS = SAKSHAT()

def dip_switch_status_changed_handler(status):
    '''
    called while the status of dip switch changed
    :param status: current status
    :return: void
    '''
    print('on_dip_switch_status_changed:')
    print(status)
    pass

def tact_event_handler(pin, status):
    '''
    called while the status of tacts changed
    :param pin: pin number which stauts of tact is changed
    :param status: current status
    :return: void
    '''
    print('tact_event_handler')
    print("%d - %s" % (pin, status))

#def handler(signum, frame):
#    SAKS.digital_display.off()
#    print "receive a signal %d"%(signum)

def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000
    # Uncomment the next line if you want the temp in Fahrenheit
    #return float(1.8*cpu_temp)+32

def get_gpu_temp():
    gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
    return float(gpu_temp)
    # Uncomment the next line if you want the temp in Fahrenheit
    # return float(1.8* gpu_temp)+32

if __name__ == "__main__":
    print("main")
    #SAKS = SAKSController()
    #print(PINS.BUZZER)
    #print(SAKS.appRoot)
    SAKS.dip_switch_status_changed_handler = dip_switch_status_changed_handler
    SAKS.tact_event_handler = tact_event_handler
    b = SAKS.buzzer
    b.beep(1)
    SAKS.ledrow.set_row([True, False, True, False, True, False, True, False])
    SAKS.ledrow.items[7].flashAction(0.02,0.02,30)
    SAKS.ledrow.on()
    print(SAKS.ds18b20.temperature)
    #SAKS.digital_display.show('#.1#.234')
    #print(SAKS.dip_switch.is_on)
    '''
    while True:
        SAKS.digital_display.show("%d%d%d%d" % (time.gmtime().tm_min / 10, time.gmtime().tm_min % 10, time.gmtime().tm_sec / 10, time.gmtime().tm_sec % 10))
        time.sleep(0.5)
    '''
    while True:
        t = get_cpu_temp()
        print("%3.1f" % t)
        SAKS.digital_display.show("%3.2f" % t)
        if t > 38:
            b.beepAction(0.02,0.02,30)
        time.sleep(1)

    input("Enter any keys to exit...")

