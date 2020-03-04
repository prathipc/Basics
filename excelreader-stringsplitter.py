import pandas as pd
import re

excelFile = 'movies.xlsx'
movies = pd.read_excel(excelFile, index_col = 0)
#print (movies.info())

#To use a where clause
#for (index_label, row_series) in empDfObj.iterrows():
for (rows, columns) in (movies[movies.LinkedRecord.notnull()].iterrows()):
    print (rows)
    #print (movies.loc[rows]['LinkedRecord'])
    value = str(movies.loc[rows]['LinkedRecord'])
    print (value)
    if (value.find('-')) != -1 :
        indexValue = re.split('-', movies.loc[rows]['LinkedRecord'])
        for i in indexValue:
            #print (type(int(i)))     
            print (movies.loc[int(i)])
            print('---------------------------')
        print ('******************************************************************')
        print()
        print()
        print()
    else:
        print (movies.loc[rows]['LinkedRecord'])
    print('---------------------------------------------------------------')

