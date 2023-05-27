from ipykernel.kernelbase import Kernel
from selenium import webdriver
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

    def do_execute(
        self,
        code: str,
        silent,
        store_history=True,
        user_expressions=None,
        allow_stdin=False,
    ):
        try:
            # shitty cell magicks
            if code.startswith(r"%tabs"):
                self.send_response(
                    self.iopub_socket,
                    "stream",
                    {
                        "name": "stdout",
                        "text": f"{pprint.pformat(self.driver.window_handles)}",
                    },
                )

            elif code.startswith(r"%switch"):
                tab_num = int(code.split(" ").pop())
                self.driver.switch_to.window(self.driver.window_handles[tab_num])
                self.send_response(
                    self.iopub_socket,
                    "stream",
                    {"name": "stdout", "text": f"SWITCHED TO TAB: {tab_num}"},
                )

            elif code.startswith(r"%type"):
                self.send_response(
                    self.iopub_socket,
                    "stream",
                    {"name": "stdout", "text": f"{type(code)}"},
                )

            elif not silent:
                result = self.driver.execute_cdp_cmd(
                    "Runtime.evaluate",
                    {
                        "expression": code,
                        "userGesture": True,  # treated as if initiated by user in the UI
                        "replMode": True,  # const/let redaclarations allowed in repl mode
                    },
                )
                stream_content = {"name": "stdout", "text": f"{pprint.pformat(result)}"}
                self.send_response(self.iopub_socket, "stream", stream_content)

        except Exception as e:
            content = {"ename": type(e).__name__, "evalue": str(e), "traceback": []}
            self.send_response(self.iopub_socket, "error", content)

        return {
            "status": "ok",
            "execution_count": self.execution_count,
            "payload": [],
            "user_expressions": {},
        }

    def _at_shutdown(self):
        # self.driver.detach()
        pass
