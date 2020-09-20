
def main(birthday):
    # Goal: Take in a birthday and describe the zodiac sign of that person

    birthday = "01/12/2000"
    # birthday = ['0', '1', '/', '1', '2', '/', '2', '0', '0', '0']

    # "MM/DD/YYYY"
    month = birthday[0] + birthday[1]
    month = int(month)
    # print("month: ", month, type(month))

    day= birthday[3]+birthday[4]
    day = int(day)
    # print("day: ", day, type(day))

    year = int(birthday[6:10])
    # print("year: ", year, type(year))

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

    for sign in dates:
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


        # get end day and month, cast to int
        end_month = range_end[0:2]
        end_month = int(end_month)
        end_day = range_end[3:5]
        end_day = int(end_day)

      #  print(start_day,end_day)

        
        
if __name__ == "__main__":
    birthday = "01/12/2000"
    main(birthday)
    a_list = [1,2,3]
    # print("a_list: ", a_list, type(a_list))




    # my_dict = dict()
    # my_dict = {
    #     'sophie' : ['cute', 'small']
    # }

    # page_finder = my_dict['sophie']
    # describer = page_finder[0]
    # print(describer)













    # Steps
        # 1 process date
        # 1 output result
        # 2 input date
        # 3 input 2 dates

    # https://en.wikipedia.org/wiki/Zodiac

    # signs and their date range
  