# 🚀 Zavvis AI CFO Backend

An intelligent, modular backend system built with **FastAPI** for Zavvis Technologies’ AI CFO product.

---

## ✨ What Does It Do?

- 🔁 **12-week cash flow forecasting**
- 💡 **Actionable financial insights**
- 📊 **KPI benchmarking** (DSO, DPO, CCC, etc.)
- 💰 **Financing recommendations**
- 🔗 **QuickBooks & Plaid integration**

---

## 🧩 Features

- Modular, domain-driven architecture
- JWT-based authentication system
- Real-time financial data processing
- Data ingestion from QuickBooks and Plaid
- KPI insights engine (cash buffer, CCC, revenue linearity)
- Scalable API design using FastAPI and PostgreSQL

---

## 📁 Project Structure

```
ai_cfo_backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── router.py
│   │       └── modules/
│   │           ├── auth/           # Signup, login, token services
│   │           ├── user/           # Profile and org settings
│   │           ├── cashflow/       # Forecasts, growth, summaries
│   │           ├── benchmarking/   # DSO, DPO, CCC, KPIs
│   │           ├── financing/      # Debt service, LOC, funding alerts
│   │           ├── reports/        # Data export and visual summaries
│   │           ├── data/           # Raw ingestion or manual upload
│   │           └── integrations/   # QuickBooks, Plaid APIs
│   ├── core/
│   │   ├── config.py               # App settings via Pydantic
│   │   ├── security.py             # JWT, password hashing
│   │   ├── oauth.py                # OAuth2 integrations
│   │   └── logger.py               # Structured logging
│   ├── db/
│   │   ├── session.py              # Database session
│   │   ├── base.py                 # SQLAlchemy base
│   │   └── models/
│   │       ├── user.py
│   │       ├── cashflow.py         # zv_cash_flow_actuals, etc.
│   │       ├── kpis.py             # DSO, DPO, CCC
│   │       ├── inventory.py        # Inventory metrics
│   │       ├── debt.py             # Debt and capex tables
│   │       ├── returns.py          # Customer returns
│   │       ├── collections.py      # Past due AR
│   │       ├── staging_qb.py       # QuickBooks raw imports
│   │       ├── staging_plaid.py    # Plaid raw imports
│   │       └── business.py         # Business/org metadata
│   ├── utils/
│   │   ├── file_parser.py          # CSV, Excel, API-to-DB helpers
│   │   ├── calculator.py           # KPI math & cash flow logic
│   │   └── formatter.py            # Label, date, and currency utils
│   └── main.py                     # Entry point for FastAPI app
├── tests/                          # Unit tests per module
├── .env                            # Environment variables
├── Dockerfile                      # Container config
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy ORM**
- **Pydantic** (data validation)
- **QuickBooks API**, **Plaid Link**
- **Docker**

---

## ⚡ Getting Started

1. **Clone the repository**
    ```sh
    git clone https://github.com/zavvis/ai-cfo-backend.git
    cd ai-cfo-backend
    ```

2. **Create virtual environment & install dependencies**
    ```sh
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Add your environment variables in `.env`**
    ```
    DATABASE_URL=postgresql://user:password@localhost/dbname
    SECRET_KEY=your-secret-key
    ```

4. **Run the app**
    ```sh
    uvicorn app.main:app --reload
    ```

---

## 🤝 Contributing

Feel free to fork this repo and submit PRs. All modules are structured for scalability.

---

## 📬 Contact

Have questions or ideas?  
Reach out to the team at [info@zavvis.ai](mailto:info@zavvis.ai)