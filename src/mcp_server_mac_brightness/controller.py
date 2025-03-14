import time
import subprocess

class MacController:
    @staticmethod
    def get_brightness() -> float:
        """获取当前亮度"""
        try:
            result = subprocess.run(['brightness', '-l'], capture_output=True, text=True)
            # 解析输出中的亮度值，格式如: "display 0: brightness 0.956055"
            brightness_line = [line for line in result.stdout.split('\n') if 'brightness' in line][0]
            brightness_value = float(brightness_line.split()[-1])
            return brightness_value * 100
        except Exception:
            return 0

    @staticmethod
    def set_brightness(level: float, duration: float = 0) -> None:
        """设置屏幕亮度"""
        target = max(5, min(level, 100)) / 100  # 转换为 0-1 范围
        
        if duration <= 0:
            subprocess.run(['brightness', '-m', str(target)])
            return
            
        # 渐变效果
        current = MacController.get_brightness() / 100
        steps = int(duration * 4)
        delta = (target - current) / steps
        
        for _ in range(steps):
            current += delta
            subprocess.run(['brightness', '-m', str(current)])
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