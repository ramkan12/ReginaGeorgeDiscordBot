# Regina George Discord Bot

A Discord bot that channels the iconic Regina George from Mean Girls. Get ready for sass, attitude, and iconic one-liners straight from the queen bee herself.

## Features

- **Authentic Regina George Personality**: Responds with signature Mean Girls quotes and attitude
- **Multiple Response Variations**: Different responses for greetings, farewells, and more
- **Private Messaging Support**: Prefix messages with `?` for private responses
- **Interactive Commands**: Roll dice, get fashion advice (though she might roast you), and more
- **Iconic References**: Burn Book, fetch, pink Wednesdays, and all your favorite Mean Girls moments

## Prerequisites

- Python 3.8 or higher
- A Discord Bot Token (from [Discord Developer Portal](https://discord.com/developers/applications))
- Discord.py library

## Installation

1. **Clone the repository**
   ```bash
   git clone <https://github.com/ramkan12/ReginaGeorgeDiscordBot.git>
   cd "regina george bot"
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory:
   ```
   TOKEN=your_discord_bot_token_here
   ```

## Usage

1. **Activate the virtual environment** (if not already activated)
   ```bash
   source venv/bin/activate
   ```

2. **Run the bot**
   ```bash
   python main.py
   ```

3. **Deactivate when done**
   ```bash
   deactivate
   ```

## Bot Interactions

The bot responds to various messages with Regina George-style sass:

| Input | Response Type |
|-------|--------------|
| `hello`, `hi` | Greeting (with attitude) |
| `how are you` | Status update (she's flawless, obviously) |
| `bye` | Farewell (finally!) |
| `roll dice` | Random dice roll with commentary |
| `who are you` | Identity confirmation |
| `fetch` | The iconic "fetch" quote |
| `burn book` | Burn Book reference |
| `?<message>` | Private message response |
| Any other message | Random sassy response |

### Example Interactions

```
User: hello
Bot: Ugh, hi...

User: fetch
Bot: Stop trying to make fetch happen. It's not going to happen.

User: burn book
Bot: Did you say Burn Book? Don't worry, your secrets are totally safe with me... or are they?
```

## Project Structure

```
regina-george-bot/
├── main.py              # Bot initialization and event handlers
├── responses.py         # Regina George response logic
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (create this)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Configuration

The bot uses environment variables for sensitive configuration:

- `TOKEN`: Your Discord bot token

Make sure to never commit your `.env` file to version control.

## How It Works

1. **main.py**: Handles Discord client setup, event listening, and message routing
2. **responses.py**: Contains the Regina George personality logic with conditional responses based on user input
3. The bot listens for messages in any channel it has access to
4. Messages starting with `?` are responded to privately
5. All other messages receive public channel responses

## Contributing

Want to add more Regina George quotes or improve the bot? Feel free to:

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

## Notes

- The bot ignores its own messages to prevent infinite loops
- All responses are inspired by Mean Girls (2004)
- Sass levels are set to maximum

## License

This project is for educational and entertainment purposes.

---

*"I'm not a regular bot, I'm a cool bot."* - Regina George Bot, probably
