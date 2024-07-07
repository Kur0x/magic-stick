# 使用ESP32-C3和MPU6050控制Home Assistant灯光

该项目展示了如何使用ESP32-C3和MPU6050传感器，根据传感器的加速度数据来控制Home Assistant的灯光。当检测到显著的加速度变化时，ESP32-C3将读取MPU6050的数据并切换Home Assistant中的灯光。

## 需求

- ESP32-C3开发板
- MPU6050加速度和陀螺仪传感器
- 已安装MicroPython固件的ESP32-C3
- 在本地网络中运行的Home Assistant实例
- Home Assistant API的长时间有效访问令牌

## 硬件连接

使用I2C接口将MPU6050连接到ESP32-C3：

- VCC连接到3.3V
- GND连接到GND
- SCL连接到GPIO
- SDA连接到GPIO

## 安装步骤

1. **刷入MicroPython固件**：确保你的ESP32-C3已经刷入MicroPython固件。

4. **上传脚本**：将提供的脚本上传到你的ESP32-C3。

5. **配置**

WiFi连接

在connect_wifi函数中替换'your_ssid'和'your_password'为你的WiFi网络凭证。

Home Assistant

将'home_assistant_local_ip'替换为你的Home Assistant实例的本地IP地址。将'YOUR_LONG_LIVED_ACCESS_TOKEN'替换为你的Home Assistant长时间有效访问令牌。将'light.your_light'替换为你想要控制的灯的实体ID。

6. **运行项目**

	1.	启动ESP32-C3：确保你的ESP32-C3已通电并连接到MPU6050传感器。
	2.	执行脚本：在ESP32-C3上运行主脚本。
	3.	监控输出：当检测到显著的加速度变化时，脚本将读取加速度数据并切换Home Assistant中的灯光。

7. **故障排除**

	•	WiFi连接问题：确保你的ESP32-C3在WiFi网络范围内，并且凭证正确。
	•	MPU6050通信问题：验证ESP32-C3与MPU6050之间的I2C连接。
	•	Home Assistant API问题：确保Home Assistant实例正在运行并在网络中可访问，访问令牌正确。

8. **许可**

该项目使用MIT许可证。
