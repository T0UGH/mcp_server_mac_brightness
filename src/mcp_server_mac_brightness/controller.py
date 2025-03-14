import time
import subprocess
import ctypes

# 加载 IOKit 框架
framework = ctypes.cdll.LoadLibrary('/System/Library/Frameworks/IOKit.framework/IOKit')

# 定义函数原型
framework.IODisplayGetFloatParameter.restype = ctypes.c_int
framework.IODisplayGetFloatParameter.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_char_p, ctypes.POINTER(ctypes.c_float)]
framework.IODisplaySetFloatParameter.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_char_p, ctypes.c_float]

class MacController:
    @staticmethod
    def get_brightness(display_id=0) -> float:
        """获取当前亮度"""
        brightness = ctypes.c_float()
        framework.IODisplayGetFloatParameter(None, display_id, b"brightness", ctypes.byref(brightness))
        return brightness.value * 100

    @staticmethod
    def set_brightness(level: float, duration: float = 0) -> None:
        """设置屏幕亮度"""
        target = max(5, min(level, 100)) / 100
        
        if duration <= 0:
            framework.IODisplaySetFloatParameter(None, 0, b"brightness", target)
            return
            
        current = MacController.get_brightness() / 100
        steps = int(duration * 4)
        delta = (target - current) / steps
        
        for _ in range(steps):
            current += delta
            framework.IODisplaySetFloatParameter(None, 0, b"brightness", current)
            time.sleep(0.25)

    @staticmethod
    def get_volume() -> int:
        """获取当前音量"""
        result = subprocess.run([
            'osascript', '-e',
            'output volume of (get volume settings)'
        ], capture_output=True, text=True)
        try:
            return int(result.stdout.strip())
        except:
            return 0

    @staticmethod
    def set_volume(level: int) -> None:
        """设置系统音量"""
        subprocess.run([
            'osascript', '-e',
            f'set volume output volume {level}'
        ])

    @staticmethod
    def toggle_mute() -> None:
        """切换静音状态"""
        subprocess.run([
            'osascript', '-e',
            'set volume with output muted'
        ])