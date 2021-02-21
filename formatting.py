from log import pdf_log
import re


def Clean_Dataframe(dataframe, name):
    """ This function cleans the tables of extra CR/LF/Newline/Whitespace"""

    try:
        # Get rid of any newlines or extra spaces in the cell contents
        df = dataframe.replace('\n', ' ', regex=True).replace('  ', ' ', regex=True)
        pdf_log(f"Table {name} Stripped extra whitespace successfully", 'OK')
        return df

    except:
        pdf_log(f"Table {name} FAILED newline/whitespace strip - NOT A TABLE.", 'FAIL')
        return None



def Verify_Table_Shape(df, name):
    """ This fuction checks to see if the table is the shape we expect. 
    If it's not, we won't be able to process it in the way we expect and 
    should defer to some sort of manual processing. """

    # Check to see if the table is right size. If not flag and exit
    if df.shape[1] != 4:
        pdf_log(f"Table {name} is not of the correct size", 'FAIL')
        return None
    
    else:
        pdf_log(f"Table {name} Read Success. Found {df.shape[0]} rows.", 'OK')
        return True



def Verify_Table_Format(df, name):
    """ This function checks for uniform points values and description 
    headings. Faulure does not block but flags the issue. """

    Fault_Flag = False

    # Log messages if the table has non-uniform headings
    if df[0][1] != 'CRITERIA':
        pdf_log(f"Table {name} Column Heading 0 Mismatch", 'WARN')
        Fault_Flag = True

        # A few tables have an extra line. Try deleting before failing out
        if df[0][2] == 'CRITERIA':
            pdf_log(f"Table {name} Deleted extra heading row. Check.", 'WARN')
            df = df.drop([1])
            df = df.reset_index(drop=True)

    if df[1][1] != 'Minimal performance':
        pdf_log(f"Table {name} Column Heading 1 Mismatch", 'WARN')
        Fault_Flag = True

    if df[2][1] != 'Adequate performance':
        pdf_log(f"Table {name} Column Heading 2 Mismatch", 'WARN')
        Fault_Flag = True
    
    if df[3][1] != 'Exemplary performance':
        pdf_log(f"Table {name} Column Heading 3 Mismatch", 'WARN')
        Fault_Flag = True

    # Log messages if the table has non-uniform point allocations
    if df[1][2] != '1-4 points':
        pdf_log(f"Table {name} Column 1 Points Mismatch", 'WARN')
        Fault_Flag = True

    if df[2][2] != '5-8 points':
        pdf_log(f"Table {name} Column 2 Points Mismatch", 'WARN')
        Fault_Flag = True
    
    if df[3][2] != '9-10 points':
        pdf_log(f"Table {name} Column 3 Points Mismatch", 'WARN')
        Fault_Flag = True
  
    # Log an all-clear message if no faults
    if Fault_Flag == False:
        pdf_log(f"Table {name} column heading and points ranges verified.", 'OK')

    return df




def Get_Category_Points(df, name):
    """ This function checks for uniform section headers 
    (e.g. DOCUMENT PORTFOLIO). Faulure does not block but 
    flags the issue. These are stripped and added to another
    column. """

    Fault_Flag = False

    if df[0][1] != 'CRITERIA':
        pdf_log(f"Table {name} Column Heading 0 Mismatch", 'WARN')
        Fault_Flag = True

    # Regex search patterns for top and bottom category headers
    # Current rules format has '(XX points)' at the end of header and
    # footwhere xx if the points total for category
    pattern = r"\s\((\d+) points\)$"
    
    match_header = re.search(pattern, df[0][0])
    match_footer = re.search(pattern, df[0][len(df)-1])

    if  match_header:
        header_pts = int(match_header.group(1))
    else:
        header_pts = 0
        Fault_Flag = True
        pdf_log(f"Table {name} failed to extract category header", 'WARN')

    if  match_footer:
        footer_pts = int(match_footer.group(1))
    else:
        footer_pts = 0
        Fault_Flag = True
        pdf_log(f"Table {name} failed to extract category footer", 'WARN')

    if (header_pts == footer_pts) and (Fault_Flag == False):
        pdf_log(f"Table {name} matching header and footer pts ({header_pts}) found.", 'OK')
        return header_pts

    else:
        return None        
    


def Get_Category_Name(df, name):
    """ This function extracts the name of the category
    (e.g. DOCUMENT PORTFOLIO) from the header row. """

    Fault_Flag = False

    # Regex search patterns for top and bottom category headers
    # Current rules format has '(XX points)' at the end of header and
    # footwhere xx if the points total for category
    pattern = r"\s\((\d+) points\)$"
    header_text = df[0][0]
    match_header = re.search(pattern, header_text)

    if  match_header:
        category = re.sub(pattern,'', header_text)
        return category

    else:
        Fault_Flag = True
        pdf_log(f"Table {name} failed to extract category header name", 'WARN')
        return 'Untitled Category'



def Clean_Headers(df, name):
    """ This function removes the category headers 
    (e.g. DOCUMENT PORTFOLIO) from the header row. 
    This function will break if the table is not formatted
    correctly. """

    last = len(df)-1

    df = df.drop([0, 1, 2])
    df = df.drop([last])

    return df



def Rename_Columns(df, name):
    """ This function renames auto-named columns"""

    df = df.rename(columns = {0:'description', 1:'min_pt_desc', 
                                2:'avg_pt_desc', 3:'max_pt_desc'})

    return df



def Add_Category_Cols(df, category_name, category_number, event_num, filename):
    """ Adds columns for the category labels and category numbers"""

    df['category'] = category_number
    df['category_name'] = category_name
    df['event'] = event_num

    return df



def Add_Item_Nums(df, name):
    """ Adds columns for the score item number (display order).
    Becasue the tables are processed one at  time, this relates to 
    the sequential index which needs to be reset after the header and
    footer rows are stripped. """
    
    df = df.reset_index(drop=True)

    return df