def read_testcase(name): 
    tmp_case = []
    f = open(f"c:/Users/Artyrie/Documents/Algorithm/Algorithms book1/{name}", 'r')
    lines = f.readlines()

    for line in lines: 
        tmp_line = list(map(int, line.split()))
        tmp_case.append(tmp_line)

    f.close()

    return tmp_case

class Find_map():
    def __init__(self, maze): 
        self.maze = maze
        self.pos = [2, 2]
        self.route = []

    def get_maze(self):
        return self.maze

    def get_pos(self): 
        return self.pos
    
    def set_pos(self, pos):
        self.pos = pos
        return True

    def is_right_can_go(self): 
        pos = self.get_pos()
        maze = self.get_maze()
        if (maze[pos[0]][pos[1] + 1] != 1): 
            return True
        else: 
            return False
    
    def is_down_can_go(self): 
        pos = self.get_pos()
        maze = self.get_maze()
        if (maze[pos[0 + 1]][pos[1]] != 1): 
            return True
        else: 
            return False
    
    def get_route(self):
        return self.route

    def add_route(self, next):
        tmp_route = self.get_route()
        tmp_route.append(next)
        self.route = tmp_route
        return True

    def show_route(self):
        way = self.get_route()
        for line in way:
            print(f"{line} -> ", end = ' ')

    def find_way(self): 
        maze = self.get_maze()
        while (True):
            pos = self.get_pos()
            item = maze[pos[0]][pos[1]]
            self.add_route((pos, item))
            
            if (item == 2):
                self.show_route()
                print("end")
                break
            else:
                if (self.is_right_can_go() == True):
                    self.set_pos([pos[0], pos[1] + 1])
                elif (self.is_down_can_go() == True):
                    self.set_pos([pos[0] + 1, pos[1]])
                else:
                    self.show_route()
                    print("Can't find goal")
                    break
        return True


def main(): 
    testcase = read_testcase("ant_find_test.txt")
    ant_maze = Find_map(testcase)
    ant_maze.find_way()
    return 0

main()