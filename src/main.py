from initWindow import InitWindow
from Factory import Factory

app = Factory.create(InitWindow)
app.run()