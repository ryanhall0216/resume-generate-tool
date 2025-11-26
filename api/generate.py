from openai import OpenAI
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from resume_logic import tailor_resume  # move your functions here


def handler(request):
    try:
        data = request.json()

        resume_text = data.get("resume", "")
        job_description = data.get("job_description", "")
        custom_prompt = data.get("custom_prompt", "")

        tailored = tailor_resume(resume_text, job_description, custom_prompt)

        return {
            "statusCode": 200,
            "body": json.dumps(tailored)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
