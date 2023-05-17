# Inverntory and cost management application
This project aims to develop a inventory and account management application for small businesses. Self-employed business entrepreneurs frequently struggle to come up with the cash needed for expenses such as inventory management, tax preparation, and bookkeeping. We want to develop a clear reporting and managing system that is simple to use. In this project we mainly maintain two databases (DB) with distinct tables. Those DBs are names as;
#### Products DB 
  This contains two tables.
* Products: Contains product details and available quantities of each product.
* Unit price: This include the marginal cost details. In the calculation, marginal price is calculated based on the total expenses. Then user can deside the selling price.
#### Expenses DB
This contains four tables.
* Phone bills : Company phone bill charges on monthly basis
* Capital cost: Include all the cost that company spend on buying necessary items
* Transport bills: Include local tranport cost
* Imported item cost : Include all the imported item cost information including shipping and custome duty charges


* ### How to use:
    * Doownload all the files.
    * Open the folder with visual studio. 
    * In the terminal, type pipenv install to install pip enviornemt
    * Type pipenv shell to enter to pipnv. Then you dont need to install other libraries. 
    * Run app.py. This is the main file.
    * Copy http link shown in the terminal. 
    * Press ctrl+shift+p and select the simple browser view.
    * Now you can follow the browser view and proceed according to instructions.
    * Both DBs are stored in db folder and you can visualize the stored data in the DBs using DBeaver or any other DB viewer software.
    * In order to upload data using csv file, make sure to copy paste your csv file in to the files folder.   
    * If you need to add more tables: Go to modules, open create_table and then open add_table.py. Define the table name and required columns as instructed and excute to proceed.
    * If you need to add more columns to table (which is not recomended to for exciting tables) you can open the modules --> create_table --> add_columns.py. Then enter data as instructed  and excute. 


 
 ### Time frame and contributions: will be added.
 
