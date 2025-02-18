import requests
import json

AZURE_OPENAI_ENDPOINT = ""
API_KEY = ""

JSON_INDENT = 2
def format_json(obj):
    """
    Formats a given JSON instance into a readable string with a defined indentation.

    Args:
        obj (Any): The JSON object to format, which should be
            a valid Python dictionary or list structure.

    Returns:
        str: A JSON-formatted string with indentation specified by the global JSON_INDENT.
    """
    try:
        return json.dumps(obj, indent=JSON_INDENT)
    except Exception as e:# (TypeError, ValueError)
        print(f"Error formatting JSON: {e}")

def create_response_format(schema):
    response_format = {
        "type": "json_schema",
        "json_schema": {
            "name": "json_output_schema",
            "schema": {**schema},
            "strict": True
        }
    }
    return response_format

def get_response_format(classification_types):
    json_output_schema = {
    "type": "object",
    "properties": {
        "response": {
            "type": "object",
            "properties": {
                    "reasoning": { "type": "string" },
                    "classification": { "type": "string", "enum": classification_types}
            },
            "additionalProperties": False,
            "required": ["reasoning", "classification"]
        }
    },
    "additionalProperties": False,
    "required": ["response"]
    }
    response_format = create_response_format(json_output_schema)
    return response_format

# Replace with your Azure OpenAI details

API_VERSION = "2024-08-01-preview"
DEPLOYMENT_NAME = "gpt-4o"

# Endpoint for creating an assistant
url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version={API_VERSION}"

headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY
}

def get_response(system_prompt, text_input, response_format):
    data = {
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text_input}
        ],
        "response_format": response_format
    }
    response = json.loads(requests.post(url, headers=headers, json=data).json()["choices"][0]["message"]["content"])["response"]
    return response