import os, pandas, zipfile


def csv_parser(path):
    os.chdir(path)

    for file_name in os.listdir(path):
        if file_name.endswith('.csv') and file_name != "Combined":
            full_name = os.path.join(path,file_name)
            df = pandas.read_csv(file_name)
            de_dupe_ip = df.drop_duplicates(subset=['Source IP'])
            de_dupe_ip.sort_values(by=['Source IP'], kind='quicksort', ignore_index=False)
            envname = os.path.splitext(file_name)[0].strip('0123456789')
            dt = pandas.DataFrame(de_dupe_ip, columns= ['Source IP'])
            dt['Environment']= envname
            dt.to_csv(f'{path}Combined.csv', index=False, header=False, mode='a')
         
        else:
            pass


if __name__ == '__main__':
    path = 'C:\\Users\\SM5047417\\Desktop\\Engineering Test\\Engineering Test Files\\'
    csv_parser(path)

