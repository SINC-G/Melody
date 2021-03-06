from .DMA import decompile as dma
from .rule.static_vuln import vuln_match_all
from .rule.url import get_url


class MATCH:
    def __init__(self, base_path, path, out_path):
        self.base_path = base_path
        self.path = path
        self.out_path = out_path
        self.source_path = []
        self._status = ""
        self.match_rule = ""

    def decompile(self) -> bool:
        result = dma.decompile(self.base_path, self.path, self.out_path)
        if type(result) == list and result:
            self.source_path = result
            return True
        else:
            print("decompile error: ", result)
            return False

    def status(self):
        system = platform.system()
        if system == "Windows":
            outs_path = self.out_path + "\\result"
        else:
            outs_path = self.out_path + "/result"
        with open(outs_path, "r", encoding="utf-8") as f:
            result = f.read()
            self._status = result
        return self._status

    def match_url(self):
        return get_url(self.source_path)

    def match_vuln_all(self):
        return vuln_match_all(self.source_path)


if __name__ == '__main__':
    out_path = r"/Users/ios/Downloads/out/"
    file_path = r"/Users/ios/Downloads/wifi.apk"
    base_path = r"/Users/ios/Desktop/DLU/Melody"
    match = MATCH(base_path, file_path, out_path).match_url()

    # match_result = match.match_url()
    # match_result = match.match_vuln_all()
    # print(match_result)
    print(match)
