import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cyber Crime Files Dashboard", page_icon="📊", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #ffffff; }
    h1 { color: #00ff66; text-align: center; font-family: 'Courier New', Courier, monospace; font-weight: bold; }
    h2 { color: #00e5ff; font-family: 'Courier New', sans-serif; }
    .stRadio > label { color: #ffffff !important; font-size: 16px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("🕵️‍♂️ Cyber Crime Files: Analytics Dashboard")
st.write("مرحباً بكم في لوحة تحكم المحققين السيبرانيين من تقديم تيم **The Cyber Detectives**. اختبروا وعيكم الآن وشاهدوا تحليل البيانات حياً!")
st.markdown("---")

# 1. محاكاة جريمة أوبر
st.header("🎯 الملف الأول: فخ أوبر (MFA Fatigue)")
st.subheader("في الساعة 3 فجراً، هاتف الموظف يمتلئ بإشعارات تسجيل دخول متكررة. يتلقى رسالة WhatsApp من شخص يدعي أنه الدعم الفني يطلب منه الضغط على 'Approve' لإيقاف الإزعاج. ما هو قرارك؟")

q1_choice = st.radio("اختر قرارك:", ["الضغط على 'Approve' لإيقاف الإشعارات والنوم.", "رفض الطلب فوراً (Deny) والإبلاغ عن الحادثة لفريق الأمان."], index=None, key="q1")

if q1_choice:
    if "رفض الطلب" in q1_choice:
        st.success("✅ قرار محترف! أنت منعت هجوم الـ MFA Fatigue وحميت شركتك.")
        chart_data = pd.DataFrame({"النسبة %": [15, 85]}, index=["ضغطوا Approve (ضحايا)", "رفضوا الطلب (محققين)"])
        st.bar_chart(chart_data, color="#00ff66")
    else:
        st.error("❌ كارثة رقمية! أنت سلمت مفاتيح الشبكة للهكر، وده بالظبط اللي دمر شركة Uber سنة 2022!")
        chart_data = pd.DataFrame({"النسبة %": [85, 15]}, index=["ضغطوا Approve (ضحايا)", "رفضوا الطلب (محققين)"])
        st.bar_chart(chart_data, color="#ff3333")

st.markdown("---")

# 2. محاكاة جريمة كولونيال بايبلاين
st.header("🎯 الملف الثاني: شلل شركة البنزين (Colonial Pipeline)")
st.subheader("شركة ضخمة تركت حساب شبكة افتراضية (VPN) قديم كان يستخدمه الموظفون سابقاً، بدون تفعيل التحقق الثنائي (MFA)، وبكلمة مرور عادية. كيف يستغل الهكر هذا الحساب في هجوم فدية؟")

q2_choice = st.radio("اختر التحليل الصحيح للجريمة:", ["الهكر لا يمكنه دخول الشبكة لأن الحساب قديم وغير مستخدم حالياً.", "الهكر سيستخدم برامج تخمين تلقائية (Brute Force) لكسر الباسورد، وبسبب غياب الـ MFA سيدخل ويشفر السيرفرات ويطلب فدية."], index=None, key="q2")

if q2_choice:
    if "الهكر سيستخدم برامج" in q2_choice:
        st.success("✅ تحليل دقيق! هذا الإهمال في الـ Cyber Hygiene هو ما تسبب في كارثة خط أنابيب Colonial Pipeline.")
        attack_data = pd.DataFrame({"عدد الهجمات عالمياً": [40, 35, 25]}, index=["هجمات فدية (Ransomware)", "هندسة اجتماعية", "أخرى"])
        st.area_chart(attack_data, color="#00e5ff")
    else:
        st.error("❌ غير صحيح! الحسابات القديمة المتروكة (Legacy Accounts) هي الهدف المفضل للهكرز لأنها غير مراقبة.")

st.markdown("---")

# 3. محاكاة جريمة سولار ويندز
st.header("🎯 الملف الثالث: الاختراق الصامت (SolarWinds)")
st.subheader("تلقى قسم تكنولوجيا المعلومات في شركتك إشعاراً بتوفر 'تحديث رسمي ونظيف' من شركة برمجيات معتمدة تتعاملون معها. كيف تتأكد من أن هذا التحديث آمن؟")

q3_choice = st.radio("اختر استراتيجية الدفاع:", ["تحميل التحديث فوراً على كل الأجهزة والوزارات لأن المصدر شركة موثوقة.", "اختبار التحديث أولاً في بيئة معزولة (Sandbox) وفحصه، وتطبيق نظام إدارة مخاطر الطرف الثالث."], index=None, key="q3")

if q3_choice:
    if "اختبار التحديث أولاً" in q3_choice:
        st.success("✅ تفكير سيبراني متقدم! هجمات سلاسل الإمداد (Supply Chain Attacks) بتستغل الثقة العمياء لتمرير الكود الخبيث.")
    else:
        st.error("❌ فخ خطير! هجوم SolarWinds نجح بالظبط لأن الضحايا وثقوا في التحديث الرسمي دون فحص معزول.")

st.markdown("---")
st.info("Team The Cyber slueuths يشكركم على المشاركة. الأمن السيبراني يبدأ بوعيك أنت أولاً. 🛡️")
