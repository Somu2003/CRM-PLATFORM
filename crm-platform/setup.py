from setuptools import setup, find_packages

setup(
    name="mini-crm-platform",
    version="1.0.0",
    description="A simplified CRM platform with AI-powered features",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.104.1",
        "uvicorn>=0.24.0",
        "streamlit>=1.28.1",
        "sqlalchemy>=2.0.23",
        "pandas>=2.1.3",
        "requests>=2.31.0",
        "google-generativeai>=0.3.2",
        "python-dotenv>=1.0.0",
    ],
    python_requires=">=3.8",
)
