from ipykernel.kernelbase import Kernel


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

    def do_execute(
        self, code, silent, store_history=True, user_expressions=None, allow_stdin=False
    ):
        if not silent:
            # stream_content = {"name": "stdout", "text": code}
            # self.send_response(self.iopub_socket, "stream", stream_content)
            stream_content = {"name": "stdout", "text": "😭SUZU😭"}
            self.send_response(self.iopub_socket, "stream", stream_content)

        return {
            "status": "ok",
            # The base class increments the execution count
            "execution_count": self.execution_count,
            "payload": [],
            "user_expressions": {},
        }
