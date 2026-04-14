# SauceDemo & ReqRes Automation Project (Playwright + Python)

This repository contains a comprehensive test automation suite covering both Frontend (UI) and Backend (API) testing.

## 🛠 Tech Stack
* **Language**: Python 3.12
* **UI Framework**: Playwright (Pytest-playwright)
* **API Client**: Requests
* **Test Runner**: Pytest
* **Design Pattern**: Page Object Model (POM)

## 📋 Test Scenarios

### Frontend (SauceDemo)
1. **Successful Login**: Authorization using `standard_user`.
2. **Locked Out User**: Validation of error messages for `locked_out_user`.
3. **Add to Cart**: Verifying the shopping cart badge after adding items.
4. **End-to-End Checkout (E2E)**: Complete flow from login to order confirmation.

### Backend (ReqRes API)
5. **GET List Users**: Validation of user data (specifically "Lawson" and "Ferguson") and total count verification.
6. **POST Create User**: Data-driven tests for user creation with different payloads.

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ViktoriaFrunze/moxymind-saucedemo-automation.git](https://github.com/ViktoriaFrunze/moxymind-saucedemo-automation.git)
   cd moxymind_automation