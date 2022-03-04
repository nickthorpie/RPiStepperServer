import subprocess
import os, tempfile

# Update the c++ reader script before running. Take this out once happy with the final product
cwd = os.path.dirname(os.path.abspath(__file__))
subprocess.run([f"g++ {cwd}/motor_client.cpp -o {cwd}/motor_client"],shell=True)


class motorClient():
    def __init__(self,dir_pin,step_pin,enable_pin,freq = 10000):
        self.dir_pin = dir_pin
        self.step_pin = step_pin
        self.enable_pin = enable_pin
        self.freq = freq

        self.init_pipe()

    def init_pipe(self):
        self.tmpdir = tempfile.mkdtemp()
        self.filename = os.path.join(self.tmpdir, "myfifo")
        try:
            os.mkfifo(self.filename)
        except OSError as e:
            print("Failed to create FIFO: %s" % e)
        else:
            self.p = subprocess.Popen([f'{cwd}/motor_client {self.filename} {self.step_pin} {self.dir_pin} {self.freq}'], shell=True)

            fifo = open(self.filename, 'w')
            fifo.write("0\0")
            self.fifo = fifo
            print("Pipeline Opened on Python Side")

    def move_to(self,value):
        assert type(value) == int, "command must be type int"
        self.fifo.write(f"{value}\0")
        self.fifo.flush()

    def close_pipe(self):
        self.fifo.close()
        os.remove(self.filename)
        os.rmdir(self.tmpdir)
        print("Successful exit")

    def __del__(self):
        self.close_pipe()
