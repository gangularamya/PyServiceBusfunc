import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os
import logging
import time


async def main(req: func.HttpRequest) -> func.HttpResponse:
    service_bus_namespace = os.environ.get("ServiceBusConnection__fullyQualifiedNamespace")
    queue_name = os.environ.get("ServiceBusQueueName")
    logging.info(f"Service Bus Namespace: {service_bus_namespace}")
    logging.info(f"Queue Name: {queue_name}")
    
    credential = DefaultAzureCredential()
    servicebus_client = ServiceBusClient(
        fully_qualified_namespace=service_bus_namespace,
        credential=credential)
    logging.info('Python HTTP trigger function processed a request.')
    
    with servicebus_client:
        sender = servicebus_client.get_queue_sender(queue_name)
        with sender:
            for i in range(20):
                message = ServiceBusMessage(f"Hello, Service Bus! Message {i+1}")
                sender.send_messages(message)
                # time.sleep(20)  # pause for 20 seconds

    return func.HttpResponse("Master environment: Message sent to Service Bus queue.")
