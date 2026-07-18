import time
import logging

from fastapi import Request


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("isl-api")


async def logging_middleware(
    request: Request,
    call_next
):

    start = time.perf_counter()

    response = await call_next(request)

    elapsed = (
        time.perf_counter() - start
    ) * 1000

    logger.info(

        "%s %s | %d | %.2f ms | %s",

        request.method,

        request.url.path,

        response.status_code,

        elapsed,

        request.client.host

    )

    return response