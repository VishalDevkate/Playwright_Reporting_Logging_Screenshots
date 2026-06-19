import os
from datetime import datetime

REPORTS_DIR = "reports"
index_path = os.path.join(REPORTS_DIR, "index.html")

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

with open(index_path, "w") as f:
    f.write(html)