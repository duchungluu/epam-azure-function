import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="HttpTrigger")
def HttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    namme = req.params.get("namme")
    if not namme:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            namme = req_body.get("namme")

    if namme:
        return func.HttpResponse(
            f"Hello, {namme}. This HTTP triggered function executed successfully."
        )
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200,
        )
