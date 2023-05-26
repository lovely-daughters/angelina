from ipykernel.kernelbase import Kernel

class MyKernel(Kernel):
    implementation = 'MyKernel'
    implementation_version = '0.1'
    language = 'no-op'
    language_version = '0.1'
    banner = "My Kernel - outputs cell content"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            stream_content = {'name': 'stdout', 'text': code}
            self.send_response(self.iopub_socket, 'stream', stream_content)
        return {'status': 'ok', 'execution_count': self.execution_count, 'payload': [], 'user_expressions': {}}