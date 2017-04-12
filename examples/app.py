from pip_services_commons.log import ConsoleLogger
from .DummyProcess import DummyProcess

if __name__ == '__main__':
    runner = DummyProcess()
    try:
        runner.run()
    except Exception as ex:
        ConsoleLogger().fatal("dummy", ex, "Error: ")
        #print(traceback.format_exc(ex))
        #sys.stderr.write(str(e) + '\n')