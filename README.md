# SAKS-SDK
距离出上一个[瑞士军刀扩展板 SAKS](http://shumeipai.nxez.com/swiss-army-knife-shield-for-raspberry-pi) 的[教程](http://shumeipai.nxez.com/swiss-army-knife-shield-for-raspberry-pi-diy-tutorials)已经过去很久了，在这期间我们在思考一个问题——既然 SAKS 的设计定位于上手快、DIY可能性多，那么为何不做得彻底一点？之所以觉得之前的教程有某些“不够彻底”，是因为当遇到较复杂的需求时，创客们不得不用代码重复去实现一些数码管动态扫描、开关检测、传感器状态读取等硬件的操作逻辑。终于我们决定开发一套SDK，将以上需要重复造的轮子进行科学封装，从而达到让创客们集中精力专心实现功能，而不用为关注底层的操控逻辑而分心。

终于我们完成了这个 SDK 并在此基础上实现了SAKS的SDK，基于Python语言用面向对象的方法实现（由于封装程度高，即便你没有系统学习过面向对象的开发方法也完全不用担心不会使用）。接下来我们会通过既定的一些例程（例如[树莓派 SAKS 扩展板实用应用 之 CPU 温度显示和警报](http://shumeipai.nxez.com/2015/09/21/cpu-temperature-display-and-alarm.html)），介绍如何基于 SAKS SDK 实现例程中的功能。

树莓派瑞士军刀扩展板 SAKS SDK 已经通过 Github 开源（GPL v2.0 许可方式）并提供下载：
https://github.com/spoonysonny/SAKS-SDK

也可通过以下命令下载。
git clone https://github.com/spoonysonny/SAKS-SDK.git

树莓派瑞士军刀扩展板购买请移步此处:
http://link.nxez.com/spoony/cps-products-saks-2015-early

随后我们将陆续完善开发文档并推出更多教程，敬请关注。同时我们非常期待有兴趣的创客、树莓派学习者深度参与进来，基于此SDK创造自己的作品、完善SDK本身！

树莓派实验室 QQ 群号 62335986

![](http://shumeipai.nxez.com/wp-content/uploads/2015/03/P1100536-0.jpg)
