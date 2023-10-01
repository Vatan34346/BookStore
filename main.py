from api import create_app
import uvicorn
from database import create_initial_db_with_tables


create_initial_db_with_tables()


app = create_app()
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

