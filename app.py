import streamlit as st
import pandas as pd
import io

# 1. Page Configuration
st.set_page_config(page_title="منظومة متابعة الطالبات الذكية", page_icon="🎓", layout="wide")

st.markdown("""
    <div style='background-color: #1E3A8A; padding: 20px; border-radius: 10px; margin-bottom: 25px;'>
        <h1 style='text-align: center; color: white; margin: 0;'>🎓 منظومة متابعة الطالبات الذكية التفاعلية</h1>
        <p style='text-align: center; color: #E2E8F0; margin: 5px 0 0 0;'>منصة القياس والتحليل الرقمي المتقدم للأداء الأكاديمي والتحصيلي</p>
    </div>
""", unsafe_allow_html=True)

if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "school"

# 2. Control Panel (8 Buttons)
st.markdown("### 🎛️ لوحة التحكم والعمليات السريعة")

r1_c1, r1_c2, r1_c3, r1_c4 = st.columns(4)
with r1_c1:
    st.markdown("<div style='text-align: center; font-size: 35px;'>📂</div>", unsafe_allow_html=True)
    if st.button("إضافة درجات المدرسة (إكسل)", key="tab_school", use_container_width=True):
        st.session_state.active_tab = "school"
with r1_c2:
    st.markdown("<div style='text-align: center; font-size: 35px;'>🧪</div>", unsafe_allow_html=True)
    if st.button("إدراج درجات القدرات (إكسل)", key="tab_qodrat", use_container_width=True):
        st.session_state.active_tab = "qodrat"
with r1_c3:
    st.markdown("<div style='text-align: center; font-size: 35px;'>🧬</div>", unsafe_allow_html=True)
    if st.button("إدراج درجات التحصيلي (إكسل)", key="tab_tahsili", use_container_width=True):
        st.session_state.active_tab = "tahsili"
with r1_c4:
    st.markdown("<div style='text-align: center; font-size: 35px;'>📊</div>", unsafe_allow_html=True)
    if st.button("تحليل الأداء العام للنتائج", key="tab_analyze", use_container_width=True):
        st.session_state.active_tab = "analyze"

r2_c1, r2_c2, r2_c3, r2_c4 = st.columns(4)
with r2_c1:
    st.markdown("<div style='text-align: center; font-size: 35px;'>📉</div>", unsafe_allow_html=True)
    if st.button("تحليل بيانات القدرات والتحصيلي", key="tab_national", use_container_width=True):
        st.session_state.active_tab = "national"
with r2_c2:
    st.markdown("<div style='text-align: center; font-size: 35px;'>🎯</div>", unsafe_allow_html=True)
    if st.button("حساب الفجوات الدولية", key="tab_gaps", use_container_width=True):
        st.session_state.active_tab = "gaps"
with r2_c3:
    st.markdown("<div style='text-align: center; font-size: 35px;'>🔍</div>", unsafe_allow_html=True)
    if st.button("نقاط الضعف والقوة الذكية", key="tab_swot", use_container_width=True):
        st.session_state.active_tab = "swot"
with r2_c4:
    st.markdown("<div style='text-align: center; font-size: 35px;'>💬</div>", unsafe_allow_html=True)
    if st.button("مراسلة ولي الأمر والتغذية الراجعة", key="tab_chat", use_container_width=True):
        st.session_state.active_tab = "chat"

st.markdown("<br><hr>", unsafe_allow_html=True)

# Demo Data Generator
def create_demo_file(file_type):
    buffer = io.BytesIO()
    if file_type == "school":
        data = {'الرقم الأكاديمي': [101, 102, 103, 104, 105], 'اسم الطالبة': ['سارة أحمد', 'نورة عبد الله', 'ريم محمد', 'هند سلطان', 'أمل فهد'], 'الرياضيات': [95, 48, 88, 72, 60], 'العلوم': [92, 55, 85, 64, 45], 'اللغة العربية': [98, 62, 90, 78, 50]}
    elif file_type == "qodrat":
        data = {'الرقم الأكاديمي': [101, 102, 103, 104, 105], 'اسم الطالبة': ['سارة أحمد', 'نورة عبد الله', 'ريم محمد', 'هند سلطان', 'أمل فهد'], 'اللفظي': [85, 55, 90, 70, 65], 'الكمي': [90, 50, 85, 68, 58]}
    else:
        data = {'الرقم الأكاديمي': [101, 102, 103, 104, 105], 'اسم الطالبة': ['سارة أحمد', 'نورة عبد الله', 'ريم محمد', 'هند سلطان', 'أمل فهد'], 'التحصيلي علمي': [88, 48, 92, 71, 60]}
    df = pd.DataFrame(data)
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    return buffer.getvalue()

