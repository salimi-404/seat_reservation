import threading

class SeatManager:
    def __init__(self, total_seats, logger):
        self.total_seats = total_seats
        self.seats = [False] * total_seats
        self.lock = threading.Lock()
        self.active_reservations = {}
        self.logger = logger

    def reset(self):
        with self.lock:
            self.seats = [False] * self.total_seats
            self.active_reservations.clear()
            self.logger.final_logs.clear()
            open(self.logger.log_file_path, "w").close()

    def request_seats(self, thread_name, count):
        with self.lock:
            start = self._find_contiguous_block(count)
            if start is None:
                self.logger.log(thread_name, count, "FAILED")
                return False
            for i in range(start, start + count):
                self.seats[i] = True
            self.active_reservations[thread_name] = (start, count)
            self.logger.log(thread_name, count, "SUCCESS")
            return True

    def cancel_reservation(self, thread_name):
        with self.lock:
            if thread_name in self.active_reservations:
                start, count = self.active_reservations.pop(thread_name)
                for i in range(start, start + count):
                    self.seats[i] = False
                self.logger.log(thread_name, count, "CANCELLED")

    def _find_contiguous_block(self, length):
        consecutive = 0
        for i in range(self.total_seats):
            if not self.seats[i]:
                consecutive += 1
                if consecutive == length:
                    return i - length + 1
            else:
                consecutive = 0
        return None

    def get_seat_status(self):
        with self.lock:
            return list(self.seats)

    def available_seats(self):
        return self.get_seat_status().count(False)
