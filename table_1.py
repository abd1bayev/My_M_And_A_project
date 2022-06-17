import pandas as pd


def table_1():
########################################################################################################################################################################

    table_1 = pd.read_csv("file:///home/docode/project/table.csv/only_wood_customer_us_1.csv")

########################################################################################################################################################################

    table_1 = table_1[["Gender","FirstName", "LastName", "Email", "Age", "City", "Country"]]

########################################################################################################################################################################

    gender = {'0':'Male', '1':'Female','M': 'Male','F': 'Female'}

########################################################################################################################################################################

    Gender = table_1['Gender'] = table_1['Gender'].replace(gender)

########################################################################################################################################################################

    table_1['Country'] = 'USA'

########################################################################################################################################################################

    table_1["Email"] = table_1["Email"].str.lower()

########################################################################################################################################################################

    table_1['FirstName'] = table_1['FirstName'].str.capitalize()

#################################################################################################################################################################################################################################

    table_1['LastName'] = table_1['LastName'].str.capitalize()

########################################################################################################################################################################

    table_1['City'] = table_1['City'].str.replace('_',' ')

########################################################################################################################################################################

    table_1['City'] = table_1['City'].str.replace('-',' ')

########################################################################################################################################################################

    table_1['FirstName'] = table_1['FirstName'].str.replace('\\','')

########################################################################################################################################################################

    table_1['LastName'] = table_1['LastName'].str.replace('\\','')

########################################################################################################################################################################

    table_1['FirstName'] = table_1['FirstName'].str.replace('"','') 

########################################################################################################################################################################

    table_1['LastName'] = table_1['LastName'].str.replace('"','')

########################################################################################################################################################################

    table_1['City'] = table_1['City'].str.title()



########################################################################################################################################################################
########################################################################################################################################################################

    # del table_1['UserName']

    # print(table_1)

    return table_1

########################################################################################################################################################################
########################################################################################################################################################################


table_1 = table_1()
