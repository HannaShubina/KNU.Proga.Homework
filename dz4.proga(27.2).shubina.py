import cgi
from string import Template


def common_w(first_string, second_string):
     # Розділення рядків на слова та знаходження їх перетину
    first_words = set(first_string.split())
    second_words = set(second_string.split())
    common_words = list(first_words.intersection(second_words))
    return common_words


def application(environ, start_response):
    # Якщо шлях URL-запиту є пустим
    if environ.get("PATH_INFO", "").lstrip("/") == "":
        form = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ)
        first_string = form.getlist("first_string", "")
        second_string = form.getlist("second_string", "")
        answer = common_w(first_string, second_string)
        result = "<h1>{} - {}</h1>".format(answer)
        # Створюємо успішну відповідь
        start_response("200 OK", [("Content-type", "text/html; charset=utf-8"), ])
        with open("templates/palindrome.html", encoding="utf-8") as f:
            page = Template(f.read()).substitute(result=result)
    else:
        # У випадку помилки, відправляємо відповідь-повідомлення з описом помилки
        start_response("404 NOT FOUND", [("Content-type", "text/html; charset=utf-8"), ])
        with open("templates/error_404.html", encoding="utf-8") as f:
            page = f.read()

    return [bytes(page, encoding="utf-8")]


HOST = ""
PORT = 8000

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print(f"сервер запущено на http://localhost:{PORT}")
    print(" === Local webserver === ")
    make_server(HOST, PORT, application).serve_forever()