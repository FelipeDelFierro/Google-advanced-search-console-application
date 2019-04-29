def GetDate():
    """"This function return a date to search according to the google search parameters"""
    dates = {'1': 'y','2': 'm','3': 'w','4': 'd'}
    print (10 * "-" , "I Will find articles in a Range of time. These are the options to search: ")
    print ("1. Yearly")
    print ("2. Monthly")
    print ("3. Weekly")
    print ("4. Daily")
    print (67 * "-")
    try:
        input_date = input("Enter your choice [1-4] : ").capitalize()
        while  input_date not in dates:
            input_date = input("Wrong option selection,please try again.\n Enter your choice [1-4] :  ").capitalize()
        else:
            if input_date in dates:
                if input_date=='1':     
                    print ("Yearly, I will find results from now until a year ago") 
                elif input_date=='2':
                    print ("Monthly, I will find results from now until a Month ago")
                elif input_date=='3':
                    print ("Weekly, I will find results from now until a Week ago")
                elif input_date=='4':
                    print ("Daily, I will find results from now until a Day ago")  
                dates[input_date]             
    except KeyError as e:
        print("the date value" + str(e) + "is not in the database")
    return dates[input_date]    