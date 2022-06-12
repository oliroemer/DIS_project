BEFORE YOU RUN MAIN FILE
    - Move "config.json" from the directory "DIS_project" to outside the directory. 

    EXAMPLE PATH: 
        - /Users/oliver/Desktop/Dis_project
        - /Users/oliver/Desktop/config.json

    - Insert path to "db_init.sql" in "commons.py", line 92.

    - Insert path to "config.json" in "commons.py", line 93.

    - Insert path to "cleaned_laptop_data.csv" in "config.json", line 7.
        If you get the following error: 
            "No such file or directory: '/Users/oliver/Desktop/Dis_project-main/Users/oliver/Desktop/Dis_project-main/data/Cleaned_Laptop_data.csv'",
        try only the last part of the path: "/data/Cleaned_Laptop_data.csv".

    - Insert password for your own postgresql login in "config.json", line 14.
    
RUN THE APP:
    - Open the directory "DIS_project" and run "main.py"
    In src directory: python3 main.py
    - Sometimes it won't run the first time but usually runs after a retry. 

This project is a prototype laptop recommender (the data is not up to date). 
Based on your requirements we use queries to parse a list of laptops that fits your needs.
As an addition to our app there is a separate page for a list of discount laptops.
From these lists you can get information regarding laptop specs, prices, and reviews/ratings.