# Infinite Technology Website

This repository contains the source code for **Infinite Technology's** marketing website.  
It is a lightweight Flask application that serves a set of Jinja‑templated pages (Home, About, Services, Portfolio and Contact) and a collection of static assets, including several `.glb` 3D models displayed with Google’s `<model-viewer>` web component.

---

## ✨ Key Features

| Area | Details |
|------|---------|
| **Backend** | Python + [Flask](https://flask.palletsprojects.com/) micro‑framework |
| **Frontend** | HTML5, CSS3, vanilla JS + `<model-viewer>` for 3D models |
| **3D Assets** | Multiple GLB models (HTML logo, Flutter, Gaming Setup, etc.) located in **`static/`** |
| **Responsive** | Meta viewport tag ensures mobile‑friendly layout |
| **SEO & Schema** | JSON‑LD organisation schema, proper meta tags |
| **Deployment Ready** | Works on any WSGI host (Render, Heroku, Railway, Fly.io, etc.) |

---

## 🚀 Quick‑start

```bash
# 1. Clone the repo
git clone https://github.com/your‑username/infinite‑technology.git
cd infinite‑technology

# 2. Create & activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Run the development server
python app.py                 # or: flask run
```

The site will be available at **http://127.0.0.1:5000** by default.

---

## 🗂️ Project Structure

```
infinite technologys/
├── app.py                 # Flask application entry‑point
├── static/                # Images, 3D models, CSS/JS if any
│   ├── *.glb
│   └── *.png / *.jpg
└── templates/             # Jinja2 HTML templates
    ├── index.html
    ├── about.html
    ├── services.html
    ├── portfolio.html
    └── contact.html
```

---

## ⚙️ Configuration

*No environment variables are required* for local development.  
For production you can set:

| Variable | Example | Purpose |
|----------|---------|---------|
| `FLASK_ENV` | `production` | Disable debug mode |
| `PORT` | `8080` | Custom port if your host needs one |

---

## ☁️ Deploying to Render

1. **Create a new Web Service** and connect your Git repository.  
2. Set the **Build Command** to:

```bash
pip install -r requirements.txt
```

3. Set the **Start Command** to:

```bash
gunicorn app:app
```

4. Choose a Python runtime (3.11 recommended) and hit **Deploy**.

Render will automatically detect changes and redeploy on every push.

---

## 📝 License

This project is released under the MIT License – see the [LICENSE](LICENSE) file for details.
