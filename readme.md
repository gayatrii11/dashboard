
## Flask - Plotly Dashboard App

 
### Get Started
- First Git Clone or Download this repository.
- Install the necessary dependencies using pip
- run the following command

	```
	pip install -r requirements.txt
	```
- Configure MySQL credentials
    - open [app.py](app.py) and edit

        ```
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'your mysql username'
        app.config['MYSQL_PASSWORD'] = 'your mysql password'
        app.config['MYSQL_DB'] = 'your database name'
        ```
- Run the app
	- in development mode (auto reload)
		
		```python
		set FLASK_ENV=development
		flask run
		```
		
