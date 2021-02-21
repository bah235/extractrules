# importing required externam package modules
import camelot
import pikepdf
import pandas as pd
from os import listdir
from os.path import isfile, join
import re

# Imports from this package
from points import extract_multiplier, strip_mult, process_points
from formatting import (Add_Item_Nums, Clean_Dataframe, Get_Category_Points, 
                        Get_Category_Name, Verify_Table_Format, 
                        Verify_Table_Shape, Clean_Headers, Rename_Columns,
                        Add_Category_Cols)
from log import pdf_log


def decrypt_pdf(filename):
    openpath = 'rules/encrypted/'
    savepath = 'rules/decrypted/'

    with pikepdf.open(openpath + filename) as pdf:
        num_pages = len(pdf.pages)
        pdf.save(savepath + filename)


# Get all the rules files
mypath = 'rules/encrypted'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

pattern_file = r"event(\d\d\d)"


df_all = pd.DataFrame(columns=['description', 'min_pt_desc', 'avg_pt_desc', 'max_pt_desc', 'min_pts', 'max_pts', 'category', 'category_name', 'event'])

event = []
cat_nums = []
cat_names = []
cat_points = []

# onlyfiles = ['event130.pdf',]

for file in onlyfiles:
    match = re.search(pattern_file, file)
    if match:
        event_num = match.group(1)
        
    PDF_Name = file
    decrypt_pdf(PDF_Name)

    name_table = camelot.read_pdf('rules/decrypted/' + PDF_Name, pages = '1-end')

    dfs = []
    count = 0


    # This block looks for tables with a 'continued' at the top, assumes a page split,
    # and appends to the  previous table.
    for idx, table in enumerate(name_table):
        pattern = r" continued$"
        match_header = re.search(pattern, table.df[0][0])
        
        if match_header:
            print('Continued Found')
            df = table.df.drop([0])
            dfs[count-1] = pd.concat([dfs[count-1], df]) 
            dfs[count-1]  = dfs[count-1].reset_index(drop=True)
        else:
            dfs.append(table.df)
            count +- 1


    
    # Process the tables
    for idx, table in enumerate(dfs):

        label = str(idx) + ' in ' + PDF_Name

        df = Clean_Dataframe(table, label)
        if Verify_Table_Shape(df, label):
            df = Verify_Table_Format(df, label)
            df = process_points(df)
            df = strip_mult(df)
            # print('after strip processs', df)

            category_pts = Get_Category_Points(df, label)
            category_name = Get_Category_Name(df, label)

            df = Clean_Headers(df, label)
            df = Rename_Columns(df, label)

            df = Add_Category_Cols(df, category_name, idx, event_num, label)

            df = Add_Item_Nums(df, label)

            print(f"A total of {category_pts} points in {category_name} (Table {idx})")

            event.append(event_num)
            cat_nums.append(idx)
            cat_names.append(category_name)
            cat_points.append(category_pts)

            df_all = pd.concat([df_all,df])
        print('\n\n')

df_cat = pd.DataFrame({"event" : event, "cat_order" : cat_nums, "cat_names" : cat_names, "cat_total_pts" : cat_points, "round" : 0})

df_all = df_all.reset_index()
df_all = df_all.rename(columns = {'index':'item_order'})

print(df_cat)
print(df_all)

df_all.to_csv('allscores.csv')
df_cat.to_csv('allcats.csv')