# Initialize Session Data
if 'df_school' not in st.session_state:
    st.session_state.df_school = pd.DataFrame({'الرقم الأكاديمي': [101, 102, 103, 104, 105], 'اسم الطالبة': ['سارة أحمد', 'نورة عبد الله', 'ريم محمد', 'هند سلطان', 'أمل فهد'], 'الرياضيات': [95, 48, 88, 72, 60], 'العلوم': [92, 55, 85, 64, 45], 'اللغة العربية': [98, 62, 90, 78, 50]})
if 'df_qodrat' not in st.session_state:
    st.session_state.df_qodrat = pd.DataFrame({'الرقم الأكاديمي': [101, 102, 103, 104, 105], 'اسم الطالبة': ['سارة أحمد', 'نورة عبد الله', 'ريم محمد', 'هند سلطان', 'أمل فهد'], 'اللفظي': [85, 55, 90, 70, 65], 'الكمي': [90, 50, 85, 68, 58]})
if 'df_tahsili' not in st.session_state:
    st.session_state.df_tahsili = pd.DataFrame({'الرقم الأكاديمي': [101, 102, 103, 104, 105], 'اسم الطالبة': ['سارة أحمد', 'نورة عبد الله', 'ريم محمد', 'هند سلطان', 'أمل فهد'], 'التحصيلي علمي': [88, 48, 92, 71, 60]})

# 3. Dynamic Tabs Routing
if st.session_state.active_tab == "school":
    st.subheader("📂 إدارة وإدراج درجات اختبارات المدرسة")
    st.download_button("📥 تحميل قالب ملف المدرسة التجريبي", data=create_demo_file("school"), file_name="قالب_درجات_المدرسة.xlsx")
    file = st.file_uploader("ارفع ملف إكسل لدرجات المدرسة الحقيقية", type=["xlsx", "xls"])
    if file:
        st.session_state.df_school = pd.read_excel(file)
        st.success("تم تحديث بيانات المدرسة بنجاح!")
    st.dataframe(st.session_state.df_school, use_container_width=True)

elif st.session_state.active_tab == "qodrat":
    st.subheader("🧪 إدارة وإدراج درجات اختبار القدرات العامة (قياس)")
    st.download_button("📥 تحميل قالب ملف القدرات التجريبي", data=create_demo_file("qodrat"), file_name="قالب_درجات_القدرات.xlsx")
    file = st.file_uploader("ارفع ملف إكسل لدرجات القدرات الحقيقية", type=["xlsx", "xls"])
    if file:
        st.session_state.df_qodrat = pd.read_excel(file)
        st.success("تم تحديث بيانات القدرات بنجاح!")
    st.dataframe(st.session_state.df_qodrat, use_container_width=True)

elif st.session_state.active_tab == "tahsili":
    st.subheader("🧬 إدارة وإدراج درجات الاختبار التحصيلي الوطني")
    st.download_button("📥 تحميل قالب ملف التحصيلي التجريبي", data=create_demo_file("tahsili"), file_name="قالب_درجات_التحصيلي.xlsx")
    file = st.file_uploader("ارفع ملف إكسل لدرجات التحصيلي الحقيقية", type=["xlsx", "xls"])
    if file:
        st.session_state.df_tahsili = pd.read_excel(file)
        st.success("تم تحديث بيانات التحصيلي بنجاح!")
    st.dataframe(st.session_state.df_tahsili, use_container_width=True)

