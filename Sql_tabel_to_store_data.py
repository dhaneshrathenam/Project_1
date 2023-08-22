import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="",#host_name
    user="",#user_name
    password="",#user_password
    database=""#database name
)
mycursor = mydb.cursor(buffered=True)

def table_exists(table_name):
    # Check if the table exists
    mycursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return mycursor.fetchone() is not None

def create_table(table_name, create_query):
    # Create a table if it doesn't exist
    if not table_exists(table_name):
        mycursor.execute(create_query)
        print(f"Table '{table_name}' created.")

# Create channel_details table
channel_details_query = (
    "CREATE TABLE channels ("
    "channel_id VARCHAR(255), "
    "channel_name VARCHAR(255), "
    "Playlist_id VARCHAR(255), "
    "subscription_count INT, "
    "views INT, "
    "Total_videos INT, "
    "channel_description TEXT, "
    "country TEXT);"
)
create_table("channels", channel_details_query)

# Create video_details table
video_details_query = (
    "CREATE TABLE videos ("
    "channel_name VARCHAR(255), "
    "channel_id VARCHAR(255), "
    "video_id VARCHAR(255), "
    "title VARCHAR(255), "
    "thumbnail VARCHAR(255), "
    "video_description TEXT, "
    "published_date VARCHAR(255), "
    "Duration VARCHAR(255), "
    "views INT, "
    "likes INT, "
    "comments INT, "
    "favorite_count INT, "
    "Definition VARCHAR(255), "
    "Caption_status VARCHAR(255));"
)
create_table("videos", video_details_query)

# Create comments_details table
comments_details_query = (
    "CREATE TABLE comments ("
    "comment_Id VARCHAR(255), "
    "video_Id VARCHAR(255), "
    "comment_text TEXT, "
    "comment_author VARCHAR(255), "
    "comment_posted_date VARCHAR(255), "
    "like_count INT, "
    "Reply_count INT);"
)
create_table("comments", comments_details_query)

# Close the database connection
mydb.close()
