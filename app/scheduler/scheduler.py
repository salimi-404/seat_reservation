import random
import time
import queue
from app.scheduler.reservation_thread import ReservationThread

class HybridScheduler:
    def __init__(self, seat_manager):
        self.seat_manager = seat_manager
        self.retry_queue = queue.PriorityQueue()
        self.failed_threads = {}

    def start_simulation(self, num_threads):
        print(f"🚀 Starting simulation with {num_threads} threads...")
        for i in range(num_threads):
            arrival_time = time.time()
            priority = random.randint(1, 10)
            requested_seats = random.randint(1, 4)
            t = ReservationThread(i, self.seat_manager, priority, arrival_time, requested_seats)
            self.retry_queue.put((priority, arrival_time, t))

        self._process_queue()

        cycle = 1
        while True:
            print(f"\n🔁 Cycle {cycle}: retrying failed threads...")
            prev_fails = len(self.failed_threads)

            self._process_failed_retries()
            time.sleep(1)

            if len(self.failed_threads) == prev_fails:
                print("✅ No more possible retries. Ending simulation.")
                break

            cycle += 1

    def _process_queue(self):
        threads = []
        while not self.retry_queue.empty():
            _, _, thread = self.retry_queue.get()
            thread.start()
            threads.append(thread)

        for t in threads:
            t.join()
            if t.result == "FAILED":
                self.failed_threads[t.thread_id] = t

    def _process_failed_retries(self):
        temp_queue = queue.PriorityQueue()
        for thread_id in list(self.failed_threads):
            old = self.failed_threads[thread_id]
            new_time = time.time()
            new_thread = ReservationThread(
                old.thread_id,
                self.seat_manager,
                old.priority,
                new_time,
                old.requested_seats
            )
            temp_queue.put((old.priority, new_time, new_thread))

        self.failed_threads.clear()
        self.retry_queue = temp_queue
        self._process_queue()
