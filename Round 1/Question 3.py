from datetime import datetime, timedelta

def compute_prev_date(dates_list:list):
    """
    """
    return [datetime.strptime(date, '%Y-%m-%d') - timedelta(days=1) for date in dates_list]
