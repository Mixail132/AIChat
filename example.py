request = {
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }

response = {
    "candidates": [
        {
            "content": {
                "parts": [
                    {
                        "text": "AI learns patterns from data to make predictions or decisions.\n"
                    }
                ],
                "role": "model"
            },
            "finishReason": "STOP",
            "avgLogprobs": -0.052846292654673256
        }
    ],
    "usageMetadata": {
        "promptTokenCount": 8,
        "candidatesTokenCount": 12,
        "totalTokenCount": 20,
        "promptTokensDetails": [
            {
                "modality": "TEXT",
                "tokenCount": 8
            }
        ],
        "candidatesTokensDetails": [
            {
                "modality": "TEXT",
                "tokenCount": 12
            }
        ]
    },
    "modelVersion": "gemini-2.0-flash",
    "responseId": "uZ-9aO73BuXxnsEP8Z_QWA"
}

example = """
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: GEMINI_API_KEY' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
"""