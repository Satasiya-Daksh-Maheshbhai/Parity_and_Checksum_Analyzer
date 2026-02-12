# 📡 Parity and Checksum Analyzer

A Django-based web application that calculates and demonstrates different Error Detection Techniques used in Computer Networks.

This project allows users to enter binary data and analyze:

## ✅ VRC (Vertical Redundancy Check)

## ✅ LRC (Longitudinal Redundancy Check)

## ✅ 2-D Parity

## ✅ Checksum (with step-by-step binary addition & 1’s complement)

# 🚀 Features

Accepts space-separated binary input

Performs:

Even parity calculation (VRC)

Column-wise parity (LRC)

Two-Dimensional Parity

Binary Checksum with carry wrap-around

Displays step-by-step checksum addition

Clean Bootstrap interface

Binary input validation

# 🖥️ Example Input
1011 1001 1100

# 📊 Output Explanation
## ✅ 1. VRC (Vertical Redundancy Check)

Adds one parity bit to each data word (even parity).

Example:

1011 → 10111
1001 → 10010
1100 → 11000

## ✅ 2. LRC (Longitudinal Redundancy Check)

Generates a parity row by checking columns:

1011
1001
1100
----
1110   ← LRC Row

## ✅ 3. 2-D Parity

Combines:

Row parity (VRC)

Column parity (LRC)

Final overall parity bit

Provides stronger error detection than single parity.

## ✅ 4. Checksum

Step-by-step binary addition:

  1011
+ 1001
+ 1100
--------
  0010   (Final Sum after carry wrap-around)
  1101   (1’s Complement → Checksum)

🛠️ Technologies Used

Python

Django

HTML5

Bootstrap 5

CSS

📂 Project Structure
Parity_and_Checksum_Analyzer/
│
├── main/
│   ├── views.py
│   ├── templates/
│   │   └── error_detection.html
│
├── manage.py
└── README.md

# ⚙️ How to Run the Project
## 1️⃣ Clone Repository
git clone https://github.com/Satasiya-Daksh-Maheshbhai/Parity_and_Checksum_Analyzer.git

## 2️⃣ Go to Project Folder
cd Parity_and_Checksum_Analyzer

## 3️⃣ Install Django
pip install django

## 4️⃣ Run Server
python manage.py runserver

## 5️⃣ Open in Browser
http://127.0.0.1:8000/

# 📖 Concepts Covered
Technique	Type	Detects
VRC	Single Parity	Single-bit errors
LRC	Column Parity	Burst errors
2-D Parity	Row + Column	Detect & locate errors
Checksum	Binary Addition	Multiple-bit errors

# 🎯 Applications

Computer Networks learning

Error detection simulation

Data communication systems

Academic CN projects

ARQ protocol understanding

# 📌 Future Enhancements

Add CRC (Cyclic Redundancy Check)

Add receiver-side verification

Add error simulation mode

Add downloadable PDF report

Improve UI visualization

# 👨‍💻 Author
Developed as a Computer Networks academic project.
## -Satasiya Daksh Maheshbhai

# ⭐ Conclusion

Parity and Checksum Analyzer provides a clear and practical demonstration of classical error detection techniques used in digital communication systems. It helps students understand how redundancy ensures data integrity during transmission.
# Sample Output :
<img width="927" height="903" alt="image" src="https://github.com/user-attachments/assets/946093d3-f907-4b47-a62b-eb9e70755af5" />
<img width="988" height="787" alt="image" src="https://github.com/user-attachments/assets/0789b0ec-f4ff-4cc3-bf3d-26b20cbf415f" />
