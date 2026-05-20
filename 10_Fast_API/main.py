from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('patient.json', 'r') as f:
        return json.load(f)

data = load_data()

@app.get('/patient/{patient_id}')
def get_patient(
    patient_id: str = Path(
        ...,
        description='This is the id of the patient',
        examples={"example1": {"value": "P001"}}
    )
):
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient Not Found')


@app.get('/sort')
def sort(
    sort_by: str = Query(..., description='Tell what do you want to sort?'),
    order: str = Query('asc', description='Do you want asc or desc?')
):
    valid_sort_by = ['height', 'age', 'bmi']

    if sort_by not in valid_sort_by:
        raise HTTPException(status_code=400, detail=f'Select from {valid_sort_by}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Choose asc or desc')

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    return sorted_data