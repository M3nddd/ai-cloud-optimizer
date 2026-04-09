import os

# 1. ضع مفتاحك الجديد هنا مباشرة بين علامات التنصيص
OPENROUTER_API_KEY = "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"

# 2. سنستخدم النسخة المجانية من النموذج لضمان عدم وجود مشاكل في رصيد الحساب
MODEL = "nvidia/nemotron-3-super-120b-a12b:free"

# 3. سطر لنتأكد أن الكود يقرأ المفتاح الجديد وليس القديم
print(f"[DEBUG] USING KEY STARTING WITH: {OPENROUTER_API_KEY[:15]}...")