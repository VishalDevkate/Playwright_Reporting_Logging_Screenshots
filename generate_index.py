import os
from datetime import datetime

REPORTS_DIR = "reports"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
run_dir = os.path.join(REPORTS_DIR, timestamp)
os.makedirs(run_dir, exist_ok=True)

# Move latest pytest-html report into timestamped folder
if os.path.exists(os.path.join(REPORTS_DIR, "report.html")):
    os.rename(
        os.path.join(REPORTS_DIR, "report.html"),
        os.path.join(run_dir, "report.html")
    )

# Build index.html with links to all past runs
links = []
for folder in sorted(os.listdir(REPORTS_DIR)):
    folder_path = os.path.join(REPORTS_DIR, folder)
    if os.path.isdir(folder_path):
        report_file = os.path.join(folder_path, "report.html")
        if os.path.exists(report_file):
            links.append(f'<li><a href="{folder}/report.html">{folder}</a></li>')

html = f"""
<!DOCTYPE html>
<html>
<head>
  <title>Unified Test Report Dashboard</title>
</head>
<body>
  <h1>Playwright + Pytest Reports</h1>
  <ul>
    {''.join(links)}
  </ul>
  <p>Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
</body>
</html>
"""

with open(os.path.join(REPORTS_DIR, "index.html"), "w") as f:
    f.write(html)