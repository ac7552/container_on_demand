
import tornado.web
import terminado
import docker
import json

class ContainersHandler(tornado.web.RequestHandler):
    def initialize(self,client):
        self.client=client

    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        # container_name = self.get_argument('container_name')
        # containers = self.client.containers(quiet=False, all=False, trunc=False, latest=False, since=None, before=None, limit=-1, size=False, filters={'name': container_name})
        container_arr = []
        # if len(containers) == 0:
        containers = self.client.containers(quiet=False, all=False, trunc=False, latest=False, since=None, before=None, limit=-1, size=False)
        for i in range(len(containers)):
            container_id = containers[i]['Id']
            container_image = containers[i]['Image']
            container_ports = containers[i]['Ports']
            container_state = containers[i]['State']
            container_names = containers[i]['Names']
            data = {'names': container_names,'container_id': container_id, 'container_image': container_image, 'container_ports':  container_ports, 'container_state': container_state}
            container_arr.append(data)
        results = json.dumps(container_arr)
        self.write(results)
        # else:
        #     container_id = containers[0]['Id']
        #     container_image = containers[0]['Image']
        #     container_ports = containers[0]['Ports']
        #     container_state = containers[0]['State']
        #     container_names = containers[0]['Names']
        #     data = {'names': container_names,'container_id': container_id, 'container_image': container_image, 'container_ports':  container_ports, 'container_state': container_state}
        #     container_arr.append(data)
        #     results = json.dumps(container_arr)
        #     self.write(results)

    def post(self):
        container_name = self.get_argument('container_name')
        container_image = self.get_argument('container_image')
        container = self.client.create_container(container_image, command="/bin/sleep 1d", name=container_name)
        self.client.start(container=container.get('Id'))
        self.write('success')
