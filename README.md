# 📦 Supply Chain Pro

**Supply Chain Pro** is a Django-based inventory and supply chain management system tailored for small to medium businesses. It allows users to manage goods, categories, customers, and barcode-based operations with personalized multi-user access.

---

## 🚀 Features

- 🔐 **User Authentication** (Custom User Model)
- 📦 **Goods Management**: Add, edit, and delete goods with price, quantity, and descriptions.
- 📁 **Category Management**: User-specific category creation and filtering.
- 🧑‍💼 **Customer Management**: Store customer info with name, email, phone, and address.
- 🧮 **Total Inventory Value Calculation**
- 🔎 **Search & Filter** goods by name, description, or category.
- 📸 **Barcode Scanning**: Add products using captured barcode images.
- 📇 **Barcode Retrieval**: Retrieve goods by scanning barcode.
- 📊 **Dashboard** with CRUD forms, filtering, and user isolation.
- 🌐 **UI** using TailwindCSS.

---

## 📂 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, TailwindCSS
- **Database**: SQLite
- **Authentication**: Django Custom User Model
- **Barcode Processing**: `pyzbar`, `Pillow`

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/supply-chain-pro.git
   cd supply-chain-pro


python -m venv env
source env/bin/activate

python manage.py makemigrations
python manage.py migrate

if getting error install the required Dependencies
🧪 Dependencies (Key Libraries)
Django
pyzbar
Pillow
opencv-python
crispy-forms (optional for forms styling)
python manage.py createsuperuser
python manage.py runserver


Open your browser and go to: http://127.0.0.1:8000/

🔑 Usage Guide
✅ Sign up and log in with a unique user account.

➕ Add categories and customers via the dashboard.

🛒 Add goods with details like name, quantity, price, category, customer, and barcode.

📷 You can Use the barcode scanner to register products by capturing barcode images.

🔍 Also, you can Use the barcode retrieval tool to find items quickly.

💼 Admins can use Django admin at /admin/ to manage everything.

📁 Project Structure (Important Files)
supply_chain_pro/
├── core/                  # Main app with models, views, forms, urls
├── templates/             # HTML templates (dashboard, login, etc.)
├── static/                # Static files (CSS, JS)
├── media/                 # Uploaded images or scanned barcodes
├── manage.py

