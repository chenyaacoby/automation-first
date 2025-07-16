# QA Automation Project – Selenium & Python

This project includes 3 automated end-to-end test cases using **Selenium**, **Python**, and **Pytest**, following the **Page Object Model (POM)**.

The tests are written for demo websites (no CAPTCHA), focusing on user flows that span multiple screens and elements.

## 🧪 Test Cases

1. **Menu Navigation + Side List Verification**  
   - Select "Forms" tab → navigate to form page → verify side menu matches main menu

2. **Form Submission with Valid Data**  
   - Fill all required fields in practice form → submit → verify success

3. **City Field Behavior Based on State Selection**  
   - Verify "City" field is disabled until "State" is selected

## 🔧 Tech Stack

- **Language:** Python 3  
- **Framework:** Pytest  
- **Automation Tool:** Selenium WebDriver  
- **Design Pattern:** Page Object Model (POM)  
- **Locators Used:** ID, Name, XPath, CSS  
- **Element Types:** Input fields, dropdowns, radio buttons, checkboxes
  
## ▶️ Run the Tests

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run all tests:
   ```bash
   pytest
   ```
