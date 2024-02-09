import os, psycopg2, logging, sys
from dotenv import load_dotenv

## Establishing connection on postgres database and creating postgres database
def get_connection():
    load_dotenv()
    try:
        connection = psycopg2.connect(   
            database = os.getenv("POSTGRES_DATABASE_NAME"),                                              
            user = os.getenv("POSTGRES_USER"),                                      
            password = os.getenv("POSTGRES_PASSWORD"),                                  
            host = os.getenv("POSTGRES_HOST"),                                            
            port = os.getenv("POSTGRES_PORT")                                          
        ) 
        logging.info("Connection to the PostgreSQL established successfully.")
        cursor = connection.cursor()

    
        return (connection)
        
    except Exception as e :
        print ("error :",e)
        return (False)
 



def create_table():
    cursor = get_connection().cursor()

    cursor.execute('''SELECT EXISTS (SELECT * FROM information_schema.tables WHERE table_name='url_details')''')
    exists = cursor.fetchone()[0] 

    #Creating table url_details
    if exists == False:  
        postgres ='''CREATE TABLE url_details(
                        input_url CHAR(1000) NOT NULL,
                        short_url CHAR(50)
                    )'''
        cursor.execute(postgres)
        logging.info("Table creating successfully")
        connection.commit()
        #Closing the connection
        connection.close()



def insert_url(connection, long_url, random_url):
    
    cursor = connection.cursor()
    # Preparing SQL queries to INSERT a record into the database.
    cursor.execute('''INSERT INTO url_details(input_url, short_url) VALUES(%s, %s)''',(long_url, random_url))
    

def fetch_url(connection, random_url):
    cursor = connection.cursor()
    #Fetching urls from the database using SELECT query
    query =(" SELECT input_url FROM url_details WHERE short_url= '{}' ".format(random_url))
    cursor.execute(query)
    answers = cursor.fetchall()[0]
    for ans in answers:
        site = ans
   
    return(site)

   