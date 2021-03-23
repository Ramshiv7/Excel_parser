import os, pandas, zipfile, os   
print(os.getcwd())

path = 'C:\\Users\\SM5047417\\Desktop\\Engineering Test\\Engineering Test Files\\'
zp_name = "Engineering Test.zip"

with zipfile.ZipFile(zp_name, "r") as zip:
    print("Extraction Starts")
    zip.extractall()
    print('Done!') 
 

os.chdir(path)

for _ in os.listdir(path):
    if _.startswith("Asia") and _.endswith('.csv'):
        df = pandas.read_csv(_)
        team1 = df.drop_duplicates(subset=['Source IP'])
        filename = "Asia"
        dt = pandas.DataFrame(team1, columns= ['Source IP'])
        dt['filename']= filename
        dt.to_csv('combined.csv', index=False, header=False, mode='a')
        print(dt)
    elif _.startswith("NA") and _.endswith('.csv'):
        df = pandas.read_csv(_)
        team1 = df.drop_duplicates(subset=['Source IP'])
        filename = "NA Prod"
        dt = pandas.DataFrame(team1, columns= ['Source IP'])
        dt['filename']= filename
        dt.to_csv('combined.csv', index=False, header=False, mode='a')
        print(dt)
    else:
        pass
