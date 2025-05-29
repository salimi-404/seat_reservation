from flask import Blueprint, render_template, request, redirect, url_for
from collections import Counter
import json
import time

from app.scheduler.logger import Logger
from app.scheduler.seat_manager import SeatManager
from app.scheduler.scheduler import HybridScheduler

main = Blueprint('main', __name__)

logger = Logger()
seat_manager = SeatManager(total_seats=100, logger=logger)
scheduler = HybridScheduler(seat_manager)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            num_threads = int(request.form["num_threads"])
            if not (1 <= num_threads <= 100):
                return "Invalid thread count", 400
        except:
            return "Bad Request", 400

        seat_manager.reset()
        scheduler.start_simulation(num_threads)
        with open("seat_state.json", "w", encoding="utf-8") as f:
            json.dump(seat_manager.get_seat_status(), f)

        return redirect(url_for("main.index"))

    seat_status = seat_manager.get_seat_status()
    logs = seat_manager.logger.get_logs()
    status_counts = Counter(entry["status"] for entry in logs)
    request_counts = Counter(entry["requested"] for entry in logs)
    reserved_percent = round(100 * sum(seat_status) / 100, 2)

    return render_template(
        "index.html",
        logs=logs,
        max_threads=100,
        seat_status=seat_status,
        reserved_percent=reserved_percent,
        status_labels=list(status_counts.keys()),
        status_values=list(status_counts.values()),
        request_labels=[f"{k} seats" for k in request_counts],
        request_values=list(request_counts.values())
    )
