# INVENTORY MANAGEMENT SYSTEM  
## Description
This is a python based application designed to manage inventory efficiently.  
It provides a RESTful API and a command-line(CLI) that allows users to add, view, and delete inventory items.  
It also integrateswith the OpenFoodFacts API to retrieve additional product information using barcodes or product names.  
## Features
- Add new inventory items.
- View all inventory items.
- Retrieve details of a specific product.
- Update product prices and stock levels.
- Delete inventory items.
- Search for products using barcodes or product names.
- Retrieve product information from the OpenFoodFacts API.
- Interact with the system through a CLI.
## API Endpoints
|HTTP Method | Endpoint           | Description |
|------------|--------------------|--------------|
|GET         | `/`               |Home page  
|  GET       | `/inventory`      |  Retrieve all inventory items |  
|GET         | `/inventory/<id>`  | Retrieve a specific inventory item|  
|POST        | `/inventory`       |Add a new inventory item |  
|PATCH       |`/inventory/<id>`   |Update an inventory item |  
|DELETE      |`/inventory/<id>`   | Delete an inventory item |  
|GET          |`/products/search`  | Search for products using OpenFoodFacts  
## Installation and setup
### 1.  Clone the repository
`git clone <repository-url>`  
### 2. Navigate to project directory
`cd inventory-management`  
### 3.Create a virtual environment
`python3 -m venv venv`  
### 4.Activate the virtual environment
`source venv/bin/activate`  
### 5.Install dependencies
`pip freeze > requirements.txt`  
### 6. Running the Application
#### Start the Flask API
`python3 app.py`  
#### Run the CLI
`python3 cli.py`
## Future improvements
1. Develop a graphical user interface.  
2. Implement user authentication and authorization.  
## Author
Jimmy Mumo



