import requests

class IRCTC:
    def __init__(self, ):

        user_input = input("""How would you like to proceed?
                              1. Enter 1 to check live train status
                              2. Enter 2 to check PNR
                              3. Enter 3 to check train schedule""")
        if user_input == '1':
            print('live train status')
        elif user_input == '2':
            print('PNR')
        elif:
            self.TrainSchedule()
    
    def TrainSchedule(self):
        TrianNo = input('Enter the Train No:')
        self.FetchData(TrianNo)

    def FetchData(self, TrianNo):
        data=requests.get("<<<<<<<<<<<<<<<<<api>>>>>>>>>>>>>{}".format(TrianNo))
        data = data.json()
        #print(data['Route'])
        for i in data['Route']:
            print(i['StationName'])


obj = IRCTC()
