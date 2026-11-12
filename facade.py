# /****************/
# Mã sinh viên: 202419007
# Họ và tên: Phạm Anh Tú
# /****************/
"""Facade: gộp nhiều thao tác của thiết bị thành chế độ sử dụng."""

from typing import Protocol

from .configuration import HomeConfiguration
from .interfaces import IDevice, IDimmable, ILockable


class IHomeSettings(Protocol):
    """Abstraction chỉ đọc cấu hình cần cho chế độ ngủ (dễ kiểm thử)."""

    @property
    def night_light_level(self) -> int: ...


class SmartHomeFacade:
    """Client yêu cầu chế độ, không cần biết trình tự bật/tắt/khóa."""

    def __init__(
        self,
        light: IDimmable,
        fan: IDevice,
        door: ILockable,
        config: IHomeSettings | None = None,
    ) -> None:
        # Dependency Injection: các thiết bị được tạo sẵn từ bên ngoài.
        self._light = light
        self._fan = fan
        self._door = door
        self._config = config if config is not None else HomeConfiguration.instance()

    def go_to_work(self) -> None:
        """Đi làm: tắt đèn, tắt quạt và khóa cửa."""
        self._light.turn_off()
        self._fan.turn_off()
        self._door.lock()

    def go_to_sleep(self) -> None:
        """Đi ngủ: tắt quạt, khóa cửa, bật đèn và đặt mức sáng ban đêm."""
        self._fan.turn_off()
        self._door.lock()
        self._light.turn_on()
        level = self._config.night_light_level
        self._light.set_brightness(level)
        print(f"Night light level: {level}%")
