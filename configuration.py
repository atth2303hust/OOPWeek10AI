# /****************/
# Mã sinh viên: 202419007
# Họ và tên: Phạm Anh Tú
# /****************/
"""Singleton: một cấu hình dùng chung trong một tiến trình Python."""

from threading import Lock
from typing import ClassVar


class HomeConfiguration:
    """Singleton khởi tạo lười, dùng Lock để tránh tạo trùng ở nhiều luồng."""

    _instance: ClassVar["HomeConfiguration | None"] = None
    _creation_lock: ClassVar[Lock] = Lock()

    def __new__(cls) -> "HomeConfiguration":
        # Cả khởi tạo thuộc tính cũng nằm trong lock: không lộ object nửa vời.
        with cls._creation_lock:
            if cls._instance is None:
                obj = super().__new__(cls)
                obj._home_name = "My Home"
                obj._night_light_level = 30
                cls._instance = obj
            return cls._instance

    def __init__(self) -> None:
        # __init__ có thể gọi nhiều lần; tuyệt đối không reset cấu hình.
        pass

    def __init_subclass__(cls, **kwargs: object) -> None:
        raise TypeError("HomeConfiguration không cho phép kế thừa.")

    @classmethod
    def instance(cls) -> "HomeConfiguration":
        """API tương tự thuộc tính Instance trong ví dụ C#."""
        return cls()

    @property
    def home_name(self) -> str:
        return self._home_name

    @home_name.setter
    def home_name(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Tên ngôi nhà không được để trống.")
        self._home_name = value.strip()

    @property
    def night_light_level(self) -> int:
        return self._night_light_level

    @night_light_level.setter
    def night_light_level(self, value: int) -> None:
        if type(value) is not int or not 0 <= value <= 100:
            raise ValueError("Mức sáng ban đêm phải từ 0 đến 100.")
        self._night_light_level = value
