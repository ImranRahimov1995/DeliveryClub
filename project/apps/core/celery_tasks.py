from config.celery import app


@app.task
def test(x, y):
    return x + y
