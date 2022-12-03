from pydantic import BaseModel


class STDModel(BaseModel):
    form_title: str = "Forms title"
    form_iso_no: str = "IF-XXXX-XXX"
    fname: str = "Setsuna"
    lname: str = "F. Seiei"
    level: str = "Gundam Meister"
    dept: str = "Celestial Being"
    email: str = "exia.email@domain"
    fullname: str = "Setuna F. Seiei"
    tel: str = "12312121"


class VPS(STDModel):
    form_title: str = "แบบฟอร์มการขอรับบริการ Virtual Private Server"
    form_iso_no: str = "IDT-FM-IF-010"
    vps_template: str = "cpu: 1vcpu, memory: 1G, disk: 100G"
    date: str = "2022-11-03"
    desc: str = "Web Hosting"
    os_name: str = "windows xx"
    domain: str = "no-domain"


class COLO(STDModel):
    form_title: str = "แบบฟอร์มการขอรับบริการ Co-Location"
    form_iso_no: str = "IDT-FM-IF-013"
    server_info: str = "Dell R740"
    inv_no: str = "xxx-xxx-xxxx-xxxxx-xxxx"
    start_date: str = "2022-12-03"
    end_date: str = "2022-12-10"
    os: str = "Windows Server 2019"
    rack_size: str = "4U"


class VPN(STDModel):
    form_title: str = "แบบฟอร์มการขอรับบริการ VPN"
    form_iso_no: str = "IDT-FM-IF-012"
    fname_th: str = "ชื่อ ภาษาไทย"
    lname_th: str = "นามสกุล ภาษาไทย"
    co_fname_th: str = "ชื่อ ภาษาไทย, ผู้ประสานงาน / ผู้ดูแลระบบของหน่วยงานเจ้าของระบบของสถาบัน"
    co_lname_th: str = "นามสกุล ภาษาไทย, ผู้ประสานงาน / ผู้ดูแลระบบของหน่วยงานเจ้าของระบบของสถาบัน"
    co_dept: str = "หน่วยงาน, ผู้ประสานงาน / ผู้ดูแลระบบของหน่วยงานเจ้าของระบบของสถาบัน"
    ip: str = "IP Address"
    port: str = "Program/Port"
    desc: str = "ความจําเป็นในการขอเข้าใช้งาน"
    start_date: str = "2022-12-03"
    end_date: str = "2022-12-10"
    dept: str = "หน่วยงาน / บริษัท"

class ACCOUNT(STDModel): # guest
    form_title: str = "แบบฟอร์มขอใช้อินเทอร์เน็ต สำหรับผู้เข้าอบรม / โครงการความร่วมมือ"
    form_iso_no: str = "IDT-FM-IF-005"
    fname_th: str = "ชื่อ ภาษาไทย"
    lname_th: str = "นามสกุล ภาษาไทย"
    cid: str = "Personal ID / Passport"
    start_date: str = "2022-12-03"
    end_date: str = "2022-12-10"
    person_type: str = "ประเภทผู้ใช้งาน"
    email: str = "อีเมลสํารอง( อีเมลสําหรับติดต่อ ใส่อีเมลอื่นที่ไม่ใช่อีเมลของสถาบัน)"

# - แบบฟอร์มการขอบัญชีผู้ใช้งานเครือข่ายอินเทอร์เน็ตแบบชั่วคราว LAN, WIFI IDT-FM-IF-007 
# - แบบฟอร์มการขออีเมลกลางสำหรับหน่วยงานหรือหลักสูตร IDT-FM-IF-006 
# - แบบฟอร์มขอบัญชีผู้ใช้งานสำหรับอาจารย์พิเศษ 
# - แบบฟอร์มการขอรับบริการ Domain IDT-FM-IF-010