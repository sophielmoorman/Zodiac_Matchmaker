
def main(birthday):
    # Goal: Take in a birthday and describe the zodiac sign of that person

    # "MM/DD/YYYY"
    month = birthday[0] + birthday[1]
    month = int(month)
    # print("month: ", month, type(month))

    day= birthday[3]+birthday[4]
    day = int(day)
    # print("day: ", day, type(day))

    year = int(birthday[6:10])
    # print("year: ", year, type(year))

    current_date = [month, day]
    
    month_dict = {
       1 : 31,
       2 : 29,
       3 : 31, #there are 30 days in march
       4 : 30,
       5 : 31,
       6 : 30,
       7 : 31,
       8 : 30,
       9 : 31,
       10 : 30,
       11 : 31,
       12 : 30}
  

    dates = {
        "Aries":          ["03/21", "04/20"],   # [21 March, 20 April]
        "Taurus":	      ["04/20", "05/21"],   # [20 April, 21 May]
        "Gemini":         ["05/21", "06/21"],   # [21 May, 21 June]
        "Cancer":         ["06/21", "07/23"],   # [21 June, 23 July]
        "Leo":	          ["07/23", "08/23"],   # [23 July, 23 August]
        "Virgo":          ["08/23", "09/23"],   # [23 August, 23 September]
        "Libra":          ["09/23", "10/23"],   # [23 September, 23 October]
        "Scorpio":        ["10/23", "11/22"],   # [23 October, 22 November]
        "Sagittarius":	  ["11/23", "12/22"],   # [23 November, 22 December]
        "Capricorn":      ["12/22", "01/20"],   # [22 December, 20 January]
        "Aquarius":       ["01/20", "02/19"],   # [20 January, 19 February]
        "Pisces":         ["02/19", "03/21"]}    # [19 February, 21 March]

    for sign in dates: # starting at i = 0, sign = dates[i]

        # get page contents (date range for sign)
        range_of_dates = dates[sign]

        # get sign start and end dates
        range_start = range_of_dates[0]
        range_end = range_of_dates[1]

        # get start day and month, cast to int
        start_month = range_start[0:2]
        start_month = int(start_month)
        start_day = range_start[3:5]
        start_day = int(start_day)

        max_days_in_month = month_dict[start_month]
        # print(max_days_in_month)

        # get end day and month, cast to int
        end_month = range_end[0:2]
        end_month = int(end_month)
        end_day = range_end[3:5]
        end_day = int(end_day)

        # make range list 
        sign_range = []

        # while loop to build range list
        date = [start_month, start_day]
        stop_date = [end_month, end_day]

        sign_range.append(date)

        # for every day in date range, add date to sign_range
        while date != stop_date : 
            my_month = date[0]
            my_day = date[1]

            new_day = my_day
            new_month = my_month

            # last day of the month
            if my_day == max_days_in_month:

                # last month of the year
                if my_month == 12:
                    new_month = 1
                else:
                    new_month = my_month + 1
                
                new_day = 1
            else:
                new_day = my_day + 1

            # please no infinite while loop
            date = [new_month, new_day]

            # build sign range array 
            sign_range.append(date)
            
        # check if date is in range list 
        if current_date in sign_range:
            return sign
    
        
        
if __name__ == "__main__":
    birthday = "11/14/2002"
    sign = main(birthday)

    print("With a birthday of ", birthday, " you have the sign", sign, ".")

    # Steps
        # 1 process date
        # 1 output result
        # 2 input date
        # 3 input 2 dates

    # https://en.wikipedia.org/wiki/Zodiac

    # signs and their date range
  