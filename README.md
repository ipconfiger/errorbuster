# errorbuster
Format traceback object to JSON for human read and easy process in Report System

### Usage

##### Installation

    pip install errorbuster


##### Format error

    import logging
    from errorbuster import formatError
    
    try:
        1/0 # any code may run with failure raise Exception
    except Exception as e:
        logging.error(formatError(e))
        

You can configure Filebeat or other log tools to collect error log

##### Output

Output error with json in one line, it's like below

    {
        'error_type': # the Type of Error,
        'error_message': # Message in Error Object,
        'traceback': [
            {
                'file_path': # file name of this stack，
                'func_name': # function name called
                'line_no':   # The line number,
                'locals': {
                    var: value
                }            # the locals of this stack
            }, ...
        ]
    }