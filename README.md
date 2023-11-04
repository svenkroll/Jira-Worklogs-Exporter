# Jira Worklogs Exporter

This project provides a Python script to export worklogs from Jira tickets to an Excel file. The tool was developed as a response to Jira's limitation where it doesn't allow the evaluation of individual worklogs without an additional plugin. This solution is catered to those who don't wish to rely on a paid plugin like Tempo.

At the end of the process, an Excel file will be generated with the following columns:

- **Ticket**: The Jira ticket key.
- **Author**: The display name of the user who logged the work.
- **Date**: The date when the work was logged.
- **Time Spent**: The amount of time logged, represented in hours.

## Prerequisites

### macOS Setup

Before setting up the virtual environment, ensure you have Python installed on your macOS. If you haven't, you can install it using [Homebrew](https://brew.sh/):

\```bash
brew install python3
\```

This will install Python 3 and the `pip` package manager.

## Setting Up the Virtual Environment

To isolate the project dependencies, we'll use a virtual environment. Here's how to set it up:

1. Navigate to the project directory.
2. Create a virtual environment named `.venv`:

\```bash
python3 -m venv .venv
\```

3. Activate the virtual environment:

\```bash
source .venv/bin/activate
\```

You'll know it's activated once your terminal prompt changes to show the `.venv` name.

## Installing Dependencies

Once inside the virtual environment, install the required packages with:

\```bash
pip install -r requirements.txt
\```

## Configuration

Before running the script, you'll need to set up your configuration:

1. Copy the `.env.dist` file:

\```bash
cp .env.dist .env
\```

2. Edit the `.env` file with your Jira details:

- `JIRA_SERVER`: Your Jira server URL.
- `JIRA_USER`: Your Jira username or email.
- `JIRA_TOKEN`: Your Jira API token.
- `PROJECT_KEY`: Your Jira project key.
- `MONTH`: The desired month in the format `YYYY-MM`.

## Running the Script

To execute the program:

\```bash
python main.py
\```

After the script completes, you'll find a `worklogsYYYY-MM.xlsx` file in the directory with the exported worklogs.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/R6R8QT94J)
