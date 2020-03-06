import pandas as pd
import re

class movieObj:
    def __init__(self, l_moviename, l_year, l_generes, l_Director, l_GrossEarnings):
        self.movie = l_moviename
        self.year = l_year
        self.generes = l_generes
        self.Director = l_Director
        self.GrossEarnings = l_GrossEarnings
    
    def printmovies(self):
        print ('The movie name is ',  self.movie, ' it was done in the year ',  self.year, 
        ' It is directed in Genere ', self.generes,  ' and it grossed $', self.GrossEarnings )

excelFile = 'movies.xlsx'
movies = pd.read_excel(excelFile, index_col = 0)
#print (movies.info())
#To use a where clause
#for (index_label, row_series) in empDfObj.iterrows():
movieList = []
for (rows, columns) in (movies[movies.LinkedRecord.notnull()].iterrows()):
    print (rows)
    #print (movies.loc[rows]['LinkedRecord'])
    value = str(movies.loc[rows]['LinkedRecord'])
 #   print (value)
    if (value.find('-')) != -1 :
        indexValue = re.split('-', movies.loc[rows]['LinkedRecord'])
        for i in indexValue:
            #print (type(int(i)))     
            title =  movies.loc[int(i)]['Title']
            year = movies.loc[int(i)]['Year']
            generes = movies.loc[int(i)]['Genres']
            director = movies.loc[int(i)]['Director']
            GrossEarnings = movies.loc[int(i)]['Gross Earnings']
            movieList.append(movieObj(title, year, generes, director,GrossEarnings))
        print('******************************************************************')
        print()
        print()
        print()
    else:
        print (movies.loc[rows]['LinkedRecord'])
    print('-}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}')


for i in movieList:
    print (i)
    i.printmovies()
