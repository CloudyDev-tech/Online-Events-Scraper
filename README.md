## 📅 Online-Events-Scraper

A Python-based CLI tool that scrapes and lists upcoming events such as **hackathons, competitions, and workshops** from platforms like **Devfolio** and **Reskill**.

Ideal for developers, students, and tech enthusiasts looking for new opportunities in the tech space.

---

### 🚀 Features

* 🧠 Scrapes latest events from:

  * [Devfolio](https://devfolio.co)
  * [Reskill](https://reskill.dev/)
* 📅 Displays event name, dates, location, and description
* 🔍 Clean, terminal-based output
* 💡 Useful for quick discovery of hackathons and upskilling events

---

### 🛠️ Technologies Used

* Python 3
* `requests`
* `BeautifulSoup` (`bs4`)
* `datetime`


---

### 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/CloudyDev-tech/Online-Events-Scraper.git
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

### ⚙️ Usage

```bash
python reskill_events.py
```

This will fetch and print a list of upcoming events from Devfolio and Reskill.

---

### 🖼️ Sample Output

```
🔹 Event: Hack the Mountains 3.0
📅 Date: July 20–22, 2025
📍 Location: Online
🌐 Platform: Devfolio
---------------------------
🔹 Event: AI Innovation Bootcamp
📅 Date: July 12–14, 2025
📍 Location: Online
🌐 Platform: Reskill
---------------------------
```

---

### 📈 Roadmap / Planned Features

* [ ] Add Devpost, MLH, IEEE, Hackerearth support
* [ ] Export to JSON / CSV
* [ ] Add filters (e.g., online-only, prize > \$1000)
* [ ] Build simple web UI (Flask or Streamlit)
* [ ] Add notification support (Telegram/email)
* [ ] Public REST API

---

### 💡 Ideas to Expand

* Google Calendar integration
* GitHub Profile Sync (log attended hackathons)
* Discord bot that posts new events
* Personal event dashboard

---

### 🤝 Contributing

Pull requests and suggestions are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

### 📄 License

MIT License. See [`LICENSE`](LICENSE) for more information.


* Devfolio API & site
* Reskill.dev event listings

---

