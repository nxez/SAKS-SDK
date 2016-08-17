=========
扩展板SDK
=========
.. currentmodule:: sakshat

SAKSHAT
=======
.. class:: SAKSHAT()

    对集成的树莓派瑞士军刀扩展板设立的类，一些有用的函数在此声明。

    .. note::

        以下声明 ``SAKS`` 为 :class:`sakshat.SAKSHAT()` 的一个实例。

        ``PINS`` 定义为 :code:`from sakshat.sakspins import SAKSPins as PINS`。

    .. py:attribute:: SAKS.buzzer

        为 :class:`sakshat.entities.Buzzer` 类的一个实例，初始化参数为 :code:`(PINS.BUZZER, GPIO.LOW)`。

    .. py:attribute:: SAKS.ledrow

        对于扩展板V2为 :class:`sakshat.entities.Led74HC595` 类，

        对于扩展板V1为 :class:`sakshat.entities.LedRow` 类。

    .. py:attribute:: SAKS.ds18b20

        为 :class:`sakshat.entities.DS18B20` 类。

    .. py:attribute:: SAKS.digital_display

        对于扩展板V2为 :class:`sakshat.entities.DigitalDisplayTM1637` 类，

        对于扩展板V1为 :class:`sakshat.entities.DigitalDisplay` 类。

    .. py:attribute:: SAKS.dip_switch

        为 :class:`sakshat.entities.DipSwitch2Bit` 类。

    .. py:attribute:: SAKS.tactrow

        为 :class:`sakshat.entities.TactRow` 类。

    .. py:attribute:: SAKS.dip_switch_status_changed_handler

        当拨码开关状态改变时调用的函数。

        blablabla

        设置此变量属性为 ``None`` 来禁用此事件。

    .. py:attribute:: SAKS.on_tact_event

        当轻触开关被按下时调用的函数。

            .. py:function:: tact_event_handler(pin, status)

                blablabla......

        设置此变量属性为 ``None`` 来禁用此事件。

SAKSPins
========
.. autoclass:: sakshat.sakspins.SAKSPins(object)
