from sqlalchemy import create_engine
# connection
engine = create_engine('postgresql+psycopg2://admin:container@postgres:5432/monthly_report') # going to be a seperate python file