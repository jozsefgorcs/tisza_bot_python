# Tiszacipő Sale Finder Bot

A Telegram bot to fetch and share discounted shoes from the Tiszacipő website.

## Features

- **Fetch Sale Items**: Download and display discounted shoes from Tiszacipő.
- **Size Specific Search**: Use the `/kifuto` command followed by the size (e.g., `/kifuto 43`) to get sale items for that specific shoe size.
- **Image Display**: Show images of the discounted shoes directly in the chat.

## Usage

1. **Add the bot to your Telegram**: Search for the bot and add it to your contacts or group.
2. **Get Sale Items by Size**: Use the command `/kifuto` followed by the desired shoe size.
    - Example: `/kifuto 43` will fetch and display all size 43 shoes on sale.

![Example Image](https://imgur.com/xWxSW4y)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/jozsefgorcs/tisza_bot_python.git
    cd tisza-bot-python
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Bot Token**: Update your bot token via environment variable with the key: `TELEGRAM_BOT_TOKEN`.

4. **Run the Bot**:
    ```bash
    python main.py
    ```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any changes or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.