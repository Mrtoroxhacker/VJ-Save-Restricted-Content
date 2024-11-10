import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20789690"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fb532f92355084d89668977d7ceb7b9e")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://kajaldhakad80:r7TQgw792ubhx0EN@cluster0.ubq2r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
