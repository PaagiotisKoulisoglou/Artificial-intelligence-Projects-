📧 AI Email Assistant
Are you drowning in emails? This AI Email Assistant is designed to be your personal inbox lifeguard! It's a smart, command-line tool that connects to your IMAP email account, helps you quickly see what's unread, and can even summarize email content using a powerful local language model. Say goodbye to email overload!

✨ Key Features
Quick Unread Scan: Get an instant, organized list of all your unread emails, complete with sender, subject, and date. No more guessing what's new.

Intelligent Summarization: Need the gist of an email without opening it? Just provide the email's unique ID (UID), and the AI will give you a concise summary of its main points.

Interactive Interface: Control the assistant right from your terminal with simple, intuitive commands.

🧠 How It Works Under the Hood
This assistant combines a few robust technologies to bring you a seamless email management experience:

imap-tools: This Python library handles the secure connection to your IMAP email server, allowing the assistant to fetch email headers and content.

langchain & langgraph: These frameworks are the brain behind the operation. They enable the creation of a sophisticated conversational agent that can understand your requests ("list unread emails," "summarize this email") and intelligently decide which internal "tool" to use to fulfill your command.

Ollama: This incredible tool allows you to run large language models (LLMs) directly on your local machine. This project is pre-configured to use the qwen3:8b model for summarization, ensuring your email data stays private and never leaves your system for processing. You can easily switch to other models supported by Ollama if you prefer!

🚀 Getting Started
Ready to take control of your inbox? Follow these steps to set up your AI Email Assistant.

Prerequisites
Before you begin, please ensure you have the following installed:

Python 3.8+: You can download it from python.org.

Ollama: Download and install Ollama from their official website: https://ollama.com/.

A Local Language Model: After installing Ollama, you'll need to pull the qwen3:8b model (or any other compatible model you wish to use) by running this command in your terminal:

ollama pull qwen3:8b

An Email Account with IMAP Access: You'll need your IMAP host address, your email username, and your password (or, even better, an app-specific password if your email provider offers one for enhanced security).

Installation Steps
Clone the Repository (or download main.py):
If you're using Git, clone this repository to your local machine:

git clone https://github.com/your-username/AI-Email-Assistant.git # Replace with your actual repo URL
cd AI-Email-Assistant

If you're just downloading main.py, make sure it's in its own project folder.

Create a Python Virtual Environment (Highly Recommended):
This keeps your project dependencies isolated and tidy.

python -m venv venv

Activate the virtual environment:

On macOS/Linux:

source venv/bin/activate

On Windows:

venv\Scripts\activate

Install Project Dependencies:
First, create a requirements.txt file in your project's root directory with the following content:

python-dotenv
imap-tools
langchain
langgraph

Then, install them using pip:

pip install -r requirements.txt

Configuration
You need to tell the assistant how to connect to your email. Create a file named .env in the root directory of your project (the same folder as main.py) and add your email credentials like this:

IMAP_HOST=your.imap.host.com
IMAP_USER=your_email@example.com
IMAP_PASSWORDT=your_email_app_password_or_regular_password

IMAP_HOST: This is the address of your email provider's IMAP server (e.g., imap.gmail.com, outlook.office365.com).

IMAP_USER: Your full email address (e.g., john.doe@example.com).

IMAP_PASSWORDT: Your email account password. For better security, if your email provider offers "app passwords" or "application-specific passwords," please generate and use one of those instead of your main account password.

Running the Assistant
Once all the setup is complete, you can launch the AI Email Assistant from your terminal:

python main.py

You'll see a prompt like this:

Type an instruction or "quit".

>

Now you can start interacting with your assistant! Try commands such as:

list unread emails

summarize email with UID 123 (replace 123 with an actual UID you get from the "list unread emails" command)

quit (to exit the application)

🤝 Contributing
We welcome contributions of all kinds! If you have ideas for new features, improvements, or if you find a bug, please feel free to:

Fork the repository.

Create a new branch for your feature or fix (git checkout -b feature/your-awesome-feature).

Make your changes and test them thoroughly.

Commit your changes with a clear, concise message (git commit -m 'feat: Add a new awesome feature').

Push your branch to your forked repository (git push origin feature/your-awesome-feature).

Open a Pull Request to the main branch of this repository.

📄 License
This project is open-sourced under the MIT License. See the LICENSE file in the repository for more details.
