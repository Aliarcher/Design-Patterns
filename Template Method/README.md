# Template Method Pattern Example (Python)

در این الگو، یک کلاس پدر (Abstract Class) متدی به نام `template_method` تعریف می‌کند که ساختار اجرای سایر متدها را مشخص می‌کند. بعضی از این متدها پیاده‌سازی پیش‌فرض دارند و بعضی باید در کلاس‌های فرزند override شوند.

---

## 📂 ساختار کلاس‌ها

- **Top (Abstract Class)**
  - متد `template_method` را پیاده‌سازی می‌کند (این متد تغییر نمی‌کند).
  - شامل متدهای:
    - `first_method` → پیاده‌سازی شده
    - `second_method` → پیاده‌سازی شده
    - `third_method` → انتزاعی
    - `fourth_method` → انتزاعی

- **One (Subclass of Top)**
  - مثال اول برای متدهاییی که باید override شوند `third_method` و `fourth_method` را پیاده‌سازی می‌کند.

- **Two (Subclass of Top)**
  - مثال دوم برای متدهاییی که باید override شوند `third_method` و `fourth_method` را پیاده‌سازی می‌کند.

---

<img width="575" height="559" alt="template_method" src="https://github.com/user-attachments/assets/4f8feaaa-17d4-4562-97e2-19fd86ad3895" />
