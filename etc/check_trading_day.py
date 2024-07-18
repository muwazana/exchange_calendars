import sys
import click
import pandas as pd
from datetime import datetime
from exchange_calendars import get_calendar

@click.command()
@click.option(
    "--date",
    default=datetime.today().strftime("%Y-%m-%d"),
    help="Date to check in YYYY-MM-DD format, default set to today",
    show_default=True,
)
@click.option(
    "--exchange",
    default="XSAU",
    help="Exchange to check, default set to XSAU",
    show_default=True,
)
def check_holiday(date, exchange):
    date = pd.Timestamp(date)
    cal = get_calendar(exchange)
    if cal.is_session(date):  # trading on
        click.echo(0)
        return 0
    else:  # trading off
        click.echo(1)
        return 1


if __name__ == "__main__":
    sys.exit(check_holiday())
