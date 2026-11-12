# /****************/
# Mã sinh viên: 202419007
# Họ và tên: Phạm Anh Tú
# /****************/
"""Giao diện dòng lệnh Smart Home Mini. Chạy: python main.py / --demo."""

import argparse

from smarthome import (
    DeviceFactory, HomeConfiguration, IDevice, IDimmable, ILockable,
    SmartHomeFacade, UnsupportedDeviceTypeError,
)


def build_home() -> tuple[dict[str, IDevice], SmartHomeFacade, HomeConfiguration]:
    """Khởi tạo ba thiết bị bằng Factory và nối thành Facade."""
    light = DeviceFactory.create("light", "Living room light")
    fan = DeviceFactory.create("fan", "Living room fan")
    door = DeviceFactory.create("door", "Main door")

    # Hai điều kiện này chỉ mô tả cấu hình ngôi nhà của ứng dụng.
    if not isinstance(light, IDimmable) or not isinstance(door, ILockable):
        raise RuntimeError("Cấu hình Factory không cung cấp đủ khả năng thiết bị.")
    config = HomeConfiguration.instance()
    facade = SmartHomeFacade(light, fan, door, config)
    devices = {item.name: item for item in (light, fan, door)}
    return devices, facade, config


def show_devices(devices: dict[str, IDevice]) -> None:
    """Hiển thị trạng thái đọc từ object, không tự phỏng đoán."""
    print("\nTRẠNG THÁI THIẾT BỊ")
    for device in devices.values():
        status = "ON" if device.is_on else "OFF"
        extras = []
        if isinstance(device, ILockable):
            extras.append("LOCKED" if device.is_locked else "UNLOCKED")
        if isinstance(device, IDimmable):
            extras.append(f"brightness={device.brightness}%")
        suffix = f" | {', '.join(extras)}" if extras else ""
        print(f"- {device.name}: {status}{suffix}")


def run_demo() -> None:
    """Kịch bản chạy cố định để tiện tái lập kết quả trong báo cáo."""
    devices, facade, config = build_home()
    config.home_name = "My Home"
    config.night_light_level = 30
    print("=== DEMO SMART HOME MINI ===")
    print(f"Singleton identity: {config is HomeConfiguration.instance()}")
    print("\n[GoToWork]")
    facade.go_to_work()
    print("\n[GoToSleep]")
    facade.go_to_sleep()
    show_devices(devices)


def run_cli() -> None:
    """Menu tương tác thật; tránh phụ thuộc vào thư viện giao diện ngoài."""
    devices, facade, config = build_home()
    print("SMART HOME MINI - FACTORY / SINGLETON / FACADE")
    while True:
        print("\n1. Xem thiết bị | 2. Đi làm | 3. Đi ngủ")
        print("4. Điều khiển một thiết bị | 5. Tạo thiết bị")
        print("6. Đổi độ sáng ban đêm | 7. Xem cấu hình | 0. Thoát")
        try:
            choice = input("Chọn: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nĐã kết thúc.")
            break

        if choice == "0":
            print("Tạm biệt!")
            break
        if choice == "1":
            show_devices(devices)
        elif choice == "2":
            facade.go_to_work()
        elif choice == "3":
            facade.go_to_sleep()
        elif choice == "4":
            show_devices(devices)
            name = input("Tên thiết bị cần điều khiển: ").strip()
            device = devices.get(name)
            if device is None:
                print("Không tìm thấy thiết bị.")
                continue
            action = input("Lệnh (on/off/lock/unlock): ").strip().casefold()
            if action == "on":
                device.turn_on()
            elif action == "off":
                device.turn_off()
            elif action == "lock" and isinstance(device, ILockable):
                device.lock()
            elif action == "unlock" and isinstance(device, ILockable):
                device.unlock()
            else:
                print("Thiết bị không hỗ trợ lệnh này.")
        elif choice == "5":
            kind = input("Loại (light/fan/door): ")
            name = input("Tên thiết bị mới: ").strip()
            if name in devices:
                print("Tên thiết bị đã tồn tại.")
                continue
            try:
                device = DeviceFactory.create(kind, name)
            except (UnsupportedDeviceTypeError, ValueError) as exc:
                print(f"Không tạo được: {exc}")
            else:
                devices[device.name] = device
                print(f"Đã tạo: {type(device).__name__} - {device.name}")
        elif choice == "6":
            try:
                config.night_light_level = int(input("Mức sáng (0-100): "))
            except ValueError as exc:
                print(f"Giá trị không hợp lệ: {exc}")
            else:
                print(f"Đã lưu mức sáng ban đêm: {config.night_light_level}%")
        elif choice == "7":
            print(f"Nhà: {config.home_name}; Mức sáng: {config.night_light_level}%")
        else:
            print("Lựa chọn không hợp lệ.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Smart Home Mini")
    parser.add_argument("--demo", action="store_true", help="Chạy demo cố định")
    args = parser.parse_args()
    if args.demo:
        run_demo()
    else:
        run_cli()


if __name__ == "__main__":
    main()
