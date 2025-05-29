from datetime import datetime
import threading

class Logger:
    def __init__(self):
        self.lock = threading.Lock()
        self.final_logs = {}
        self.log_file_path = "log.txt"

    def log(self, thread_name, requested, status):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        entry = {
            "thread": thread_name,
            "requested": requested,
            "status": status,
            "timestamp": timestamp
        }

        with self.lock:
            self.final_logs[thread_name] = entry
            with open(self.log_file_path, "a", encoding="utf-8") as f:
                f.write(f"{thread_name} | Requested: {requested} | Status: {status} | Time: {timestamp}\n")

        color = "\033[92m" if status == "SUCCESS" else "\033[91m" if status == "FAILED" else "\033[94m"
        print(f"{color}{thread_name} | Requested: {requested} | Status: {status} | Time: {timestamp}\033[0m")

    def get_logs(self):
        with self.lock:
            return list(self.final_logs.values())