elif st.session_state.active_tab == "analyze":
    st.subheader("📊 تحليل الأداء العام والرسوم البيانية للمدرسة")
    df = st.session_state.df_school
    subjects = df.columns.drop(['الرقم الأكاديمي', 'اسم الطالبة'])
    
    m1, m2 = st.columns(2)
    m1.metric("أعلى متوسط مادة في المدرسة", f"{df[subjects].mean().max().round(1)}")
    m2.metric("أدنى متوسط مادة في المدرسة", f"{df[subjects].mean().min().round(1)}")
    
    st.write("#### 📈 الرسم البياني المقارن لمواد المدرسة لكل طالبة:")
    st.bar_chart(df.set_index('اسم الطالبة')[subjects])

elif st.session_state.active_tab == "national":
    st.subheader("📉 جدول وتحليل بيانات اختبارات القدرات والتحصيلي المدمج")
    try:
        m_df = pd.merge(st.session_state.df_qodrat, st.session_state.df_tahsili, on=['الرقم الأكاديمي', 'اسم الطالبة'])
        st.dataframe(m_df, use_container_width=True)
        national_subjects = m_df.columns.drop(['الرقم الأكاديمي', 'اسم الطالبة'])
        st.write("### 📊 مقارنة أداء الطالبات في الاختبارات الوطنية:")
        st.line_chart(m_df.set_index('اسم الطالبة')[national_subjects])
    except Exception as e:
        st.error(f"خطأ في دمج البيانات: {e}")

elif st.session_state.active_tab == "gaps":
    st.subheader("🎯 مؤشر حساب الفجوات الأكاديمية بين المدرسة والاختبارات الدولية")
    df_s = st.session_state.df_school
    math_avg = df_s['الرياضيات'].mean()
    sci_avg = df_s['العلوم'].mean()
    
    converted_math = (math_avg / 100) * 600
    converted_sci = (sci_avg / 100) * 600
    
    gap_math = converted_math - 500
    gap_sci = converted_sci - 500
    
    g1, g2 = st.columns(2)
    g1.metric("فجوة مادة الرياضيات الدولية", f"{gap_math:.1f} نقطة")
    g2.metric("فجوة مادة العلوم الدولية", f"{gap_sci:.1f} نقطة")
    
    gap_df = pd.DataFrame({
        'المعيار': ['معدل المدرسة الحالي', 'المستهدف الدولي المعتمد'],
        'الرياضيات': [converted_math, 500],
        'العلوم': [converted_sci, 500]
    }).set_index('المعيار')
    st.bar_chart(gap_df)

elif st.session_state.active_tab == "swot":
    st.subheader("🔍 مصفوفة نقاط الضعف والقوة الذكية للطالبات")
    df = st.session_state.df_school
    subjects = df.columns.drop(['الرقم الأكاديمي', 'اسم الطالبة'])
    for idx, row in df.iterrows():
        with st.expander(f"🔎 تقرير الطالبة: {row['اسم الطالبة']}"):
            str_list = [f"{sub} ({row[sub]})" for sub in subjects if row[sub] >= 85]
            weak_list = [f"{sub} ({row[sub]})" for sub in subjects if row[sub] < 60]
            st.write(f"💪 نقاط التميز والقوة: {', '.join(str_list) if str_list else 'مستقرة'}")
            st.write(f"⚠️ نقاط الضعف والدعم: {', '.join(weak_list) if weak_list else 'لا توجد فجوات خطيرة'}")

elif st.session_state.active_tab == "chat":
    st.subheader("💬 نظام إرسال الرسائل والتغذية الراجعة لأولياء الأمور")
    df = st.session_state.df_school
    selected_student = st.selectbox("اختر اسم الطالبة:", df['اسم الطالبة'])
    custom_msg = f"المكرم ولي أمر الطالبة/ {selected_student}\n\nنود إحاطتكم علماً بمستواها الأكاديمي الحالي بتقرير المدرسة.\nنأمل التعاون لتعزيز مهاراتها المستهدفة."
    final_text = st.text_area("نص رسالة الإشعار:", custom_msg, height=150)
    if st.button("📱 إرسال إشعار SMS محاكي"):
        st.success(f"✅ تم الإشعار بنجاح لولي أمر الطالبة: {selected_student}")
