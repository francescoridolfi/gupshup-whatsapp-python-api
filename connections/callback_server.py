from http.server import BaseHTTPRequestHandler, HTTPServer
from pprint import pprint
import sys
sys.path.append("..")
from objects import input, message
from utils import functions as func
import settings


def main_server(bot, scripts):
    class Server(BaseHTTPRequestHandler):

        objects = [input.MESSAGE, input.CONTEXT, input.SENDER, input.BOT_NAME, input.CHANNEL]

        def do_HEAD(self, content="application/json"):
            self.send_response(200)
            self.send_header('Content-type', content)
            self.end_headers()

        def do_GET(self):
            return self.respond(self.path, self.get_params(self.path, "GET"))

        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            return self.respond(self.path, self.get_params(data, "POST"))

        def get_params(self, path, method):
            path = path[:-1] if path.endswith("&") else path
            if method == "GET":
                return {} if "?" not in path or len(path.split("?")[1]) == 0 else dict(
                    (item.split("=")[0], func.html_decoder(item.split("=")[1]))
                    for item in path.split("?")[1].split("&"))
            elif method == "POST":
                return dict((item.split("=")[0], func.html_decoder(item.split("=")[1]))
                            for item in path.decode().split("&"))
            return {}

        def handle_http(self, path, params):

            if params == {}:
                return bytes("", 'UTF-8')

            pprint(params)

            if input.CHANNEL in params:
                print("CHANNEL: "+params[input.CHANNEL])
                if params[input.CHANNEL] is 'whatsapp':
                    print("non è whatsapp")
                    return bytes("", 'UTF-8')

            for key in self.objects:
                if key in params:
                    params[key] = func.json_decoder(params[key])
                    if key == input.MESSAGE and message.MSG_IMG_TYPE in params[key] and \
                            message.MSG_IMG_IMG in params[key]:
                        if params[key][message.MSG_IMG_TYPE] is "image":
                            params[key][message.MSG_IMG_IMG] = func.json_decoder(params[key][message.MSG_IMG_IMG])

            if settings.SERVER["LOGS"]["ENABLE"]:
                with open(settings.SERVER["LOGS"]["PATH"], "a+") as log:
                    log.write("\n"+str(params))

            inbound = input.INPUT(params)

            payload = None
            for script in scripts:
                info = script.get_script_info()
                print(info["events"])
                if "MessageReceived" in info["events"]:
                    res = info["events"]["MessageReceived"](bot, inbound)
                    payload = "" if payload is None else payload
                    if res is not None:
                        payload += res

            return bytes(payload, 'UTF-8')

        def respond(self, path, params):
            self.do_HEAD()
            response = self.handle_http(path, params)
            self.wfile.write(response)
    return Server


def run_server(chat, bot, scripts):
    HOST = settings.SERVER["HOST"]
    PORT = settings.SERVER["PORT"]

    server_class = main_server(bot, scripts)
    httpd = HTTPServer((HOST, PORT), server_class)
    chat.log('Server Starts - %s:%s' % (HOST, PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    chat.log('Server Stops - %s:%s' % (HOST, PORT))
