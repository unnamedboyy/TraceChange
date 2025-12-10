# 🔍 TraceChange  
A Streamlit-based application for detecting and analyzing changes between two tabular datasets.

TraceChange helps you compare an **Old** dataset and a **New** dataset, classify differences, visualize changes, and export results with color-coded Excel highlighting. This tool is ideal for data analysts, engineers, system auditors, and anyone who works with versioned data such as inventory lists, configuration tables, or asset registries.

---

## 🚀 Features

### ✓ Row Difference Detection
TraceChange automatically identifies:
- **Added rows** — present only in the new dataset  
- **Deleted rows** — present only in the old dataset  
- **Modified rows** — same key but different values  
- **Duplicate rows** — repeated entries  
- **Merged Duplicates** — optional cleanup action  
- **Same rows** — unchanged  

### ✓ Excel Export with Highlighting
The exported Excel file uses intuitive color coding:
- 🟩 **Added**  
- 🟥 **Deleted**  
- 🟨 **Modified (row)**  
- 🟨🔆 **Modified (cell-level highlights)**  
- 🟦 **Duplicate / Merged Duplicate**  

### ✓ Interactive Review
- Filter differences using status tabs  
- Select which rows to include in the export  
- Remove all deleted rows (optional)  
- Merge duplicates (optional)

### ✓ Smart Comparison
- Case-insensitive key matching  
- Auto-detection of changed columns  
- Stable ordering for clear visual analysis  

---

## 📁 Project Structure
TraceChange/
│
├── app.py # Home page
├── pages/
│ └── 1_Table_Compare.py # Main comparison module
├── README.md
├── .gitignore
├── requirements.txt
└── LICENSE (optional)

---

Siap! Berikut bagian **Installation & Setup** yang ditulis ulang dengan bahasa yang lebih rapi, profesional, dan mudah diikuti.

---

## 🧩 Installation & Setup

### **1️⃣ Clone the repository**

bash
git clone https://github.com/<your-username>/TraceChange.git
cd TraceChange

---

### **2️⃣ (Optional) Create and activate a virtual environment**

Using a virtual environment is recommended to keep dependencies isolated.

#### **Windows**
bash
python -m venv venv
venv\Scripts\activate


#### **macOS / Linux**
bash
python3 -m venv venv
source venv/bin/activate

---

### **3️⃣ Install required dependencies**

Make sure `pip` is updated, then install the packages listed in `requirements.txt`.

bash
pip install --upgrade pip
pip install -r requirements.txt

---

### **4️⃣ Run the application**

Start the Streamlit app using:

bash
streamlit run app.py

After launching, Streamlit will open the app in your default browser:

http://localhost:8501

You will see the **Home page** and a sidebar containing the **Table Comparison** module.

