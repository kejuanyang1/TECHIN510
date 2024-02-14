# TECHIN 510 LAB 5
Data Visualization for events in Seattle

## What's Included
- `scraper.py`: The web scraper script, and save data to postgres database.
- `api.py`: contains apis for web scraper.
- `app.py`: The frontend page.
- `db.py`: contains database manipulation functions
- `requirements.txt`: A text file listing the Python dependencies for the project, which can be installed using `pip`.

## Learned Lessons
- I learned how to use DBeaver to create, connect and inspect postgres database.
- I learned and practiced how to save scraped data into postgres database.
- I learned how to create charts for visualization in streamlit.

## Questions
- The location returned in seattle events sometimes only contains "South", "North" or "West", so I added a `get_location` function to process them by adding "Seattle" in the end. In this way, the geolocation can be correct.