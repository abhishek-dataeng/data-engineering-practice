import logging

logging.basicConfig(level=logging.INFO,
                    filename="/home/abhishek/projects/python_prep/logs/app_log2.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def order_processing(orders: list) -> dict:
    logger.info("Starting order processing for %d orders.",len(orders))
    skipped,processed=0,0
    for order in orders:
        if 'amount' not in order or 'order_id' not in order:
            logger.error("Order missing required field %d",order)
            skipped +=1
            continue
        elif order['amount'] < 0:
            logger.warning("Skipping order %d with negative amount %",order['order_id'],order['amount'])
            skipped += 1
            continue
        processed += 1

    logger.info("Finished: %d and Skippd: %d",processed,skipped)
    return {'Processed': processed, 'Skipped': skipped}

