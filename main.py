import time
from bs4 import BeautifulSoup
import cfscrape
from discord_webhook import DiscordWebhook

# https://discord.com/api/webhooks/909258630556168272/8KkAI2fl6AMtKJhSXE2WI4SBzXVwfHxoQSeB29Bpj5KNE4K7fVmL11Q3j0l1zZNOhe7A

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def find_price(str):
    soup = BeautifulSoup(str, 'lxml')
    table = soup.findAll('div',attrs={"class":"product-availability"})
    price = soup.findAll('span', attrs={"class":"woocommerce-Price-amount amount"})
    if 'Indisponível' in table[0].text:
        print(bcolors.FAIL, '>> Out of stock', 'Price:', price[1].text ,bcolors.ENDC)
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/909258630556168272/8KkAI2fl6AMtKJhSXE2WI4SBzXVwfHxoQSeB29Bpj5KNE4K7fVmL11Q3j0l1zZNOhe7A', content='>> Out of stock ' + 'Price: ' + price[1].text)
        webhook.execute()
    elif 'Em stock' in table[0].text:
        print(bcolors.OKGREEN, '>> In Stock', 'Price:', price[1].text, bcolors.ENDC)
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/909258630556168272/8KkAI2fl6AMtKJhSXE2WI4SBzXVwfHxoQSeB29Bpj5KNE4K7fVmL11Q3j0l1zZNOhe7A', content='>> In Stock ' + 'Price: ' + price[1].text)
        webhook.execute()

if __name__ == "__main__":
    links = ['https://nanochip.pt/produto/placa-grafica-asus-radeon-rx5600-xt-tuf-x3-6gb-oc-ddr6/','https://nanochip.pt/produto/placa-grafica-msi-radeon-rx5700-xt-8gb-ddr6-pci-e-4-0/', 'https://nanochip.pt/produto/placa-grafica-msi-radeon-rx-5700-xt-evoke-oc-8gb-ddr6-pci-e/', 'https://nanochip.pt/produto/placa-grafica-msi-radeon-rx-5700-xt-mech-oc-8gb-ddr6-pci-e/', 'https://nanochip.pt/produto/placa-grafica-msi-radeon-rx5700-xt-gaming-x-8gb-ddr6-pci-e/', 'https://nanochip.pt/produto/placa-grafica-sapphire-radeon-rx5700-xt-pulse-8gb-ddr6-pci-e/']
    scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance

    while True:
        print(' >> Pinging Started!')
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/909258630556168272/8KkAI2fl6AMtKJhSXE2WI4SBzXVwfHxoQSeB29Bpj5KNE4K7fVmL11Q3j0l1zZNOhe7A', content='==Ping Started==')
        webhook.execute()
        for cur in links:
            page = scraper.get(cur).text
            find_price(page)
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/909258630556168272/8KkAI2fl6AMtKJhSXE2WI4SBzXVwfHxoQSeB29Bpj5KNE4K7fVmL11Q3j0l1zZNOhe7A', content='==Ping Ended==')
        webhook.execute()
        time.sleep(6000)

  
    




