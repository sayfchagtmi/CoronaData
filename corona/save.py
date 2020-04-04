from corona import DataInfo
DEFAULT_FILE_NAME = "Coronavirus.csv"

def save_data(parsed_page, path=''):
    update_date = parsed_page.find("div",{"style":'font-size:13px; color:#999; text-align:center'}).text.replace('Last updated: ','')
    table = parsed_page.find("table",{"id":"main_table_countries_today"})
    rows = [row for row in table.findAll("tr")]
    headers = [th.text.replace('\n',' ').replace(',',';') for th in rows[0].findAll("th")]
    if len(path)!=0
        if path[-1]=='/':
            fpath = path+DEFAULT_FILE_NAME
        else:
            fpath = path+'/'+DEFAULT_FILE_NAME
    f = open(fpath, "w")
    f.write(','.join(headers) + '\n')
    rows = rows[1:]
    for row in rows:
        line = [info.text.replace('\n',' ').replace(',','.') for info in row.findAll("td")]
        if line[0]!= 'Total:	':
            f.write(','.join(line) + '\n')
    f.close()
    return DataInfo(fpath, update_date)
