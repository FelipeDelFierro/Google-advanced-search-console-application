Languages={"Arabic":"ar",
"Bulgarian":"bg",
"Catalan":"ca",
"Croatian":"hr",
"Chinese (Simplified)":"zh-Hans",
"Chinese (Traditional)":"zh-Hant",
"Czech":"cs",
"Danish":"da",
"Dutch":"nl",
"English":"en",
"Filipino":"fil",
"Finnish":"fi",
"French":"fr",
"German":"de",
"Greek":"el",
"Hebrew":"he",
"Hindi":"hi",
"Hungarian":"hu",
"Indonesian":"id",
"Italian":"it",
"Japanese":"ja",
"Korean":"ko",
"Latvian":"lv",
"Lithuanian":"lt",
"Norwegian":"no",
"Polish":"pl",
"Portuguese":"pt",
"Romanian":"ro",
"Russian":"ru",
"Serbian":"sr",
"Slovak":"sk",
"Slovenian":"sl",
"Spanish":"es",
"Swedish":"sv",
"Thai":"th",
"Turkish":"tr",
"Ukrainian":"uk",
"Vietnamese":"vi"}

def GetLanguage(Languages):
    """This function return the user Language parameter according to the Google parameters of Languages"""
    userLanguage = ''
    try:
        userLanguage = input("Write your Language in english : ").capitalize()

        while  userLanguage not in Languages:
             userLanguage = input("Please write a valid Language, you can see the Languages excel file : ").capitalize()
        else:
          for a, b in  Languages.items():
            if userLanguage in Languages:
                  Languages[userLanguage]
    except Exception as e:
        print("Language is not in the database or is bad writing, Please see the excel file named countries and find your country", e)
    return Languages[userLanguage]
