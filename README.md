# Cyber-Password-Toolkit


Welcome to **Cyber Password Toolkit** – a simple, professional cybersecurity web tool for generating strong passwords and testing password strength based on NIST (SP 800-63B) standards.

Hosted Live 👉 [https://cyber-password-toolkit.onrender.com/](https://cyber-password-toolkit.onrender.com/)


##  Features

-  **Password Generator**: Instantly generates secure passwords between 12–24 characters.
-  **Password Strength Tester**:
    - Checks if password meets NIST minimum requirements (≥ 8 characters).
    - Displays estimated crack time for passwords.
    - Shows a **live updating strength bar** (Red → Orange → Green).
-  **Show/Hide Password** option for better usability.
-  **Fully hosted** on Render with HTTPS protection.


## 🛠 Built With

- **Python 3** (Flask Framework)
- **HTML5 / CSS3 / JavaScript**
- **Render.com** (for hosting)
- **zxcvbn** password strength estimator



##  Getting Started (Local Development)

1. Clone the repo:
    ```bash
    git clone https://github.com/yourusername/Cyber-Password-Toolkit.git
    cd Cyber-Password-Toolkit
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    python app.py
    ```

4. Visit `http://localhost:5000` in your browser!



##  About NIST SP 800-63B Password Guidelines

- Minimum password length of **8 characters**.
- No requirement for symbols, uppercase, or numbers.
- Allow spaces, emojis, and unicode characters.
- Encourage long and memorable passwords over complex short ones.
- Passwords should be checked against breach lists (optional).

*This toolkit respects the above principles while evaluating password strength.*



##  Screenshots

| Generator Page | Strength Tester Page |
|:--------------:|:--------------------:|
| ![Generator](static/screenshots/generator.png) | ![Tester](static/screenshots/tester.png) |

(*Optional - you can add real screenshots later!*)



##  Future Improvements

- Check passwords against breached password databases (HaveIBeenPwned API).
- Add animated background effects for a more cyberpunk look.
- Dark/Light mode toggle.



##  Author

Made with ❤️ by **Vinu Varshith**

- GitHub: [vinuvarshith95](https://github.com/vinuvarshith95)
- LinkedIn: [vinuvarshithalagappan](https://www.linkedin.com/in/vinuvarshithalagappan/)



