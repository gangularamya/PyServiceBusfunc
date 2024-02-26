import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os
import logging
import time


async def main(req: func.HttpRequest) -> func.HttpResponse:
    service_bus_namespace = "PythonFuncServiceBusResPrem.servicebus.windows.net"
    # connection_string = os.getenv("ServiceBusConnectionString")
    queue_name = "demosb"
    
    credential = DefaultAzureCredential()
    servicebus_client = ServiceBusClient(service_bus_namespace, credential)
    logging.info('Python HTTP trigger function processed a request.')


    # message = ServiceBusMessage("Hello, Service Bus!")

    # servicebus_client = ServiceBusClient.from_connection_string(connection_string)
    # with servicebus_client:
    #     sender = servicebus_client.get_queue_sender(queue_name)
    #     with sender:
    #         for i in range(100):
    #             message = ServiceBusMessage(f"Hello, Service Bus! Message {i+1}")
    #             sender.send_messages(message)
                # time.sleep(20)  # pause for 20 seconds

    # sender = servicebus_client.get_queue_sender(queue_name)
    with servicebus_client:
        sender = servicebus_client.get_queue_sender(queue_name)
        with sender:
            for i in range(20):
                message = ServiceBusMessage(f"Hello, Service Bus! Message {i+1}")
                sender.send_messages(message)
                # time.sleep(20)  # pause for 20 seconds

    return func.HttpResponse("Test: Message sent to Service Bus queue.")
