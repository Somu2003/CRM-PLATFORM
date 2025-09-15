# 🎯 Mini CRM Platform

A modern, full-stack Customer Relationship Management (CRM) platform built with **FastAPI** and **Streamlit**.  
This comprehensive solution enables businesses to manage customers, create marketing campaigns, track orders, and analyze business performance through an intuitive web interface.

![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🌟 Features

### 👥 Customer Management
- **CRUD Operations** - Add, view, edit, and delete customers  
- **Advanced Search** - Find customers by name or email  
- **Customer Analytics** - Track spending patterns and order history  
- **Data Export** - Export customer data for external use  

### 🎯 Campaign Management
- **Campaign Creation** - Design and launch marketing campaigns  
- **Audience Targeting** - Segment customers (All, High-Value, New, Inactive)  
- **AI Message Generation** - Automated message templates with personalization  
- **Campaign Analytics** - Track delivery rates, open rates, and performance  
- **Campaign Control** - Pause, resume, and manage active campaigns  

### 📦 Order Management
- **Order Tracking** - Complete order lifecycle management  
- **Customer Integration** - Automatic customer total updates  
- **Product Categories** - Organize orders by category  
- **Order Analytics** - Revenue tracking and order insights  

### 📊 Business Analytics
- **Real-time Dashboard** - Key performance indicators (KPIs)  
- **Customer Segmentation** - Visual breakdown of customer types  
- **Revenue Analytics** - Track total revenue and average customer value  
- **Interactive Charts** - Plotly-powered visualizations  
- **Business Insights** - Automated recommendations and insights  

### 🔐 Security & Authentication
- **Simple Authentication** - Demo login system  
- **Session Management** - Secure user sessions  
- **Data Protection** - Input validation and sanitization  

---

## 🛠️ Technology Stack

**Backend**  
- FastAPI  
- SQLAlchemy  
- SQLite  
- Pydantic  
- Uvicorn  

**Frontend**  
- Streamlit  
- Plotly  
- Pandas  
- Requests  

**Deployment**  
- Render.com  
- GitHub (CI/CD)  

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+  
- Git  
- Modern web browser  

### Local Development Setup

#### Clone the Repository
```bash
git clone https://github.com/Somu2003/mini-crm-platform.git
cd mini-crm-platform
```

#### Set Up Backend
```bash
cd backend

# Create virtual environment
python -m venv env

# Activate environment
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start backend server
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

#### Set Up Frontend (in a new terminal)
```bash
cd frontend

# Create virtual environment
python -m venv env

# Activate environment
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start frontend application
streamlit run app.py
```

#### Access the Application
- Frontend: [http://localhost:8501](http://localhost:8501)  
- Backend API: [http://localhost:8000](http://localhost:8000)  
- API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)  

**Demo Login**  
- Email: Any email (e.g. demo@example.com)  
- Password: Any password  

---
## Architecture Diagram

<img width="237" height="892" alt="image" src="https://github.com/user-attachments/assets/1a9822b7-9dd3-480d-ac60-20aeab11cec1" />

## 📁 Project Structure
```
mini-crm-platform/
├── backend/
│   ├── app.py                 # FastAPI application
│   ├── requirements.txt       # Backend dependencies
│   └── runtime.txt            # Python version for deployment
├── frontend/
│   ├── app.py                 # Streamlit application
│   ├── utils/
│   │   └── api_client.py      # API communication client
│   ├── requirements.txt       # Frontend dependencies
│   └── runtime.txt            # Python version for deployment
├── README.md                  # Project documentation
└── LICENSE                    # MIT License
```

---

## 🌐 Live Demo
- 🔗 [Frontend](https://mini-crm-frontend-q2xw.onrender.com)  
- 🔗 [Backend API](https://mini-crm-backend.onrender.com)  
- 🔗 [API Docs](https://mini-crm-backend.onrender.com/docs)  

---

## 📖 Usage Guide

### Getting Started
- Login → Use any email/password  
- Explore Dashboard → View key metrics  
- Manage Customers → Add, edit, search customers  
- Create Campaigns → Launch targeted campaigns  
- Track Orders → Monitor orders & revenue  
- Analyze Performance → Review insights  

### Key Workflows

**Adding a New Customer**  
1. Navigate to "Customers" → "Add Customer"  
2. Enter details (name, email, phone)  
3. Click "Add Customer"  
4. Customer appears in list  

**Creating a Campaign**  
1. Go to "Campaigns" → "Create Campaign"  
2. Enter campaign name & audience  
3. Write template (use `{name}` for personalization)  
4. Optionally use **Generate AI Messages**  
5. Click "Launch Campaign"  

**Viewing Analytics**  
- Visit "Analytics" → KPIs, segmentation, revenue, insights  

---

## 🚢 Deployment (Render.com)

1. Fork repo → Clone your fork  
2. Deploy Backend (FastAPI)  
   - Build: `pip install -r requirements.txt`  
   - Start: `uvicorn app:app --host 0.0.0.0 --port $PORT`  
3. Deploy Frontend (Streamlit)  
   - Build: `pip install -r requirements.txt`  
   - Start: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`  
   - Env Var: `BACKEND_URL=https://your-backend.onrender.com`  

---

## 🧪 API Endpoints

**Customers**  
- `GET /customers` → List  
- `POST /customers` → Create  
- `PUT /customers/{id}` → Update  
- `DELETE /customers/{id}` → Delete  

**Campaigns**  
- `GET /campaigns`  
- `POST /campaigns`  
- `PUT /campaigns/{id}`  
- `DELETE /campaigns/{id}`  
- `GET /campaigns/{id}/stats`  

**Orders**  
- `GET /orders`  
- `POST /orders`  
- `PUT /orders/{id}`  
- `DELETE /orders/{id}`  

**Analytics**  
- `GET /analytics/dashboard`  
- `GET /analytics/customer-segments`  

**AI Features**  
- `GET /ai/generate-message`  

---

## 🤝 Contributing
We welcome contributions:  
1. Fork → Create branch → Commit → PR  
2. Follow **PEP 8** guidelines  
3. Add docstrings & clear commits  
4. Update docs for new features  

---

## 🔮 Future Enhancements
- Email Integration  
- Advanced Analytics  
- User Management (RBAC)  
- Data Import/Export (CSV)  
- Mobile Responsiveness  
- API Rate Limiting  
- PostgreSQL Support  
- Real-time Notifications  

---

## 📊 Sample Data
- 5 Sample Customers  
- 3 Sample Campaigns  
- 5 Sample Orders  

---

## 🔒 Security Considerations
- Input validation & sanitization  
- SQL injection protection  
- CORS configuration  
- Session-based auth (demo)  

---

## 📈 Performance Features
- Caching  
- DB Indexing  
- Async FastAPI  
- Pagination-ready  

---

## 📄 License
This project is licensed under the MIT License. See [LICENSE](./LICENSE).

---

## 🙏 Acknowledgments
- FastAPI team  
- Streamlit team  
- Render.com  
- Open Source Community  

---

## 📞 Contact
**Developer:** Somu2003  
**GitHub:** [@Somu2003](https://github.com/Somu2003)  
**Project Link:** [Mini CRM Platform](https://github.com/Somu2003/mini-crm-platform)  
