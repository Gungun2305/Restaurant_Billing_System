import os
import streamlit as st
from ui.main_ui import run_ui
from utils.db_utils import init_db

DB_PATH = "db/restaurant.db"

def main():
    os.makedirs("db", exist_ok=True)
    os.makedirs("data", exist_ok=True)

    init_db(DB_PATH)

    run_ui(DB_PATH)
    
        

if __name__ == "__main__":
    main()
