import json, os, sys, base64

PLACEHOLDER = {
    "project_info": {
        "project_id": "placeholder",
        "project_number": "000000000000",
        "firebase_url": "https://placeholder.firebaseio.com"
    },
    "client": [
        {
            "client_info": {
                "mobilesdk_app_id": "1:000000000000:android:0000000000000000",
                "android_client_info": {
                    "package_name": "nl.giejay.android.tv.immich",
                    "certificate_hash": []
                }
            },
            "api_key": [
                {
                    "current_key": "AIzaSyPlaceholderKey0000000000000000000000"
                }
            ],
            "oauth_client": [
                {
                    "client_id": "000000000000-00000000000000000000000000000000.apps.googleusercontent.com",
                    "client_type": 3
                }
            ]
        }
    ],
    "ARTIFACT_VERSION": "1"
}

DEST = "./app/google-services.json"

b64 = os.environ.get("GOOGLE_SERVICES_BASE64", "")
if b64:
    try:
        decoded = base64.b64decode(b64).decode("utf-8")
        parsed = json.loads(decoded)
        json.dump(parsed, open(DEST, "w"), indent=2)
        print("Decoded GOOGLE_SERVICES_BASE64 into google-services.json")
        sys.exit(0)
    except Exception as e:
        print(f"GOOGLE_SERVICES_BASE64 decode/parse failed: {e}, using placeholder")

EXAMPLE = "./app/google-services.example"
if os.path.exists(EXAMPLE):
    try:
        parsed = json.load(open(EXAMPLE))
        json.dump(parsed, open(DEST, "w"), indent=2)
        print("Copied google-services.example into google-services.json")
        sys.exit(0)
    except Exception as e:
        print(f"google-services.example is invalid JSON: {e}, using hardcoded placeholder")

json.dump(PLACEHOLDER, open(DEST, "w"), indent=2)
print("Generated placeholder google-services.json")
