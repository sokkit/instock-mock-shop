# InStock Mock Shop

Welcome to the InStock Mock Shop repository! Our platform simulates online marketplaces such as Etsy and Shopify, allowing users to experience the functionalities of these platforms in a sandbox environment.

The platform is built using the Flask framework, a lightweight and popular web application framework in Python. The code is hosted on PythonAnywhere, a cloud-based platform for web hosting, where it is easily accessible and can be deployed with minimal setup.

The repository is divided into two folders, each containing scripts that simulate the servers of two mock shops. By running these scripts, users can interact with the simulated shops so we can emulate various online sales platform for development and testing.

## Getting Started

If you haven't already, ensure that you have version 3.10.4 of Python installed. To install Python on your system, you can follow the instructions provided on the [official Python website](https://www.python.org/downloads/).

To get started with the InStock Mock Shop, please clone this repository:
```
git clone https://git.cardiff.ac.uk/cm6331-2022-23-1/instock-mock-shop.git
```

Go to the directory where you want to run the shop server, then run the following commands:

Start the virtual environment:
```
pipenv shell
```

Install required packages: 
```
pipenv install 
```

Once you have installed the required packages, you can start the server by running the following command: 
```
flask run
```

The server should now be running on your local machine. You can access the InStock Mock Shop platform at http://localhost:5000.
