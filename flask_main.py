from flask import Flask
app = Flask(__name__)
from sortedListNoDubl import SortedListNoDubl

@app.route('/')
def hello():
    ar1 = SortedListNoDubl([1, 6, 2, 3])
    return "Hello World! {}".format(ar1)

if __name__ == '__main__':
    f = open("text.txt", "w")
    f.write("content")
    f.close()
    app.run()
#comment
