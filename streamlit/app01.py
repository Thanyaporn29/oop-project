
import datetime
import streamlit as st
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('../background2.jpg')    
   

h = st.header('"Ovulation calculator website"')
p = st.write('Wellcome ')
banner = st.image('../ovulation project.png')
w = st.write('>> การจะคำนวณวันตกไข่ในลักษณะนี้ให้แม่นยำจะใช้ได้กับผู้หญิงที่มีรอบเดือนสม่ำเสมอเท่านั้น'
              'เช่น รอบเดือนจะมาทุกๆ 28 วันเสมอ<<')


rainbow_text_css = """
    background-image: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);
    -webkit-background-clip: text;
    color: transparent;
    font-weight: bold;
    font-size: 32px;
"""

rainbow_text_css2 = '''
    background-image: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);
    -webkit-background-clip: text;
    color: transparent;
    font-weight: bold;'''

# แสดงข้อความด้วย CSS สีรุ้ง
h.markdown('<p style="{}">"Ovulation calculator website"</p>'.format(rainbow_text_css), unsafe_allow_html=True)
st.markdown('<p style="{}">คำนวณภาวะตกไข่ธรรมชาติในระบบสืบพันธุ์ของผู้หญิง</p>'.format(rainbow_text_css2), unsafe_allow_html=True)
   

def calculate_ovulation_day(first_day, n):
    try:
        n = int(n)
        ovulation_day = first_day + datetime.timedelta(days=n-14)
        from_day = ovulation_day - datetime.timedelta(days=4)
        return [from_day, ovulation_day]
    except ValueError:
        return None

def main():

    if 'first_day' not in st.session_state:
        st.session_state.first_day = datetime.date(2024, 3, 1)
    if 'n' not in st.session_state:
        st.session_state.n = None

    # ผู้ใช้ป้อนข้อมูล
    first_day = st.date_input("วันแรกของประจำเดือน (เดือนล่าสุด)", datetime.date(2024, 3, 1))
    n = st.text_input('โดยปกติ รอบเดือนของคุณจะมาทุกกี่วัน ?')


    # ปุ่มสำหรับคำนวณ
    calculate = st.button('คำนวณวันไข่ตก')
    if calculate:
        if first_day and n:
            ovulation_day = calculate_ovulation_day(first_day, n)
            if ovulation_day:
                st.success(f'วันไข่ตกของคุณคือ วันที่ : {ovulation_day[0].strftime("%d")} - {ovulation_day[1].strftime("%d")}')
            else:
                st.error('เกิดข้อผิดพลาดในการคำนวณ')
        else:
            st.warning('กรุณากรอกข้อมูลให้ครบถ้วน')
    
            
    # ปุ่ม Reset
    Reset = st.button('Reset')
    if Reset:
        st.session_state.first_day = ''
        st.session_state.n = None

if __name__ == '__main__':
    main()


knowledge_1 = st.subheader('วันไข่ตกคืออะไร ? มาทำความรู้จักกันเลย')
w = st.write('การไข่ตก (Ovulation) ตกไข่ หรือที่เรียกกันว่า ไข่ตก เป็นกลไกธรรมชาติในระบบสืบพันธุ์ของผู้หญิง'
             'ที่เกิดขึ้นทุกเดือนจนกว่าจะเข้าสู่วัยทองหรือวัยหมดประจำเดือน โดยการตกไข่ตามปกติ'
             'จะใช้เวลารอบละประมาณ 28-35 วัน เริ่มนับจากวันแรกของการมีรอบเดือนที่มีประจำเดือนมา'
             'ซึ่งวันที่ไข่ตกนี้เองจะเป็นวันที่ไข่ใบที่สุกที่สุดออกมาจากรังไข่แล้วเคลื่อนไปยังส่วนปลายของท่อนำไข่ และพร้อมในการมีปฏิสนธิหากมีเพศสัมพันธ์')

knowledge_2 = st.subheader('การตกไข่เกิดขึ้นเมื่อไหร่ ?')
w = st.write('การไข่ตกจะเกิดขึ้น ประมาณช่วงกลางของรอบประจำเดือน วันไข่ตกของผู้หญิงจะมีความแตกต่างกันออกไปเนื่องจากความแตกต่างในรอบเดือนและระยะเวลาของรอบเดือน'
             'โดยปกติแล้วการไข่ตกจะเกินขึ้นในช่วง 2 สัปดาห์ก่อนรอบเดือนถัดไป ซึ่งกระบวนการตกไข่จะเริ่มไล่ลำดับวงจร ดังนี้\n'

                ' - ระยะก่อนไข่ตก เป็นช่วงก่อนที่ประจำเดือนรอบใหม่จะเริ่มขึ้น ต่อมใต้สมองจะหลั่ง ฟอลลิเคิลสติมิวเลติงฮอร์โมน (Follicle Stimulating Hormone หรือ FSH)'
                        'เพื่อช่วยกระตุ้นรังไข่ให้เจริญเติบโตก่อนที่จะมีการตกไข่ และเมื่อรังไข่เติบโตขึ้นก็จะสร้างฮอร์โมนเอสโตรเจนเพื่อทำให้ผนังมดลูกหนาและแข็งแรงขึ้น สำหรับเตรียมพร้อมต่อการตั้งครรภ์\n'

                ' - ระยะไข่ตก ต่อมใต้สมองในร่างกายจะผลิต ลูทิไนซิงฮอร์โมน (Luteinizing Hormone หรือ LH) เพื่อกระตุ้นให้ไข่และเซลล์ต่าง ๆ'
                        'ที่สร้างขึ้นในรังไข่เคลื่อนตัวไปยังท่อนำไข่ หรืออาจเรียกช่วงนี้ว่าเป็นระยะเจริญพันธ์ คือพร้อมที่จะมีการปฏิสนธิเกิดขึ้น'
                        'ซึ่งการตกไข่จะเกิดขึ้นในช่วงวันที่ 14 และจะมีการตกไข่แค่เพียง 12-24 ชั่วโมงเท่านั้น\n'

                ' - ระยะหลังไข่ตก หากมีการปฏิสนธิเกิดขึ้น ก็จะมีการฝังตัวอ่อนในมดลูกต่อไป แต่ถ้าหากไม่มีการปฏิสนธิเกิดขึ้น ก็จะมีเลือดขับออกทางช่องคลอดในวันที่ 28 ซึ่งนับเป็นรอบเดือนใหม่\n')

            
