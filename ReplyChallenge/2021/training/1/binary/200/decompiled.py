# uncompyle6 version 3.5.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.5 (default, Nov 16 2020, 22:23:17) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
# Embedded file name: ./pybot.py
# Compiled at: 2018-08-28 16:20:55
import sys

class CCServer:

    def __init__(self, hostname):
        self.xor_key = 'd3cRYp7_k3Y'
        self.hostname = hostname

    def decrypt_hostname(self):
        plain_host = []
        for i in range(len(self.hostname)):
            c1 = self.hostname[i]
            c2 = ord(self.xor_key[(i % len(self.xor_key))])
            plain_host.append(chr(c1 ^ c2))

        print '[+] Decrypting C&C hostname'
        return ('').join(plain_host)


class Bot:

    def __init__(self, server):
        self.prompt = '\x1b[31mbot$\x1b[0m '
        self.cc = server
        self.commands = [self.download_file, self.upload_file, self.send_info,
         self.run_cmd, self.port_scan, self.query_cc, self.kill]

    def download_file(self):
        """ Download remote file from C&C and store it locally """
        pass

    def upload_file(self):
        """ Upload local file to C&C """
        pass

    def send_info(self):
        """ Send collected info to C&C """
        pass

    def run_cmd(self):
        """ Execute command locally and send results to C&C """
        pass

    def port_scan(self):
        """ Perform port scan and send results to C&C """
        pass

    def query_cc(self):
        """ Get info from C&C  """
        self.cc.decrypt_hostname()

    def kill(self):
        """ Kill this bot """
        pass

    def list_commands(self):
        for num, cmd in enumerate(self.commands):
            print str(num) + ') ' + cmd.__name__

        try:
            choice = int(raw_input('\n' + self.prompt))
        except ValueError:
            print 'Please enter an integer number.'
            sys.exit(1)

        return choice

    def menu(self):
        choice = self.list_commands()
        while 0 <= choice < len(self.commands) and choice != self.commands.index(self.kill):
            print '\n[+]%s' % self.commands[choice].__doc__
            self.commands[choice]()
            print
            choice = self.list_commands()


if __name__ == '__main__':
    hostname = [
     31, 117, 47, 21, 99, 32, 88, 110, 5, 71, 54, 2, 112, 12, 60,
     45, 2, 7, 51, 69, 80, 52, 25]
    server = CCServer(hostname)
    bot = Bot(server)
    bot.menu()
