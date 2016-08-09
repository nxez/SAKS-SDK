========
实用工具
========
.. currentmodule:: sakshat.entities

.. note::

    所有的 GPIO 针脚号码皆使用博通(BCM)编号。


蜂鸣器
======

.. class:: Buzzer(pin, real_true = GPIO.HIGH)

    初始化蜂鸣器

    :param int pin:
        针脚号码
    :param int real_true:
        GPIO.HIGH 或者 GPIO.LOW
    :return:
        ``None``