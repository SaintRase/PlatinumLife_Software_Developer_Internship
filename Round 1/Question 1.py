from datetime import datetime

def is_date_format_correct(date:str)->bool:
    """
    This function takes in a date in string format
    and returns true if the date matches the format
    YYYY-MM-DD and false if it doesn't
    """
    try:
        # try parse the date using the format YYYY-MM-DD
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

print(is_date_format_correct('2022/01/01'))
print(is_date_format_correct('1999-01-01'))
print(is_date_format_correct('20221129'))
