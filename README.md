# Setting up the Django Project

Before starting the app, follow these steps:

1. **Activate the Virtual Environment**  
   Open the folder containing your virtual environment (`myenv`) and activate it:

   - For **Windows**:
     ```bash
     myenv\Scripts\activate
     ```

2. **Install Required Dependencies**  
   After activating the virtual environment, install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ````

3. **Navigate to the Django Project Directory**  
   Go to the project directory:

   ```bash
   cd nombre_mystere
   ````

4. **Apply Database Migrations**  
   Run the following command to apply any pending migrations to the database:

   ```bash
   python manage.py migrate
   ````

 5. **Start the Development Server**  
 Finally, run the Django development server:

 ```bash
 python manage.py runserver
 ````

After these steps, your Django project should be running at http://127.0.0.1:8000/!
