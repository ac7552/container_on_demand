
import tornado.web
import json

class ImagesHandler(tornado.web.RequestHandler):
    def initialize(self,client):
        self.client=client

    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        all_images = self.client.images(name=None, quiet=False, all=False, filters=None)
        image_arr = []
        for i in range(len(all_images)):
            image_name = all_images[i]['RepoTags'][0]
            data = {'image_name': image_name}
            image_arr.append(data)
        results = json.dumps(image_arr)
        self.write(results)

    def post(self):
        image_name = self.get_argument('image_name')
        self.client.pull(image_name, stream=False)
        self.write('success')
