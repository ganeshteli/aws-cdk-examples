import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    
    logger.info(f'Event: - {event}')
   
    return {
        "statusCode":200,
        "body": "Function invoked"
    }

if __name__ == '__main__':
    print(lambda_handler(None,None))