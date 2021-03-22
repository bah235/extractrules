# Importing required external package modules
import camelot
import pikepdf
import pandas as pd
from os import listdir
from os.path import isfile, join
import re
import logging


# Imports from this package
from points import extract_multiplier, strip_mult, process_points
from formatting import (Add_Item_Nums, Clean_Dataframe, Get_Category_Points, 
                        Get_Category_Name, Verify_Table_Format, 
                        Verify_Table_Shape, Clean_Headers, Rename_Columns,
                        Add_Category_Cols)
from log import pdf_log


logging.basicConfig(filename='TSAscores.log', level=logging.INFO,
                             format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

logging.info("Starting PDF scrub")

def decrypt_pdf(filename):
    """ Function to open a PDF, decrypt, and resave """
    openpath = 'rules/encrypted/'
    savepath = 'rules/decrypted/'

    with pikepdf.open(openpath + filename) as pdf:
        num_pages = len(pdf.pages)
        pdf.save(savepath + filename)



# Get all the rules files
mypath = 'rules/encrypted'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

pdf_log(onlyfiles)


df_all = pd.DataFrame(columns=['description', 'min_pt_desc', 'avg_pt_desc', 
                                'max_pt_desc', 'min_pts', 'max_pts', 
                                'category', 'category_name', 'event'])

# Initalize empty lists for collecting categories
event = []
cat_nums = []
cat_names = []
cat_points = []

# If you wanted to run on only a single or small number of files, you can 
# uncomment the line below and use a list. Caution, this needs a list. So 
# for only one item, You need a trailing comma to it stays as a list rather
# than decomposing to a single variable.

# onlyfiles = ['event207.pdf',]

pattern_file = r"event(\d\d\d)"


# Main loop that runs over every file in the list.
for file in onlyfiles:
    
    # Extract the event number by regex match on filename
    match = re.search(pattern_file, file)
    if match:
        event_num = match.group(1)
        
    PDF_Name = file
    
    decrypt_pdf(PDF_Name)
    pdf_log(f"Decrypted {PDF_Name}")

    # Extract table data from the PDF
    name_table = camelot.read_pdf('rules/decrypted/' + PDF_Name, pages = '1-end')

    pdf_log(f"In {PDF_Name} we have found {len(name_table)} tables")

    # Init some variable that will be used for all tables in PDF.
    dfs = []
    count = 0


    # This block looks for tables with a 'continued' at the top, assumes a 
    # page split has occurred, and appends to the preceeding table. We can't
    # Just use the built interator index because that breaks when there is
    # more than one continued table in the file.

    for idx, table in enumerate(name_table):
        pattern = r" continued$"
        match_header = re.search(pattern, table.df[0][0])
        
        if match_header:
            pdf_log(f"Continued Found block found in table {idx}. Appending to previous.")
            df = table.df.drop([0])
            dfs[count-1] = pd.concat([dfs[count-1], df]) 
            dfs[count-1]  = dfs[count-1].reset_index(drop=True)
        else:
            dfs.append(table.df)
            count +- 1

    pdf_log(f"After cleaning continued tables, we have {len(dfs)} tables")
    
    # After cleaning up the continued tables, process all normally.
    for idx, table in enumerate(dfs):

        label = str(idx) + ' in ' + PDF_Name

        df = Clean_Dataframe(table, label)

        # This function checks for a table of expected size.
        # Skip if the table is the wrong shape and do nothing.
        if Verify_Table_Shape(df, label):

            df = Verify_Table_Format(df, label)
            df = process_points(df)
            df = strip_mult(df)

            category_pts = Get_Category_Points(df, label)
            category_name = Get_Category_Name(df, label)

            df = Clean_Headers(df, label)
            df = Rename_Columns(df, label)
            df = Add_Category_Cols(df, category_name, idx, event_num, label)
            df = Add_Item_Nums(df, label)

            pdf_log(f"A total of {category_pts} points in {category_name} (Table {idx})")

            # Transfer the information about the tables category to a 
            # list of categories.
            event.append(event_num)
            cat_nums.append(idx)
            cat_names.append(category_name)
            cat_points.append(category_pts)

            # Append the contents of this table to the list of all score items
            df_all = pd.concat([df_all,df])

            pdf_log(f"Done with {label}, adding to Dataframe.")
        # Extra newlines in terminal log for readability.
        print('\n\n')
    
    pdf_log(f"All table reads done with {PDF_Name} *****")

# After all file(s) processed, convert category info to dataframe and export to csv.
df_cat = pd.DataFrame({"event" : event, "cat_order" : cat_nums, "cat_names" : cat_names, "cat_total_pts" : cat_points, "round" : 0})
print(df_cat)
df_cat.to_csv('allcats.csv')

# Convert the table subindexs to a tp be the display order and generate
# a new sequential index for the whole table. Save to CSV.
df_all = df_all.reset_index()
df_all = df_all.rename(columns = {'index':'item_order'})
print(df_all)
df_all.to_csv('allscores.csv')
