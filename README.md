# 🎫 Smart Ticket Management System

A web-based ticket management system built using **Python, Flask, SQLite, and AI-based classification** to intelligently prioritize and process support tickets.

---

## Features
- Raise support tickets via UI
- AI-powered ticket classification
- Priority-based ticket queue
- Admin panel to process tickets
- Real-time ticket statistics
- Persistent storage using SQLite

---

## Architecture Overview

Frontend (HTML + CSS + JS)
        ↓
Flask REST APIs
        ↓
AI Classifier + Priority Engine
        ↓
In-Memory Priority Queue (heap)
        ↓
SQLite Database (Source of Truth)

---

## Technologies Used
- **Python 3**
- **Flask** – backend & APIs
- **SQLite** – database
- **Heap Queue (heapq)** – priority queue
- **HTML, CSS, JavaScript** – frontend
- **AI/NLP (Rule-based / extendable)** – ticket classification

---

##  AI Usage Explained
- User ticket description is analyzed
- Category predicted (Network, HR, General, etc.)
- Priority assigned automatically based on category
- Queue orders tickets using priority + FIFO logic

---

## ⚙️ How Ticket Processing Works
1. Ticket submitted → stored in DB
2. Ticket added to priority queue
3. Admin clicks "Process Next Ticket"
4. Highest priority OPEN ticket is closed
5. Queue and DB stay synchronized

---

##  Challenges Faced
- Synchronizing in-memory queue with persistent DB
- Handling app restarts without losing queue state
- Preventing ghost tickets after page reload
- Ensuring admin processing works independently

---

##  Solutions Implemented
- DB used as single source of truth
- Queue rebuilt from DB on app startup
- Strict validation for ticket submission
- Clear separation of concerns (DB, Queue, AI)

---

##  Future Enhancements
- Authentication for admin panel
- ML-based NLP classification
- Ticket SLA & timestamps
- Email notifications
- Docker deployment

---

## 👨‍💻 Author
**Abhinay Goswami**  
Backend / Python / AI Enthusiast
