# Electric energy dashboard
Hello there! Welcome to the dashboard made by team 1!

*We are live: https://share.streamlit.io/itsmesafak/electric-energy-dashboard/main.py

---
## Setup and installations
First of all, lets clone the repo. You can do this by opening your command prompt (terminal) and executing the following command:
```sh
git clone https://github.com/ItsMeSafak/electric-energy-dashboard
```
This creates a copy of the project on you local machine! There may occur an error saying that 'git is unrecognized'. This means that you should install git first. 
- *Installing git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git*

Open a terminal and execute the following command:
```sh 
pip install -r requirements.txt
```
It may be saying things like 'Requirements already satisfied', but thats a good thing. Once you can enter another command in the terminal, that means the installation of the packages is complete. Also in case you add new packages, add them to the requirements.txt file and rerun the same script.

---
## Executing the code
To run the streamlit application locally, simply execute the following command:
```sh
streamlit run main.py
```
After compiling the code, it should tell you that you can view the app in your browser at the URL *http://localhost:8501* or something like that. If not, there may have gone something wrong with the installation of packages. Perhaps rerun the command above.

---
## Commit changes
Committing changes can be a bit of a pain in the a**. But to ease it out, I made a [commit](commit.sh) script that does all the work for you. Before we get into let, let's discuss the theory. 

While working on a project, we would like to seperate the development and main or master versions of the project. In this project, there are 2 branches: development and master. All our progress should be pushed on the development branch and all that is finished and done should be pushed on the master branch. The development branch is exactly the same as master, but a bit more messy.

**IMPORTANT!** When working on the project, please stay in the **development** branch. You can do this by simply executing the following command:
```sh
git checkout development
```

Now you are allowed to break everything (but don't). Now in order to push your changes live, we need to open up the terminal again (left-below **Terminal** tab) and this time press the **down arrow** and select command prompt. Now you can execute the following command:
```sh
commit.sh [your message]
```
Note that the [your message] part should be in quotes, so you get something like 
```sh
commit.sh "this is my message"
```

In case an error pops up, please contact me or check out the following link (if you dare):
- https://www.jetbrains.com/help/pycharm/resolving-conflicts.html#distributed-version-control-systems
- https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
 
 ---
 ## API/dataset usage
 ### Charge pole data
 Just like everyone, we receiveda csv file consisting of charging moments of a single charging pole. This data consists of the following columns:
 - **Started**: The starting datetime of charging.
 - **Ended**: The ending datetime of charging.
 - **TotalEnergy**: The total consumed energy in Watt per hour.
 - **ConnectedTime**: Total time connected to the pole in hours (1 = 1 hour).
 - **ChargeTime**: Total time actual charging to the pole in hours (1 = 1 hour).
 - **MaxPower**: Maximum requested energy in Watt

What we first did is analyze the data and check whether everything is correct. We noticed that a few rows had incorrect data input, where the ended date would be earlier than the started date. Also there were some columns that had a longer charge charge time than connected time. These rows were filtered out.

### RDW Data
https://opendata.rdw.nl/Voertuigen/Open-Data-RDW-Gekentekende_voertuigen_brandstof/8ys7-d773
https://opendata.rdw.nl/Voertuigen/Open-Data-RDW-Gekentekende_voertuigen/m9d7-ebf2


The RDW dataset is a set that consists of registrated cars in the Netherlands. The RDW has lots of different datasets regarding the cars in Holland, we picked the one that lists all the registrated cars with their date and another dataset that shows the fuel type of the car. We merged this into one dataframe and deleted more than half of the columns. We also checked on whether there were duplicate entries in the dataset and it turned out to be true. We analysed these records and we concluded that the records are exactly the same. The columnds we mainly focussed on were as follows:
-  **voertuigsoort**: The type of the vehicle.
- **merk**: Brand of the vehicle.
- **handelsbenaming**: Trading name of the vehicle.
- **datum_tenaamstelling**: Date of registration.
- **brandstof_omschrijving**: Fuel type.

### OCM Data
https://openchargemap.org/site/develop/api

Another dataset we made use of is the OCM API. This API reveals lots of data regarding charging points for vehicles all over the globe. In our case we mainly focussed on the Netherlands. In this dataset we focussed on the following columns:
- **isRecentlyVerified**: Whether the charging point got verified recently.
- **UsageType.Title**: The name of the charging type.
- **AddressInfo.Latitude, AddressInfo.Latitude**: The lat and lon coordiantes of the given charging point.
- **AdressInfo.StateOrProvince**: The state or province the charging point is located in.
- **Connections**: The possible connections of the charging point.
- **NumberOfPoints**: The amount of sockets available at the point.
- **StatusTypeID**: ID of the status, whether if its operational or not.

 ---
 ## Handy links
- [Streamlit cheat sheet](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py)
- [How to actually use git properly](https://www.freecodecamp.org/news/how-to-use-git-efficiently-54320a236369/)
- [Streamlit dashboard example(s)](https://streamlit.io/gallery)


*Now you are ready to go! Happy coding :smile:!*
