thedir = r'C:\Users\ASUS\Dropbox\PM'
result = {}

domain = os.environ['userdomain']
result['userdomain']=domain

for name in os.listdir(thedir):
    folder = os.path.join(thedir, name)
    if os.path.isdir(folder):
        result[folder] = os.access(folder, os.X_OK)

        
Desktop_output = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\output.csv')

with open(Desktop_output, 'w') as f:
    for key in result.keys():
        f.write("%s,%s\n"%(key,result[key]))