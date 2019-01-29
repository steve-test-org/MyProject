import os
import json
import boto3

COLOR = 'ff0000'


def main():
    client = boto3.client('cloudwatch')

    env = os.environ['EnvironmentName']

    response = client.put_dashboard(DashboardName=f'Demo-{env}', DashboardBody=get_body(env))
    print(response)


def get_body(env):
    body = {
        "widgets": [
            {
                "type": "text",
                "x": 0,
                "y": 0,
                "width": 21,
                "height": 15,
                "properties": {
                    "markdown": f"\n# {env}\n\n\n\n![alt text](https://htmlcolors.com/color-image/{COLOR}.png)\n"
                }
            }
        ]
    }

    return json.dumps(body)


if __name__ == "__main__":
    main()
