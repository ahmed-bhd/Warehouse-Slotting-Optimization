# main.py
import sys
from src.orchestration.pipeline import SlottingPipeline

def main():
    print("DEBUG: main.py started")
    try:
        print("DEBUG: Instantiating pipeline...")
        pipeline = SlottingPipeline()
        print("DEBUG: Calling run_full_analysis()...")
        pipeline.run_full_analysis()
        print("DEBUG: Pipeline finished successfully.")
    except Exception as e:
        print(f"DEBUG: An error occurred: {e}")
        import traceback
        traceback.print_exc() # This will show you exactly which line is failing
        sys.exit(1)

if __name__ == "__main__":
    main()