from estruturas.linked_list.linked_list import LinkedList

request_pipeline = LinkedList()

request_pipeline.append("Authentication")
request_pipeline.append("Validation")
request_pipeline.append("Controller")
request_pipeline.prepend("Logging")

print("\n===== REQUEST PIPELINE =====")
print(request_pipeline)
print(f"Total de etapas: {len(request_pipeline)}")


middleware = request_pipeline.find("Authentication")

if middleware is not None:
    print(f"Middleware encontrado: {middleware.data}")
else:
    print("Middleware não encontrado.")


removed = request_pipeline.remove("Validation")

if removed:
    print("\nMiddleware Validation removido.")
else:
    print("\nMiddleware Validation não foi encontrado.")

print(f"Pipeline atual: {request_pipeline}")