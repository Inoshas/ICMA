# Inventory and cost management system
A small business inventory and account management application is what this project wants to create. Entrepreneurs who work for themselves frequently struggle to find the money for costs like inventory control, tax preparation, and bookkeeping. We want to create a transparent, user-friendly reporting and management system. We primarily maintain two databases (DB) in this project, each with unique tables. The names of those DBs are: 
#### Products Database 
  This contains two tables.
* Products: Lists each product's specifications and available stock levels.
* Unit price: This includes information on marginal costs. Based on the overall expenses, the marginal price is computed in the computation. User can then choose the selling price.
#### Expenses DB
This contains four tables.
* Phone bills : Company phone bill charges on monthly basis
* Capital cost: Include all the cost that company spend on buying necessary items
* Transport bills: Include local tranport cost
* Imported item cost : Include all the imported item cost information including shipping and custome duty charges


## This project has the following folders: 
* Modules: There are two main Python modules in the modules subdirectory. The primary functions of the create_table module is to  create new tables and columns for the exisiting database. Users can understand the structure of the existing tables by openning expenses_db.py and products_db.py files. Meantime, it is possible to insert new tables and columns using create_table.py and insert_column.py.  Users don't need to edit any of these unless they want to customize the tables, in which case we recommend using these files.
* db: This includes the two primary databases. If you want to see what's within, we recommend using DBeaver or another helpful viewer.
* files: The user can manually upload data or utilize a CSV file to add new data to the database. The csv file must be placed in this folder, and any user-generated reports will be saved here as well.
* templates: This folder includes all the html templates.

* ### How to use:
    * Doownload all the files.
    * Open the folder with visual studio. 
    * In the terminal, type pipenv install to install pip enviornemt
    * Type pipenv shell to enter to pipnv. Then you dont need to install other libraries. 
    * Run app.py. This is the main file.
    * Copy http link shown in the terminal. 
    * Press ctrl+shift+p and select the simple browser view.
    * Paste the link and press Enter.
    * Now you can follow the browser view and proceed accordingly.
    * You can visualize the stored data in the DBs using DBeaver or any other DB viewer software.
    * In order to upload data using csv file, make sure to copy paste your csv file in to the files folder.   
    * If you need to add more tables: Go to modules, open create_table and then open add_table.py. Define the table name and required columns as instructed and excute to proceed.
    * If you need to add more columns to table (which is not recomended to for exciting tables) you can open the modules --> create_table --> add_columns.py. Then enter data as instructed  and excute. Please follow this procedure, only if you wish to customize insert_data.py accordingly. 
    
 
