from dotenv import load_dotenv
load_dotenv()
import os
import mindsdb_sdk

server = mindsdb_sdk.connect(login=os.getenv("MINDSDB_LOGIN"), password=os.getenv('MINDSDB_PASS'))
project = server.get_project()


def text_to_image(prompt):
    pred = project.query(
        f'''SELECT * 
        FROM mindsdb.dalle 
        WHERE text = "{prompt}"'''
    )
    url = pred.fetch().img_url
    return url[0]
