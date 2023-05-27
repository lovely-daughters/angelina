from ipykernel.kernelbase import Kernel
from selenium import webdriver
import subprocess
import pprint


class Angelina(Kernel):
    implementation = "ange"
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
                tab_info = []
                for idx, handle in enumerate(self.driver.window_handles):
                    self.driver.switch_to.window(handle)
                    tab_title = self.driver.title
                    tab_info.append(f"{idx:02d} - {tab_title}")

                self.send_response(
                    self.iopub_socket,
                    "stream",
                    {
                        "name": "stdout",
                        "text": "\n".join(tab_info),
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

            else:
                transpiled_code = subprocess.check_output(
                    [
                        "ts-node",
                        "/Users/elim-mbp-01/Documents/angelina/angelina_kernel/misc/transpile.ts",
                        code,
                    ]
                ).decode("utf-8")
                result = self.driver.execute_cdp_cmd(  # most important line
                    "Runtime.evaluate",
                    {
                        "expression": transpiled_code,
                        "userGesture": True,  # treated as if initiated by user in the UI
                        "replMode": True,  # const/let redaclarations allowed in repl mode
                    },
                )
                stream_content = {
                    "name": "stdout",
                    "text": f"{pprint.pformat(result)}",
                }
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
