# MCP Mac Brightness Server

A Model Context Protocol server for controlling Mac screen brightness and system volume.

## Features

- Screen Brightness Control
  - Get current screen brightness
  - Set screen brightness with optional fade duration
  - Supports brightness range: 0-100%

- System Volume Control
  - Get current system volume
  - Set system volume
  - Toggle system mute state

## Requirements

- Python >= 3.10
- macOS (uses native macOS frameworks)
- Required permissions for screen and audio control

## Installation

```bash
uv pip install -e .
```

## Usage

### Start the Server

### Available Tools

1. get_screen_brightness()
   
   - Returns current screen brightness (0-100)
2. set_screen_brightness(brightness: float, duration: float = 0)
   
   - Set screen brightness level
   - brightness : Target brightness (0-100)
   - duration : Fade duration in seconds (0 for immediate change)
3. get_system_volume()
   
   - Returns current system volume (0-100)
4. set_system_volume(volume: int)
   
   - Set system volume level (0-100)
5. toggle_system_mute()
   
   - Toggle system audio mute state
## Configuration
Configure in Claude desktop:

```json
{
    "mac_brightness": {
        "command": "uv",
        "args": ["run", "/absolute/path/to/src/mcp_server_mac_brightness/server.py"]
    }
}
 ```

## Error Handling

- Input validation for brightness and volume levels
- Comprehensive error messages for system API failures
- Graceful error handling for permission issues

## License

MIT License