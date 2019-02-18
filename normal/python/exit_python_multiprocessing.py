import signal, multiprocessing, time, logging, os

def exit_signal_handler(sig=None, frame=None):
    signal_names = dict((k, v) for v, k in signal.__dict__.iteritems() if v.startswith('SIG'))
    logging.info('catch signal %s, exit ...', signal_names.get(sig, sig))
    while(multiprocessing.active_children()):
        for p in multiprocessing.active_children():
            p.terminate()
        time.sleep(.2)
    os._exit(0)

def run():
    while 1:
        print 1
        time.sleep(1)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_signal_handler)
    signal.signal(signal.SIGTERM, exit_signal_handler)
    signal.signal(signal.SIGHUP, exit_signal_handler)

    process = multiprocessing.Process(target=run)
    process.start()
    process = multiprocessing.Process(target=run)
    process.start()
    process = multiprocessing.Process(target=run)
    process.start()
