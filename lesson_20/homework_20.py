from datetime import datetime

KEY = "Key TSTFEED0300|7E3E|0400"
INPUT_LOG = "hblog.txt"
OUTPUT_LOG = "hb_test.log"

def analyze_heartbeat(input_file=INPUT_LOG, output_file=OUTPUT_LOG):
    with open(input_file, "r") as f:
        lines = f.readlines()

    # Відбираємо тільки потрібний ключ
    filtered_log = [line for line in lines if KEY in line]

    # Створюємо список (datetime, рядок)
    timestamps = []
    for line in filtered_log:
        ts_index = line.find("Timestamp ")
        if ts_index != -1:
            ts_str = line[ts_index + 10 : ts_index + 18]
            try:
                ts_time = datetime.strptime(ts_str, "%H:%M:%S")
                timestamps.append((ts_time, line.strip()))
            except ValueError:
                continue

    # Сортуємо по часу
    timestamps.sort(key=lambda x: x[0])

    # Аналіз різниці
    log_lines = []
    for i in range(1, len(timestamps)):
        prev_time, _ = timestamps[i-1]
        curr_time, _ = timestamps[i]

        delta = (curr_time - prev_time).total_seconds()
        if delta < 0:
            delta += 24*3600  # перехід через північ

        if 31 < delta < 33:
            log_lines.append(f"{curr_time.strftime('%H:%M:%S')} WARNING heartbeat={delta} sec")
        elif delta >= 33:
            log_lines.append(f"{curr_time.strftime('%H:%M:%S')} ERROR heartbeat={delta} sec")

    # Запис у файл
    with open(output_file, "w") as f:
        for line in log_lines:
            f.write(line + "\n")

    print(f"Готово! Результат записано у {output_file}")

analyze_heartbeat()
