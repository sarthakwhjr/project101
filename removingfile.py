
import dropbox
class Transferdata:
        def __init__(self,accesstoken):
                     self.accesstoken=accesstoken
        def uploadfiles(self,file_from,file_to):
                 dbx = dropbox.Dropbox(self.accesstoken)
                 with open(file_from, 'rb') as f:
                  dbx.files_upload(f.read(), file_to)
                 

def main():
        accesstoken="kM06Xp1WUY0AAAAAAAAAAfGwqJv3BYdwgz6OWAvPsueuj5yC2VUcvnreJzuZwUQZ"
        transferdata=Transferdata(accesstoken)     
        filefrom=input("give the file path")
        fileto=input("enter the full path to upload the dropbox")
        transferdata.uploadfiles(filefrom,fileto)
        print("file upload")
main() 