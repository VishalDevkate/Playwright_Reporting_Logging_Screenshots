# Playwright + Pytest Automation Framework

This project is a **Python Playwright automation framework** built with **Pytest**, featuring:
- Page Object Model (POM)
- Environment‑specific configs (QA, Staging, Prod)
- Rich reporting (pytest‑html + Allure dashboard)
- Screenshots, logs, and traces on failure
- Docker + CI/CD matrix strategy
- Slack/MS Teams notifications

## 🚀 Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>

2. **Create virtual environment (Python 3.11/3.12 recommended)**
   ```bash
   py -3.12 -m venv venv
   venv\Scripts\activate
   
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   playwright install --with-deps
   
4. **Run tests**
   ```bash
   pytest featureA_tests --env=qa --alluredir=allure-results/featureA
   pytest featureB_tests --env=staging --alluredir=allure-results/featureB
   pytest featureC_tests --env=prod --alluredir=allure-results/featureC
   
5. **Generate reports**
   ```bash
   mkdir merged-results
   cp -r allure-results/*/* merged-results/
   python generate_index.py
   allure generate merged-results -o allure-report --clean
   allure open allure-report

## CI/CD
- Push to main → GitHub Actions runs matrix jobs per feature folder.
- Results merged into one Allure dashboard and published to GitHub Pages.
- Slack/MS Teams notifications sent with report links.
---

## 📂 Folder Structure

project-root/
│
├── pytest.ini                # Global defaults (markers, plugins, retries)
├── config.yaml               # Environment configs (qa/staging/prod)
├── conftest.py                # Global fixtures/hooks (browser, env loader)
├── generate_index.py          # Builds unified report index
│
├── featureA_tests/            # Login feature
│   ├── conftest.py
│   └── test_login.py
│
├── featureB_tests/            # Dropdown feature
│   ├── conftest.py
│   └── test_dropdown.py
│
├── featureC_tests/            # Checkbox feature
│   ├── conftest.py
│   └── test_checkbox.py
│
├── reports/                   # HTML reports + screenshots + traces
│   ├── index.html
│   └── <timestamped folders>
├── allure-results/            # Raw Allure results
├── allure-report/             # Generated Allure dashboard
└── .github/
    └── workflows/
        └── pytest-matrix.yml  # CI/CD pipeline

---

## ✨ Features

- **Global Config (`pytest.ini`)**  
  Shared markers, retries, reporting options.

- **Per‑Feature Config (`conftest.py`)**  
  Each folder defines its own fixtures (e.g., login, dropdown, checkbox).

- **Environment Config (`config.yaml`)**  
  Switch between QA, Staging, Prod with `--env` option.

- **Reporting**  
  - `pytest-html` → lightweight HTML reports per run.  
  - `allure-pytest` → rich dashboard with features, stories, severity, screenshots.

- **CI/CD Matrix**  
  Runs each feature folder separately, merges Allure results into one unified dashboard.

- **Notifications**  
  Slack/MS Teams alerts with links to reports.

---

🏆 Benefits
- Clean separation of configs per feature folder.
- Unified reporting dashboard for overall visibility.
- Dockerized + CI/CD ready.
- Rich Allure grouping (@allure.feature, @allure.story, @allure.severity).
- Screenshots and traces attached to failed tests.
