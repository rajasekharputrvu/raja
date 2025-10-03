from bs4 import BeautifulSoup
import pandas as pd

html_file_path = r"C:\Users\z0149910\Downloads\FCME24_diva_report0002 (1).html"

with open(html_file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

results = []

# Try all <span> tags — some DiVa reports use <span title="✔ Passed"> etc.
spans = soup.find_all("span")
print(f"🔍 Total <span> tags found: {len(spans)}")

for span in spans:
    title = span.get("title", "")
    if "Passed" in title or "✔" in title:
        status = "Pass"
    elif "Failed" in title or "❌" in title:
        status = "Fail"
    else:
        continue

    # Try to get parent text to extract test case name
    parent_text = span.find_parent().get_text(strip=True)
    
    # Filter out useful test case IDs (heuristic)
    if "_Service" in parent_text or "9.1." in parent_text:
        test_case_id = parent_text
        results.append({"Test Case ID": test_case_id, "Status": status})

# Print few results for debug
for r in results[:5]:
    print(r)

if results:
    df = pd.DataFrame(results).drop_duplicates()
    excel_output = "DiVa_Test_Case_Summary.xlsx"
    df.to_excel(excel_output, index=False)
    print(f"✅ Excel file generated: {excel_output}")
else:
    print("❌ Still no test cases found. HTML structure may need deeper inspection.")
