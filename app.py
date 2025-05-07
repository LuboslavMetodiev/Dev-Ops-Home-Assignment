from flask import Flask
import redis
import os

app = Flask(__name__)

# Get Redis host and port from environment variables
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))

# Redis connection
redis_client = redis.StrictRedis(
    host=redis_host, port=redis_port, db=0, decode_responses=True
)


@app.route("/")
def hello_world():
    return "<p>Hello World</p>"


@app.route("/visited")
def visited():
    # Count the visit count in redis
    visits = redis_client.incr("visit_count")
    return f"<p>This page has been visited {visits} times.</p>"


@app.route("/health")
def health():
    # Checks connection to Redis
    try:
        redis_client.ping()
        return "<p>Redis is healthy</p>", 200
    except redis.ConnectionError:
        return "<p>Redis connection failed</p>", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)