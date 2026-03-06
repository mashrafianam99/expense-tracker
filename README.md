# 💰 Expense Tracker

A simple and clean expense tracking web application built with Python (Flask) and SQLite. Designed to help users manage and track their daily expenses efficiently with an intuitive interface and reliable backend storage.

This project demonstrates full-stack web development with a focus on clean code, user experience, and real-world functionality—ideal for both learning and portfolio showcasing.

## ✨ Features

- 📊 **Dashboard View** - Clean, card-based interface displaying total expenses at a glance
- ✍️ **Add Expenses** - Easy-to-use form to record expenses with amount, category, date, and notes
- 🗑️ **Delete Expenses** - Remove expenses with a single click
- 📈 **Expense Summary** - View spending by category and time period
- 💾 **Persistent Storage** - All data stored securely in SQLite database
- 🎨 **Clean UI** - Professional, minimal design with responsive layout
- 🔍 **Search & Filter** - Find expenses quickly by category or date range
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask
- **Frontend:** HTML5, CSS3
- **Database:** SQLite
- **Version Control:** Git, GitHub
- **Deployment:** Render (or similar platform)

## 📋 Prerequisites

Before you begin, ensure you have:
- Python 3.7 or higher installed
- pip (Python package manager)
- Git
- A modern web browser
- Basic knowledge of Python and Flask (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mashrafianam99/expense-tracker.git
cd expense-tracker
```

### 2. Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

```bash
python app.py
```

The app will automatically create the SQLite database on first run.

### 5. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 💻 Usage

### Adding an Expense

1. Click the **"Add Expense"** button on the dashboard
2. Enter the following details:
   - **Amount:** Expense amount (in your currency)
   - **Category:** Select from predefined categories
   - **Date:** Pick the date of the expense
   - **Notes:** Optional details about the expense
3. Click **"Save Expense"**

### Viewing Expenses

- View all expenses on the main dashboard
- See total spending amount at the top
- Expenses are listed with amount, category, date, and notes

### Deleting an Expense

1. Find the expense you want to remove
2. Click the **delete icon** or **"Delete"** button
3. Confirm the deletion

### Filtering Expenses

- Filter by category dropdown
- Filter by date range using date inputs
- Search functionality for quick lookups

## 📁 Project Structure

```
expense-tracker/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── config.py             # Configuration settings
├── database.py           # Database initialization & queries
├── templates/
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Dashboard view
│   ├── add_expense.html  # Add expense form
│   └── edit_expense.html # Edit expense form (optional)
├── static/
│   ├── css/
│   │   └── style.css     # Main styling
│   ├── js/
│   │   └── main.js       # Frontend logic
│   └── images/           # Icons and images
├── database.db           # SQLite database (auto-generated)
└── README.md
```

## 🔧 Configuration

Edit `config.py` to customize:

```python
# Database configuration
DATABASE = 'database.db'

# Flask settings
DEBUG = True
SECRET_KEY = 'your-secret-key-here'

# Currency symbol
CURRENCY = '₹'  # Change to your currency

# Categories
CATEGORIES = ['Food', 'Transport', 'Entertainment', 'Utilities', 'Other']
```

## 📊 Database Schema

### Expenses Table

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key (auto-increment) |
| amount | FLOAT | Expense amount |
| category | TEXT | Category of expense |
| date | DATE | Date of expense |
| notes | TEXT | Additional notes |
| created_at | TIMESTAMP | Creation timestamp |

## 🚀 Deployment

### Deploy on Render

1. Push your code to GitHub
2. Visit [Render.com](https://render.com)
3. Connect your GitHub repository
4. Set environment variables
5. Deploy!

**Live Demo:** [Expense Tracker App](https://expense-tracker-2-a1eu.onrender.com)

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] User authentication and registration
- [ ] Monthly/yearly reports and statistics
- [ ] Data export to CSV/PDF
- [ ] Budget setting and alerts
- [ ] Multiple user accounts
- [ ] Chart visualizations for spending trends
- [ ] Category-wise spending breakdown
- [ ] Recurring expense support

## 📄 License

This project is open source and available under the MIT License. See the LICENSE file for details.

## 🐛 Troubleshooting

**Port 5000 already in use?**
```bash
# Use a different port
python app.py --port 8000
```

**Database not found?**
```bash
# Reinitialize the database
python -c "from app import init_db; init_db()"
```

**Module not found errors?**
```bash
# Ensure virtual environment is activated and dependencies are installed
pip install -r requirements.txt
```

## 📧 Contact & Support

For questions, bugs, or feature requests, please:
- Open an issue on GitHub
- Contact [Mashrafi Anam](https://github.com/mashrafianam99)
- Email: your-email@example.com

---

**Made with 💙 by Mashrafi Anam**

