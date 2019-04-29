def remove_char(s):
    return s[1 : -1]
def url_builder(country,language,date):
    """This function build the query and return a Google Url using .format...
    Also it receive a country,language,date. from the respectives files.py """
    #Inputs
    withand = input("I will find all these words, please write me words separated by spaces(AND) :  ").replace(" ","+")
    withquotes = input("You can specify with exact words or phrases, exact words in double quotes : ").replace(" ","+")
    withquotes= remove_char(withquotes)
    withor = input("I will find any of these words: Type OR between all the words you want(OR)  : ").replace(" ","+")
    badwords =  input("Write badwords separated by spaces : ").replace(" ","+")
    url = 'https://www.google.com/search?hl=en&as_q={}&as_epq={}&as_oq={}&num=100&as_eq={}&lr=lang_{}&cr={}&as_qdr={}&as_sitesearch={}&as_occt=any&safe=images&as_filetype=&as_rights='.format(withand,withquotes,withor,badwords,language,country,date)      
    return url
def url_builder_SpecificSite(country,language,date):
    """This function build the query and return a Google Url using .format...
    Also it receive a country,language,date. from the respectives files.py """
    #Inputs
    withand = input("I will find all these words, please write me words separated by spaces(AND) :  ").replace(" ","+")
    withquotes = input("You can specify with exact words or phrases, exact words in double quotes : ").replace(" ","+")
    withquotes= remove_char(withquotes)
    withor = input("I will find any of these words: Type OR between all the words you want(OR)  : ").replace(" ","+")
    badwords =  input("Write badwords separated by spaces : ").replace(" ","+")
    site=input("Write a specific website search")
    url = 'https://www.google.com/search?hl=en&as_q={}&as_epq={}&as_oq={}&num=100&as_eq={}&lr=lang_{}&cr={}&as_qdr={}&as_sitesearch={}&as_occt=any&safe=images&as_filetype=&as_rights='.format(withand,withquotes,withor,badwords,language,country,date,site)      
    return url

