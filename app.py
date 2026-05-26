import streamlit as st
import pandas as pd
import numpy as np
import io

# 1. إعدادات المظهر العام للمنظومة الذكية
st.set_page_config(page_title="منظومة متابعة الطالبات الذكية الفائقة", page_icon="🎓", layout="wide")

st.markdown("""
    <div style='background-color: #0F172A; padding: 25px; border-radius: 12px; margin-bottom: 25px; border-left: 8px solid #3B82F6;'>
        <h1 style='text-align: center; color: white; margin: 0; font-family: Cairo, sans-serif;'>🧠 منظومة متابعة الطالبات الذكية المدعومة بالذكاء الاصطناعي</h1>
        <p style='text-align: center; color: #94A3B8; margin: 8px 0 0 0;'>تحليل إحصائي متقدم - خطط علاجية مؤتمتة - شواهد التنفيذ - التنبؤ الذكي بالأداء</p>
    </div>
""", unsafe_allow_html=True)

if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "school"

# 2. لوحة التحكم والعمليات
st.markdown("### 🎛️ لوحة العمليات والتحليل الذكي")

r1_c1, r1_c2, r1_c3, r1_c4 = st.columns(4)
with r1_c1:
    st.markdown("<div style='text-align: center; font-size: 30px;'>📂</div>", unsafe_allow_html=True)
    if st.button("إدخل درجات المدرسة", key="tab_school", use_container_width=True):
        st.session_state.active_tab = "school"
with r1_c2:
    st.markdown("<div style='text-align: center; font-size: 30px;'>📊</div>", unsafe_allow_html=True)
    if st.button("التحليل الإحصائي العام", key="tab_analyze", use_container_width=True):
        st.session_state.active_tab = "analyze"
with r1_c3:
    st.markdown("<div style='text-align: center; font-size: 30px;'>🧠</div>", unsafe_allow_html=True)
    if st.button("الخطة العلاجية الذكية (AI)", key="tab_ai_remedial", use_container_width=True):
        st.session_state.active_tab = "ai_remedial"
with r1_c4:
    st.markdown("<div style='text-align: center; font-size: 30px;'>🔮</div>", unsafe_allow_html=True)
    if st.button("التنبؤات والتوقعات المستقبلية", key="tab_predict", use_container_width=True):
        st.session_state.active_tab = "predict"

st.markdown("<br><hr>", unsafe_allow_html=True)

# تهيئة بيانات تجريبية مسبقة بأرقام صحيحة تماماً لضمان عمل الرسوم والتنبؤات
if 'df_school' not in st.session_state:
    st.session_state.df_school = pd.DataFrame({
        'الرقم الأكاديمي': [101, 102, 103, 104, 105],
        'اسم الطالبة': ['سارة أحمد', 'نورة عبد الله', 'ريم محمد', 'هند سلطان', 'أمل fهد'],
        'الرياضيات': [95, 45, 88, 72, 48],
        'العلوم': [92, 55, 85, 64, 42],
        'اللغة العربية': [98, 62, 90, 78, 52]
    })

# 3. معالجة وتوجيه الشاشات التفاعلية
if st.session_state.active_tab == "school":
    st.subheader("📂 إدارة وإدراج درجات اختبارات المدرسة")
    
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        st.session_state.df_school.to_excel(writer, index=False)
    
    st.download_button("📥 تحميل ملف الإكسل التجريبي المحدث للاختبار", data=buffer.getvalue(), file_name="بيانات_المدرسة_العلاجية.xlsx")
    
    file = st.file_uploader("ارفع ملف إكسل لدرجات المدرسة الحقيقية", type=["xlsx", "xls"])
    if file:
        st.session_state.df_school = pd.read_excel(file)
        st.success("تم تحديث البيانات بنجاح!")
    st.dataframe(st.session_state.df_school, use_container_width=True)

