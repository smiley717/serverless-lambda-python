import json
import psycopg2
from os import environ

DB_CONN = environ.get('DB_CONN')

header = {'access-control-allow-origin': '*'}

conn = None


def open_connection():
    global conn
    try:
        if conn is None:
            conn = psycopg2.connect(DB_CONN)
        elif conn.closed:
            conn = psycopg2.connect(DB_CONN)

    except Exception as err:
        print("[ERROR] Unexpected error: Could not connect to DB instance.")
        raise err


def make_response(statusCode, body, header):
    return {
        'body': json.dumps(body),
        'statusCode': statusCode,
        'headers': header
    }


def main(event, context):
    try:
        open_connection()
        customer_id = event['pathParameters']['id']
        print(f"[INFO] customer id: {customer_id}")

        with conn:
            with conn.cursor() as cur:
                try:
                    query = """
                                SELECT * FROM customers WHERE id = %s
                            """
                    cur.execute(query, (customer_id,))
                    record = cur.fetchone()
                    customer_name = record[1]

                except Exception as err:
                    print(f"[ERROR] GetCustomer: ", err)
                    body = {
                        "message": "Could not retrieve customer name.",
                    }
                    return make_response(400, body, header)

    finally:
        if conn is not None and not conn.closed:
            conn.close()

    body = {
        "message": "You have retrieved customer name successfully!",
        "name": customer_name
    }

    return make_response(200, body, header)
