import os
import configparser



class GetConfig():

    def __init__(self):
        self.pwd = os.path.split(os.path.realpath(__file__))[0]
        self.config_path = os.path.join(
            os.path.split(self.pwd)[0], 'Config.ini')
        self.config_file = configparser.ConfigParser()
        self.config_file.read(self.config_path)

    def get_paras(self):
        return dict(self.config_file['list'])




if __name__ == "__main__":
    gc = GetConfig()
    # print(gc.pwd)
    print(gc.config_path)
    print(gc.get_paras())
