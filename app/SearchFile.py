import os
import re
import subprocess
from glob import glob


class SearchFile():
    def __init__(self, filedir):
        self.filedir = os.path.join(filedir, "**")

    def do_grep(self, filename, keyword):
        coms = ['grep', '-R', '-e']
        coms.append(keyword)
        coms.append(filename)
        print('do grep as :', coms)
        cmd = subprocess.Popen(
            coms, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, error = cmd.communicate()
        ret_lines = ''.join(stdout.decode('UTF-8'))
        print(ret_lines)
        return ret_lines

    def get_all_files(self, *args):
        if len(args) == 0:
            return [f for f in glob(os.path.join(self.filedir, '*'), recursive=True) if os.path.isfile(f)]
        else:
            ret_list = []
            for r in args:
                ret_list.extend(
                    [f for f in glob(os.path.join(self.filedir, r), recursive=True) if os.path.isfile(f)])
            return list(set(ret_list))

    def grep_file(self, filename, keyword, regr):
        print("finding {} in {}".format(keyword, filename))
        ret = []
        if regr == 0:
            with open(filename, 'r') as f:
                for line in f.readlines():
                    if re.search(keyword, line, re.IGNORECASE):
                        new_keyword = '<span style="background-color:#FFFF00;">' + keyword + '</span>'
                        ret.append(
                            {filename: re.sub(keyword, new_keyword, line.strip())})

        else:  # something wrong with it
            # print('$1', filename)
            pat = re.compile(keyword)
            with open(filename, 'r') as f:
                for line in f.readlines():
                    if re.search(pat, line, re.IGNORECASE):
                        new_keyword = '<span style="background-color:#FFFF00;">' + keyword + '</span>'
                        old_line = line.strip()
                        new_line = re.sub(keyword, new_keyword, line.strip())
                        print(old_line, new_line)
                        ret.append(
                            {filename: re.sub(keyword, new_keyword, line.strip())})

        print(ret)
        return ret


if __name__ == "__main__":
    sf = SearchFile('d:\p_proj\log_example\dir1')
    print(sf.get_all_files('*.log'))
    # print(sf.grep_file('d:\\p_proj\\log_example\\dir1\\log2.log', 'LOG8', 0))
