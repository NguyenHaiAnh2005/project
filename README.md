# 🌷 Hế Lô Thanh Phương

Một app Streamlit nhỏ xinh bằng tiếng Việt: lời nhắn dễ thương ngẫu nhiên,
bóng bay, chọn tâm trạng và đếm niềm vui trong mỗi phiên sử dụng.

## Chạy trên máy

Yêu cầu Python 3.10 trở lên.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Trên Windows, kích hoạt bằng `.venv\Scripts\activate`.
Không cần API key hay cơ sở dữ liệu. Bộ đếm và lời nhắn lưu trong phiên Streamlit,
không lưu vĩnh viễn. Font Google là tùy chọn; khi offline app dùng font hệ thống.

## Kiểm tra tương tác

```bash
python -m unittest discover -s tests -v
```

## Đưa lên Streamlit Community Cloud

Sau khi push lên GitHub, chọn repository này trong Streamlit Community Cloud,
chọn nhánh đã push và đặt entrypoint là `app.py`, rồi Deploy.
