# Django E-commerce Application with PayPal Integration

🌐 Welcome to our Django-based E-commerce application! This project combines the power of Python, Django, HTML, CSS, and JavaScript to create a robust online shopping experience. We've also integrated PayPal as the payment gateway for secure and convenient transactions.

## Features

✨ **User Authentication**: Users can sign up, log in, and manage their profiles, ensuring a personalized shopping experience.

🛒 **Product Management**: Easily add, update, and delete products from the admin panel. Each product comes with detailed information, including price, description, and images.

🛍️ **Shopping Cart**: Users can add products to their cart, review items, and proceed to checkout for a seamless shopping process.

💳 **PayPal Integration**: Securely process payments using PayPal, a trusted and widely used payment gateway.

🔄 **Ajax for Dynamic Updates**: Experience real-time updates without page refreshes. Ajax is implemented for smooth interaction and improved user experience.

📦 **Order Tracking**: Users can track their orders and view order history.

🔒 **Security**: The application prioritizes user data security, utilizing Django's built-in security features.

## Prerequisites

Ensure you have the following installed:

- Python (version x.x)
- Django (version 4.2.6)
- Virtualenv

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    ```

2. Create a virtual environment:

    ```bash
    virtualenv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your browser and go to [http://localhost:8000](http://localhost:8000) to view the application.

## Configuration

1. Set up your PayPal credentials in `settings.py`:

    ```python
    PAYPAL_CLIENT_ID = 'your_paypal_client_id'
    PAYPAL_SECRET_KEY = 'your_paypal_secret_key'
    ```

2. Customize other settings as needed.

## Usage

- Visit the admin panel at [http://localhost:8000/admin](http://localhost:8000/admin) to manage products, users, and orders.

- Explore the website, add products to your cart, and proceed through the checkout process to test the PayPal integration.

## Contributions

We welcome contributions! Please fork the repository and create a pull request with your improvements.

🚀 Happy coding and happy selling! 🛍️
