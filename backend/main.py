# مرحبًا بك في ملف المحرك الرئيسي لمشروع مركز الصيانة
# هذا الملف يجمع كل الوظائف التي صممناها معًا (من المرحلة 5 إلى 10)

# =================================================================
# 1. استيراد الأدوات اللازمة
# =================================================================
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional # سنحتاجها لاحقًا

# =================================================================
# 2. إنشاء التطبيق الرئيسي (أساس المشروع)
# =================================================================
app = FastAPI()

# =================================================================
# 3. تصميم نماذج البيانات (الاستمارات الإلكترونية)
# =================================================================

# نموذج لبيانات العميل
class Customer(BaseModel):
    customer_name: str
    phone_number: str

# نموذج لبيانات السيارة
class Car(BaseModel):
    customer_id: int
    make: str
    model: str
    license_plate: str

# نموذج لبيانات أمر الشغل
class JobOrder(BaseModel):
    car_id: int
    customer_complaint: str
    reception_notes: str
    odometer_reading: int

# نموذج لبيانات تحديث التشخيص الفني
class DiagnosisUpdate(BaseModel):
    technical_diagnosis: str
    labor_cost: float

# نموذج لبيانات إضافة قطعة غيار
class AddPartToJobOrder(BaseModel):
    part_id: int
    quantity_used: int

# نموذج لبيانات عملية الدفع
class PaymentDetails(BaseModel):
    amount_paid: float
    payment_method: str

# =================================================================
# 4. برمجة وظائف النظام (عقل النظام المفكر)
# =================================================================

# --- رسالة ترحيبية ---
@app.get("/")
def read_root():
    return {"message": "أهلاً بك في الواجهة الخلفية (Backend) لنظام إدارة مركز الصيانة"}

# --- وظائف العملاء والسيارات ---
@app.post("/add_customer/")
def create_customer(customer: Customer):
    print(f"تم تسجيل العميل: {customer.customer_name}")
    # هنا سيتم كتابة كود الحفظ في قاعدة البيانات
    return {"message": f"تم تسجيل العميل '{customer.customer_name}' بنجاح!"}

@app.post("/add_car/")
def create_car(car: Car):
    print(f"تم تسجيل سيارة برقم لوحة: {car.license_plate}")
    # هنا سيتم كتابة كود الحفظ في قاعدة البيانات
    return {"message": f"تم تسجيل السيارة '{car.license_plate}' بنجاح!"}

# --- وظائف أوامر الشغل ---
@app.post("/create_job_order/")
def create_job_order(job_order: JobOrder):
    new_job_order_id = 1053 # رقم وهمي للتوضيح
    print(f"تم إنشاء أمر شغل جديد برقم: {new_job_order_id}")
    return {"message": "تم فتح أمر الشغل بنجاح!", "job_order_id": new_job_order_id}

@app.get("/job_order/{job_order_id}")
def get_job_order_details(job_order_id: int):
    # هنا سنبحث في قاعدة البيانات ونرجع البيانات الحقيقية
    return {"job_order_id": job_order_id, "status": "قيد الفحص", "customer_complaint": "بيانات وهمية للتوضيح"}

@app.put("/job_order/{job_order_id}/diagnose")
def add_diagnosis(job_order_id: int, diagnosis: DiagnosisUpdate):
    print(f"تم تحديث التشخيص لأمر الشغل رقم: {job_order_id}")
    return {"message": f"تم تحديث أمر الشغل بنجاح!", "new_status": "في انتظار موافقة العميل"}

# --- وظائف المخزون ---
@app.post("/job_order/{job_order_id}/add_part")
def add_part_to_job_order(job_order_id: int, part_info: AddPartToJobOrder):
    print(f"تم صرف قطعة غيار رقم {part_info.part_id} لأمر الشغل {job_order_id}")
    return {"message": "تم إضافة قطعة الغيار وتحديث المخزون بنجاح!", "inventory_updated": True}

# --- وظائف الفوترة ---
@app.post("/job_order/{job_order_id}/create_invoice")
def create_invoice_for_job_order(job_order_id: int):
    print(f"تم إنشاء فاتورة لأمر الشغل: {job_order_id}")
    return {"message": "تم إنشاء الفاتورة بنجاح!", "invoice_id": 501, "total_amount": 1140.0}

@app.post("/invoice/{invoice_id}/record_payment")
def record_payment_for_invoice(invoice_id: int, payment: PaymentDetails):
    print(f"تم تسجيل دفعة للفاتورة: {invoice_id}")
    return {"message": "تم تسجيل الدفع بنجاح!", "new_status": "مدفوعة بالكامل"}
