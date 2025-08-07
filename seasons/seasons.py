import sys
from datetime import datetime, timedelta, date
import inflect
p = inflect.engine()

def main():
    print(season(input("Date of Birth: ")))

def season(s):
    if s.count('-') != 2:
        sys.exit('Invalid Date')
    else:
        try:
            dob = date.fromisoformat(s)
        except ValueError:
            sys.exit('Invalid Date')
        now = date.today()
        time = now - dob
        return p.number_to_words(int(time.total_seconds() // 60), andword="").capitalize() + ' minutes'

if __name__ == "__main__":
    main()
