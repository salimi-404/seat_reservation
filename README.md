
# 🎟️ سامانه شبیه‌سازی رزرو صندلی با Flask

یک پروژه‌ی شبیه‌سازی رزرو صندلی با استفاده از **Flask** و **چندریسمانی (Multi-threading)** به زبان پایتون.  
در این سامانه، کاربران (ریسمان‌ها) با اولویت‌های مختلف تلاش می‌کنند تا تعدادی صندلی رزرو کنند.  
سامانه از منطق اولویت‌محور، احتمال لغو تصادفی، تلاش مجدد برای درخواست‌های ناموفق و یک داشبورد گرافیکی حرفه‌ای برای نمایش وضعیت رزروها پشتیبانی می‌کند.

---

## ✨ امکانات و ویژگی‌ها

- ✅ پشتیبانی از چندریسمانی (Multi-threading) برای شبیه‌سازی هم‌زمان درخواست‌ها
- 🔢 تعیین تعداد صندلی و محدودیت تعداد درخواست همزمان
- 🎯 استفاده از اولویت و زمان ورود برای تصمیم‌گیری در رزرو
- 🔁 تلاش مجدد (Retry) برای درخواست‌های ناموفق
- 📉 داشبورد وب تعاملی شامل:
  - نمودار میله‌ای و دایره‌ای برای وضعیت رزروها
  - نمایش تعداد درخواست‌ها بر حسب تعداد صندلی
  - نقشه گرافیکی صندلی‌ها
  - جدول لاگ با جزئیات کامل
- 🧠 الگوریتم هیبریدی مدیریت درخواست‌ها
- 🧪 تست‌های خودکار با استفاده از `pytest`
- 🛠 ساختار ماژولار و قابل گسترش مبتنی بر معماری Flask

---

## 📁 ساختار پروژه
```
.
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   └── routes.cpython-313.pyc
│   ├── routes.py
│   ├── scheduler
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   ├── logger.cpython-313.pyc
│   │   │   ├── reservation_thread.cpython-313.pyc
│   │   │   ├── scheduler.cpython-313.pyc
│   │   │   └── seat_manager.cpython-313.pyc
│   │   ├── reservation_thread.py
│   │   ├── scheduler.py
│   │   └── seat_manager.py
│   ├── static
│   └── templates
│       └── index.html
├── log.txt
├── README.md
├── requirements.txt
├── run.py
├── seat_state.json
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-313.pyc
    │   ├── test_logger.cpython-313-pytest-8.3.5.pyc
    │   └── test_seat_manager.cpython-313-pytest-8.3.5.pyc
    └── test_seat_manager.py
```



---

## 🚀 نصب و اجرای پروژه

### ۱. کلون کردن پروژه

```bash
git clone https://github.com/YOUR_USERNAME/seat-reservation-system.git
cd seat-reservation-system
```
۲. نصب وابستگی‌ها
```
python -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate
pip install -r requirements.txt
```
۳. اجرای برنامه (رابط گرافیکی)
```
python run.py
```
آدرس: http://localhost:5000
اجرای حالت CLI (بدون UI)
```
python run.py cli
```
در این حالت دو فایل خروجی تولید می‌شود:
```
    log.txt

    seat_state.json
```
🧪 اجرای تست‌ها
```
pip install pytest
pytest
```
✅ تست‌های پروژه، بخش‌های اصلی مثل مدیریت صندلی و سیستم لاگ را پوشش می‌دهند.
📊 پیش‌نمایش داشبورد

پس از اجرا، UI شامل موارد زیر خواهد بود:

    فرم آغاز شبیه‌سازی

    ۳ نمودار (Bar, Pie, Request Distribution)

    نمایش گرافیکی نقشه صندلی‌ها

    جدول کامل لاگ

🧠 تکنولوژی‌های استفاده‌شده در پروژه
تکنولوژی / ابزار	توضیح
```
Python 3.13	زبان اصلی برنامه‌نویسی
Flask	فریم‌ورک وب برای ایجاد UI و API
threading	برای شبیه‌سازی هم‌زمان کاربران
queue.PriorityQueue	زمان‌بندی با اولویت‌بندی
Chart.js (CDN)	رسم نمودارهای داینامیک در UI
HTML + CSS	طراحی رابط گرافیکی
Jinja2	قالب‌دهی HTML در Flask
Pytest	تست‌های خودکار
```
🔮 بهبودهای پیشنهادی (TODO)

استفاده از دیتابیس برای ذخیره‌سازی دائمی اطلاعات

آپدیت زنده داشبورد با WebSocket

RESTful API برای رزرو خودکار از بیرون

احراز هویت و چندکاربره‌سازی

اجرای پروژه با Docker

بهینه‌سازی برای موبایل

ارسال ایمیل یا نوتیفیکیشن پس از رزرو موفق

👨‍💻 توسعه‌دهنده
Git Hub : https://github.com/salimi-404
Email : mamad.h.salimi@gmail.com
📝 مجوز (License)

این پروژه تحت مجوز MIT منتشر شده است.
آزادید از آن استفاده، کپی، تغییر و منتشر کنید — تنها کافی‌ست کپی مجوز در پروژه باقی بماند.
