# /****************/
# Mã sinh viên: 202419007
# Họ và tên: Phạm Anh Tú
# /****************/
"""Các hợp đồng trừu tượng: chỉ đưa thao tác vào interface phù hợp."""

from abc import ABC, abstractmethod


class IDevice(ABC):
    """Hợp đồng chung của mọi thiết bị có thể bật/tắt."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Tên thiết bị."""

    @property
    @abstractmethod
    def is_on(self) -> bool:
        """Thiết bị đang bật hay tắt."""

    @abstractmethod
    def turn_on(self) -> None:
        """Bật thiết bị."""

    @abstractmethod
    def turn_off(self) -> None:
        """Tắt thiết bị."""


class ILockable(ABC):
    """Hợp đồng khóa/mở khóa, không áp đặt lên quạt hoặc đèn."""

    @property
    @abstractmethod
    def is_locked(self) -> bool:
        """Trạng thái khóa."""

    @abstractmethod
    def lock(self) -> None:
        """Khóa cửa."""

    @abstractmethod
    def unlock(self) -> None:
        """Mở khóa cửa."""


class IDimmable(IDevice):
    """Mở rộng IDevice cho thiết bị hỗ trợ điều chỉnh độ sáng."""

    @property
    @abstractmethod
    def brightness(self) -> int:
        """Độ sáng 0..100."""

    @abstractmethod
    def set_brightness(self, level: int) -> None:
        """Áp dụng độ sáng."""
