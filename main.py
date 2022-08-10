import http.client, time
CATS_TO_DOWN_LOAD = 100
CAAS = "cataas.com"

def main():
    start_time = time.time()
    conn = http.client.HTTPSConnection(CAAS)
    for cat in range(0, CATS_TO_DOWN_LOAD):
        conn.request("GET", "/cat")
        res = conn.getresponse()
        extention = res.headers.get("Content-Type").split("/")[1]
        with open(f"cats/cat{cat}.{extention}", "wb") as fp:
            fp.write(res.read())
            print(f"The cat {cat} is done!")
    print("Total time: " + str(time.time() - start_time))


if __name__ == "__main__":
    main()