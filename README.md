# Playwright + Pytest Automation Framework

This project is a **Python Playwright automation framework** built with **Pytest**, featuring:
- Page Object Model (POM)
- Environment‑specific configs (QA, Staging, Prod)
- Rich reporting (pytest‑html + Allure dashboard)
- Screenshots, logs, and traces on failure
- Docker + CI/CD matrix strategy
- Slack/MS Teams notifications

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

## 🚀 Usage

### 1. Install Dependencies
```bash
pip install -r requirements.txt
playwright install --with-deps

