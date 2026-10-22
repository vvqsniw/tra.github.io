from flask import Flask, render_template, request

app = Flask(__name__)
app.template_folder = 'templates'

places = [
    # เชียงใหม่
    {
        "id": "001",
        "image": "doi_suthep.jpg",
        "name": "วัดพระธาตุดอยสุเทพ",
        "description": "วัดบนดอย วิวสวย มองเห็นเมืองเชียงใหม่",
        "location": "เชียงใหม่",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมดอยวิว", "โฮสเทลบนดอย"],
        "open": "06:00 - 18:00"
    },
    {
        "id": "002",
        "image": "night_safari_chiangmai.jpg",
        "name": "เชียงใหม่ไนท์ซาฟารี",
        "description": "สวนสัตว์กลางคืนที่ใหญ่ที่สุดในเอเชีย",
        "location": "เชียงใหม่",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมซาฟารี", "รีสอร์ตเขาแก้ว"],
        "open": "18:00 - 24:00"
    },
    {
        "id": "003",
        "image": "chiangmai_old_town.jpg",
        "name": "เมืองเก่าเชียงใหม่",
        "description": "ย่านประวัติศาสตร์และวัดโบราณมากมาย",
        "location": "เชียงใหม่",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมใจกลางเมือง", "เกสต์เฮาส์เมืองเก่า"],
        "open": "ตลอดวัน"
    },

    # เชียงราย
    {
        "id": "004",
        "image": "chiang_rai_bazaar.jpg",
        "name": "ไนท์บาซาร์เชียงราย",
        "description": "ตลาดกลางคืน ของกินของฝากเพียบ",
        "location": "เชียงราย",
        "type": "ตลาด",
        "nearby_hotels": ["โรงแรมกลางเมือง", "รีสอร์ตแม่น้ำ"],
        "open": "17:00 - 22:00"
    },
    {
        "id": "005",
        "image": "white_temple.jpg",
        "name": "วัดร่องขุ่น",
        "description": "วัดสีขาวลวดลายสวยงามเป็นเอกลักษณ์",
        "location": "เชียงราย",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมอาร์ต", "รีสอร์ตริมแม่น้ำ"],
        "open": "08:00 - 17:00"
    },
    {
        "id": "006",
        "image": "singha_park.jpg",
        "name": "อุทยานสิงห์",
        "description": "สวนดอกไม้และกิจกรรมสำหรับครอบครัว",
        "location": "เชียงราย",
        "type": "สวนสาธารณะ",
        "nearby_hotels": ["โฮมสเตย์สิงห์ปาร์ค", "รีสอร์ตเขียว"],
        "open": "07:00 - 18:00"
    },

    # กรุงเทพ
    {
        "id": "007",
        "image": "grand_palace.jpg",
        "name": "พระบรมมหาราชวัง",
        "description": "สถานที่สำคัญทางประวัติศาสตร์และศิลปะ",
        "location": "กรุงเทพ",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมใกล้ราชวัง", "โฮสเทลสีลม"],
        "open": "08:30 - 15:30"
    },
    {
        "id": "008",
        "image": "chatuchak_market.jpg",
        "name": "ตลาดนัดจตุจักร",
        "description": "ตลาดใหญ่สุดในกรุงเทพ มีของขายมากมาย",
        "location": "กรุงเทพ",
        "type": "ตลาด",
        "nearby_hotels": ["โรงแรมใกล้ตลาด", "เกสต์เฮาส์ลาดพร้าว"],
        "open": "06:00 - 18:00"
    },
    {
        "id": "009",
        "image": "asiatique_riverfront.jpg",
        "name": "เอเชียทีค เดอะ ริเวอร์ฟร้อนท์",
        "description": "ตลาดริมแม่น้ำเจ้าพระยา ยามค่ำคืน",
        "location": "กรุงเทพ",
        "type": "ตลาด",
        "nearby_hotels": ["โรงแรมริมน้ำ", "รีสอร์ตสุขุมวิท"],
        "open": "17:00 - 23:00"
    },

    # ภูเก็ต
    {
        "id": "010",
        "image": "patong_beach.jpg",
        "name": "หาดป่าตอง",
        "description": "ชายหาดชื่อดัง มีชีวิตชีวาและกิจกรรมมากมาย",
        "location": "ภูเก็ต",
        "type": "ชายหาด",
        "nearby_hotels": ["โรงแรมริมทะเล", "รีสอร์ตหาดป่าตอง"],
        "open": "ตลอดวัน"
    },
    {
        "id": "011",
        "image": "big_buddha_phuket.jpg",
        "name": "พระใหญ่ภูเก็ต",
        "description": "พระพุทธรูปขนาดใหญ่บนภูเขา วิวสวย",
        "location": "ภูเก็ต",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โฮสเทลภูเก็ต", "โรงแรมวิวทะเล"],
        "open": "07:00 - 18:00"
    },
    {
        "id": "012",
        "image": "old_town_phuket.jpg",
        "name": "เมืองเก่าภูเก็ต",
        "description": "ย่านประวัติศาสตร์และสถาปัตยกรรมชิโน-โปรตุกีส",
        "location": "ภูเก็ต",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมใจกลางเมือง", "เกสต์เฮาส์เมืองเก่า"],
        "open": "ตลอดวัน"
    },

    # กระบี่
    {
        "id": "013",
        "image": "railay_beach.jpg",
        "name": "หาดไร่เลย์",
        "description": "ชายหาดสวย น้ำทะเลใส เหมาะแก่การปีนผา",
        "location": "กระบี่",
        "type": "ชายหาด",
        "nearby_hotels": ["รีสอร์ตหาดไร่เลย์", "โฮมสเตย์ทะเล"],
        "open": "ตลอดวัน"
    },
    {
        "id": "014",
        "image": "emerald_pool.jpg",
        "name": "สระมรกต",
        "description": "น้ำแร่สีเขียวมรกตในป่าเขตร้อน",
        "location": "กระบี่",
        "type": "น้ำพุร้อนธรรมชาติ",
        "nearby_hotels": ["รีสอร์ตป่าเขา", "โรงแรมกระบี่"],
        "open": "08:00 - 17:00"
    },
    {
        "id": "015",
        "image": "thung_teao_forest.jpg",
        "name": "ป่าพรุทุ่งทะเล",
        "description": "ป่าชายเลนที่สวยงามและหลากหลายชนิดสัตว์ป่า",
        "location": "กระบี่",
        "type": "สวนธรรมชาติ",
        "nearby_hotels": ["โฮมสเตย์ริมทะเล", "รีสอร์ตป่าพรุ"],
        "open": "07:00 - 18:00"
    },

    # นครราชสีมา (โคราช)
    {
        "id": "016",
        "image": "phimai_historical_park.jpg",
        "name": "อุทยานประวัติศาสตร์พิมาย",
        "description": "โบราณสถานขอมเก่าแก่แห่งใหญ่ที่สุดในภาคอีสาน",
        "location": "นครราชสีมา",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมพิมาย", "รีสอร์ตโคราช"],
        "open": "08:00 - 18:00"
    },
    {
        "id": "017",
        "image": "khao_yai_national_park.jpg",
        "name": "อุทยานแห่งชาติเขาใหญ่",
        "description": "ป่าใหญ่และธรรมชาติอุดมสมบูรณ์",
        "location": "นครราชสีมา",
        "type": "อุทยานแห่งชาติ",
        "nearby_hotels": ["รีสอร์ตเขาใหญ่", "บ้านพักในอุทยาน"],
        "open": "06:00 - 18:00"
    },
    {
        "id": "018",
        "image": "saraburi_waterfall.jpg",
        "name": "น้ำตกเหวนรก",
        "description": "น้ำตกสวยและเส้นทางเดินป่า",
        "location": "นครราชสีมา",
        "type": "น้ำตก",
        "nearby_hotels": ["รีสอร์ตใกล้น้ำตก", "โฮมสเตย์ธรรมชาติ"],
        "open": "08:00 - 17:00"
    },

    # สุโขทัย
    {
        "id": "019",
        "image": "sukhothai_historical_park.jpg",
        "name": "อุทยานประวัติศาสตร์สุโขทัย",
        "description": "เมืองหลวงโบราณของอาณาจักรสุโขทัย",
        "location": "สุโขทัย",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมสุโขทัย", "เกสต์เฮาส์ใกล้อุทยาน"],
        "open": "08:00 - 18:00"
    },
    {
        "id": "020",
        "image": "si_satchanalai_historical_park.jpg",
        "name": "อุทยานประวัติศาสตร์ศรีสัชนาลัย",
        "description": "โบราณสถานเก่าแก่ในจังหวัดสุโขทัย",
        "location": "สุโขทัย",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมศรีสัชนาลัย", "โฮมสเตย์ชุมชน"],
        "open": "08:00 - 18:00"
    },
    {
        "id": "021",
        "image": "nam_tok_si_pla.jpg",
        "name": "น้ำตกศรีประจันต์",
        "description": "น้ำตกสวยในอุทยานแห่งชาติ",
        "location": "สุโขทัย",
        "type": "น้ำตก",
        "nearby_hotels": ["รีสอร์ตสุโขทัย", "บ้านพักธรรมชาติ"],
        "open": "08:00 - 17:00"
    },

    # สงขลา
    {
        "id": "022",
        "image": "hat_yai_city_park.jpg",
        "name": "สวนสาธารณะหาดใหญ่",
        "description": "สวนสาธารณะใจกลางเมืองหาดใหญ่",
        "location": "สงขลา",
        "type": "สวนสาธารณะ",
        "nearby_hotels": ["โรงแรมหาดใหญ่", "เกสต์เฮาส์เมือง"],
        "open": "06:00 - 20:00"
    },
    {
        "id": "023",
        "image": "songkhla_beach.jpg",
        "name": "หาดสมิหลา",
        "description": "ชายหาดสวยชื่อดังของสงขลา",
        "location": "สงขลา",
        "type": "ชายหาด",
        "nearby_hotels": ["รีสอร์ตหาดสมิหลา", "โรงแรมริมทะเล"],
        "open": "ตลอดวัน"
    },
    {
        "id": "024",
        "image": "tinsulanond_museum.jpg",
        "name": "พิพิธภัณฑ์สงขลา",
        "description": "พิพิธภัณฑ์ที่บอกเล่าประวัติศาสตร์ของสงขลา",
        "location": "สงขลา",
        "type": "พิพิธภัณฑ์",
        "nearby_hotels": ["โรงแรมกลางเมือง", "เกสต์เฮาส์สงขลา"],
        "open": "09:00 - 17:00"
    },

    # ขอนแก่น
    {
        "id": "025",
        "image": "kaen_nakhon_lake.jpg",
        "name": "บึงแก่นนคร",
        "description": "บึงน้ำใจกลางเมืองขอนแก่น มีสวนสาธารณะ",
        "location": "ขอนแก่น",
        "type": "สวนสาธารณะ",
        "nearby_hotels": ["โรงแรมขอนแก่น", "เกสต์เฮาส์ใจกลางเมือง"],
        "open": "06:00 - 20:00"
    },
    {
        "id": "026",
        "image": "phu_wang_national_park.jpg",
        "name": "อุทยานแห่งชาติภูเวียง",
        "description": "อุทยานแห่งชาติและแหล่งฟอสซิลไดโนเสาร์",
        "location": "ขอนแก่น",
        "type": "อุทยานแห่งชาติ",
        "nearby_hotels": ["รีสอร์ตภูเวียง", "โฮมสเตย์ธรรมชาติ"],
        "open": "07:00 - 18:00"
    },
    {
        "id": "027",
        "image": "khon_kaen_zoo.jpg",
        "name": "สวนสัตว์ขอนแก่น",
        "description": "สวนสัตว์สำหรับครอบครัวและเด็กๆ",
        "location": "ขอนแก่น",
        "type": "สวนสัตว์",
        "nearby_hotels": ["โรงแรมใกล้สวนสัตว์", "เกสต์เฮาส์ขอนแก่น"],
        "open": "08:00 - 17:00"
    },

    # น่าน
    {
        "id": "028",
        "image": "nan_old_town.jpg",
        "name": "เมืองเก่าน่าน",
        "description": "ย่านประวัติศาสตร์และวัฒนธรรมล้านนา",
        "location": "น่าน",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมน่าน", "เกสต์เฮาส์เมืองเก่า"],
        "open": "ตลอดวัน"
    },
    {
        "id": "029",
        "image": "doi_phu_kan.jpg",
        "name": "ดอยภูคา",
        "description": "ภูเขาที่สวยงามและอากาศเย็น",
        "location": "น่าน",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["รีสอร์ตภูเขา", "โฮมสเตย์"],
        "open": "06:00 - 18:00"
    },
    {
        "id": "030",
        "image": "wat_phumin.jpg",
        "name": "วัดภูมินทร์",
        "description": "วัดเก่าแก่และภาพจิตรกรรมฝาผนังที่มีชื่อเสียง",
        "location": "น่าน",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมน่าน", "เกสต์เฮาส์ใกล้วัด"],
        "open": "08:00 - 17:00"
    },
    # อยุธยา
    {
        "id": "031",
        "image": "ayutthaya_historical_park.jpg",
        "name": "อุทยานประวัติศาสตร์พระนครศรีอยุธยา",
        "description": "โบราณสถานและวัดเก่าแก่แห่งกรุงศรีอยุธยา",
        "location": "อยุธยา",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมริมน้ำ", "เกสต์เฮาส์อยุธยา"],
        "open": "08:00 - 18:00"
    },
    {
        "id": "032",
        "image": "wat_chai_watthanaram.jpg",
        "name": "วัดไชยวัฒนาราม",
        "description": "วัดโบราณริมแม่น้ำเจ้าพระยา",
        "location": "อยุธยา",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมใกล้วัด", "รีสอร์ตริมน้ำ"],
        "open": "08:00 - 18:00"
    },
    {
        "id": "033",
        "image": "bang_pa_in_palace.jpg",
        "name": "พระราชวังบางปะอิน",
        "description": "พระราชวังฤดูร้อนที่สวยงามและยิ่งใหญ่",
        "location": "อยุธยา",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมบางปะอิน", "เกสต์เฮาส์อยุธยา"],
        "open": "08:30 - 16:30"
    },

    # พิษณุโลก
    {
        "id": "034",
        "image": "wat_phra_sri_rattana_mahayana.jpg",
        "name": "วัดพระศรีรัตนมหาธาตุ",
        "description": "วัดสำคัญและมีพระพุทธชินราชที่งดงาม",
        "location": "พิษณุโลก",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมพิษณุโลก", "รีสอร์ตใจกลางเมือง"],
        "open": "06:00 - 18:00"
    },
    {
        "id": "035",
        "image": "phu_lang_ka_national_park.jpg",
        "name": "อุทยานแห่งชาติภูแลนคำ",
        "description": "ป่าเขาและวิวธรรมชาติที่สวยงาม",
        "location": "พิษณุโลก",
        "type": "อุทยานแห่งชาติ",
        "nearby_hotels": ["รีสอร์ตธรรมชาติ", "โฮมสเตย์"],
        "open": "06:00 - 18:00"
    },
    {
        "id": "036",
        "image": "kaeng_krachan_waterfall.jpg",
        "name": "น้ำตกแก่งกระจาน",
        "description": "น้ำตกและธรรมชาติสวยงามในจังหวัดพิษณุโลก",
        "location": "พิษณุโลก",
        "type": "น้ำตก",
        "nearby_hotels": ["รีสอร์ตน้ำตก", "โรงแรมใกล้ป่า"],
        "open": "08:00 - 17:00"
    },

    # ระยอง
    {
        "id": "037",
        "image": "koh_samet.jpg",
        "name": "เกาะเสม็ด",
        "description": "เกาะสวยน้ำใสหาดทรายขาว",
        "location": "ระยอง",
        "type": "ชายหาด",
        "nearby_hotels": ["รีสอร์ตเกาะเสม็ด", "โฮมสเตย์ชายหาด"],
        "open": "ตลอดวัน"
    },
    {
        "id": "038",
        "image": "rayong_waterfall.jpg",
        "name": "น้ำตกเขาชะเมา",
        "description": "น้ำตกและป่าไม้ธรรมชาติ",
        "location": "ระยอง",
        "type": "น้ำตก",
        "nearby_hotels": ["รีสอร์ตธรรมชาติ", "โฮมสเตย์เขาชะเมา"],
        "open": "08:00 - 17:00"
    },
    {
        "id": "039",
        "image": "rayong_city_park.jpg",
        "name": "สวนสาธารณะระยอง",
        "description": "สวนสาธารณะสำหรับพักผ่อนในเมืองระยอง",
        "location": "ระยอง",
        "type": "สวนสาธารณะ",
        "nearby_hotels": ["โรงแรมระยอง", "เกสต์เฮาส์ใจกลางเมือง"],
        "open": "06:00 - 20:00"
    },

    # นครศรีธรรมราช
    {
        "id": "040",
        "image": "pranang_beach.jpg",
        "name": "หาดปากนคร",
        "description": "ชายหาดสวยน้ำใสในนครศรีธรรมราช",
        "location": "นครศรีธรรมราช",
        "type": "ชายหาด",
        "nearby_hotels": ["รีสอร์ตชายหาด", "โฮมสเตย์ริมทะเล"],
        "open": "ตลอดวัน"
    },
    {
        "id": "041",
        "image": "wat_phra_maha_chedi.jpg",
        "name": "วัดพระมหาธาตุวรมหาวิหาร",
        "description": "วัดสำคัญคู่เมืองนครศรีธรรมราช",
        "location": "นครศรีธรรมราช",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมนครศรีธรรมราช", "เกสต์เฮาส์ใกล้วัด"],
        "open": "08:00 - 18:00"
    },
    {
        "id": "042",
        "image": "khanom_beach.jpg",
        "name": "หาดขนอม",
        "description": "ชายหาดสงบ เหมาะแก่การพักผ่อน",
        "location": "นครศรีธรรมราช",
        "type": "ชายหาด",
        "nearby_hotels": ["รีสอร์ตขนอม", "โฮมสเตย์ริมทะเล"],
        "open": "ตลอดวัน"
    },

    # ชลบุรี
    {
        "id": "043",
        "image": "pattaya_beach.jpg",
        "name": "หาดพัทยา",
        "description": "ชายหาดชื่อดังและสถานที่เที่ยวกลางคืน",
        "location": "ชลบุรี",
        "type": "ชายหาด",
        "nearby_hotels": ["โรงแรมพัทยา", "รีสอร์ตริมทะเล"],
        "open": "ตลอดวัน"
    },
    {
        "id": "044",
        "image": "nong_nooch_garden.jpg",
        "name": "สวนสวยหนองนุช",
        "description": "สวนพฤกษศาสตร์และแสดงวัฒนธรรม",
        "location": "ชลบุรี",
        "type": "สวนสาธารณะ",
        "nearby_hotels": ["โรงแรมใกล้สวน", "รีสอร์ตพัทยา"],
        "open": "08:00 - 18:00"
    },
    {
        "id": "045",
        "image": "koh_larn.jpg",
        "name": "เกาะล้าน",
        "description": "เกาะใกล้พัทยา น้ำใส เหมาะแก่การพักผ่อน",
        "location": "ชลบุรี",
        "type": "ชายหาด",
        "nearby_hotels": ["รีสอร์ตเกาะล้าน", "โฮมสเตย์"],
        "open": "ตลอดวัน"
    },

    # สระบุรี
    {
        "id": "046",
        "image": "kaeng_kho_national_park.jpg",
        "name": "อุทยานแห่งชาติแก่งคอย",
        "description": "อุทยานธรรมชาติ น้ำตกและผาจำลอง",
        "location": "สระบุรี",
        "type": "อุทยานแห่งชาติ",
        "nearby_hotels": ["รีสอร์ตสระบุรี", "โฮมสเตย์"],
        "open": "07:00 - 18:00"
    },
    {
        "id": "047",
        "image": "saraburi_waterfall.jpg",
        "name": "น้ำตกเจ็ดสาวน้อย",
        "description": "น้ำตกสวยและเส้นทางเดินป่า",
        "location": "สระบุรี",
        "type": "น้ำตก",
        "nearby_hotels": ["โรงแรมใกล้น้ำตก", "รีสอร์ตธรรมชาติ"],
        "open": "08:00 - 17:00"
    },
    {
        "id": "048",
        "image": "wat_muang.jpg",
        "name": "วัดมิ่งเมือง",
        "description": "วัดสำคัญในจังหวัดสระบุรี",
        "location": "สระบุรี",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมสระบุรี", "เกสต์เฮาส์ใกล้วัด"],
        "open": "08:00 - 18:00"
    },

    # ราชบุรี
    {
        "id": "049",
        "image": "damnoen_saduak_floating_market.jpg",
        "name": "ตลาดน้ำดำเนินสะดวก",
        "description": "ตลาดน้ำที่มีชื่อเสียงและของกินมากมาย",
        "location": "ราชบุรี",
        "type": "ตลาด",
        "nearby_hotels": ["โรงแรมราชบุรี", "รีสอร์ตริมคลอง"],
        "open": "06:00 - 12:00"
    },
    {
        "id": "050",
        "image": "kaeng_krachan_national_park.jpg",
        "name": "อุทยานแห่งชาติแก่งกระจาน",
        "description": "อุทยานธรรมชาติ ป่าไม้และน้ำตก",
        "location": "ราชบุรี",
        "type": "อุทยานแห่งชาติ",
        "nearby_hotels": ["รีสอร์ตแก่งกระจาน", "โฮมสเตย์"],
        "open": "06:00 - 18:00"
    },
    {
        "id": "051",
        "image": "rajabhakti_park.jpg",
        "name": "อุทยานราชภักดิ์",
        "description": "สวนประติมากรรมพระบรมราชานุสาวรีย์",
        "location": "ราชบุรี",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมราชบุรี", "เกสต์เฮาส์เมือง"],
        "open": "06:00 - 20:00"
    },

    # ตาก
    {
        "id": "052",
        "image": "tha_lueak_hot_spring.jpg",
        "name": "บ่อน้ำพุร้อนท่าลือ",
        "description": "น้ำพุร้อนธรรมชาติในจังหวัดตาก",
        "location": "ตาก",
        "type": "น้ำพุร้อน",
        "nearby_hotels": ["รีสอร์ตน้ำพุร้อน", "โฮมสเตย์"],
        "open": "08:00 - 20:00"
    },
    {
        "id": "053",
        "image": "tak_waterfall.jpg",
        "name": "น้ำตกทีลอซู",
        "description": "น้ำตกที่สวยงามและใหญ่ที่สุดในไทย",
        "location": "ตาก",
        "type": "น้ำตก",
        "nearby_hotels": ["รีสอร์ตใกล้น้ำตก", "โฮมสเตย์ธรรมชาติ"],
        "open": "08:00 - 17:00"
    },
    {
        "id": "054",
        "image": "tak_old_town.jpg",
        "name": "เมืองเก่าตาก",
        "description": "ย่านประวัติศาสตร์และวัฒนธรรม",
        "location": "ตาก",
        "type": "สถานที่ท่องเที่ยว",
        "nearby_hotels": ["โรงแรมตาก", "เกสต์เฮาส์เมืองเก่า"],
        "open": "ตลอดวัน"
    }

]

@app.route('/', methods=['GET', 'POST'])
def index():
    search = ''
    selected_location = ''
    selected_type = ''
    
    if request.method == 'POST':
        search = request.form.get('search', '').strip()
        selected_location = request.form.get('location', '')
        selected_type = request.form.get('type', '')

    result = places

    if search:
        result = [p for p in result if search.lower() in p['name'].lower() or search.lower() in p['location'].lower()]

    if selected_location:
        result = [p for p in result if p['location'] == selected_location]

    if selected_type:
        result = [p for p in result if p['type'] == selected_type]

    provinces = sorted(set(p['location'] for p in places))
    types = sorted(set(p['type'] for p in places))

    return render_template(
        'index.html',
        places=result,
        provinces=provinces,
        types=types,
        selected_location=selected_location,
        selected_type=selected_type
    )

if __name__ == '__main__':
    app.run(debug=True)
