### Python 通过adb和手机交互

### 安装

* 在电脑上安装 [Universal Adb Driver](http://universaladbdriver.com/) 或者其它的ADB工具

* 连接手机：手机需要打开`开发者模式`
    * USB连接
        ```
            adb devices  # 验证是否连接成功
        ```
    * WIFI连接（手机需要ROOT，我第一次连接时：先用USB连接成功，然后切换为无线连接）
        ```
            adb tcpip 5555  # 切换为无线模式
            adb connect ip address  # 连接
            adb devices  # 验证是否连接成功
        ```
* 可以把手机开发者中的`显示触摸操作`和`指针位置`打开


### adb shell
[Android开发中adb命令的常用方法](http://blog.csdn.net/zhangjg_blog/article/details/10431649)

* 在命令行中输入 `adb shell` 可以直接进入android手机的shell环境。
* 输入 `exit` 即可退出shell环境。

> 所有以"adb shell"开头的命令,都可以先执行adb shell命令进入目标设备的Linux Shell环境, 
然后在目标设备的Linux Shell中再执行"adb shell"之后的命令。
如adb shell dumpsys activity, 可以先执行adb shell, 然后再Linux Shell中再执行dumpsys activity。

