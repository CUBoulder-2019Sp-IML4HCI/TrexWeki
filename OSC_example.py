import OSC

class OSCMessenger:
        def __init__(self):
                self.in_address = '127.0.0.1', 6448
                self.out_address = '127.0.0.1', 12000
                self.input_channel = '/wek/inputs'
                self.output_channel = '/wek/outputs'
                self.input_client = OSC.OSCClient()
                self.output_client = OSC.OSCClient()
                self._connect()

        def _connect(self):
                self.input_client.connect(self.in_address)
                self.output_client.connect(self.out_address)

        def send_io_message(self,inp,out):
                in_msg = OSC.OSCMessage(self.input_channel)
                in_msg.append(inp)
                self.input_client.send(in_msg)
                out_msg = OSC.OSCMessage(self.output_channel)
                out_msg.append(out)
                self.output_client.send(out_msg)

        def __del__(self):
                self.input_client.close()
                self.output_client.close()
                print("[INFO] Closed input and output OSC clients")


