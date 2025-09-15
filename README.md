# CRM-PLATFORM
🎯 Mini CRM Platform
A modern, full-stack Customer Relationship Management (CRM) platform built with FastAPI and Streamlit. This comprehensive solution enables businesses to manage customers, create marketing campaigns, track orders, and analyze business performance through an intuitive web interface.

[![Python](https://img.shields.iohttps://img.shields.io/badge/FastAPI-0ps://img.ps://img.shields.io/badge/License-MIT-yellow 🌟 Features

👥 Customer Management
Complete CRUD Operations - Add, view, edit, and delete customers

Advanced Search - Find customers by name or email

Customer Analytics - Track spending patterns and order history

Data Export - Export customer data for external use

🎯 Campaign Management
Campaign Creation - Design and launch marketing campaigns

Audience Targeting - Segment customers (All, High-Value, New, Inactive)

AI Message Generation - Automated message templates with personalization

Campaign Analytics - Track delivery rates, open rates, and performance

Campaign Control - Pause, resume, and manage active campaigns

📦 Order Management
Order Tracking - Complete order lifecycle management

Customer Integration - Automatic customer total updates

Product Categories - Organize orders by category

Order Analytics - Revenue tracking and order insights

📊 Business Analytics
Real-time Dashboard - Key performance indicators (KPIs)

Customer Segmentation - Visual breakdown of customer types

Revenue Analytics - Track total revenue and average customer value

Interactive Charts - Plotly-powered visualizations

Business Insights - Automated recommendations and insights

🔐 Security & Authentication
Simple Authentication - Demo login system

Session Management - Secure user sessions

Data Protection - Input validation and sanitization

🛠️ Technology Stack
Backend
FastAPI - Modern, fast web framework for building APIs

SQLAlchemy - SQL toolkit and Object-Relational Mapping

SQLite - Lightweight, serverless database

Pydantic - Data validation using Python type annotations

Uvicorn - Lightning-fast ASGI server

Frontend
Streamlit - The fastest way to build and share data apps

Plotly - Interactive graphing library

Pandas - Powerful data analysis and manipulation tool

Requests - HTTP library for API communication

Deployment
Render.com - Cloud platform for modern applications

GitHub - Version control and CI/CD integration

🚀 Quick Start
Prerequisites
Python 3.11 or higher

Git

A modern web browser

Local Development Setup
Clone the Repository

bash
git clone https://github.com/Somu2003/mini-crm-platform.git
cd mini-crm-platform
Set Up Backend

bash
cd backend

# Create virtual environment
python -m venv env

# Activate virtual environment
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start backend server
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
Set Up Frontend (in a new terminal)

bash
cd frontend

# Create virtual environment
python -m venv env

# Activate virtual environment
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start frontend application
streamlit run app.py
Access the Application

Frontend: http://localhost:8501

Backend API: http://localhost:8000

API Documentation: http://localhost:8000/docs

Demo Login
Email: Any email address (demo@example.com)

Password: Any password

📁 Project Structure
text
mini-crm-platform/
├── backend/
│   ├── app.py                 # FastAPI application
│   ├── requirements.txt       # Backend dependencies
│   └── runtime.txt           # Python version for deployment
├── frontend/
│   ├── app.py                # Streamlit application
│   ├── utils/
│   │   └── api_client.py     # API communication client
│   ├── requirements.txt      # Frontend dependencies
│   └── runtime.txt          # Python version for deployment
├── README.md                 # Project documentation
└── LICENSE                   # MIT License
🌐 Live Demo
🔗 Frontend Application: https://mini-crm-frontend-q2xw.onrender.com

🔗 Backend API: https://mini-crm-backend.onrender.com

🔗 API Documentation: https://mini-crm-backend.onrender.com/docs

📖 Usage Guide
Getting Started
Login - Use any email and password for demo access

Explore Dashboard - View key metrics and recent activity

Manage Customers - Add, edit, or search for customers

Create Campaigns - Launch targeted marketing campaigns

Track Orders - Monitor order history and revenue

Analyze Performance - Review business analytics and insights

Key Workflows
Adding a New Customer
Navigate to "Customers" → "Add Customer"

Fill in customer details (name, email, phone)

Click "Add Customer"

Customer appears in the customer list

Creating a Marketing Campaign
Go to "Campaigns" → "Create Campaign"

Enter campaign name and select audience type

Write message template (use {name} for personalization)

Use "Generate AI Messages" for inspiration

Click "Launch Campaign"

Viewing Business Analytics
Visit "Analytics" section

Review KPIs: revenue, customers, orders

Analyze customer segmentation

Review business insights and recommendations

🚢 Deployment
Deploy to Render.com
Fork the Repository

bash
# Fork on GitHub, then clone your fork
git clone https://github.com/your-username/mini-crm-platform.git
Deploy Backend

Create account on Render.com

Connect your GitHub repository

Create Web Service for backend

Build Command: pip install -r requirements.txt

Start Command: uvicorn app:app --host 0.0.0.0 --port $PORT

Deploy Frontend

Create another Web Service for frontend

Build Command: pip install -r requirements.txt

Start Command: streamlit run app.py --server.port $PORT --server.address 0.0.0.0

Environment Variable: BACKEND_URL = https://your-backend.onrender.com

Environment Variables
Frontend: BACKEND_URL - URL of the deployed backend service

🧪 API Endpoints
Customers
GET /customers - List all customers

POST /customers - Create new customer

PUT /customers/{id} - Update customer

DELETE /customers/{id} - Delete customer

Campaigns
GET /campaigns - List all campaigns

POST /campaigns - Create new campaign

PUT /campaigns/{id} - Update campaign

DELETE /campaigns/{id} - Delete campaign

GET /campaigns/{id}/stats - Get campaign statistics

Orders
GET /orders - List all orders

POST /orders - Create new order

PUT /orders/{id} - Update order

DELETE /orders/{id} - Delete order

Analytics
GET /analytics/dashboard - Get dashboard statistics

GET /analytics/customer-segments - Get customer segmentation data

AI Features
GET /ai/generate-message - Generate AI-powered message templates

🤝 Contributing
We welcome contributions to the Mini CRM Platform! Here's how you can help:

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Make your changes and add tests if applicable

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

Development Guidelines
Follow PEP 8 style guidelines for Python code

Add docstrings to new functions and classes

Write clear commit messages

Update documentation for new features

🐛 Issues and Support
If you encounter any issues or have questions:

Check existing issues on GitHub Issues

Create a new issue with detailed description and steps to reproduce

Include system information (OS, Python version, browser)

🔮 Future Enhancements
 Email Integration - Send actual marketing emails

 Advanced Analytics - More detailed reporting and insights

 User Management - Multi-user support with role-based access

 Data Import/Export - CSV import/export functionality

 Mobile Responsiveness - Optimized mobile interface

 API Rate Limiting - Production-ready API security

 Database Migration - PostgreSQL support for production

 Real-time Notifications - WebSocket-based live updates

📊 Sample Data
The application comes pre-loaded with sample data including:

5 Sample Customers with realistic profiles and spending data

3 Sample Campaigns showing different audience targeting

5 Sample Orders demonstrating order tracking capabilities

🔒 Security Considerations
Input validation and sanitization on all endpoints

SQL injection protection through SQLAlchemy ORM

CORS configuration for secure cross-origin requests

Session-based authentication (demo implementation)

📈 Performance Features
Caching - Frontend data caching for improved performance

Database Indexing - Optimized database queries

Async Processing - FastAPI async capabilities

Pagination Ready - Scalable data loading architecture

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
FastAPI team for the excellent web framework

Streamlit team for making data apps incredibly easy to build

Render.com for providing excellent hosting services

Open Source Community for the amazing tools and libraries

📞 Contact
Developer: Somu2003
GitHub: @Somu2003
Project Link: https://github.com/Somu2003/mini-crm-platform
