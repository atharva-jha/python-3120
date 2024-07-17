import yt_dlp

# Enter the url for the download url = input("Enter video url: ")

ydl_opts = {}

with yt_dlp. YoutubeDL(ydl_opts) as ydl: ydl.download([url])

print("Video downloaded successfully!")
#code 2
from colorama import Fore print(Fore. RED + "hello world") print(Fore. BLUE + "hello world") print(Fore. GREEN + "hello world")

print(Fore. YELLOW + "CLCODING.COM")

print(Fore. CYAN + "THANK YOU")
#code 3
import barcode from barcode import Code128

def generate_barcode(data): code = Code128(data) code.save("barcode") print("Barcode generated.")

data = "1234-5678-9012" generate_barcode(data)
#code 4
import barcode from barcode import Code128

def generate_barcode(data): code = Code128(data) code.save("barcode") print("Barcode generated.")

data = "1234-5678-9012" generate_barcode(data)
#code 5
from faker import Faker

fake Faker()

print(fake.name())

print(fake.address())

print(fake.text())

print(fake.email())

print(fake.country())

print(fake.latitude(), fake.longitude())

print(fake.url())
