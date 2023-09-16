import speedtest

wifi = speedtest.Speedtest(secure=True)

def wifitest():
    print("Getting download speed ...")
    download_speed = wifi.download()

    print("Getting upload speed ...")
    upload_speed = wifi.upload()

    print("Download: ", download_speed / 1000000)
    print("Upload: ", upload_speed / 1000000)
    
    message = "wifitest_callback:" + str(round(download_speed / 1000000,2)) + ":" + str(round(upload_speed / 1000000,2))

    return (message)
