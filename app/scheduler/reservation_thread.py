import threading
import time
import random

CONFIG = {
    'cancellation_chance': 0.3
}

class ReservationThread(threading.Thread):
    def __init__(self, thread_id, seat_manager, priority, arrival_time, requested_seats):
        super().__init__()
        self.thread_id = thread_id
        self.thread_name = f"Thread-{thread_id}"
        self.seat_manager = seat_manager
        self.priority = priority
        self.arrival_time = arrival_time
        self.requested_seats = requested_seats
        self._result_lock = threading.Lock()
        self._result = None

    @property
    def result(self):
        with self._result_lock:
            return self._result

    @result.setter
    def result(self, value):
        with self._result_lock:
            self._result = value

    def run(self):
        success = self.seat_manager.request_seats(self.thread_name, self.requested_seats)
        self.result = "SUCCESS" if success else "FAILED"
        if success and random.random() < CONFIG['cancellation_chance']:
            time.sleep(random.uniform(0.5, 1.0))
            self.seat_manager.cancel_reservation(self.thread_name)
