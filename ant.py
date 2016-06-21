import pygame

class Ant:
    def __init__(self):
        self.nodes = {}
        self.node_size = 10

        self.width = 1001
        self.height = 1001

        self.backg_color = (145,73,48)
        self.pixel_color = (207,148,110)
        self.ant_color = (0,0,0)

        self.ant_start_x = 501/self.node_size
        self.ant_start_y = 501/self.node_size
        self.ant_x = self.ant_start_x
        self.ant_y = self.ant_start_y
        self.ant_dir = "up"

        self.paused = True

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.screen.fill(self.backg_color)

        pygame.display.set_caption("Ant")

    def init(self):
        pygame.init()

        self.font = pygame.font.SysFont("monospace", 15)

        self.running = True

        while self.running:
            for event in pygame.event.get():
                self.event(event)

            self.update()
            self.render()

        self.cleanup()

    def update(self):
        killNode = None
        createNode = None

        if (self.ant_x, self.ant_y) in self.nodes:
            if self.ant_dir == "up":
                self.ant_dir = "left"
                killNode = (self.ant_x, self.ant_y)
                self.ant_x -= 1
            elif self.ant_dir == "down":
                self.ant_dir = "right"
                killNode = (self.ant_x, self.ant_y)
                self.ant_x += 1
            elif self.ant_dir == "left":
                self.ant_dir = "down"
                killNode = (self.ant_x, self.ant_y)
                self.ant_y += 1
            elif self.ant_dir == "right":
                self.ant_dir = "up"
                killNode = (self.ant_x, self.ant_y)
                self.ant_y -= 1
        else:
            if self.ant_dir == "up":
                self.ant_dir = "right"
                createNode = (self.ant_x, self.ant_y)
                self.ant_x += 1
            elif self.ant_dir == "down":
                self.ant_dir = "left"
                createNode = (self.ant_x, self.ant_y)
                self.ant_x -= 1
            elif self.ant_dir == "left":
                self.ant_dir = "up"
                createNode = (self.ant_x, self.ant_y)
                self.ant_y -= 1
            elif self.ant_dir == "right":
                self.ant_dir = "down"
                createNode = (self.ant_x, self.ant_y)
                self.ant_y += 1

        if killNode in self.nodes:
            del self.nodes[killNode]

        if createNode is not None:
            if createNode[0] > 0 and createNode[0] < self.width/self.node_size:
                if createNode[1] > 0 and createNode[1] < self.height/self.node_size:
                    self.nodes[createNode] = 1
                    pygame.draw.rect(self.screen, self.pixel_color, (createNode[0]*self.node_size, createNode[1]*self.node_size, self.node_size, self.node_size))


    def event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_p:
                self.paused = not self.paused

    def render(self):
        # draw ant at current position
        pygame.draw.rect(self.screen, self.ant_color, (self.ant_x*self.node_size, self.ant_y*self.node_size, self.node_size, self.node_size))

        pygame.display.flip()

    def cleanup(self):
        pygame.quit()

if __name__ == "__main__":
    ant = Ant()
    ant.init()
