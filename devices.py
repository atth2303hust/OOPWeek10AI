# /****************/
# Mã sinh viên: 202419007
# Họ và tên: Phạm Anh Tú
# /****************/
"""Các thiết bị cụ thể; trạng thái được đóng gói bằng thuộc tính nội bộ."""

from .interfaces import IDevice, IDimmable, ILockable


def _validate_name(name: str) -> str:
    """Không cho phép tên trống hoặc không phải chuỗi."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Tên thiết bị phải là chuỗi không rỗng.")
    return name.strip()


class SmartLight(IDimmable):
    """Đèn có thể bật/tắt và điều chỉnh độ sáng."""

    def __init__(self, name: str) -> None:
        self._name = _validate_name(name)
        self._is_on = False
        self._brightness = 100

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_on(self) -> bool:
        return self._is_on

    @property
    def brightness(self) -> int:
        return self._brightness

    def turn_on(self) -> None:
        self._is_on = True
        print(f"{self.name}: ON")

    def turn_off(self) -> None:
        self._is_on = False
        print(f"{self.name}: OFF")

    def set_brightness(self, level: int) -> None:
        if type(level) is not int or not 0 <= level <= 100:
            raise ValueError("Mức sáng phải là số nguyên từ 0 đến 100.")
        self._brightness = level
        print(f"{self.name}: brightness {level}%")


class SmartFan(IDevice):
    """Quạt chỉ thực thi thao tác chung bật/tắt."""

    def __init__(self, name: str) -> None:
        self._name = _validate_name(name)
        self._is_on = False

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_on(self) -> bool:
        return self._is_on

    def turn_on(self) -> None:
        self._is_on = True
        print(f"{self.name}: ON")

    def turn_off(self) -> None:
        self._is_on = False
        print(f"{self.name}: OFF")


class SmartDoor(IDevice, ILockable):
    """Cửa có trạng thái bật/tắt bộ điều khiển và khóa/mở khóa riêng."""

    def __init__(self, name: str) -> None:
        self._name = _validate_name(name)
        self._is_on = False
        self._is_locked = False

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_on(self) -> bool:
        return self._is_on

    @property
    def is_locked(self) -> bool:
        return self._is_locked

    def turn_on(self) -> None:
        self._is_on = True
        print(f"{self.name}: ON")

    def turn_off(self) -> None:
        self._is_on = False
        print(f"{self.name}: OFF")

    def lock(self) -> None:
        self._is_locked = True
        print(f"{self.name}: LOCKED")

    def unlock(self) -> None:
        self._is_locked = False
        print(f"{self.name}: UNLOCKED")
