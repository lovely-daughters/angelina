from ipykernel.kernelbase import Kernel


class LoliKernel(Kernel):
    implementation = "Loli"
    implementation_version = "1.0"
    language = "no-op"
    language_version = "0.1"
    language_info = {
        "name": "Any text",
        "mimetype": "text/plain",
        "file_extension": ".txt",
    }
    banner = "UUUUOOOOOOOOOOOOOGGGGGGGGGGGGGGGGHHHHHHHHHHHH"

    def do_execute(
        self, code, silent, store_history=True, user_expressions=None, allow_stdin=False
    ):
        print("SANITY CHECK")
        if not silent:
            # stream_content = {"name": "stdout", "text": code}
            # self.send_response(self.iopub_socket, "stream", stream_content)
            self.send_response(self.iopub_socket, "stream", "😭")

        return {
            "status": "ok",
            # The base class increments the execution count
            "execution_count": self.execution_count,
            "payload": [],
            "user_expressions": {},
        }
