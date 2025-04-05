import serial

def read_uart(port='/dev/serial0', baudrate=230400, timeout=1):
    try:
        with serial.Serial(port, baudrate, timeout=timeout) as ser:
            print(f"Открыт порт {port} со скоростью {baudrate}")
            while True:
                if ser.in_waiting > 0:
                    data = ser.readline().decode('utf-8', errors='ignore').strip()
                    print(f"Получено: {data}")
    except serial.SerialException as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    read_uart()

