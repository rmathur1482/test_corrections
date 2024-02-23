def count_unique_proteins(list_proteins):
    return len(set([i[:7] for i in list_proteins]))

def count_proteins(list_protein):
    protein_freq = {}
    protein_families = [i[:7] for i in list_protein]
    for i in protein_families:
        if i in protein_freq:
            protein_freq[i] += 1
        else:
            protein_freq[i] = 1
    return protein_freq

def merge_protein_counts(dict1, dict2):
    combined_dict={}
    for i in dict1:
        if i in dict1 and i in dict2:
            combined_dict[i] = (dict1[i], dict2[i])
        elif i in dict1 or i in dict2:
            if i in dict1:
                combined_dict[i] = (dict1[i], 0)
            elif i in dict2:
                combined_dict[i] = (0, dict2[i])
    return combined_dict

def dates_to_iso8601 (date_list):
    ISO_dates = []
    for i in date_list:
        m_d_y = i.split()
        month = m_d_y[0]
        day = m_d_y[1].replace(',', '').zfill(2)
        year = m_d_y[2]
        month_to_date = {'January':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07', 'August':'08', 'September':'09', 'October':'10', 'November':'11', 'December': '12'}
        month_date = month_to_date[month]
        date = year + '-' + month_date + '-' + day
        ISO_dates.append(date)
    return ISO_dates

def sort_dates(date_list):
    tuple = []
    date_list_1 = convert_to_ISO(date_list)
    for i in range(len(date_list_1)):
        tuple.append((date_list_1[i], date_list[i]))
    #sortes = sorted(date_list_1)
    tuple.sort(key=lambda x: x[0])
    sorte_d = [i[1] for i in tuple]
    return sorte_d
