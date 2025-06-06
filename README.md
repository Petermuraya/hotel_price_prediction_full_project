# 🏨 Hotel Price Prediction System

![System Architecture](https://img.shields.io/badge/architecture-fullstack-brightgreen)
![ML Model](https://img.shields.io/badge/model-XGBoost-orange)
![Frontend](https://img.shields.io/badge/frontend-Next.js-blue)
![Backend](https://img.shields.io/badge/backend-Express-black)

A full-stack application that predicts hotel prices using machine learning, with a Next.js frontend and Node.js/Express backend.

## ✨ Features

- **Real-time price predictions** based on location, amenities, and seasonality
- **Interactive dashboard** with visualizations
- **Admin panel** for model management
- **REST API** for integration
- **Historical data analysis**

## 🛠 Tech Stack

### Frontend
| Technology | Purpose |
|------------|---------|
| Next.js 14 | React framework |
| TypeScript | Type safety |
| Tailwind CSS | Styling |
| Chart.js | Data visualization |

### Backend
| Technology | Purpose |
|------------|---------|
| Node.js 18 | Runtime |
| Express.js | API framework |
| PostgreSQL | Database |
| Redis | Caching |

### Machine Learning
| Technology | Purpose |
|------------|---------|
| Python 3.9 | ML environment |
| Scikit-learn | Model training |
| XGBoost | Prediction algorithm |
| Pandas | Data processing |

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.9+
- PostgreSQL 12+
- Redis 6+

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/hotel-price-prediction.git
cd hotel-price-prediction

# Install dependencies
npm run setup  # Runs install for all services
cp .env.example .env
cp frontend/.env.example frontend/.env.local
cp backend/.env.example backend/.env
cp ml-service/.env.example ml-service/.env
# Start all services in development mode
npm run dev

# Or start individually:
# Frontend
cd frontend && npm run dev

# Backend 
cd backend && npm run dev

# ML Service
cd ml-service && python app.py