knowledge_3 = st.subheader('1 รอบเดือนมีการตกไข่เพียง 1 ครั้ง!')
w = st.write('สำหรับวันที่ไข่ตกของแต่ละคนจะแตกต่างกันไป ขึ้นอยู่กับรอบเดือน โดยปกติแล้วเมื่อไข่ตกมาแล้วนั้น ไข่จะมีชีวิตในท่อนำไข่ได้ 12-24 ชั่วโมงเท่านั้น'
             'หากมีเพศสัมพันธ์ในช่วงเวลานี้ก็มีโอกาสที่จะเกิดการปฏิสนธิได้มาก หากไข่ได้รับการผสมก็จะไปฝังตัวกับเยื่อบุผนังมดลูกกลายเป็นตัวอ่อนและเกิดเป็นการตั้งครรภ์ขึ้น'
             'แต่ถ้าไข่ไม่มีการปฏิสนธิหรือผสมไม่สำเร็จ อีก 14 วันหลังจากนั้นก็จะกลายเป็นประจำเดือนตามปกติ')


knowledge_4 = st.subheader('นับวันตกไข่อย่างไรให้แม่น ?')
w  = st.write('ปกติแล้วการนับวันไข่จะตกจะนับในช่วงประมาณ 2 สัปดาห์ก่อนที่ประจำเดือนรอบใหม่จะมา ซึ่งการจะคำนวณวันตกไข่ในลักษณะนี้ให้แม่นยำ'
            'จะใช้ได้กับผู้หญิงที่มีรอบเดือนสม่ำเสมอเท่านั้น เช่น รอบเดือนจะมาทุกๆ 28 วันเสมอ วันไข่ตกก็อยู่ในช่วงวันที่ 14 ของรอบเดือน'
            'โดยนับวันที่ประจำเดือนมาวันแรกเป็นวันที่ 1 ของรอบเดือน เมื่อนับวันได้แล้ว การมีเพศสัมพันธ์ในช่วงก่อนวันตกไข่ประมาณ 2 วัน หรือกล่าวง่ายๆ'
            'ก็คือ ตั้งแต่วันที่ 12 ของรอบเดือนก็จะมีโอกาสตั้งครรภ์ได้แล้ว เพราะอสุจิจะมีชีวิตรอผสมไข่อยู่ได้ประมาณ 2 วันก่อนการตกไข่')

knowledge_5 = st.subheader('ประจำเดือนมาไม่ปกติ ควรปรึกษาแพทย์')
w = st.write('สำหรับคนที่มีปัญหาประจำเดือนมาไม่ปกติ มาบ้าง ไม่มาบ้าง แนะนำว่าควรเข้ารับการเข้าตรวจเพื่อหาสาเหตุ'
             'เพราะการที่ประจำเดือนจะมาหรือไม่นั้นอาจเกิดได้จากหลายสาเหตุ ทั้งความผิดปกติทางฮอร์โมนและการมีโรคแฝงต่างๆ ที่ควรได้รับการรักษา')

blue_text_css = '''
    color: blue;
    font-weight: bold;
'''

# แสดงข้อความด้วย CSS สีน้ำเงิน
knowledge_1.markdown('<p style="{}">วันไข่ตกคืออะไร ? มาทำความรู้จักกันเลย</p>'.format(blue_text_css), unsafe_allow_html=True)
knowledge_2.markdown('<p style="{}">การตกไข่เกิดขึ้นเมื่อไหร่ ?</p>'.format(blue_text_css), unsafe_allow_html=True)
knowledge_3.markdown('<p style="{}">1 รอบเดือนมีการตกไข่เพียง 1 ครั้ง!</p>'.format(blue_text_css), unsafe_allow_html=True)
knowledge_4.markdown('<p style="{}">นับวันตกไข่อย่างไรให้แม่น ?</p>'.format(blue_text_css), unsafe_allow_html=True)
knowledge_5.markdown('<p style="{}">ประจำเดือนมาไม่ปกติ ควรปรึกษาแพทย์</p>'.format(blue_text_css), unsafe_allow_html=True)
