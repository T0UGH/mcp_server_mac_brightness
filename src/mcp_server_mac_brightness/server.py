from mcp.server.fastmcp import FastMCP
from .controller import MacController

# Initialize FastMCP server
mcp = FastMCP("mac_control")
controller = MacController()

@mcp.tool()
async def get_screen_brightness() -> str | float:
    """获取当前屏幕亮度 (0-100)"""
    try:
        brightness = controller.get_brightness()
        return brightness
    except Exception as e:
        return f"获取亮度失败: {str(e)}"

@mcp.tool()
async def set_screen_brightness(brightness: float, duration: float = 0) -> str:
    """设置屏幕亮度
    
    Args:
        brightness: 亮度百分比 (0-100)
        duration: 渐变时间(秒)，0 表示立即改变
    """
    if not 0 <= brightness <= 100:
        return "亮度必须在 0-100 之间"
    
    try:
        controller.set_brightness(brightness, duration)
        return f"成功设置亮度为 {brightness}%"
    except Exception as e:
        return f"设置亮度失败: {str(e)}"

@mcp.tool()
async def get_system_volume() -> int | str:
    """获取当前系统音量 (0-100)"""
    try:
        return controller.get_volume()
    except Exception as e:
        return f"获取音量失败: {str(e)}"

@mcp.tool()
async def set_system_volume(volume: int) -> str:
    """设置系统音量
    
    Args:
        volume: 音量大小 (0-100)
    """
    if not 0 <= volume <= 100:
        return "音量必须在 0-100 之间"
    
    try:
        controller.set_volume(volume)
        return f"成功设置音量为 {volume}%"
    except Exception as e:
        return f"设置音量失败: {str(e)}"

@mcp.tool()
async def toggle_system_mute() -> str:
    """切换系统静音状态"""
    try:
        controller.toggle_mute()
        return "成功切换静音状态"
    except Exception as e:
        return f"切换静音失败: {str(e)}"