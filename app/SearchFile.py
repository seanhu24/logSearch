import os
import re
from glob import glob


class SearchFile():
    def __init__(self, filedir):
        self.filedir = filedir

    def get_all_files(self, *args):
        if len(args) == 0:
            return [f for f in glob(os.path.join(self.filedir, '*')) if os.path.isfile(f)]
        else:
            ret_list = []
            for r in args:
                ret_list.extend(
                    [f for f in glob(os.path.join(self.filedir, r)) if os.path.isfile(f)])

            return list(set(ret_list))

    def grep_file(self, filename, keyword, regr):
        ret = []
        if regr == 0:
            with open(filename, 'r') as f:
                for line in f.readlines():
                    if re.search(keyword, line, re.IGNORECASE):
                        ret.append({filename: line.strip()})

        else:  # something wrong with it
            pat = re.compile(keyword)
            with open(filename, 'r') as f:
                for line in f.readlines():
                    if re.search(pat, line, re.IGNORECASE):
                        ret.append({filename: line.strip()})

        return ret


if __name__ == "__main__":
    sf = SearchFile('d:\p_proj\log_example\dir1')
    print(sf.get_all_files('log2.*', 'log1.*'))
    print(sf.grep_file('d:\\p_proj\\log_example\\dir1\\log2.log', 'LOG8', 0))
