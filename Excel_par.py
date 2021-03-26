import os, pandas, zipfile, sys

def csv_parser(path):

    #Changing the working directory
    os.chdir(path)

    #Traversing through the CSV Files
    for file_name in os.listdir(path):
        if file_name.endswith('.csv') and file_name != "Combined" or file_name != "Combined_temp":
            full_name = os.path.join(path,file_name)
            df = pandas.read_csv(file_name)
            de_dupe_ip = df.drop_duplicates(subset=['Source IP'])
            envname = os.path.splitext(file_name)[0].strip('0123456789')
            dt = pandas.DataFrame(de_dupe_ip, columns= ['Source IP'])
            dt['Environment']= envname
            dt.to_csv(f'{path}\Combined_temp.csv', index=False, header=False, mode='a')

        else:
            pass

    #Sorting the Combined CSV file
    final = pandas.read_csv(f'{path}\Combined_temp.csv')
    final.columns = ['Source IP', 'ENV']
    final_data = final.sort_values(by=['Source IP'], ascending=True)
    final_data.to_csv(f'{path}\Combined.csv', index=False)


if __name__ == '__main__':
    path = sys.argv[1]
    csv_parser(path)
