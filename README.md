# 🕵️ Crime Records Management System

A professional and lightweight web application to securely log, track, and manage crime reports. Built using **Flask**, **SQLAlchemy**, and **MySQL**, this system allows authenticated users to register crimes with optional evidence files, view them in a styled dashboard, filter/search by various criteria, and delete records with ease.

---

## 🚀 Features

✅ **User Authentication**  
- Sign Up and Log In using hashed passwords  
- Session-based access control (`Flask-Login`)  

📋 **Add Crime Report**  
- Description, location, type, severity, date  
- Upload evidence (images/documents)

🗂️ **View & Manage Reports**  
- View all crimes on a dashboard  
- Display uploaded image evidence  
- Delete crime records with confirmation

🔎 **Search & Filter**  
- Filter by description, date range, type, and location  
- Pagination support for large datasets

🏠 **Homepage**  
- Custom home page styled for law enforcement usage

📁 **File Upload Handling**  
- Evidence files stored under `static/uploads` securely

---

## 💻 Tech Stack

- **Python 3**
- **Flask**
- **Flask-SQLAlchemy**
- **Flask-Login**
- **MySQL / MariaDB**
- **HTML + Jinja2 Templates**
- **CSS (Responsive & Styled)**

## Future Improvements
- User roles (Admin, Officer, Viewer)

- Crime update/edit feature

- Downloadable reports (PDF/CSV)

- Dashboard with charts/analytics

## 🤝 Contributing
Pull requests are welcome! For suggestions, contact me or open an issue.