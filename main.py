
import pandas as pd
movies = pd.read_csv("IMDb movies.csv") #calls on IMDb movies file where the information is stored

def findDecades (decade): #creates a function that may be called upon if the user would like to add more than one decade
  while decade.lower() != "done":
      decades.append(decade[:3]) #takes first three characters of the user's input to determine decade
      decade = input("Are there any other decades you are interested in? Enter done if not: ").lower()
  return decades

def findGenres (genre): #creates a function that may be called upon if the user would like to add more than one genre
  while genre.lower() != "done":
          genres.append(genre.lower())
          genre = input("Are there any other genres you would like to add? Enter done if not: ").lower()
  return genres
  
def findLength(lengthMin, lengthMax): #creates a function that searches the length of each movie and may be called upon if the user wants to filter in the maximum/minimum length of a movie
    lengthRange.append(int(lengthMin))
    lengthRange.append(int(lengthMax))
    return lengthRange

def findLanguage(language): #creates a function that may be called upon if the user would like to add more than one language 
  while language.lower() != "done":
          languages.append(language.lower())
          language = input("Are there any other languages you would like to add? Enter done if not: ").lower()
  return languages

def movieRec(avgMin, genres, decades, lengthRange, languages): #puts all user input into a list and filters through dataset for matches
   goodMovies = []
   for index, i in movies.iterrows(): #goes to each row of the dataset
        i["language"] = str(i["language"]).lower().split(",") #separates each set of genres into individual strings
   for index, i in movies.iterrows():
        if (i["avg_vote"] >= avgMin) and (i["genre"].lower() in genres) and (str(i["year"])[0:3] in decades) and (i["duration"] >= lengthRange[0] and (i["duration"] <= lengthRange[1])) and (i["language"]) in languages:
            goodMovies.append(i["title"]) #this adds the movie title to the list
   for i in goodMovies:
       print(i)
   return goodMovies


