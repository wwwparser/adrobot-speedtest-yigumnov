#!/usr/bin/env python3
"""Простой замерятель скорости интернета.

Делает N последовательных запросов к указанному адресу, дожидается ответа
на каждый, считает среднее время запроса, суммарный объём скачанных данных
и печатает итоговую скорость в МБ/с.
"""
import sys
import time
import urllib.request

ATTEMPTS = 10


def measure(url: str, attempts: int = ATTEMPTS) -> None:
    total_time = 0.0
    total_bytes = 0

    for i in range(1, attempts + 1):
        start = time.perf_counter()
        with urllib.request.urlopen(url) as response:
            data = response.read()
        elapsed = time.perf_counter() - start

        total_time += elapsed
        total_bytes += len(data)
        print(f"Запрос {i}/{attempts}: {elapsed:.3f} с, {len(data) / 1024:.1f} КБ")

    avg_time = total_time / attempts
    total_mb = total_bytes / (1024 * 1024)
    speed_mb_s = total_mb / total_time if total_time else 0.0

    print()
    print(f"Среднее время запроса: {avg_time:.3f} с")
    print(f"Скачано данных: {total_mb:.2f} МБ")
    print(f"Скорость: {speed_mb_s:.2f} МБ/с")


def main() -> None:
    if sys.stdout.encoding != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 2:
        print("Использование: python speedtest.py <URL>")
        sys.exit(1)
    measure(sys.argv[1])


if __name__ == "__main__":
    main()
