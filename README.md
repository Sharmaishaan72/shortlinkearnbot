# Shortlink Earn Bot

A Telegram bot that allows users to earn rewards by interacting with shortlinks. This bot is built using the following technologies:

- **aiogram**: For handling Telegram bot interactions.
- **Quart**: For hosting a web application.
- **ngrok**: To expose the web application to the internet.
- **Polling**: For receiving updates from Telegram.

## Features

- Users interact with shortlinks to earn rewards.
- Uses ngrok for exposing the web interface during development.
- Uses both Telegram polling and web interaction.

---

## Prerequisites

1. **Python 3.8+**
2. **Dependencies**:
   - `aiogram`
   - `quart`
   - `sqlite3` (built-in with Python)
   - `ngrok` (installed separately or via Python's pyngrok)

Install the required Python libraries:

```bash
pip install aiogram quart ngrok
```

3. **ngrok**:
   - [Download and install ngrok](https://ngrok.com/download).
   - Set up an ngrok account and obtain an authentication token.
   - Authenticate ngrok:
     ```bash
     ngrok authtoken <your-auth-token>
     ```

---

## Example Workflow

1. A user sends a command to the Telegram bot to start earning rewards.
2. The bot provides a shortlink for the user to visit.
3. The user completes the task and gets rewarded.
---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature-name'`
4. Push to the branch: `git push origin feature-name`
5. Create a pull request.

---

---

## Note

The bot has been written in less than an hour, so code quality is absolutely trash. Please feel free to create a pull request with an improved version/code quality. This is just an example bot demonstrating the usage of aiogram and Quart, and it uses webhooks to reward users.

