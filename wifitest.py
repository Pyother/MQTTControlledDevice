import speedtest

wifi = speedtest.Speedtest()

print("Getting download speed")
download_speed = wifi.download()

print("Getting upload speed")
upload_speed = wifi.upload()

print("Download: ", download_speed)
print("Upload: ", upload_speed)