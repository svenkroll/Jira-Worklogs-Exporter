import calendar
import pandas as pd
import datetime
import os

from dateutil.relativedelta import relativedelta
from jira import JIRA
from dotenv import load_dotenv


def get_worklogs_from_jira(_JIRA_SERVER, _JIRA_USER, _JIRA_TOKEN, _PROJECT_KEY, _MONTH):
    # connect to Jira
    jira = JIRA(server=_JIRA_SERVER, basic_auth=(_JIRA_USER, _JIRA_TOKEN))

    #calculate the last day of the month used in the JQL
    year, month = map(int, _MONTH.split('-'))
    _, last_day = calendar.monthrange(year, month)

    tickets = jira.search_issues(f'project = {_PROJECT_KEY} AND worklogDate >= "{_MONTH}-01" AND worklogDate <= "{_MONTH}-{last_day}"', maxResults=1000)

    data = []
    start_date = datetime.datetime.strptime(_MONTH, '%Y-%m').date()
    end_date = start_date + relativedelta(months=1) - datetime.timedelta(days=1)

    for ticket in tickets:
        worklogs = ticket.fields.worklog.worklogs
        for worklog in worklogs:
            worklog_date = datetime.datetime.strptime(worklog.started.split('T')[0], '%Y-%m-%d').date()

            if start_date <= worklog_date <= end_date:
                entry = {
                    'Ticket': ticket.key,
                    'Author': worklog.author.displayName,
                    'Date': worklog.started.split('T')[0],
                    'Time Spent': worklog.timeSpentSeconds / 3600
                }
                data.append(entry)

    _df = pd.DataFrame(data)
    return _df


def save_worklogs_as_excel(dataframe, _MONTH):
    filename = f'worklogs{_MONTH}.xlsx'
    dataframe.to_excel(filename, index=False)


if __name__ == '__main__':
    load_dotenv()

    JIRA_SERVER = os.getenv('JIRA_SERVER')
    JIRA_USER = os.getenv('JIRA_USER')
    JIRA_TOKEN = os.getenv('JIRA_TOKEN')
    PROJECT_KEY = os.getenv('PROJECT_KEY')
    MONTH = os.getenv('MONTH')

    df = get_worklogs_from_jira(JIRA_SERVER, JIRA_USER, JIRA_TOKEN, PROJECT_KEY, MONTH)
    save_worklogs_as_excel(df, MONTH)
