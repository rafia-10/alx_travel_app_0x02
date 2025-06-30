# Milestone 4: Payment Integration with Chapa API
Overview
Implemented a seamless payment system using Chapa’s API to handle bookings securely with real-time payment verification.

# Features
Added a Payment model to track transaction details and statuses.

Integrated Chapa’s sandbox environment for safe payment testing.

Users can initiate payments linked to their bookings and get a secure checkout URL.

Payment status verified via API callbacks; updates stored automatically.

Graceful handling of failed or incomplete payments.

Ready for live deployment with environment variables for API keys.

Email confirmations via Celery for async background tasks.

# How to Test
Use the sandbox secret key in your .env file (CHAPA_SECRET_KEY).

Create a booking via API and initiate payment.

Follow the checkout URL from the response to complete payment on Chapa sandbox.

Verify payment status using the verification endpoint.

##Notes
Update your .env with your actual Chapa API credentials.

Ensure Django environment is configured to allow these payment endpoints.

Future work: add full email notification support with Celery and Redis.
