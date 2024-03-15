import datetime
import streamlit as st
import base64

def calculate_ovulation_day(first_day, n):
    try:
        n = int(n)
        ovulation_day = first_day + datetime.timedelta(days=n-14)
        return ovulation_day
    except ValueError:
        return None

def main():

    if 'first_day' not in st.session_state:
        st.session_state.first_day = datetime.date(2019, 7, 6)
    if 'n' not in st.session_state:
        st.session_state.n = None

    # ผู้ใช้ป้อนข้อมูล
    first_day = st.date_input("วันแรกของประจำเดือน (เดือนล่าสุด)", datetime.date(2019, 7, 6))
    n = st.text_input('โดยปกติ รอบเดือนของคุณจะมาทุกกี่วัน ?')


    # ปุ่มสำหรับคำนวณ
    Calculate = st.button('คำนวณวันไข่ตก')
    if Calculate :
        if first_day and n:
            ovulation_day = calculate_ovulation_day(first_day, n)
            if ovulation_day:
                st.success(f'วันไข่ตกของคุณคือ วันที่ : {ovulation_day.strftime("%d")}')
            else:
                st.error('เกิดข้อผิดพลาดในการคำนวณ')
        else:
            st.warning('กรุณากรอกข้อมูลให้ครบถ้วน')
    
    # ปุ่ม Reset
    Reset = st.button('Reset')
    if Reset :
        st.session_state.first_day = ''
        st.session_state.n = None


if __name__ == '__main__':
    main()

