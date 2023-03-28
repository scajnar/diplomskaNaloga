import logging
import inspect

class Logger:
    def __init__(self):
        # set up the logger with the calling subclass name
        frame = inspect.currentframe().f_back
        calling_class = frame.f_locals.get('self').__class__
        logger_name = f"{__name__}"
        for cls in reversed(inspect.getmro(calling_class)):
            if cls.__name__ != 'object':
                logger_name += f".{cls.__name__}"
        self.log = logging.getLogger(logger_name)
        self.log.setLevel(logging.INFO)

        # set up the console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # set up the formatter
        formatter = logging.Formatter('%(asctime)s - %(message)s (%(filename)s:%(lineno)d)', '%H:%M:%S')
        console_handler.setFormatter(formatter)

        # add the console handler to the logger
        self.log.addHandler(console_handler)

    def info(self, message, frame=None, explicit=False):
        if explicit:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            # set up the formatter
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)', '%H:%M:%S')
            console_handler.setFormatter(formatter)

            # add the console handler to the logger
            self.log.addHandler(console_handler)


        if frame is None:
            frame = inspect.currentframe().f_back

        filename = frame.f_code.co_filename
        lineno = frame.f_lineno

        record = logging.LogRecord(
            name=self.log.name,
            level=logging.INFO,
            pathname=filename,
            lineno=lineno,
            msg=message,
            args=None,
            exc_info=None
        )

        self.log.handle(record)
        # flush the log messages immediately
        for handler in self.log.handlers:
            handler.flush()
