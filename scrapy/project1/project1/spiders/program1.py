import scrapy


class Spider1(scrapy.Spider):
    name = "program1"
    start_urls = ["https://sahyadri.edu.in/Home/Campus", "https://nmamit.nitte.edu.in/"]

    # Set the user agent (Optional)
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0(Windows NT 10.0; Win64;x64)AppleWebKit/537.6 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    }

    def parse(self, response):
        # Extract images
        images = response.css("img::attr(src)").getall()

        # Extract paragraphs
        paragraphs = response.css("p::text").getall()

        # Save images links to file
        with open("image1.txt", "a") as file:
            for image in images:
                file.write(image + "\n")

        # Save paragraphs links to file
        with open("paragraph1.txt", "a") as file:
            for paragraph in paragraphs:
                file.write(paragraph + "\n")
