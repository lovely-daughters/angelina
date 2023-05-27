from ipykernel.kernelbase import Kernel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import pprint

class Angelina(Kernel):
    implementation = "Angelina"
    implementation_version = "0.5.14"
    language = "javascript"
    language_version = "ES6"
    language_info = {
        "name": "JavaScript",
        "mimetype": "application/javascript",
        "file_extension": ".js",
    }
    banner = "Angelina Ajimu"
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        options = webdriver.ChromeOptions()
        options.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=options)
        self.sanity = "0"
    
    def pformat(self, obj):
        return pprint.pformat(obj)
        
    def do_execute(
        self, code: str, silent, store_history=True, user_expressions=None, allow_stdin=False
    ):
        # shitty cell magicks
        if code.startswith(r"%tabs"):
            self.send_response(self.iopub_socket, "stream", {"name": "stdout", "text": f"{self.pformat(self.driver.window_handles)}"})
        elif code.startswith(r"%switch"):
            tab_num = int(code.split(" ").pop())
            self.driver.switch_to.window(self.driver.window_handles[tab_num])
            self.send_response(self.iopub_socket, "stream", {"name": "stdout", "text": f"SWITCHED TO TAB: {tab_num}"})
        elif code.startswith(r"%type"):
            self.send_response(self.iopub_socket, "stream", {"name": "stdout", "text": type(code)})
        elif not silent:
            stream_content = {"name": "stdout", "text": f"😭 {self.sanity}"}
            self.send_response(self.iopub_socket, "stream", stream_content)

        return {
            "status": "ok",
            # The base class increments the execution count
            "execution_count": self.execution_count,
            "payload": [],
            "user_expressions": {},
        }
        