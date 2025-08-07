import pandas as pd
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("../targetflux_crawler/leads.csv")

@app.get("/search")
def search(
    query: str = Query(None, description="Recherche texte"),
    tech_recharge: bool = Query(None, description="Filtre Recharge True/False")
):
    results = df.copy()
    if query:
        mask = results['shop_name'].str.contains(query, case=False, na=False) | \
               results['meta_desc'].str.contains(query, case=False, na=False)
        results = results[mask]
    if tech_recharge is not None:
        results = results[results['tech_recharge'] == tech_recharge]
    return results.head(100).to_dict(orient="records")