print("Welcome to your personalized movie-reccomendation app!") #this begins the main code
status = input("If you would like to get a movie reccomendation please type 'begin'. Otherwise please enter 'exit': ")
answers = []
while status.lower() != "exit":
    ratingQuestion = input("Do you have a rating that your movie needs to reach? Enter 'yes' or 'no': ").lower()
    if ratingQuestion != "no":
      answers.append("yes")
      avgMin = float(input("What is the minimum rating of your movie? Please enter a number between 0 and 10: "))
    else:
        answers.append("no")

    decadesQuestion = input("Do you have any particular decade(s) to watch a movie from? Enter 'yes' or 'no': ").lower()
    if decadesQuestion != "no":
      answers.append("yes")
      decades = []
      decade = (input("What decade would you like the movie to be from? Please enter a year between 1900 and 2019: "))[:3]
      findDecades(decade)
      recOrNo = input("Would you like to be recommended a genre from this decade? Enter 'yes' or 'no': ").lower() #gives the user option between reccomending a genre versus choosing their own
      if recOrNo != "no":
        genresXDecade = {"biography": 0, "drama":0, "adventure":0, "history":0, "crime":0, "western":0,"fantasy":0, "comedy":0, "horror":0, "family":0, "action":0, "romance":0, "mystery":0, "animation":0, "sci-fi":0, "musical":0, "thriller":0, "music":0, "film-noir":0, "war":0, "sport":0, "adult":0, "documentary":0, "reality-tv":0} #creates a dictionary and counts how often each genre occurs in the dataset
        for index, each_row in movies.iterrows():
            if str(each_row["year"])[0:3] in decades:
                each_row["genre"] = each_row['genre'].split(", ") #separates each set of genres into individual strings
                for i in each_row["genre"]:
                    i = i.lower().strip()
                    genresXDecade[i] += 1
        num1 = 0
        num1Key = [] 
        for key, value in genresXDecade.items(): #this looks at which value is the highest in the dictionary based on the decade inputted and recommend a genre or genres back to the user
            if value > num1:
                num1 = value
                num1Key.append(key)
        print(f"This is the most common movie genre(s) from your decade of choice: {num1Key[-1]}")
            
    else:
        answers.append("no")
    
    genresQuestion = input("Do you have any genres in mind? Enter 'yes' or 'no': ").lower()
    if genresQuestion != "no":
        answers.append("yes")
        genres = []
        genre = input("Please type in a genre from this list: biography, drama, adventure, history, crime, western,fantasy, \ncomedy, horror, family, action, romance, mystery, animation, sci-fi, \nmusical, Thriller, music, film-noir, war, sport, adult, documentary: ")
        findGenres(genre)
    else:
        answers.append("no")

    lengthQuestion = input("Do you have a particular length of movie in mind? Enter 'yes' or 'no': ").lower()
    if lengthQuestion != "no":
      answers.append("yes")
      lengthRange = []
      lengthMin = int(input("What is the minimum length that your movie should be: "))
      lengthMax= int(input("What is the maximum length that your movie should be: "))
      findLength(lengthMin, lengthMax)
    else:
        answers.append("no")

    languageQuestion = input("Do you have a particular language you would like your movie to be in? Enter 'yes' or 'no': ").lower()
    if languageQuestion != "no":
      answers.append("yes")
      languages = []
      language = input("Please type in a language from this list: English, Italian, German, Danish, French, Hungarian, Russian, \nSpanish, Swedish, Japanese, None, Sign Languages, Czech, Yiddish, Hindi, Portuguese, Ukrainian, Turkish, Dutch, Marathi, Finnish, Norwegian,\n Polish, Swiss German, Latin, Romanian, Mandarin, Slovenian, Sicilian, Greek, Arabic, Serbo-Croatian, Tamil, Bengali, Georgian, Albanian, Azerbaijani, Burmese, Croatian, \nBulgarian, Korean, Urdu, Cantonese, Hebrew, Serbian, Malayalam, Sinhalese, Esperanto, Slovak, Kirghiz, Tagalog, Aymara, Armenian, Persian, Estonian, Aboriginal, Tupi, Wolof, Scots, Filipino, Kannada, Macedonian, Bambara, Indonesia, Kurdish, Vietnamese, Irish, Telugu, Gujarati,\n Basque, Icelandic, Scanian, More, Sanskrit, Hakka, Frisian, Min Nan, Belarusian, Dyula, Saami, Zulu,\n Romany, Afrikaans, Bosnian, Cree, Mongolian, Latvian, Flemish, Welsh, Kazakh, Catalan, Haitian, Tajik, Khmer, Akan, Chinese, Hokkien, Thai, Lithuanian, Punjabi, Tibetan, Faroese, Nahuatl, Nenets, Tzotzil, American Sign Language, Maya, Malay, Inuktitut, Maltese, Kabuverdianu,\n Xhosa, Nepali, Pushto, Chechen, Aramaic, Yoruba, Dari, Dzongkha, Spanish Sign Language, Sardinian, Rotuman, Berber languages, 'Purepecha, Russian Sign \nLanguage, Luxembourgish, Lao, Guarani, Tarahumara, Low German, North American Indian, Neapolitan, Kinyarwanda, Kru, Tigrigna, Amharic, Brazilian Sign Language, Maori, Greenlandic, Swahili, Southern Sotho, Shanghainese, Ukrainian Sign Language, Quechua, Samoan, Gallegan, Kashmiri, Pular, Aromanian, Tswana, Somali, Egyptian (Ancient), Assamese, Himachali, Rhaetian, Lingala, Wayuu, Yakut, Haida, Tatar: ")
      findLanguage(language)
    else:
        answers.append("no")


    if answers[0] == "no": #this text block will look at the answers list and if the user inputted "no" for a certain filter it will automatically set it's value to a default value that is declared below
        avgMin = 0
    if answers[2] == "no":
        decades = ["190", "191", "192", "193", "194", "195", "196", "197", "198", "199", "200", "201"]
    if answers[1] == "no":
        genres = ["biography", "drama", "adventure", "history", "crime", "western","fantasy", "comedy", "horror", "family", "action", "romance", "mystery", "animation", "sci-fi", "musical", "thriller", "music", "film-noir", "war", "sport", "adult", "documentary", "reality-tv"]
    if answers[3] == "no":
        lengthRange = [0, 3360]
    if answers[4] == "no":
        languages = ['English', 'Italian', 'German', 'Danish', 'French', 'Hungarian', 'Russian', 'Spanish', 'Swedish', 'Japanese', 'None', 'Sign Languages', 'Czech', 'Yiddish', 'Hindi', 'Portuguese', 'Ukrainian', 'Turkish', 'Dutch', 'Marathi', 'Finnish', 'Norwegian', 'Polish', 'Swiss German', 'Latin', 'Romanian', 'Mandarin', 'Slovenian', 'Sicilian', 'Greek', 'Arabic', 'Serbo-Croatian', 'Tamil', 'Bengali', 'Georgian', 'Albanian', 'Azerbaijani', 'Burmese', 'Croatian', 'Bulgarian', 'Korean', 'Urdu', 'Cantonese', 'Hebrew', 'Serbian', 'Malayalam', 'Sinhalese', 'Esperanto', 'Slovak', 'Kirghiz', 'Tagalog', 'Aymara', 'Armenian', 'Persian', 'Estonian', 'Aboriginal', 'Tupi', 'Wolof', 'Scots', 'Filipino', 'Kannada', 'Macedonian', 'Bambara', 'Indonesian', 'Kurdish', 'Vietnamese', 'Irish', 'Telugu', 'Gujarati', 'Basque', 'Icelandic', 'Scanian', 'More', 'Sanskrit', 'Hakka', 'Frisian', 'Min Nan', 'Belarusian', 'Dyula', 'Saami', 'Zulu', 'Romany', 'Afrikaans', 'Bosnian', 'Cree', 'Mongolian', 'Latvian', 'Flemish', 'Welsh', 'Kazakh', 'Catalan', 'Haitian', 'Tajik', 'Khmer', 'Akan', 'Chinese', 'Hokkien', 'Thai', 'Lithuanian', 'Punjabi', 'Tibetan', 'Faroese', 'Nahuatl', 'Nenets', 'Tzotzil', 'American Sign Language', 'Maya', 'Malay', 'Inuktitut', 'Maltese', 'Kabuverdianu', 'Xhosa', 'Nepali', 'Pushto', 'Chechen', 'Aramaic', 'Yoruba', 'Dari', 'Dzongkha', 'Spanish Sign Language', 'Sardinian', 'Rotuman', 'Berber languages', 'Purepecha', 'Russian Sign Language', 'Luxembourgish', 'Lao', 'Guarani', 'Tarahumara', 'Low German', 'North American Indian', 'Neapolitan', 'Kinyarwanda', 'Kru', 'Tigrigna', 'Amharic', 'Brazilian Sign Language', 'Maori', 'Greenlandic', 'Swahili', 'Southern Sotho', 'Shanghainese', 'Ukrainian Sign Language', 'Quechua', 'Samoan', 'Gallegan', 'Kashmiri', 'Pular', 'Aromanian', 'Tswana', 'Somali', 'Egyptian (Ancient)', 'Assamese', 'Himachali', 'Rhaetian', 'Lingala', 'Wayuu', 'Yakut', 'Haida', 'Tatar']


    movieRec(avgMin, genres, decades, lengthRange, languages) #runs the main method
    status = input("This is a list of some movies we recommend for you! Please type 'exit' if you are satisfied with your results. Otherwise type 'again': ")# gives users a chance to try again if they are not satisfied with their results

  



