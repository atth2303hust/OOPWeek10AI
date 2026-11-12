# /****************/
# Mã sinh viên: 202419007
# Họ và tên: Phạm Anh Tú
# /****************/
"""Simple Factory: nơi duy nhất biết constructor từng thiết bị."""

from .devices import SmartDoor, SmartFan, SmartLight
from .interfaces import IDevice


class UnsupportedDeviceTypeError(ValueError):
    """Tương đương về ý nghĩa với ArgumentException trong tài liệu C#."""


class DeviceFactory:
    """Chuyển lựa chọn nhập vào thành một đối tượng tuân thủ IDevice."""

    @staticmethod
    def create(device_type: str, name: str) -> IDevice:
        if not isinstance(device_type, str):
            raise UnsupportedDeviceTypeError("Loại thiết bị phải là chuỗi.")

        kind = device_type.strip().casefold()
        constructors = {"light": SmartLight, "fan": SmartFan, "door": SmartDoor}
        if kind not in constructors:
            raise UnsupportedDeviceTypeError(
                f"Unsupported device type: {device_type!r}"
            )
        return constructors[kind](name)
