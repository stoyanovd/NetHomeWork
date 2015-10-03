from functools import partial
import threading
from makers.ConnectsKeeper import ConnectsKeeper

from makers.client import client_main
from makers.output import output_main, lost_keeper
from makers.server import server_main

if __name__ == '__main__':
    ck = ConnectsKeeper()
    threads = [threading.Thread(target=partial(server_main, ck=ck)),
               threading.Thread(target=partial(client_main, ck=ck)),
               threading.Thread(target=partial(output_main, ck=ck)),
               threading.Thread(target=partial(lost_keeper, ck=ck))]

    for t in threads:
        t.start()
