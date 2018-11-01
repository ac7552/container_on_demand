
# Container on Demand 	

A python application that generates a terminal in the browser that links to a Docker container

## Getting Started

2. Clone the below repo:

        git clone https://github.com/ac7552/container_on_demand.git

3. In the cloned repo run the below commands:

        vagrant up 
        vagrant ssh
        cd /vagrant
        
 4. Login as root with: 
 
        ssh root@localhost

5. Next, run the application with the command below and go to http://0.0.0.0:3009/ in your browser.

        $ python app.py


## Languages used:
   CSS, Javascript, Python

## Technologies/Libraries used:
  Docker, Vagrant, Terminado, XTerm, Bootstrap
  

## Code Snippet:

  - The code below monkey patches the terminado Termsocket class, which enables xterm to link to a docker container
````Python
class WebSocketHandler(terminado.TermSocket):
    def initialize(self,term_manager):
        self.term_manager= terminado.SingleTermManager(shell_command=['sudo', 'docker' ,'exec' ,'-it',       self.request.uri.split('/')[-1], 'sh'])
        self.term_name = ""
        self.size = (None, None)
        self.terminal = None

        self._logger = logging.getLogger(__name__)
````


## Built With

* [XTerm](https://xtermjs.org/) - The javascript library used
* [Tornado](https://www.tornadoweb.org/en/stable/) - The Web Framework used
* [Docker](https://docs.docker.com/docker-for-mac/install/) - Containers for an easy setup



## Authors

* **Aaron Campbell**

## Languages used:
   CSS, Javascript, Python

## Technologies/Libraries used:
  Docker, Vagrant, Terminado, XTerm, Bootstrap, Tornado

