from atlas.core.orchestrator import AnalysisPipeline
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file

path = os.getenv("PATH_TO_ANALYZE")
#print(path)

orchestrator = AnalysisPipeline()
orchestrator.analyze(path)

