import streamlit as st
import pandas as pd

# إعدادات الصفحة والعنوان المتصفح
st.set_page_config(page_title="متابعة الطالبات الذكي", page_icon="🎓", layout="wide")

# عنوان التطبيق الرئيسي
st.markdown("<h1 style='text-align: center; color: #4A4A4A;'>🎓 تطبيق متابعة الطالبات الذكي</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# تهيئة متغير الجلسة (Session State) لمعرفة الأيقونة النشطة
if 'active_action' not in st.session_state:
    st.session_state.active_action = None

# إنشاء 4 أعمدة بجانب بعضها البعض للأيقونات التفاعلية
col1, col2, col3, col4 = st.columns(4)

# الأيقونة الأولى: إضافة ملف إكسل (باللون الأزرق)
with col1:
    st.markdown("<div style='text-align: center; font-size: 40px;'>📂</div>", unsafe_allow_html=True)
    if st.button("إضافة ملف إكسل", key="btn_upload", use_container_width=True, type="primary"):
        st.session_state.active_action = "upload"

# الأيقونة الثانية: تحليل النتائج (باللون الأخضر)
with col2:
    st.markdown("<div style='text-align: center; font-size: 40px;'>📊</div>", unsafe_allow_html=True)
    if st.button("تحليل النتائج", key="btn_analyze", use_container_width=True):
        st.session_state.active_action = "analyze"

# الأيقونة الثالثة: نقاط الضعف والقوة (باللون البرتقالي/الأصفر)
with col3:
    st.markdown("<div style='text-align: center; font-size: 40px;'>🔍</div>", unsafe_allow_html=True)
    if st.button("نقاط الضعف والقوة", key="btn_swot", use_container_width=True):
        st.session_state.active_action = "swot"

# الأيقونة الرابعة: تقديم تغذية راجعة (باللون الأحمر/الوردي)
with col4:
    st.markdown("<div style='text-align: center; font-size: 40px;'>💡</div>", unsafe_allow_html=True)
    if st.button("تقديم تغذية راجعة", key="btn_feedback", use_container_width=True):
        st.session_state.active_action = "feedback"

st.markdown("<br><hr>", unsafe_allow_html=True)

# --- استجابة التطبيق للأيقونات التفاعلية عند الضغط عليها ---

if st.session_state.active_action == "upload":
    st.subheader("📂 قسم إضافة ملف إكسل")
    uploaded_file = st.file_uploader("الرجاء اختيار ملف إكسل الخاص بدرجات الطالبات", type=["xlsx", "xls"])
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            st.success("تم رفع الملف بنجاح!")
            st.dataframe(df.head()) # عرض عينة من البيانات
        except Exception as e:
            st.error(f"حدث خطأ أثناء قراءة الملف: {e}")

elif st.session_state.active_action == "analyze":
    st.subheader("📊 قسم تحليل النتائج")
    st.info("هنا يتم احتساب المتوسطات العامة ونسب النجاح والرسوب فور رفع الملف.")
    # مثال توضيحي محاكي للتحليل
    st.metric(label="متوسط درجات الفصل", value="88.5%")

elif st.session_state.active_action == "swot":
    st.subheader("🔍 قسم تحديد نقاط الضعف والقوة")
    st.warning("يتم هنا فرز الطالبات المتميزات والطالبات اللاتي يحتجن إلى دعم إضافي.")
    # توزيع توضيحي بسيط
    col_strength, col_weakness = st.columns(2)
    with col_strength:
        st.success("💪 نقاط القوة: تميز في مهارات التفكير الإبداعي")
    with col_weakness:
        st.error("⚠️ نقاط الضعف: تحديات في مهارات العمليات الحسابية المتقدمة")

elif st.session_state.active_action == "feedback":
    st.subheader("💡 قسم تقديم التغذية الراجعة")
    st.success("توليد تقارير وتوجيهات تلقائية بناءً على مستويات الطالبات.")
    txt_feedback = st.text_area("اكتب توجيه عام للمعلمات أو أولياء الأمور:", "يرجى التركيز على مراجعة الفصول الثلاثة الأولى...")
    if st.button("حفظ التغذية الراجعة"):
        st.write("تم حفظ التقرير بنجاح!")
