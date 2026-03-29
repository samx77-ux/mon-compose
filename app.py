import os
import psycopg2
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        conn = psycopg2.connect(
            host=os.environ["DB_HOST"],
            dbname=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"]
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        conn.close()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"je maitrise  Docker je suis un peu un DevOps  DB : {version}".encode())

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
