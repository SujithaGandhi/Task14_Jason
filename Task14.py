import requests
# Python class for REST API architecture
class Api:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)
   
    # method to fetch the current status of my REST API server
    def server_status(self):        
        return self.response.status_code
   
    # method to fetch data from the REST API server
    def fetch_data(self):
        try:
            if self.server_status() == 200:
                return self.response.json()
        except:
            print("ERROR : URL not found !")


# method to fetch all the names from the API server
    def fetch_name(self):
        try:
            result = []
            if self.server_status() == 200:
                for data in self.fetch_data():
                    result.append(data['region'])
                return result
        except:
            print("ERROR : URL not found !")

 # method to fetch the countries with currency


    def inr_countries(self, currenct_short_form):
        try:
            if self.server_status() == 200:
                result = []
                for data in self.fetch_data():
                    if 'currencies' in data and currenct_short_form in data['currencies']:
                        result.append(data['name']['common'])
                return result
        except requests.RequestException as error:
            print("ERROR : Currency does not exist !", error)

 
url_1 = 'https://restcountries.com/v3.1/all'

rest_api_server = Api(url_1)
for data in rest_api_server.fetch_data():
    print("*********Fetch all data from the jason*******************")
    print("---------------------------------")
    print()
    print(data)

for name in rest_api_server.fetch_name():
    print("*********Fetch all names from the jason*******************")
    print("---------------------------------")
    print()
    print(name)

    print("*********Fetch all Country, curriences from the jason*******************")
    print("---------------------------------")
    print()
    print(rest_api_server.inr_countries('INR'))




