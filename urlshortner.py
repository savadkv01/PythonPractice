import pyshorteners

def main():
    url = input("Enter the URL: \n")
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    print("Shortened URL: ", shortened_url)

if __name__ == "__main__":
    main()
