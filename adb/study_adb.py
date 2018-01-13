"""
    python adb connect android
"""
import subprocess
import re
import time
from PIL import Image


# 获取设备信息
def get_device_info():
    result = subprocess.check_output("adb devices")
    print("devices: {}".format(result.decode().strip()))
    result = subprocess.check_output("adb shell wm size")
    print("size: {}".format(result.decode().strip()))
    result = subprocess.check_output("adb shell wm density")
    print("density: {}".format(result.decode().strip()))
    pass


# 获取系统属性
def get_system_info():
    """
        getprop就是将配置文件里的信息读取出来并经过整理后，并以字典的形式展示给用户的。
            getprop ro.serialno 查看机器的序列号
            getprop ro.carrier 查看机器的CID号
            getprop ro.hardware 查看机器板子代号
            getprop ro.bootloader 查看SPL(Hboot)版本号
    :return: 
    """
    result = subprocess.check_output("adb shell getprop")
    result = result.decode().split("\r\r\n")
    print("all prop: {}".format(result))
    result = subprocess.check_output("adb shell getprop ro.product.model")
    print("ro.product.model: {}".format(result.decode().strip()))
    pass


# 获取屏幕尺寸
def get_screen_size():
    result = subprocess.check_output("adb shell wm size", shell=True)
    result = result.decode()
    m = re.search("(\d+)x(\d+)", result)
    if m:
        result = m.group(0)
        width = m.group(1)
        height = m.group(2)
        print("{} {}/{}".format(result, width, height))
    pass


# 截取屏幕:从输出流中读取
def screen_capture_pipe():
    start_time = time.clock()
    process = subprocess.Popen("adb shell screencap -p", shell=True, stdout=subprocess.PIPE)
    screen_result = process.stdout.read()
    screen_result = screen_result.replace(b"\r\r\n", b"\n")

    with open("tem.png", "wb") as f:
        f.write(screen_result)

    Image.open("tem.png").show()
    print(time.clock() - start_time)
    pass


# 截取屏幕:先存到手机上
def screen_capture_pull():
    start_time = time.clock()
    # 截屏
    result = subprocess.call("adb shell screencap -p /sdcard/screen_shot.png", shell=True)
    if result == 0:
        # 下载
        result = subprocess.call("adb pull /sdcard/screen_shot.png tem2.png", shell=True)
        if result == 0:
            # 删除
            result = subprocess.call("adb shell rm /sdcard/screen_shot.png", shell=True)
            if result != 0:
                print("error of adb shell rm")
            # 显示
            Image.open("tem2.png").show()
        else:
            print("error of adb pull")
    else:
        print("error of adb shell screencap -p")
    print(time.clock() - start_time)
    pass


# 发送按键事件
def shell_input():
    """
    Usage: input [<source>] <command> [<arg>...]
    The sources are: 
      mouse
      keyboard
      joystick
      touchnavigation
      touchpad
      trackball
      stylus
      dpad
      touchscreen
      gamepad
    The commands and default sources are:
      text <string> (Default: touchscreen)
      keyevent [--longpress] <key code number or name> ... (Default: keyboard)
      tap <x> <y> (Default: touchscreen)
      swipe <x1> <y1> <x2> <y2> [duration(ms)] (Default: touchscreen)
      press (Default: trackball)
      roll <dx> <dy> (Default: trackball)
    :return: 
    """
    start_time = time.clock()
    # 发送文本
    # result = subprocess.call("adb shell input text test123")  # 发送文本内容，不能发送中文

    # 按键事件
    # result = subprocess.call("adb shell input keyevent KEYCODE_HOME")  # 点击HOME键，3
    # result = subprocess.call("adb shell input keyevent KEYCODE_CALL")  # 拨号键，5
    # result = subprocess.call("adb shell input keyevent KEYCODE_ENDCALL")  # 关闭屏幕，挂机键，6
    # result = subprocess.call("adb shell input keyevent KEYCODE_MENU")  # 菜单键，82
    # result = subprocess.call("adb shell input keyevent KEYCODE_BACK")  # 返回键，4
    # result = subprocess.call("adb shell input keyevent KEYCODE_SEARCH")  # 搜索键，84
    # result = subprocess.call("adb shell input keyevent KEYCODE_CAMERA")  # 拍照键，27
    # result = subprocess.call("adb shell input keyevent KEYCODE_POWER")  # 电源键，26
    # result = subprocess.call("adb shell input keyevent KEYCODE_ENTER")  # 回车键，66

    # 点击屏幕
    # result = subprocess.call("adb shell input tap 540 1600")  # 点击屏幕上的点（水平x，垂直y）

    # 滑动事件：向设备发送一个滑动的指令，并且可以选择设置滑动的时长。
    # result = subprocess.call("adb shell input swipe 500 500 800 800")  # <x1> <y1> <x2> <y2>
    # 长按事件
    result = subprocess.call("adb shell input swipe 500 500 500 500 10000")  # 长按10秒

    print(result)
    print(time.clock() - start_time)
    pass


# 启动Activity
def start_activity():
    result = subprocess.call("adb shell am start -n com.alisure.mjob/.MainActivity")
    print(result)
    pass


if __name__ == '__main__':
    # 获取设备信息
    # get_device_info()

    # 获取系统属性
    # get_system_info()

    # 获取屏幕尺寸
    # get_screen_size()

    # 截取屏幕
    # screen_capture_pull()

    # 发送按键事件
    # shell_input()

    # 启动Activity
    start_activity()

    pass
