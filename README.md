# SauceDemo Automation Project (Playwright + Python)

This is a professional test automation project for the [SauceDemo](https://www.saucedemo.com/) e-commerce website.

## 🛠 Tech Stack
* **Language**: Python 3.12
* **Framework**: Pytest
* **Automation Tool**: Playwright
* **Design Pattern**: Page Object Model (POM)

## 📋 Test Scenarios
1. **Successful Login**: Authorization using `standard_user`. *Critical for verifying system access.*
2. **Locked Out User**: Validation of error messages when logging in as `locked_out_user`. *Testing negative scenarios and error handling.*
3. **Add to Cart**: Adding an item to the shopping cart and verifying the cart badge counter. *Core business logic of product selection.*
4. **End-to-End Checkout (E2E)**: A complete user journey from login to the "THANK YOU FOR YOUR ORDER" screen. *Verifying the critical path of the purchase process.*

## 🚀 How to Run the Project Locally

1. **Clone the repository:**
   ```bash
   git clone <your_repository_link>
   cd moxymind_automation