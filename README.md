# مشروع Web API المتكامل بـ Python (بديل مشروع ASP.NET Core)

تم بناء هذا المشروع بالكامل باستخدام **Python (FastAPI + SQLAlchemy)** تنفيذاً لمطلوب الواجب الجامعي للأسبوع الخامس مع استبدال تقنية **ASP.NET Core** بتقنية **Python Web API**.

---

## 🔁 مقارنة المكونات (ASP.NET Core مقابل Python FastAPI)

| متطلب الواجب | ASP.NET Core | Python (المطبق في المشروع) |
| :--- | :--- | :--- |
| **إدارة المستخدمين والمصادقة** | ASP.NET Core Identity | SQLAlchemy User Model + Passlib (bcrypt) |
| **مخطط التوكن (JWT Schema)** | JwtBearer Authentication Schema | PyJWT + FastAPI HTTPBearer Security |
| **اختبار التوكن في Swagger** | Swagger UI (`Authorize` Button) | Swagger UI تفاعلي أوتوماتيكي عبر `/docs` |
| **الربط مع قاعدة البيانات** | Entity Framework Core (EF Core) | SQLAlchemy ORM + SQLite/PostgreSQL |
| **عمليات CRUD والحماية** | Controllers + `[Authorize]` | APIRouter + `Depends(get_current_user)` |
| **الاستضافة أونلاين** | MonsterASP.NET / RunASP | Render.com / PythonAnywhere / Railway |

---

## 📁 هيكل المشروع (Project Structure)

```
APItaklif/
│── database.py            # إعداد الاتصال بقاعدة البيانات (SQLAlchemy Engine & Session)
│── models.py              # نماذج الجداول: المستخدمين (Users) والمنتجات (Products)
│── schemas.py             # Pydantic Schemas للتحقق من البيانات مدخلات ومخرجات
│── auth.py                # تشفير كلمات المرور، توليد JWT والتحقق منه وحماية المسارات
│── routers/
│   ├── __init__.py
│   ├── auth_router.py     # مسارات التسجيل وتسجيل الدخول (/auth/register & /auth/login)
│   └── products_router.py # عمليات CRUD الكاملة المدمجة مع قاعدة البيانات والحماية
│── main.py                # نقطة الانطلاق لتطبيق FastAPI وإعداد واجهة Swagger UI
│── requirements.txt       # ملف المكتبات المطلوبة للتثبيت
│── Procfile               # ملف التوجيه الخاص باستضافة Heroku/Render
│── render.yaml            # ملف إعدادات التوزيع المباشر على Render
└── README.md              # دليل التشغيل والاستضافة
```

---

## 🚀 كيفية التشغيل والتجربة على الجهاز المحلي (Local Execution)

### 1. تثبيت المكتبات المطلوبة:
افتح موجه الأوامر (Terminal/PowerShell) في مجلد المشروع وقم بتنفيذ الأمر التالي:
```bash
pip install -r requirements.txt
```

### 2. تشغيل الـ API:
```bash
python main.py
```
أو عبر uvicorn مباشرة:
```bash
uvicorn main:app --reload
```

سيتم تشغيل السيرفر على الرابط المحلي:
`http://127.0.0.1:8000`

---

## 🧪 اختبار الـ API واختبار زر Authorize في Swagger UI

1. افتح الرابط الحي للـ Swagger UI في المتصفح:
   `http://127.0.0.1:8000/docs`

2. **التسجيل (Register):**
   - افتح Endpoint: `POST /auth/register`
   - اضغط على **Try it out**.
   - أدخل اسم المستخدم، البريد، وكلمة المرور واضغط **Execute**.

3. **تسجيل الدخول (Login) والحصول على التوكن:**
   - افتح Endpoint: `POST /auth/login`
   - أدخل اسم المستخدم وكلمة المرور واضغط **Execute**.
   - انسخ التوكن `access_token` الناتج من الاستجابة.

4. **تفعيل الحماية (Authorize Button):**
   - اضغط على زر **Authorize** (الموجود في أعلى الصفحة جهة اليمين وعليه رمز القفل).
   - ضع التوكن الذي نسخته في حقل Value ثم اضغط **Authorize**.
   - الآن أصبحت كافة العمليات المحمية مفعلة بحسابك!

5. **اختبار عمليات CRUD المحمية (`/products`):**
   - `POST /products/`: إضافة منتج جديد مرتبط بحسابك.
   - `GET /products/`: عرض جميع المنتجات من قاعدة البيانات.
   - `GET /products/{id}`: جلب تفاصيل منتج محدد عبر ID.
   - `PUT /products/{id}`: تعديل بيانات منتج محدد.
   - `DELETE /products/{id}`: حذف منتج محدد.

---

## 🌐 رفع واستضافة الـ API أونلاين على منصة Render (Online Hosting Guide)

للحصول على رابط حي لـ Swagger يعمل من أي متصفح لإرساله للدكتور:

1. **انشئ مستودع (Repository) جديد على GitHub**:
   - ارفع جميع ملفات هذا المشروع إلى حسابك في GitHub.

2. **سجل في منصة [Render.com](https://render.com)**:
   - قم بإنشاء حساب مجاني أو سجّل الدخول عبر GitHub.

3. **إنشاء Web Service جديد**:
   - اضغط على **New +** ثم اختر **Web Service**.
   - اربط حساب GitHub واختر مستودع المشروع (`APItaklif`).

4. **إعدادات الخدمة على Render**:
   - **Name**: `my-python-api` (أو أي اسم تفضله).
   - **Environment**: `Python 3`.
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

5. **الضغط على Deploy Web Service**:
   - خلال دقيقة إلى دقيقتين سيكتمل الرفع وسيظهر لك الرابط العام للخدمة مثل:
   `https://my-python-api.onrender.com`

6. **رابط Swagger النهائي**:
   - الرابط الحي لـ Swagger سيكون:
   `https://my-python-api.onrender.com/docs`
   - سيعمل الرابط من أي متصفح ومن أي جهاز مع إمكانية تجربة زر **Authorize** وعمليات الـ CRUD وقاعدة البيانات أونلاين مباشرة!
