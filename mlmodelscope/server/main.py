from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pred/{dataset_id}")
def read_prediction(dataset_id: str):
    def find_agent():
        return
    agent = find_agent()

    accuracy = agent.predict(dataset_id)

    return {"accuracy": accuracy, "dataset_id": dataset_id}
