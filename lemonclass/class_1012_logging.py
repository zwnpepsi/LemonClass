import logging

logger=logging.getLogger("python全栈1期logging课")
logger.setLevel(logging.INFO)

# filehandler=logging.FileHandler("python1.log",encoding="utf-8")
# filehandler.setLevel(logging.INFO)

streamhandler=logging.StreamHandler()
streamhandler.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# filehandler.setFormatter(formatter)
streamhandler.setFormatter(formatter)

# logger.addHandler(filehandler)
logger.addHandler(streamhandler)

logger.info("第一条测试信息")
logger.warning("第2条测试信息")
logger.error("第三条测试信息")

