# 🎥 Multi-Client Video Streaming System

A real-time video broadcasting system built with **Flask**, **Flask-SocketIO**, and **Python threading**, enabling simultaneous streaming of video frames to multiple clients. The system ensures synchronized frame delivery using concurrent threads and real-time communication protocols.

---

## 🚀 Project Overview

This project simulates a server that reads a video file, extracts its frames, and transmits them in real time to all connected clients. Clients receive and display the video in their browsers through a WebSocket-based connection, allowing synchronized playback.

The system is designed to:

- Serve multiple clients concurrently
- Deliver synchronized video frames
- Handle real-time communication using SocketIO
- Log connection events and stream performance
- Optionally display visual statistics using a dashboard

---

## 🛠️ Technologies Used

| Technology         | Purpose                                  |
|--------------------|------------------------------------------|
| Flask              | Web framework for HTTP routing           |
| Flask-SocketIO     | WebSocket communication with clients     |
| Threading (Python) | Concurrent frame broadcasting            |
| OpenCV (cv2)       | Video frame extraction and manipulation  |
| HTML / JavaScript  | Client-side video rendering              |
| Plotly / Dash      | Real-time dashboard for system metrics   |
| Logging            | Structured logs for debugging and stats  |

---

## 📁 Project Structure

video_streaming/
├── app.py # Main Flask app with SocketIO
├── video_sender.py # Threaded frame reader and broadcaster
├── static/
│ └── js/client.js # Client-side SocketIO code
├── templates/
│ └── index.html # HTML interface for users
├── video/
│ └── sample.mp4 # Input video for streaming
├── dashboard.py # Optional dashboard with real-time graphs
├── log/
│ └── log.txt # Log file for server events
├── requirements.txt # List of dependencies
└── README.md # Project documentation


---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/video_streaming.git
cd video_streaming

2. Install dependencies

pip install -r requirements.txt

3. Place your video

Replace video/sample.mp4 with any video you want to broadcast.
4. Run the application

python app.py

5. Open in browser

Navigate to:

http://localhost:5000

You can test with multiple tabs or devices to simulate multi-client playback.
📈 Real-Time Dashboard (Optional)

To run the dashboard for monitoring stream performance:

python dashboard.py

This provides:

    Client connection history

    Frame delivery rate

    Visual alerts on missed/skipped frames

📝 Sample Logs

[INFO] 2025-05-29 12:00:34 — Frame 156 broadcasted to 3 clients
[INFO] 2025-05-29 12:00:38 — New client connected: 192.168.1.7
[WARNING] 2025-05-29 12:01:12 — Frame skipped due to encoding delay

📚 Educational Value

This project is a practical example of:

    Real-time server-client communication using WebSockets

    Multithreading and synchronization in Python

    Efficient media streaming with OpenCV

    Backend-to-frontend integration for low-latency delivery

    Logging and performance monitoring in live systems

🛡️ .gitignore Recommendation

__pycache__/
*.pyc
log/
*.log
video/sample.mp4
.env

🔮 Potential Improvements

    Support for live webcam streaming

    Adaptive bitrate handling

    Client buffering and reconnection logic

    Pause/play sync across clients

    WebRTC integration for P2P delivery

    Deployment with Docker for scalability

👤 Author

Developed by Mohammad Hasan Salimi
📧 mamad.h.salimi@gmail.com
🔗 GitHub Profile
📄 License

This project is licensed under the MIT License.