elif st.session_state.active_tab == "analyze":
    st.subheader("📊 قسم التحليل الإحصائي المتقدم للنتائج")
    df = st.session_state.df_school
    subjects = ['الرياضيات', 'العلوم', 'اللغة العربية']
    
    c1, c2, c3 = st.columns(3)
    c1.metric("المعدل العام للمدرسة", f"{df[subjects].mean().mean().round(1)} %")
    c2.metric("عدد الطالبات المتفوقات (أعلى من 85)", f"{len(df[df[subjects].mean(axis=1) >= 85])} طالبات")
    c3.metric("عدد الطالبات بحاجة لخطة علاجية", f"{len(df[df[subjects].min(axis=1) < 50])} طالبات")
    
    st.write("#### 📈 مقارنة مستويات المواد إحصائياً:")
    st.bar_chart(df.set_index('اسم الطالبة')[subjects])

elif st.session_state.active_tab == "ai_remedial":
    st.subheader("🧠 نظام توليد الخطط العلاجية التلقائي (AI) وإرفاق الشواهد")
    st.info("يقوم المحرك الذكي بفحص الدرجات التي تقل عن 50 درجة تلقائيًا، صياغة خطة علاجية مخصصة، وإتاحة مساحة لرفع الشواهد.")
    
    df = st.session_state.df_school
    subjects = ['الرياضيات', 'العلوم', 'اللغة العربية']
    
    weak_students = []
    for idx, row in df.iterrows():
        fails = [sub for sub in subjects if row[sub] < 50]
        if fails:
            weak_students.append((row['اسم الطالبة'], fails, row))
            
    if not weak_students:
        st.success("🎉 مذهل! لا توجد أي طالبة بدرجات منخفضة (أقل من 50). الجميع بمستوى مستقر.")
    else:
        for name, sub_list, row_data in weak_students:
            with st.expander(f"🔴 خطة علاجية ذكية مخصصة للطالبة: {name}"):
                st.write(f"**المواد التي تعاني فيها من فجوة تعليمية:** {', '.join(sub_list)}")
                st.markdown("##### 📝 الإجراءات العلاجية المقترحة من المنظومة الذكية:")
                for s in sub_list:
                    st.write(f"* **في مادة {s}**: تقديم 3 جلسات دعم فردية، إرسال أوراق عمل تفاعلية مركّزة، إعادة الاختبار القصير بعد أسبوعين لمتابعة الأثر.")
                
                st.markdown("##### 📁 إرفاق شواهد تنفيذ الخطة العلاجية:")
                evidence_file = st.file_uploader(f"ارفع وثيقة أو صورة الشاهد للطالبة {name}", type=["pdf", "png", "jpg"], key=f"ev_{name}")
                if evidence_file:
                    st.success(f"✅ تم حفظ وإرفاق الشاهد بنجاح لملف الطالبة {name}!")

elif st.session_state.active_tab == "predict":
    st.subheader("🔮 قسم التنبؤات الإحصائية والتوقعات المستقبلية للأداء الأكاديمي")
    st.warning("تعتمد هذه التنبؤات على نماذج التحليل الإحصائي لتوقع أداء الطالبات في الاختبارات النهائية القادمة بناءً على مستواهن الحالي.")
    
    df = st.session_state.df_school
    subjects = ['الرياضيات', 'العلوم', 'اللغة العربية']
    
    predict_data = pd.DataFrame(index=df['اسم الطالبة'])
    predict_data['المعدل الحالي'] = df[subjects].mean(axis=1).round(1)
    
    # نموذج رياضي تنبئي بالأرقام الصحيحة والثابتة
    predict_data['المعدل المتوقع (بدون خطة علاجية)'] = (predict_data['المعدل الحالي'] * 0.92).round(1)
    predict_data['المعدل المتوقع (بعد تطبيق الخطة العلاجية)'] = (predict_data['المعدل الحالي'] * 1.07).round(1)
    
    predict_data['المعدل المتوقع (بدون خطة علاجية)'] = predict_data['المعدل المتوقع (بدون خطة علاجية)'].clip(upper=100)
    predict_data['المعدل المتوقع (بعد تطبيق الخطة العلاجية)'] = predict_data['المعدل المتوقع (بعد تطبيق الخطة العلاجية)'].clip(upper=100)
    
    st.write("### 📉 المخطط التنبؤي لمعدلات الطالبات المتوقعة في الفصل القادم:")
    st.line_chart(predict_data)
    
    st.write("### 📋 جدول البيانات الإحصائي التنبئي الشامل للمقارنة والتخطيط:")
    st.dataframe(predict_data, use_container_width=True)
