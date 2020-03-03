import pandas as pd

excelFile = 'movies.xlsx'
movies = pd.read_excel(excelFile, index_col = 0)
#movies = pd.read_excel(excelFile)

#print (movies.columns)
rows, columns =  movies.shape
print (rows)
print (columns)

# print the columns
#print (movies.head())

# To print just few columns
#print (movies[['Title', 'Year']])
#print (movies['Director'])

#To use a where clause
print (movies[['Title', 'Year']][movies.Country == 'Germany'])

#If i do not index it, then RECORD ID becomes a column by itself. 
#print (movies[['Title', 'Year']][movies.RECORDID == 5])

#If i index it.. then the below row cannot be used.. The below statement will
# give me the record id with 17
print ('***********')
print (movies.loc[17])

#Gives me the statistics of the dataframe
print (movies.describe())

